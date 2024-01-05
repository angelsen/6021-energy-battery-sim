from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # Other fields as necessary

    def __str__(self):
        return self.name

class DutyCycle(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    # Other fields as necessary

    def __str__(self):
        return self.name
    
class Location(models.Model):
    duty_cycle = models.ForeignKey(DutyCycle, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    #address = models.TextField()
    # Other location-specific fields

    def __str__(self):
        return self.name

class OperatingSchedule(models.Model):
    duty_cycle = models.ForeignKey(DutyCycle, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    operating_loads = models.ManyToManyField('OperatingLoad', blank=True)

    def __str__(self):
        return f"{self.duty_cycle.name} Schedule"

class OperatingLoad(models.Model):
    duty_cycle = models.ForeignKey(DutyCycle, on_delete=models.CASCADE)
    load_type = models.CharField(max_length=100)
    load_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.load_type}: {self.load_value}"

