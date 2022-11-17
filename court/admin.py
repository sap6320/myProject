from django.contrib import admin
from .models import user_query,court,booking

# Register your models here.
admin.site.register(user_query)
admin.site.register(court)
admin.site.register(booking)
