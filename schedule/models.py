from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название маршрута')
    start_point = models.CharField(max_length=100, verbose_name='Начальная станция')
    end_point = models.CharField(max_length=100, verbose_name='Конечная станция')

    def __str__(self):
        return self.name


class Schedule(models.Model):
    name = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.TimeField(verbose_name='Начало движения')
    arrival_time = models.TimeField(verbose_name='Окончание движения')
    interval = models.IntegerField(verbose_name='Интервал движения')

    def __str__(self):
        return f'{self.name} - {self.departure_time} to {self.arrival_time}'
