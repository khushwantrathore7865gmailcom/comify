from django.contrib import admin
from .models import Service,Feature_service,Baner,service_picture
# Register your models here.
admin.site.register(Service)
admin.site.register(Feature_service)
admin.site.register(Baner)
admin.site.register(service_picture)