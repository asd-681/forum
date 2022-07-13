from django.contrib import admin
from service.models import Post, Comment, Support
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)

class SupportAdmin(admin.ModelAdmin):
    list_display = ['header', 'question', 'type_question', 'date_create','application_status','date_change_status', 'user']
    list_editable = ['type_question','application_status']
    def save_model(self, request, obj):
        obj.user = request.user
        obj.save()

admin.site.register(Support, SupportAdmin)