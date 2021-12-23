from rest_framework import serializers
from .models import PriorityTracking, User, ExpressPriorityTracking, PriorityWithSigTracking

class PriorityTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriorityTracking
        fields = [
            'priority',
            'user',
            'pk'
            # 'user'
        ]

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

   
class SaveFileSerializer(serializers.Serializer):
    
    class Meta:
        model = PriorityTracking
        fields = [
            'priority',
            'user'
            ]


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]


class ExpressPriorityTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpressPriorityTracking
        fields = [
            'express_priority',
            'user',
            'pk'
            # 'user'
        ]

class FileUploadSerializer1(serializers.Serializer):
    file = serializers.FileField()



class SaveFileSerializer1(serializers.Serializer):
    
    class Meta:
        model = ExpressPriorityTracking
        fields = [
            'express_priority',
            'user'
            ]


# priorityWithSig
class SigPriorityTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriorityWithSigTracking
        fields = [
            'priority_with_sig',
            'user',
            'pk'
            # 'user'
        ]

class FileUploadSerializer2(serializers.Serializer):
    file = serializers.FileField()



class SaveFileSerializer2(serializers.Serializer):
    class Meta:
        model = PriorityWithSigTracking
        fields = [
            'priority_with_sig',
            'user'
            ]