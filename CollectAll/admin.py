from django.contrib import admin
from .models import Collection, CollectionType, CollectionItem, UserComment
# Register your models here.

admin.site.register(Collection)
admin.site.register(CollectionType)
admin.site.register(CollectionItem)
admin.site.register(UserComment)
