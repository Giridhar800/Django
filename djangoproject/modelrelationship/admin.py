from django.contrib import admin
from modelrelationship.models import Book, Post, Dance

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['bookn', 'booka', 'bookpd', 'user']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['p_title', 'p_category', 'p_publishdate', 'user']

@admin.register(Dance)
class DanceAdmin(admin.ModelAdmin):
    list_display = ['dance_name', 'dance_duration', 'dance_by']