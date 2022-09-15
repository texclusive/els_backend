from rest_framework import serializers
from .models import PriorityTracking, User, ExpressPriorityTracking, PriorityWithSigTracking, ExpressWithSigPriorityTracking, LabelData, FirstClassTracking 


# user serializer
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'pk'
        ]


# priority serializer
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


# express serializer
class ExpressPriorityTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpressPriorityTracking
        fields = [
            'express_priority',
            'user',
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


# first class
class FirstClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstClassTracking
        fields = [
            'first_class',
            'user',
            'pk'
            # 'user'
        ]


class FileUploadSerializer4(serializers.Serializer):
    file = serializers.FileField()


class SaveFileSerializer4(serializers.Serializer):
    class Meta:
        model = FirstClassTracking
        fields = [
            'first_class',
            'user'     
        ]

# class PriorityTrackingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PriorityTracking
#         fields = [
#             'priority',
#             'user',
#             'pk'
#             # 'user'
#         ]

class GeeksSerializer(serializers.Serializer):
    # initialize fields
    json_data = serializers.JSONField()
    
class LabelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabelData
        fields = [
            'senderData',
            ]

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LabelList
#         fields = ['mylist']