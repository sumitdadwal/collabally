from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_looking_for_collaborator', 'profile_picture') # Fields to display in the list view
    list_filter = ('is_looking_for_collaborator',) # Fields to filter by in the sidebar
    search_fields = ('user__username', 'user__email') # Fields to search by

admin.site.register(Profile, ProfileAdmin)

