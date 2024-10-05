from django.contrib import admin
from .models import warrior, Spell


# Register your models here.
class WarriorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hp', 'ap', 'dp')
    #list_filter = ()
    search_fields = ('name', 'hp')

admin.site.register(warrior,WarriorAdmin)
admin.site.register(Spell)


