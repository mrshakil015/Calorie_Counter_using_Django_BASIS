from django.urls import path
from calorie_counter_app.views import *

urlpatterns = [
    path('', login_view, name='login_view'),
    path('register/',register_view, name='register_view'),
    path('logout/',logout_view, name='logout_view'),
    path('dashboard/', dashboard_view, name='dashboard_view'),

    path('profile/',profile_page, name='profile_page'),
    path('update-profile/',profile_update_view, name='profile_update_view'),

    path('calorie-consumed-list/',calorie_consumed_list,name='calorie_consumed_list'),
    path('add_consumed_calorie/',add_consumed_calorie, name='add_consumed_calorie'),
    path('update-consumed-calorie/<str:id>/',update_consumed_calorie, name='update_consumed_calorie'),
    path('delete-consumed-calorie/<str:id>/',delete_consumed_calorie, name='delete_consumed_calorie'),
]