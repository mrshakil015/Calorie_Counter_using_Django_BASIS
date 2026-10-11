from django.contrib import admin
from calorie_counter_app.models import *


admin.site.register([UserProfileModel, ConsumedCalorieModel])