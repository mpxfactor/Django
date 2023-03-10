from django.contrib import admin
from .models import Receiver
from import_export import resources
from import_export.admin import ExportActionMixin

# Register your models here.


class ReceiverResource(resources.ModelResource):
    class Meta:
        model = Receiver
        fields = ('id', 'name', 'address', 'website', 'created')
        # to change the order in which it is exported
        export_order = ('website', 'created', 'addresss', 'name', 'id')


class ReceiverAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = ReceiverResource


admin.site.register(Receiver, ReceiverAdmin)
