from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import ProjectListView, ProjectDetailView, item_add, set_item_status, \
    update_version, component_create, component_delete, set_component_order


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^set-status/(?P<item_pk>\d+)/(?P<status_pk>\d+)/$',
        set_item_status, name='set_item_status'),
    url(r'^update-version/(?P<version_pk>\d+)/'
        r'(?P<item_pk>\d+)/(?P<status_pk>\d+)/$',
        update_version, name='update_version'),
    url(r'^$', ProjectListView.as_view(), name='project_list'),
    url(r'^(?P<slug>[\w-]+)/$',
        ProjectDetailView.as_view(), name='project_detail'),
    url(r'^(?P<project_slug>[\w-]+)/add-item/(?P<component_pk>\d+)/(?P<layer_pk>\d+)/$',
        item_add, name='item_add'),
    url(r'^(?P<project_slug>[\w-]+)/delete-component/(?P<component_pk>\d+)/$',
        component_delete, name='component_delete'),
    url(r'^(?P<project_slug>[\w-]+)/create-component/$',
        component_create, name='component_create'),
    url(r'^(?P<project_slug>[\w-]+)/set-order/$',
        set_component_order, name='set_component_order'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
