from django.contrib import admin, auth
from models import DiceModel, RollButtonText, Games, Character

admin.site.register(DiceModel)
admin.site.register(RollButtonText)
admin.site.register(Games)
admin.site.register(Character)
