from django.contrib import admin
from django.utils.html import format_html
from .models import BusinessDetails

admin.site.site_header = "JNPOnline Admin Panel"
admin.site.site_title = "JNPOnline Admin"
admin.site.index_title = "Welcome to JNPOnline Dashboard"

@admin.register(BusinessDetails)
class BusinessDetailsAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'owner_name', 'mobile_number', 'is_approved', 'approved_by', 'approve_button')
    list_filter = ('is_approved',)
    
    def approve_button(self, obj):
        """Display an approval/unapproval button in the admin panel."""
        if obj.is_approved:
            return format_html(f'<a class="button" href="/admin/businesses/{obj.id}/toggle_approval/">Unapprove</a>')
        return format_html(f'<a class="button" href="/admin/businesses/{obj.id}/toggle_approval/">Approve</a>')
    approve_button.allow_tags = True
    approve_button.short_description = "Approve/Unapprove"

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path('<int:business_id>/toggle_approval/', self.admin_site.admin_view(self.toggle_approval), name="toggle-approval"),
        ]
        return custom_urls + urls

    def toggle_approval(self, request, business_id):
        """Toggle the approval status when the admin clicks the button."""
        business = BusinessDetails.objects.get(id=business_id)
        business.toggle_approval(request.user)
        return self.response_post_save_change(request, business)
