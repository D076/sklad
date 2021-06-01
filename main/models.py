from django.db import models

# Create your models here.


# Един измерения
class Unit(models.Model):
    name = models.CharField(max_length=50)
    abbrev = models.CharField(max_length=10)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.abbrev


class Mat(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class OrgList(models.Model):
    name = models.CharField(max_length=100)
    okpo = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class ResponsPerson(models.Model):
    name = models.CharField(max_length=100)
    func = models.CharField(max_length=30)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Storage(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    respons_person = models.ForeignKey(ResponsPerson, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class StorageMat(models.Model):
    count = models.DecimalField(max_digits=19, decimal_places=10)
    mat = models.ForeignKey(Mat, on_delete=models.DO_NOTHING)
    storage = models.ForeignKey(Storage, on_delete=models.DO_NOTHING)


class MatComing(models.Model):
    code = models.CharField(max_length=50)
    date = models.DateField()
    count = models.DecimalField(max_digits=19, decimal_places=10)
    mat = models.ForeignKey(Mat, on_delete=models.DO_NOTHING)
    storage = models.ForeignKey(Storage, on_delete=models.DO_NOTHING)
    org = models.ForeignKey(OrgList, on_delete=models.DO_NOTHING)


class MatDepart(models.Model):
    code = models.CharField(max_length=50)
    date = models.DateField()
    count = models.DecimalField(max_digits=19, decimal_places=10)
    mat = models.ForeignKey(Mat, on_delete=models.DO_NOTHING)
    storage = models.ForeignKey(Storage, on_delete=models.DO_NOTHING)
    org = models.ForeignKey(OrgList, on_delete=models.DO_NOTHING)
