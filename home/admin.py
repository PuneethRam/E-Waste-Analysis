from django.contrib import admin

from django.apps import apps
from .models import Resource
from .models import Recycle
from .models import EwasteLocation

# Register your models here.
admin.site.register(Resource)
admin.site.register(Recycle)
admin.site.register(EwasteLocation)


app_models = apps.get_app_config('home').get_models()
for model in app_models:
    try:    

        admin.site.register(model)

    except Exception:
        pass
