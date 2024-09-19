from django.contrib import admin


from .models import UserConfirmation, User


class UserConfirmationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'confirmation_code', 'created_at')
    list_display_links = ('id', 'user')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('user', 'confirmation_code', 'created_at')
        return super().get_readonly_fields(request, obj)

    class Meta:
        model = UserConfirmation
        fields = ('user', 'confirmation_code', 'created_at')


admin.site.register(UserConfirmation, UserConfirmationAdmin)
