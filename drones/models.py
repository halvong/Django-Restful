from django.db import models

#dronecategory = DroneCategory.objects.get(name="xxx")
#dronecategory.drone_set.all() w/o related_name
#dronecategory.drones.all() w/ related_name
class DroneCategory(models.Model):
    name = models.CharField(max_length=250)
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

#Drone.objects.filter(drone_category="xxx")
class Drone(models.Model):
    name = models.CharField(max_length=250)
    #drones refers to Drone class. DroneCategory.drones.all()
    drone_category = models.ForeignKey(DroneCategory, related_name='drones', on_delete=models.CASCADE)
    manufacturing_date = models.DateTimeField()
    has_it_competed = models.BooleanField(default=False)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

#pilot = Pilot.objects.get(name="xxx")
#pilot.competition_set.all() w/o related_name
#pilot.competitions.all() w/ related_name
class Pilot(models.Model):
    MALE = 'M'; FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'),)
    name = models.CharField(max_length=150, blank=False, default='')
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE)
    races_count = models.IntegerField()
    inserted_timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

#Pilot to many Competition
#Competition.objects.filter(pilot="xxx")
class Competition(models.Model):
    pilot = models.ForeignKey(Pilot, related_name='competitions', on_delete=models.CASCADE)
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    distance_in_feet = models.IntegerField()
    distance_achievement_date = models.DateTimeField()
    
    class Meta:
        # Order by distance in descending order
        ordering = ('-distance_in_feet',)