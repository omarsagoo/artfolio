from django.contrib import admin
from .models import Artwork

# Register your models here.
class ArtPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image', 'short_desc', 'long_desc', 'tag', 'time_posted', 'updated')

admin.site.register(Artwork)