from django.contrib import admin
from ksports.models import Person, Sports, Message


class PersonAdmin(admin.ModelAdmin):
    '''person admin'''
    list_display = ('name', 'sports', 'update_time',)
    search_fields = ('name',)
    list_filter = ('update_time',)
    ordering = ('-update_time',)


class MessageAdmin(admin.ModelAdmin):
    '''message admin'''
    list_display = ('content', 'update_time',)
    search_fields = ('content',)
    list_filter = ('update_time',)
    ordering = ('-update_time',)


class SportsAdmin(admin.ModelAdmin):
    '''sports admin'''
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Person, PersonAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Sports, SportsAdmin)
