from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from create.models import Create
from tinymce.widgets import TinyMCE
from django.db import models
from reversion.admin import VersionAdmin

@admin.register(Create)
class PostAdmin(VersionAdmin):
    pass

