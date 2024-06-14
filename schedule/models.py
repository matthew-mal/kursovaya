from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    name = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()

    def __str__(self):
        return f'{self.name} - {self.departure_time} to {self.arrival_time}'