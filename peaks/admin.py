from django.contrib import admin

from peaks.models import CustomUser, Pereval_added, Images, Coords, Level

admin.site.register(CustomUser)
admin.site.register(Pereval_added)
admin.site.register(Images)
admin.site.register(Coords)
admin.site.register(Level)
