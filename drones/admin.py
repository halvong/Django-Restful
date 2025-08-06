from django.contrib import admin

from .models import DroneCategory, Drone, Pilot, Competition


@admin.register(DroneCategory)
class DroneCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Drone)
class DroneAdmin(admin.ModelAdmin):
    list_display = ['name', 'drone_category', 'manufacturing_date', 'has_it_competed', 'inserted_timestamp', 'owner']
    raw_id_fields = ['owner']
    readonly_fields = ['owner']

@admin.register(Pilot)
class PilotAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'races_count', 'inserted_timestamp']

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ['pilot', 'drone', 'distance_in_feet', 'distance_achievement_date']
    raw_id_fields = ['pilot', 'drone']
