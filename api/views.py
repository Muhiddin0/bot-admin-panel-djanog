from main.models import Bot, User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializer import BotListSerializer, BotCreateSerializer, UserListSerializer, UserCreatedSerializer
from django.http import HttpResponse
import requests
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

# Create your views here.

def index(request):
    return HttpResponse("<h1>Salom ! APIga xush kelibsiz</h1>")
    
class BotViewSet(ViewSet):
    def list(self, request):
        queryset = Bot.objects.all()
        serializer = BotListSerializer(queryset, many=True)

        return Response(serializer.data, status=200)
    
    def post(self, request):
        data = [request.data]
        serialzier = BotCreateSerializer(data=data, many=True)
        if serialzier.is_valid():
            bot_data = requests.get(f'https://api.telegram.org/bot{data[0]["bot_tokken"]}/getMe').json()
            
            print('==================')
            print(bot_data)
            print('==================')

            if bot_data['ok'] == True:
                bot_data = bot_data['result']
            
                Bot.objects.create(
                    name = bot_data['first_name'],
                    username = bot_data['username'],
                    bot_id = bot_data['id'],
                    bot_tokken=data[0]['bot_tokken']
                )
                return Response(serialzier.data, status=200)
            return Response({
                'ok':False,
                'message':'bad bot tokken'
            }, status=400)

        return Response(serialzier.errors, status=400)

class BotRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotListSerializer
    lookup_field='bot_tokken'

    def delete(self, request, bot_tokken):
        bot =  get_object_or_404(Bot, bot_tokken=bot_tokken)
        bot.delete()
        return Response({'ok':True,'message':'bot deletee succesfuly'})


class UserView(APIView):
    def get(self, request, bot_tokken):
        bot = get_object_or_404(Bot, bot_tokken=bot_tokken)
        queryset = User.objects.filter(bot=bot)
        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, bot_tokken):
        data = request.data
        serializer = UserCreatedSerializer(data=request.data)
        bot = get_object_or_404(Bot, bot_tokken=bot_tokken)

        if serializer.is_valid():
            User.objects.create(
                first_name=data['first_name'],
                user_id=data['user_id'],
                bot=bot
            )
            return Response({
                'ok':True,
                'message':'user successfuly created'
            })
        return Response(serializer.errors)
    
    def delete(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return Response({'ok':True, 'message':'user succesfuly deleted'})
