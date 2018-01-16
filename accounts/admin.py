from django.contrib import admin
from accounts.models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_city', 'user_phone', 'user_description')

    def user_city(self, obj):
        return obj.city

    def user_phone(self, obj):
        return obj.phone

    def user_description(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('id')
        return queryset
    
admin.site.register(UserProfile, UserProfileAdmin)

