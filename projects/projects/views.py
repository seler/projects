from django.views.generic import ListView, DetailView
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

        return context


from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ItemForm


def new_tag(old_tag):
    old_tag_split = old_tag.split(".")
    tag = ".".join(old_tag_split[:-1] + [str(int(old_tag_split[-1]) + 1)])
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
        form = ItemForm(initial={'version': tag})
        form.fields['status'].choices = status_choices

    return render(request, 'projects/item_form.html', {'form': form})


def set_item_status(request, item_pk, status_pk):
    item = Item.objects.get(pk=item_pk)
    status = Status.objects.get(pk=status_pk)
    item.status = status
    item.save()
    return HttpResponseRedirect(
        item.version.component.project.get_absolute_url())
