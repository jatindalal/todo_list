from django.contrib import admin
from .models import to_do_list, item

admin.site.register(to_do_list)
admin.site.register(item)
