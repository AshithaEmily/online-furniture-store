from django.contrib import admin
from koppee.models import admindb, catdb, furnituredb
# Register your models here.
admin.site.register(admindb)
admin.site.register(catdb)
admin.site.register(furnituredb)