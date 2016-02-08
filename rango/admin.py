from django.contrib import admin
from rango.models import Category, CatPage, Answers, AnswerUserLikes, AnswerUserDislikes
#, UserProfile


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'url')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('post_date', 'author', 'content', 'category')


class AnswerUserLikesAdmin(admin.ModelAdmin):
    list_display = ('answer', 'user', 'time')


class AnswerUserDislikesAdmin(admin.ModelAdmin):
    list_display = ('answer', 'user', 'time')


admin.site.register(Category, CategoryAdmin)
admin.site.register(CatPage, PageAdmin)
admin.site.register(Answers, AnswersAdmin)
admin.site.register(AnswerUserLikes, AnswerUserLikesAdmin)
admin.site.register(AnswerUserDislikes, AnswerUserDislikesAdmin)

# admin.site.register(UserProfile)