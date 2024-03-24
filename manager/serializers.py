from rest_framework import serializers
from manager.models import Manager
from django.contrib.auth.models import User


class ManagerListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Manager
        fields = 'id user full_name phone_number email count_transaction created_at'.split()

    def get_user(self, manager):
        return manager.user.username if manager.user else None
    
    def get_email(self, manager):
        return manager.user.email if manager.user else None


class ManagerCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    full_name = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=15)
    count_transaction = serializers.IntegerField(default=0)
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField(max_length=200)

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Username already exists")
        return username
    
    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")
        return email
    
    def validate_phone_number(self, phone_number):
        if Manager.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError("Phone number already exists")
        return phone_number
    
    def create(self, validated_data):
        username = validated_data['username']
        full_name = validated_data['full_name']
        phone_number = validated_data['phone_number']
        count_transaction = validated_data['count_transaction']
        email = validated_data['email']
        password = validated_data['password']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        manager = Manager.objects.create(
            user=user, 
            full_name=full_name, 
            phone_number=phone_number, 
            count_transaction=count_transaction
        )

        return manager
    

