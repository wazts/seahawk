from django.contrib import admin
from tags.models import Tag

class TagAdmin (admin.ModelAdmin):
	fields = ['time_created', 'user', 'beacon_tagged', 'ip']
	list_display = ('user', 'beacon_tagged', 'ip', 'time_created')

admin.site.register (Tag)
