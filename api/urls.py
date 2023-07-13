
from django.urls import path, include
from .views import index, BotViewSet, BotRetrieveUpdateDestroyView, UserView

urlpatterns = [
    path('', index),
    path('bots/', BotViewSet.as_view({'get':'list', 'post':'post'})),
    path('bots/<str:bot_tokken>/', BotRetrieveUpdateDestroyView.as_view()),
    path('bots/<str:bot_tokken>/users', UserView.as_view()),
]
  