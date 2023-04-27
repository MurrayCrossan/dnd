from django.contrib import admin
from .models import Table, TableEntry

# Register your models here.
#class PersonAdmin(admin.ModelAdmin):

class TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'getNumofEntries',)
    
    @admin.display(description='Number of Entries')
    def getNumofEntries(self, obj):
        return len(obj.tableentry_set.all())

class TableEntryAdmin(admin.ModelAdmin):
    model = TableEntry
    list_display = ('snip', 'getTableName',)
    list_filter = (('table', admin.RelatedFieldListFilter),)

    @admin.display(description='Name of table')
    def getTableName(self, obj):
        return obj.table

admin.site.register(Table, TableAdmin)
admin.site.register(TableEntry, TableEntryAdmin)