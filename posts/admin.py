from django.contrib import admin

# Register your models here.

from posts.models import Posts


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "update", "timestamp"]
    list_editable = ["title"]
    list_display_links = ["update"]
    list_filter = ["update","timestamp"]
    search_fields = ["contents"]

    class Meta:
        model = Posts


admin.site.register(Posts, PostModelAdmin)

