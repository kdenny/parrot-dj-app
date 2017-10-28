from django.conf.urls import url

from maintenance import views

urlpatterns = [
    url(r'^maintenance/$', views.MaintenanceListView.as_view()),
    url(r'^maintenance/apartment/(?P<apartment_key>[0-9]+)/$', views.MaintenanceListView.as_view()),
    url(r'^maintenance/(?P<maint_id>[0-9]+)/$', views.MaintenanceUpdateView.as_view()),
]