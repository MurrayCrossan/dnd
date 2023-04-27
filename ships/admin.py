from django.contrib import admin
from .models import CrewMember,Ship

# Register your models here.

class CrewMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'species', 'ship', 'role', 'co', 'important')
    list_filter = (('ship', admin.RelatedOnlyFieldListFilter), ('important', admin.BooleanFieldListFilter),)
        

class ShipAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'noOfCrew')

    @admin.display(description="No Of Crew")
    def noOfCrew(self, obj):
        return len(obj.crewmember_set.all())


admin.site.register(Ship, ShipAdmin)
admin.site.register(CrewMember, CrewMemberAdmin)