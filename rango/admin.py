from django.contrib import admin
from rango.models import Category, CatPage, Answers, AnswerUserLikes, AnswerUserDislikes, User, Subject
#, UserProfile


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'url')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes', 'slug', 'subject')
    prepopulated_fields = {'slug': ('name',)}


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('post_date', 'author', 'content', 'category')


class AnswerUserLikesAdmin(admin.ModelAdmin):
    list_display = ('user', 'time', 'answer')


class AnswerUserDislikesAdmin(admin.ModelAdmin):
    list_display = ('user', 'time', 'answer')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_superuser', 'date_joined', 'last_login')
    # list_filter = ('is_staff', 'is_superuser')


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('school_en', 'slug', 'url', 'name')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(CatPage, PageAdmin)
admin.site.register(Answers, AnswersAdmin)
admin.site.register(AnswerUserLikes, AnswerUserLikesAdmin)
admin.site.register(AnswerUserDislikes, AnswerUserDislikesAdmin)
admin.site.register(Subject, SubjectAdmin)



# admin.site.register(UserProfile)