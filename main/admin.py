from django.contrib import admin
from .models import Mat, OrgList, Unit, ResponsPerson, Storage, StorageMat, MatComing, MatDepart
# Register your models here.
admin.site.register(Unit)
admin.site.register(Mat)
admin.site.register(OrgList)
admin.site.register(ResponsPerson)
admin.site.register(Storage)
admin.site.register(StorageMat)
admin.site.register(MatComing)
admin.site.register(MatDepart)
