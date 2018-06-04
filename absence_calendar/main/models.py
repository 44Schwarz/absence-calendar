from django.db import models

# Create your models here.


class Department(models.Model):
    # for company's departments
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    start_working = models.DateField
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)


class Period(models.Model):
    start_date = models.DateField
    end_date = models.DateField

    def __str__(self):
        return '{} - {}'.format(self.start_date, self.end_date)
