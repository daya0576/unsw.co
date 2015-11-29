from django.contrib import admin
from rango.models import Category, Page, UserProfile



class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'url')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes', 'slug')
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)