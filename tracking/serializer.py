from rest_framework import serializers
from .models import PriorityTracking, User, ExpressPriorityTracking, PriorityWithSigTracking, ExpressWithSigPriorityTracking, LabelData

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
            'email',
            'pk'
            
        ]


class ExpressPriorityTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpressPriorityTracking
        fields = [
            'express_priority',
            'user',
            
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


# ExpressWithSig
class SigExpressTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpressWithSigPriorityTracking
        fields = [
            'express_priority_with_sig',
            'user',
            'pk'
            # 'user'
        ]

class FileUploadSerializer3(serializers.Serializer):
    file = serializers.FileField()



class SaveFileSerializer3(serializers.Serializer):
    class Meta:
        model = ExpressWithSigPriorityTracking
        fields = [
            'express_priority_with_sig',
            'user'
            ]

class GeeksSerializer(serializers.Serializer):
    # initialize fields
    json_data = serializers.JSONField()
    
class LabelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabelData
        fields = [
            'senderData',
            ]
        