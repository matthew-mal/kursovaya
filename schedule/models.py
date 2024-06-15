from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название маршрута')

    def __str__(self):
        return self.name


class Schedule(models.Model):
    name = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name='Название маршрута')
    start_point = models.CharField(max_length=100, verbose_name='Начальная станция', blank=True)
    end_point = models.CharField(max_length=100, verbose_name='Конечная станция', blank=True)
    departure_time = models.TimeField(verbose_name='Начало движения')
    arrival_time = models.TimeField(verbose_name='Окончание движения')
    interval = models.IntegerField(verbose_name='Интервал движения')

    def __str__(self):
        return f'{self.name} - {self.start_point} to {self.end_point}'


class Station(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='stations')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TimeSlot(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='time_slots')
    departure_time = models.TimeField()
