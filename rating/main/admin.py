from django.contrib import admin

from .models import Book,BookReview

# Register your models here.

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('is','name','author','rating','image')
admin.site.register(Book)


admin.site.register(BookReview)