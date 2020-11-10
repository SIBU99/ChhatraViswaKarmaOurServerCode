from django.contrib import admin
from .models import (
    Farmer,
    Expert,
    Verify,
)
# Register your models here.

admin.site.register(Farmer)
admin.site.register(Expert)
admin.site.register(Verify)