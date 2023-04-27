from csv import list_dialects
from pydoc import describe
from django.contrib import admin
from .models import Person, Continent, Organisation, Location, Nation, Shop, Ship, Item

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'gender', 'race', 'location')
    list_filter = (('location', admin.RelatedOnlyFieldListFilter),)

class ShipAdmin(admin.ModelAdmin):
    list_display = ('name', 'captain', 'port', 'getNumCrew')
    list_filter = (('port', admin.RelatedOnlyFieldListFilter),)

    @admin.display(description='Number of Crew')
    def getNumCrew(self, obj):
        return len(obj.crew.all())


class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'location')
    list_filter = (('location', admin.RelatedOnlyFieldListFilter),)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')

class NationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'continent')
    list_filter = (('continent', admin.RelatedOnlyFieldListFilter),)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'nation')

class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'getNumMembers')

    @admin.display(description='Number of members')
    def getNumMembers(self, obj):
        return len(obj.person_set.all())


admin.site.register(Continent)
admin.site.register(Nation, NationAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Ship, ShipAdmin)
admin.site.register(Item, ItemAdmin)