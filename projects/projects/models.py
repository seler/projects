from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Project(models.Model):

    name = models.CharField(max_length=255, verbose_name=_(u"name"))
    slug = models.SlugField(verbose_name=_(u"slug"), unique=True)
    managers = models.ManyToManyField('auth.User', verbose_name=_(u"managers"),
                                      blank=True)

    class Meta:
        verbose_name = _(u"project")
        verbose_name_plural = _(u"projects")
        ordering = ("name", )

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('project_detail', (self.slug, ))

    @property
    def components(self):
        if not hasattr(self, '_components'):
            self._components = self.component_set.all()
        return self._components


class Layer(models.Model):

    name = models.CharField(max_length=255, verbose_name=_(u"name"))
    order = models.PositiveSmallIntegerField(default=0,
                                             verbose_name=_(u"order"))

    class Meta:
        verbose_name = _(u"layer")
        verbose_name_plural = _(u"layers")
        ordering = ('order', )

    def __unicode__(self):
        return self.name


class Component(models.Model):

    project = models.ForeignKey('Project', verbose_name=_(u"project"))
    name = models.CharField(max_length=255, verbose_name=_(u"name"))
    order = models.PositiveSmallIntegerField(blank=True, default=None,
                                             verbose_name=_(u"order"))

    class Meta:
        verbose_name = _(u"component")
        verbose_name_plural = _(u"components")
        ordering = ('order', )

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.order is None and Component.objects.all().count():
            self.order = Component.objects.all().order_by('-order')[0].order + 1
        elif self.order is None:
            self.order = 0
        return super(Component, self).save(*args, **kwargs)

    @property
    def layers(self):
        if not hasattr(self, '_layers'):
            layers = Layer.objects.all()
            for layer in layers:
                layer.items = layer.item_set.filter(version__component=self)
            self._layers = layers
        return self._layers

    @property
    def latest_version(self):
        if not hasattr(self, '_latest_version'):
            try:
                self._latest_version = self.version_set.latest()
            except Version.DoesNotExist:
                self._latest_version = None
        return self._latest_version


class Version(models.Model):

    component = models.ForeignKey('Component', verbose_name=_(u"component"))
    tag = models.CharField(max_length=255, default="v0.1",
                           verbose_name=_(u"tag"))
    created = models.DateTimeField(editable=False, verbose_name=_(u"created"))

    class Meta:
        verbose_name = _(u"version")
        verbose_name_plural = _(u"versions")
        ordering = ('-created', )
        unique_together = (('component', 'tag'), )
        get_latest_by = 'created'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created = timezone.now()
        return super(Version, self).save(*args, **kwargs)


class Item(models.Model):

    layer = models.ForeignKey('Layer', verbose_name=_(u"layer"))
    version = models.ForeignKey('Version', verbose_name=_(u"version"))
    status = models.ForeignKey('Status', verbose_name=_(u"status"))

    url = models.URLField(verbose_name=_(u"url"))

    class Meta:
        verbose_name = _(u"item")
        verbose_name_plural = _(u"items")
        ordering = ('-version__tag', )

    def __unicode__(self):
        return "{} {}".format(self.layer, self.version)

    def up_to_date(self):
        if not hasattr(self, '_up_to_date'):
            self._up_to_date = self.layer.items[0].version ==  \
                self.version.component.latest_version
        return self._up_to_date


class Status(models.Model):

    name = models.CharField(max_length=255, verbose_name=_(u"name"))
    order = models.PositiveSmallIntegerField(default=0,
                                             verbose_name=_(u"order"))
    SEVERITY_DEFAULT = 'default'
    SEVERITY_PRIMARY = 'primary'
    SEVERITY_SUCCESS = 'success'
    SEVERITY_INFO = 'info'
    SEVERITY_WARNING = 'warning'
    SEVERITY_DANGER = 'danger'
    SEVERITY_CHOICES = (
        (SEVERITY_DEFAULT, _("deffault")),
        (SEVERITY_PRIMARY, _("primary")),
        (SEVERITY_SUCCESS, _("success")),
        (SEVERITY_INFO, _("info")),
        (SEVERITY_WARNING, _("warning")),
        (SEVERITY_DANGER, _("danger")),
    )
    severity = models.CharField(max_length=255, choices=SEVERITY_CHOICES,
                                default=SEVERITY_DEFAULT,
                                verbose_name=_(u"severity"))

    class Meta:
        verbose_name = _(u"status")
        verbose_name_plural = _(u"statuses")
        ordering = ('order', )

    def __unicode__(self):
        return self.name


class File(models.Model):

    file = models.FileField(upload_to="files", verbose_name=_(u"file"))

    project = models.ForeignKey('Project', verbose_name=_(u"project"),
                                null=True)
    component = models.ForeignKey('Component', verbose_name=_(u"component"),
                                  null=True)
    layer = models.ForeignKey('Layer', verbose_name=_(u"layer"),
                              null=True)
    version = models.ForeignKey('Version', verbose_name=_(u"version"),
                                null=True)

    class Meta:
        verbose_name = _(u"file")
        verbose_name_plural = _(u"files")

    def __unicode__(self):
        return self.file.name
