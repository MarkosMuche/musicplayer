
from django.contrib import admin
from . models import Song

class SongAdmin(admin.ModelAdmin):
      list_display = [field.name for field in Song._meta.fields]


admin.site.register(Song, SongAdmin)