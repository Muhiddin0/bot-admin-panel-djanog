from main.models import Bot, User
from rest_framework import serializers



class BotListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = "__all__"

class BotCreateSerializer(serializers.Serializer):
    bot_tokken = serializers.CharField(max_length=1000)
    def validate(self, data):
        bot_tokken = data['bot_tokken']
        bot = Bot.objects.filter(bot_tokken=bot_tokken)
        if bool(bot):
            raise serializers.ValidationError('Bot already created')
            
        return data
    
    class Meta:
        model = Bot
        fields = ('bot_tokken',)

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ('bot', 'first_name', 'user_id')

class UserCreatedSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('first_name', 'user_id')