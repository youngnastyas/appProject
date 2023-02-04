from django.contrib import admin
from .models import Story, TagsModel
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


class BookResource(resources.ModelResource):

    class Meta:
        model = Story


class ProductResource(resources.ModelResource):
    class Meta:
        model = Story


class ProductAdmin(ImportExportActionModelAdmin):
    resource_class = ProductResource
    list_display = [field.name for field in Story._meta.fields if field.name != "id"]
    #inlines = [ProductImageInline]


admin.site.register(Story, ProductAdmin)

class ProductAdmin2(ImportExportActionModelAdmin):
    resource_class = ProductResource
    list_display = [field.name for field in TagsModel._meta.fields if field.name != "id"]
    #inlines = [ProductImageInline]


admin.site.register(TagsModel, ProductAdmin2)



