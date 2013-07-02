from django.contrib import admin
from movie.models import Movie, User, Comment


class MovieAdmin(admin.ModelAdmin):
    '''movie admin'''
    list_display = ('name', 'score', 'update_time', 'image', 'content', 'ftp', 'validate',)
    search_fields = ('name',)
    list_filter = ('update_time',)
    ordering = ('-update_time',)


class UserAdmin(admin.ModelAdmin):
    '''user admin'''
    list_display = ('name', 'email', 'passwd',)
    search_fields = ('name',)
    list_filter = ('email',)
    ordering = ('name',)


class CommentAdmin(admin.ModelAdmin):
    '''comment admin'''
    list_display = ('id', 'content', 'user', 'movie', 'pid',)
    search_fields = ('content',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
