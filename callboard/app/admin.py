from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from django.db import models
# Register your models here.
from .models import Post, Response



class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Post, SomeModelAdmin)

admin.site.register(Response)