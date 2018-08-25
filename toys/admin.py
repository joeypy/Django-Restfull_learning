from django.contrib import admin
from .models import Toy

# Register your models here.

class ToyAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created',)
    list_display = ('name', 'id', 'description', 'toy_category', 'release_date', 'created', 'was_included_in_home')

admin.site.register(Toy, ToyAdmin)