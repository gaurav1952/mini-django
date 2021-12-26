from django.contrib import admin
from .models import  sotasks
admin.site.site_header = 'TO DO'
admin.site.site_title = 'TO DO APP '
# Register your models here.
admin.site.register(sotasks)
