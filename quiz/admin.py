from django.contrib import admin
from .models import Quiz
from .models import Player_info
from .models import Player_name
# Register your models here.
admin.site.register(Quiz)
admin.site.register(Player_info)
admin.site.register(Player_name)