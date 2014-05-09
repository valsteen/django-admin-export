from django.conf.urls import *
from django.contrib.admin.views.decorators import staff_member_required
from .views import AdminExport, AdminExportRelated

urlpatterns = patterns('',
    url(r'^export_to_xls/$', staff_member_required(AdminExport.as_view()), name='export_to_xls'),
    url(r'^export_to_xls_related/$', staff_member_required(AdminExportRelated.as_view()), name='export_to_xls_related'),
)