from django.contrib import admin
from .models import Bloggers
from modeltranslation.admin import TranslationAdmin


# Register your models here.

class Admin(admin.ModelAdmin):
    list_display = ("name", "text")


class Bloggers_tr(TranslationAdmin):
    list_display = ("name", "text")


admin.site.register(Bloggers, Admin)
