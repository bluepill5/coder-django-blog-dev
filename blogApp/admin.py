from django.contrib import admin
from blogApp.models import *

# Modelos que se tiene acceso
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Article)
