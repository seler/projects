import json

from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import ItemForm, ComponentForm, ComponentDeleteForm, \
    ComponentNotepadForm, ComponentMoveForm
from .models import Project, Layer, Component, File, Status, Version, Item


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(*args,
                                                                  **kwargs)
        context['layers'] = Layer.objects.all()
        context['statuses'] = Status.objects.all()
        context['management_access'] = self.request.user.is_superuser or \
            self.object.managers.filter(pk=self.request.user.pk).exists()
        context['component_form'] = ComponentForm(project=self.object,
            initial={'project': self.object})

        return context


def new_tag(old_tag):
    old_tag_split = old_tag.split('.')
    old_tag_split = old_tag_split[0].split('v') + old_tag_split[1:]
    tag = "v" + ".".join(filter(None, old_tag_split[:-1] + [str(int(old_tag_split[-1]) + 1)]))
    return tag


def item_add(request, project_slug, component_pk, layer_pk):
    project = Project.objects.get(slug=project_slug)
    component = Component.objects.get(pk=component_pk)
    layer = Layer.objects.get(pk=layer_pk)
    version = component.latest_version
    items = Item.objects.filter(layer=layer, version__component=component)
    new_version_required = items and items[0].version == version

    if new_version_required:
        tag = new_tag(version.tag)
    elif version:
        tag = version.tag
    else:
        tag = "v0.1"

    # for now statuses are global
    status_choices = Status.objects.all().values_list('pk', 'name')

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        form.fields['status'].choices = status_choices
        if form.is_valid():
            item = Item()
            if form.cleaned_data['file']:
                file = File(file=request.FILES['file'])
                file.project = project
                file.component = component
                file.layer = layer
                file.version = version
                file.save()
                item.url = file.file.url
            else:
                item.url = form.cleaned_data['url']
            item.layer = layer
            item.version, created = Version.objects.get_or_create(
                tag=form.cleaned_data['version'],
                component=component)
            item.status = Status.objects.get(pk=form.cleaned_data['status'])
            item.save()
            return HttpResponseRedirect(project.get_absolute_url())
    else:
        url_qs = Item.objects.filter(version__component=component,
                                     layer=layer)
        if url_qs.exists():
            url = url_qs[0].url
        else:
            url = ''
        form = ItemForm(initial={'version': tag, 'url': url})
        form.fields['status'].choices = status_choices

    return render(request, 'projects/item_form.html', {'form': form})


def set_item_status(request, item_pk, status_pk):
    item = Item.objects.get(pk=item_pk)
    status = Status.objects.get(pk=status_pk)
    item.status = status
    item.save()
    return HttpResponseRedirect(
        item.version.component.project.get_absolute_url())


def update_version(request, version_pk, item_pk, status_pk):
    old_item = Item.objects.get(pk=item_pk)
    status = Status.objects.get(pk=status_pk)
    version = Version.objects.get(pk=version_pk)
    item = Item()
    item.layer = old_item.layer
    item.url = old_item.url
    item.version = version
    item.status = status
    item.save()
    return HttpResponseRedirect(
        item.version.component.project.get_absolute_url())


def component_create(request, project_slug):
    project = Project.objects.get(slug=project_slug)

    if request.method == 'POST':
        form = ComponentForm(request.POST, request.FILES)
        if form.is_valid():
            component = form.save(commit=False)
            component.project = project
            component.save()
            return HttpResponseRedirect(project.get_absolute_url())
    else:
        form = ComponentForm(initial={'project': project})

    return render(request, 'projects/component_form.html', {'form': form})


def component_delete(request, project_slug, component_pk):
    project = Project.objects.get(slug=project_slug)
    component = Component.objects.get(pk=component_pk)

    if request.method == 'POST':
        form = ComponentDeleteForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['component_pk'] == component.pk:
                component.delete()
                return HttpResponseRedirect(project.get_absolute_url())

    form = ComponentDeleteForm(initial={'component_pk': component.pk})

    return render(request, 'projects/delete_form.html', {'form': form})


@csrf_exempt
def set_component_order(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    components = Component.objects.filter(project=project)
    if request.method == 'POST':
        data = json.loads(request.body)
        for component in components:
            component.order = data[str(component.pk)]
            component.save()
    return HttpResponse("OK")


def component_notepad(request, project_slug, component_pk):
    project = Project.objects.get(slug=project_slug)
    component = Component.objects.get(pk=component_pk)

    if request.method == 'POST':
        form = ComponentNotepadForm(request.POST, request.FILES)
        if form.is_valid():
            component.notepad = form.cleaned_data['notepad']
            component.save()
            return HttpResponseRedirect(project.get_absolute_url())

    form = ComponentNotepadForm(initial={'notepad': component.notepad})

    return render(request, 'projects/notepad_form.html',
                  {'form': form, 'project': project, 'component': component})


def component_move(request, project_slug, component_pk):
    project = Project.objects.get(slug=project_slug)
    component = Component.objects.get(pk=component_pk)
    valid_targets = Component.objects.filter(project=project).exclude(pk=component_pk)

    if request.method == 'POST':
        form = ComponentMoveForm(component, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(component.get_absolute_url())

    form = ComponentMoveForm(component, valid_targets=valid_targets)

    return render(request, 'projects/notepad_form.html',
                  {'form': form, 'project': project, 'component': component})
