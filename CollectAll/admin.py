from django.contrib import admin
from .models import Collection, CollectionType, CollectionItem, UserComment

# Register your models here.

admin.site.register(CollectionType)
admin.site.register(CollectionItem)
admin.site.register(UserComment)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
	list_display = ('name', 'collection_notes', 'CollectMember')
	fieldsets = (
		(None, {
			'fields': ('name', 'collection_notes', 'collection_favorite', 'CollectMember')
		}),
	)
