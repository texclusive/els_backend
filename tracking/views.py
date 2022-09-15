from ast import Store
import io, csv, pandas as pd
from django.dispatch import receiver
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status, mixins
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from turtle import width
from .serializer import (
    PriorityTrackingSerializer, 
    FileUploadSerializer, 
    FileUploadSerializer1, 
    FileUploadSerializer2, 
    FileUploadSerializer3, 
    FileUploadSerializer4,
    UserListSerializer, 
    ExpressPriorityTrackingSerializer, 
    SigPriorityTrackingSerializer, 
    SigExpressTrackingSerializer,
    FirstClassSerializer,
    # LabelDataSerializer,
    # GeeksSerializer
    )
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import (
    User,
    PriorityTracking,  
    ExpressPriorityTracking, 
    PriorityWithSigTracking, 
    ExpressWithSigPriorityTracking,
    FirstClassTracking,
    # LabelData
    )
from django.db import IntegrityError
from rest_framework.authentication import (
    SessionAuthentication, 
    BasicAuthentication, 
    TokenAuthentication)                                                            
from rest_framework.pagination import PageNumberPagination
from fpdf import FPDF, HTMLMixin
from django.http import FileResponse, HttpResponse
from rest_framework.exceptions import ParseError
 


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 50


class FirstClasTrackingCount(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                qs = FirstClassTracking.objects.filter(user_id=request.user.id).count() 
        return Response({"fcount" : qs})


class UploadFirstClassTracking(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FileUploadSerializer4
   
    def post(self, request, *args, **kwargs):
        mydata = []
        # Get user trying to upload tracking
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                requested_user = ss.user
                
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
   
        if not file.name.endswith('.csv'):
            return Response({"status": "unsupported file"}, status.HTTP_406_NOT_ACCEPTABLE) 

        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = FirstClassTracking(
                       first_class = row[0],
                       user = requested_user
                       )
            mydata.append(new_file)
            if len(new_file.first_class) < 26:
                return Response({"status": "forbidden",
                                "incomplete_number": f"{new_file.first_class}"}, status.HTTP_403_FORBIDDEN)

        for number in mydata:
            if FirstClassTracking.objects.filter(first_class=number.first_class).exists():
                return Response({"existed_number": number.first_class})

        try:
            # new_file.save()
            FirstClassTracking.objects.bulk_create(mydata)
            return Response({"success": "success"}, status.HTTP_201_CREATED)
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args):
                return Response({"status": "duplicate found"}, status.HTTP_403_FORBIDDEN)
                    
        return Response({"status": "success"}, status.HTTP_201_CREATED)


# Delete all first class
class DeleteAllFirstClassNumber(APIView):
    def delete(self, request, *args, **kwargs):
        # incomplete....filter deletion by user
        qs = FirstClassTracking.objects.all()
        qs.delete()
        return Response('You have sucessfully deleted all express with sig numbers')


# Delete selected first class numbers
class DeleteSingleFirstClassNumber(APIView):
    def delete(self, request, selected=None):
        selectedNumber = selected.split(",") 
        for index in range(0, len(selectedNumber)):
            qs = FirstClassTracking.objects.filter(first_class=selectedNumber[index])
            qs.delete()
        return Response('Successfully deleted')


class ListFirstClassTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = FirstClassTracking.objects.all()
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                qs = FirstClassTracking.objects.filter(user_id=ss.user.pk)[:10]

        serializer = FirstClassSerializer(qs, many=True)
        if request.user:
            return Response(serializer.data)


class FirstClassTrackingSets(generics.ListAPIView):
    # queryset = ExpressWithSigPriorityTracking.objects.all()
    serializer_class = FirstClassSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user_id = self.request.user.id
        return FirstClassTracking.objects.filter(user_id=user_id)

class DeleteFirstClassTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, first_class=None):
        qs = FirstClassTracking.objects.filter(first_class=first_class)
        if qs.exists():
            qs.delete()
            return Response('number has been successfully deleted')
        else:
            raise ParseError('number has been used')


# Delete all express with sig numbers
class DeleteAllExpressWithSigNumber(APIView):
    def delete(self, request, *args, **kwargs):
        qs = ExpressWithSigPriorityTracking.objects.all()
        qs.delete()
        return Response('You have sucessfully deleted all express with sig numbers')


# Delete selected express with sig numbers
class DeleteFromExpressWithSigNumber(APIView):
    def delete(self, request, selected=None):
        selectedNumber = selected.split(",") 
        for index in range(0, len(selectedNumber)):
            qs = ExpressWithSigPriorityTracking.objects.filter(express_priority_with_sig=selectedNumber[index])
            qs.delete()
        return Response('Working.....now on express with sig numbers')


class ExpressWithSigTrackingSets(generics.ListAPIView):
    # queryset = ExpressWithSigPriorityTracking.objects.all()
    serializer_class = SigExpressTrackingSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user_id = self.request.user.id
        return ExpressWithSigPriorityTracking.objects.filter(user_id=user_id)



# Delete all priority with sig numbers
class DeleteAllPriorityWithSigNumber(APIView):
    def delete(self, request, *args, **kwargs):
        qs = PriorityWithSigTracking.objects.all()
        qs.delete()
        return Response('You have sucessfully deleted all priority with sig numbers')


# Delete selected priority with sig numbers
class DeleteFromPriorityWithSigNumber(APIView):
    def delete(self, request, selected=None):
        selectedNumber = selected.split(",") 
        for index in range(0, len(selectedNumber)):
            qs = PriorityWithSigTracking.objects.filter(priority_with_sig=selectedNumber[index])
            qs.delete()
            # print(selectedNumber[index])
        return Response('Working.....now on priority with sig numbers')


class PriorityWithSigTrackingSets(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # queryset = PriorityWithSigTracking.objects.all()
    serializer_class = SigPriorityTrackingSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user_id = self.request.user.id
        return PriorityWithSigTracking.objects.filter(user_id=user_id)

    

#Delete all express numbers
class DeleteAllPriorityExpressNumber(APIView):
    def delete(self, request, *args, **kwargs):
        qs = ExpressPriorityTracking.objects.all()
        # qs.delete()
        print(qs)
        return Response('You have sucessfully deleted all express numbers')


#Delete selected express number
class DeleteFromPriorityExpressTrackingList(APIView):
    def delete(self, request, selected=None):
        selectedNumber = selected.split(",") 
        for index in range(0, len(selectedNumber)):
            qs = ExpressPriorityTracking.objects.filter(express_priority=selectedNumber[index])
            qs.delete()
            print(selectedNumber[index])
        return Response('Working.....now on express')


class ExpressPriorityTrackingSets(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # queryset = ExpressPriorityTracking.objects.all()
    serializer_class = ExpressPriorityTrackingSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user_id = self.request.user.id
        return ExpressPriorityTracking.objects.filter(user_id=user_id)


#Delete all priority numbers
class DeleteAllPriorityNumber(APIView):
    def delete(self, request, *args, **kwargs):
        qs = PriorityTracking.objects.all()
        qs.delete()
        return Response('You have sucessfully deleted all numbers now now')


# Delete selected priority numbers
class DeleteFromPriorityTrackingList(APIView):
    def delete(self, request, selected=None):
        selectedNumber = selected.split(",") 
        for index in range(0, len(selectedNumber)):
            qs = PriorityTracking.objects.filter(priority=selectedNumber[index])
            qs.delete()
        return Response('Successfully deleted')


class PriorityTrackingSets(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # queryset = PriorityTracking.objects.all()
    serializer_class = PriorityTrackingSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user_id = self.request.user.id
        return PriorityTracking.objects.filter(user_id=user_id)


# priority
class DeleteUser(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    def delete(self, request, user_id=None):
        try:
            qs = User.objects.filter(pk=user_id)
            print(qs)
            qs.delete()
            # # print(user_pk)
        
            return Response('User has been deleted')
        except PriorityTracking.DoesNotExist:
            return Response('User does not exist')


class UserList(APIView):
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        serializer = UserListSerializer(qs, many=True)
        return Response(serializer.data)


class TrackingCount(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                qs = PriorityTracking.objects.filter(user_id=request.user.id).count()
            
        return Response({"pcount" : qs})

class UploadPriorityTracking(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FileUploadSerializer
   
    def post(self, request, *args, **kwargs):
        mydata = []
        # Get user trying to upload tracking
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                requested_user = ss.user
                
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
   
        if not file.name.endswith('.csv'):
            return Response({"status": "unsupported file"}, status.HTTP_406_NOT_ACCEPTABLE) 

        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = PriorityTracking(
                       priority = row[0],
                    #    priority = row['priority'],
                       user = requested_user
                       )
            mydata.append(new_file)
            if len(new_file.priority) < 26:
                return Response({"status": "forbidden",
                                "incomplete_number": f"{new_file.priority}"}, status.HTTP_403_FORBIDDEN)

        for number in mydata:
            if PriorityTracking.objects.filter(priority=number.priority).exists():
                return Response({"existed_number": number.priority})

        try:
            # new_file.save()
            PriorityTracking.objects.bulk_create(mydata)
            return Response({"success": "success"}, status.HTTP_201_CREATED)
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args):
                return Response({"status": "duplicate found"}, status.HTTP_403_FORBIDDEN)
                    
        return Response({"status": "success"}, status.HTTP_201_CREATED)


class DeletePriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, priority=None):
        qs = PriorityTracking.objects.filter(priority=priority)
        if qs.exists():
            qs.delete()
            return Response('number has been successfully deleted')
        else:
            raise ParseError('number has been used')


        # qs = PriorityTracking.objects.get(priority=priority)
        # qs.delete()
        # return Response('Tracking deleted')
        # snippet = self.get_object(pk)
        # snippet.delete()


class ListPriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = PriorityTracking.objects.all()
        # content = {
        #     'user': str(request.user),  # `django.contrib.auth.User` instance.
        #     'auth': str(request.auth),  # None
        # }
        # print(content)
        # token = Token.objects.get_or_create(user=user)
        # print(request.user.id)
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            # print(ss)
            if ss.user.pk == request.user.id:
                # print(ss.user.pk)
                qs = PriorityTracking.objects.filter(user_id=ss.user.pk)[:10]

        # y = User.objects.filter(id=request.user.id)
        # print(y)
        # ss, token = Token.objects.get_or_create(user=y)
        serializer = PriorityTrackingSerializer(qs, many=True)
        if request.user:
            return Response(serializer.data)
        # data = {
        #     'name': 'Paul',
        #     'age': 30
        # }
        # return Response(data)

    # def post(self, request, *args, **kwargs):
    #     serializer = PriorityTrackingSerializer(data=request.data)
    #     # print(serializer.data['priority'])
    #     if serializer.is_valid():
          
    #         sw = serializer.data['priority'] = "92055903419874465273204333"
    #         print(sw)
    #         # serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)


    # def get(self, request, format=None):
    #     content = {
    #         'user': str(request.user),  # `django.contrib.auth.User` instance.
    #         'auth': str(request.auth),  # None
    #     }
    #     return Response(content)




# class TestView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     permission_classes = (IsAuthenticated, )

#     serializer_class = PriorityTrackingSerializer
#     queryset = PriorityTracking.objects.filter(user=2)

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
        

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class Upload(APIView):
#     permission_classes = (IsAuthenticated, )

#     def get(self, request, *args, **kwargs):
#         qs = PriorityTracking.objects.all()
#         serializer = PriorityTrackingSerializer(qs, many=True)
#         return Response(serializer.data)
#         # data = {
#         #     'name': 'Paul',
#         #     'age': 30
#         # }
#         # return Response(data)

#     def post(self, request, *args, **kwargs):
#         serializer = PriorityTrackingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

 
# class CustomAuthToken(ObtainAuthToken):
#     def get(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })



# priorityWithSig
class SigPriorityTrackingCount(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        # for user in User.objects.all():
        #     ss, token = Token.objects.get_or_create(user=user)
        #     if ss.user.pk == request.user.id:
        qs = PriorityWithSigTracking.objects.filter(user_id=request.user.id).count()
        return Response({"psigcount" : qs})



class UploadSigPriorityTracking(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = FileUploadSerializer2
   
    def post(self, request, *args, **kwargs):
        # Get user trying to upload tracking
        mydata = []

        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                requested_user = ss.user
                
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
   
        if not file.name.endswith('.csv'):
            return Response({"status": "unsupported file"}, status.HTTP_406_NOT_ACCEPTABLE) 

        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = PriorityWithSigTracking(
                       priority_with_sig = row[0],
                    #    priority = row['priority'],
                       user = requested_user
                       )
            mydata.append(new_file)
            if len(new_file.priority_with_sig) < 26:
                return Response({"status": "forbidden",
                                "incomplete_number": f"{new_file.priority_with_sig}"}, status.HTTP_403_FORBIDDEN)

        
        for number in mydata:
            if PriorityWithSigTracking.objects.filter(priority_with_sig=number.priority_with_sig).exists():
                return Response({"existed_number": number.priority_with_sig})
                 

        try:
            PriorityWithSigTracking.objects.bulk_create(mydata)
            return Response({"success": "success"}, status.HTTP_201_CREATED)
            # new_file.save()
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args):
                return Response({"status": "duplicate found"})

        return Response({"status": "success"}, status.HTTP_201_CREATED)


class DeleteSigPriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, priority_with_sig=None):
        qs = PriorityWithSigTracking.objects.filter(priority_with_sig=priority_with_sig)
        if qs.exists():
            qs.delete()
            return Response('number has been successfully deleted')
        else:
            raise ParseError('number has been used')



class ListSigPriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = PriorityWithSigTracking.objects.all()
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                qs = PriorityWithSigTracking.objects.filter(user_id=ss.user.pk)[:10]

        serializer = SigPriorityTrackingSerializer(qs, many=True)
        if request.user:
            return Response(serializer.data)





# express
class ExpressTrackingCount(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                qs = ExpressPriorityTracking.objects.filter(user_id=request.user.id).count()
        return Response({"pcountexp" : qs})



class UploadExpressPriorityTracking(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FileUploadSerializer1
   
    def post(self, request, *args, **kwargs):
        mydata = []
        # Get user trying to upload tracking
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                requested_user = ss.user
                
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
   
        if not file.name.endswith('.csv'):
            return Response({"status": "unsupported file"}, status.HTTP_406_NOT_ACCEPTABLE) 

        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = ExpressPriorityTracking(
                       express_priority = row[0],
                    #    priority = row['priority'],
                       user = requested_user
                       )
            mydata.append(new_file)

            if len(new_file.express_priority) < 26:
                return Response({"status": "forbidden",
                                "incomplete_number": f"{new_file.express_priority}"}, status.HTTP_403_FORBIDDEN)

        for number in mydata:
            if ExpressPriorityTracking.objects.filter(express_priority=number.express_priority).exists():
                return Response({"existed_number": number.express_priority})

        try:
            ExpressPriorityTracking.objects.bulk_create(mydata)
            return Response({"success": "success"}, status.HTTP_201_CREATED)
            # new_file.save()
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args):
                return Response({"status": "duplicate found"}, status.HTTP_403_FORBIDDEN)

        return Response({"status": "success"}, status.HTTP_201_CREATED)


class DeleteExpressPriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, express_priority=None):
        qs = ExpressPriorityTracking.objects.filter(express_priority=express_priority)
        if qs.exists():
            qs.delete()
            return Response('number has been successfully deleted')
        else:
            raise ParseError('number has been used')
            # return Response('no match found')

        # qs.delete()
        
        # try:
        #     qs = ExpressPriorityTracking.objects.get(express_priority=express_priority)
        #     qs.delete()
        #     return Response('Tracking deleted')
        # except ExpressPriorityTracking.DoesNotExist:
        #     return Response('Tracking not found')


class ListExpressPriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = ExpressPriorityTracking.objects.all()
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                qs = ExpressPriorityTracking.objects.filter(user_id=ss.user.pk)[:10]

        serializer = ExpressPriorityTrackingSerializer(qs, many=True)
        if request.user:
            return Response(serializer.data)




# express with sig
class SigExpressTrackingCount(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                qs = ExpressWithSigPriorityTracking.objects.filter(user_id=request.user.id).count()
        return Response({"pcountexpsig" : qs})



class UploadSigExpressPriorityTracking(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = FileUploadSerializer3
   
    def post(self, request, *args, **kwargs):
        mydata = []
        # Get user trying to upload tracking
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                requested_user = ss.user
                
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
   
        if not file.name.endswith('.csv'):
            return Response({"status": "unsupported file"}, status.HTTP_406_NOT_ACCEPTABLE) 

        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = ExpressWithSigPriorityTracking(
                       express_priority_with_sig = row[0],
                       user = requested_user
                       )
            mydata.append(new_file)

            if len(new_file.express_priority_with_sig) < 26:
                return Response({"status": "forbidden",
                                "incomplete_number": f"{new_file.express_priority_with_sig}"})
        
                
            # elif ExpressWithSigPriorityTracking.objects.filter(express_priority_with_sig=new_file.express_priority_with_sig).exists():
            #     print(ExpressWithSigPriorityTracking.objects.filter(express_priority_with_sig=new_file.express_priority_with_sig).exists())
            #     return Response({"status": "Duplicate data found"}, status.HTTP_404_FORBIDDEN)

            # try:
            #     ExpressWithSigPriorityTracking.objects.bulk_create([new_file])
            #     # new_file.save()
            # except IntegrityError as e:
            #     if 'UNIQUE constraint' in str(e.args):
            #         return Response({"status": "duplicate found"}, status.HTTP_403_FORBIDDEN)
        for number in mydata:
            # print(x.express_priority_with_sig)
            if ExpressWithSigPriorityTracking.objects.filter(express_priority_with_sig=number.express_priority_with_sig).exists():
                return Response({"status": "Duplicate data found",
                                 "existed_number": f"{number.express_priority_with_sig}"})

        try:
            ExpressWithSigPriorityTracking.objects.bulk_create(mydata)
            return Response({"success": "success"}, status.HTTP_201_CREATED)
            # new_file.save()
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e.args):
                return Response({"status": "duplicate found"}, status.HTTP_403_FORBIDDEN)

        # return Response({"success": "success"}, status.HTTP_201_CREATED)


class DeleteSigExpressPriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, express_priority_with_sig=None):
        qs = ExpressWithSigPriorityTracking.objects.filter(express_priority_with_sig=express_priority_with_sig)
        if qs.exists():
            qs.delete()
            return Response('number has been successfully deleted')
        else:
            raise ParseError('number has been used')
             


class ListSigExpressPriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = ExpressPriorityTracking.objects.all()
        for user in User.objects.all():
            ss, token = Token.objects.get_or_create(user=user)
            if ss.user.pk == request.user.id:
                qs = ExpressWithSigPriorityTracking.objects.filter(user_id=ss.user.pk)[:10]

        serializer = SigExpressTrackingSerializer(qs, many=True)
        if request.user:
            return Response(serializer.data)


class StoreData:
    my_store = 'red'

    def __init__(self, x):
        self.x = x

    def show(self):
        print(f"{self.x}")

class MyFPDF(FPDF, HTMLMixin):
	pass


def report(request):
    get_stored_data = StoreData.my_store
    senders_data = get_stored_data[0]
    receiver_data = get_stored_data[1]
    weight = get_stored_data[2]
    barcode_target = get_stored_data[3]
    number_data = get_stored_data[4]
    today_date = get_stored_data[5]
    sender_name = get_stored_data[6]
    senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
    receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

    pdf = MyFPDF('L', 'mm', 'letter')
    pdf.add_page()
    pdf.set_font('helvetica', '', 15)
    pdf.set_line_width(0.8)
    pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
    pdf.image("media/images/1p.jpg", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
    pdf.line(98.55, 55.3, 252.45, 55.3)
    pdf.image("media/images/p2.png", x = 98.70, y = 55.75, w = 153.20, h = 0, type = '', link = '')
    pdf.line(98.55, 70.5, 252.45, 70.5)
    pdf.set_xy(98.55, 73)
    pdf.set_xy(204.5, 72.5)
    pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')


    pdf.set_xy(212, 80)
    pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
    
    for index in range(len(senders_info)):
        for key in senders_info[index]: 
            incre_by_one = index * 6
            incre = 73 + incre_by_one
            pdf.set_xy(99, incre)
            pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

    for index in range(len(receivers_info)):
        for key in receivers_info[index]:
            incre_by_one = index * 6
            incre = 119.5 + incre_by_one
            pdf.set_xy(118.5, incre)
            pdf.set_font('helvetica', '', 14.8)
            pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

    pdf.line(98.55, 153, 252.45, 153)
    pdf.set_font('helvetica', 'B', 12)  
    pdf.text(155.4, 159, 'USPS TRACKING #EP')
    # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=12.2&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
    pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
    # pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=4.72&bc4=1.2&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
    pdf.set_font('helvetica', 'B', 13.5)  
    pdf.text(137.5, 197, "{}".format(number_data))
    pdf.line(98.55, 198.55, 252.45, 198.55)
    pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
    pdf.output('{}.pdf'.format(sender_name), 'F')
    return FileResponse(open('{}.pdf'.format(sender_name), 'rb'), as_attachment=True, content_type='application/pdf')


def report_sig(request):
    get_stored_data = StoreData.my_store
    senders_data = get_stored_data[0]
    receiver_data = get_stored_data[1]
    weight = get_stored_data[2]
    barcode_target = get_stored_data[3]
    number_data = get_stored_data[4]
    today_date = get_stored_data[5]
    sender_name = get_stored_data[6]
    # print(x)
    senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
    receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

    pdf = MyFPDF('L', 'mm', 'letter')
    pdf.add_page()
    pdf.set_font('helvetica', '', 15)
    pdf.set_line_width(0.8)
    pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
    pdf.image("media/images/1p.jpg", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
    pdf.line(98.55, 55.3, 252.45, 55.3)
    pdf.image("media/images/p2.png", x = 98.70, y = 55.75, w = 153.20, h = 0, type = '', link = '')
    pdf.line(98.55, 70.5, 252.45, 70.5)
    pdf.set_xy(98.55, 73)
    # for line in sales:
    #     pdf.cell(170, 6, f"{line['item'].ljust(30)} {line['amount'].rjust(15)}", 0, 1,'L')
    pdf.set_xy(204.5, 72.5)
    pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')
    # pdf.cell(50, 6, "Ship Date:07/29/22", 0, 1,'L')

    pdf.set_xy(212, 80)
    pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
    
    for index in range(len(senders_info)):
        for key in senders_info[index]:
            incre_by_one = index * 6
            incre = 73 + incre_by_one
            pdf.set_xy(99, incre)
            pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

    for index in range(len(receivers_info)):
        for key in receivers_info[index]:
            incre_by_one = index * 6
            incre = 119.5 + incre_by_one
            pdf.set_xy(118.5, incre)
            pdf.set_font('helvetica', '', 14.8)
            pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')


    pdf.line(98.55, 153, 252.45, 153)
    pdf.set_font('helvetica', 'B', 12)  
    pdf.text(140.4, 159, 'USPS SIGNATURE TRACKING #EP')
    # pdf.image(image_url)
    # pdf.image("{}".format(image_url))
    pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=5.1&bc4=1.3&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
    pdf.set_font('helvetica', 'B', 13.5)  
    pdf.text(137.5, 197, "{}".format(number_data))
    # pdf.text(137.5, 197, '9210 3564 7281 3047 3532 7281 31')
    pdf.line(98.55, 198.55, 252.45, 198.55)
    pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
  
    pdf.output('{}.pdf'.format(sender_name), 'F')
    return FileResponse(open('{}.pdf'.format(sender_name), 'rb'), as_attachment=True, content_type='application/pdf')



def report_exp_sig(request):
    get_stored_data = StoreData.my_store
    senders_data = get_stored_data[0]
    receiver_data = get_stored_data[1]
    weight = get_stored_data[2]
    barcode_target = get_stored_data[3]
    number_data = get_stored_data[4]
    today_date = get_stored_data[5]
    sender_name = get_stored_data[6]
    senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
    receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

    pdf = MyFPDF('L', 'mm', 'letter')
    pdf.add_page()
    pdf.set_font('helvetica', '', 14.8)
    pdf.set_line_width(0.8)
    pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
    pdf.image("media/images/e.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
    pdf.line(98.55, 54.3, 252.45, 54.3)
    pdf.image("media/images/e2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
    pdf.line(98.55, 69.5, 252.45, 69.5)
    pdf.set_xy(98.55, 72)
    pdf.set_xy(204.5, 71.5)
    pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')


    pdf.set_xy(212, 79)
    pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
    
    for index in range(len(senders_info)):
        for key in senders_info[index]:
            incre_by_one = index * 6
            incre = 71 + incre_by_one
            pdf.set_xy(99, incre)
            pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')
    
    pdf.text(99, 102, 'SIGNATURE WAIVED')

    for index in range(len(receivers_info)):
        for key in receivers_info[index]:
            incre_by_one = index * 6
            incre = 119.5 + incre_by_one
            pdf.set_xy(118.5, incre)
            pdf.set_font('helvetica', '', 14.8)
            pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')


    
    pdf.line(98.55, 153, 252.45, 153)
    pdf.set_font('helvetica', 'B', 12)  
    pdf.text(155.4, 159, 'USPS TRACKING #EP')
    pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=4.72&bc4=1.2&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
    pdf.set_font('helvetica', 'B', 13.5)  
    pdf.text(137.5, 197, "{}".format(number_data))
    pdf.line(98.55, 198.55, 252.45, 198.55)
    pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
    pdf.output('{}.pdf'.format(sender_name), 'F')
    return FileResponse(open('{}.pdf'.format(sender_name), 'rb'), as_attachment=False, content_type='application/pdf')



def report_exp(request):
    get_stored_data = StoreData.my_store
    senders_data = get_stored_data[0]
    receiver_data = get_stored_data[1]
    weight = get_stored_data[2]
    barcode_target = get_stored_data[3]
    number_data = get_stored_data[4]
    today_date = get_stored_data[5]
    sender_name = get_stored_data[6]
    senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
    receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

    pdf = MyFPDF('L', 'mm', 'letter')
    pdf.add_page()
    pdf.set_font('helvetica', '', 14.8)
    pdf.set_line_width(0.8)
    pdf.rect(98.10, 12.95, 154.40, 197.5, style = '')
    pdf.image("media/images/e.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
    pdf.line(98.55, 54.3, 252.45, 54.3)
    pdf.image("media/images/e2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
    pdf.line(98.55, 69.5, 252.45, 69.5)
    pdf.set_xy(98.55, 72)
    pdf.set_xy(204.5, 71.5)
    pdf.cell(50, 6, "Ship Date:{}".format(today_date), 0, 1,'L')


    pdf.set_xy(212, 79)
    pdf.cell(40, 3, "Weight: {} lb".format(weight), 0, 1,'R')
    
    for index in range(len(senders_info)):
        for key in senders_info[index]:
            incre_by_one = index * 6
            incre = 71 + incre_by_one
            pdf.set_xy(99, incre)
            pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')
    
    pdf.text(99, 102, 'SIGNATURE WAIVED')

    for index in range(len(receivers_info)):
        for key in receivers_info[index]:
            incre_by_one = index * 6
            incre = 119.5 + incre_by_one
            pdf.set_xy(118.5, incre)
            pdf.set_font('helvetica', '', 14.8)
            pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')


    
    pdf.line(98.55, 153, 252.45, 153)
    pdf.set_font('helvetica', 'B', 12)  
    pdf.text(155.4, 159, 'USPS TRACKING #EP')
    pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=4.72&bc4=1.2&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 164.2, w = 140.45, h = 26.4, type = '', link = '')
    pdf.set_font('helvetica', 'B', 13.5)  
    pdf.text(137.5, 197, "{}".format(number_data))
    pdf.line(98.55, 198.55, 252.45, 198.55)
    pdf.image("media/images/s.jpg", x = 164.35, y = 200.5, w = 22, h = 8, type = '', link = '')
    pdf.output('{}.pdf'.format(sender_name), 'F')
    return FileResponse(open('{}.pdf'.format(sender_name), 'rb'), as_attachment=False, content_type='application/pdf')


def report_fc(request):
    get_stored_data = StoreData.my_store
    senders_data = get_stored_data[0]
    receiver_data = get_stored_data[1]
    weight = get_stored_data[2]
    barcode_target = get_stored_data[3]
    number_data = get_stored_data[4]
    today_date = get_stored_data[5]
    sender_name = get_stored_data[6]
    senders_info =list(map(lambda x:{x[0]:x[1]},senders_data.items() ))
    receivers_info =list(map(lambda x:{x[0]:x[1]},receiver_data.items() ))

    pdf = MyFPDF('L', 'mm', 'letter')
    pdf.add_page()
    pdf.set_font('helvetica', '', 14)
    pdf.set_line_width(0.8)
    pdf.rect(98.10, 12.95, 154.40, 196.20, style = '')
    pdf.image("media/images/f.png", x = 98.70, y = 13.60, w = 153.20, h = 0, type = '', link = '')
    pdf.line(98.55, 54.3, 252.45, 54.3)
    pdf.image("media/images/f2.png", x = 98.70, y = 54.75, w = 153.20, h = 0, type = '', link = '')
    pdf.line(98.55, 69.5, 252.45, 69.5)
    # pdf.set_xy(98.55, 72)
    pdf.set_xy(207, 71.5)
    pdf.cell(50, 5.7, "Ship Date:{}".format(today_date), 0, 1,'L')

    pdf.set_xy(211, 79)
    pdf.cell(40, 3, "Weight: {} oz".format(weight), 0, 1,'R')

    for index in range(len(senders_info)):
        for key in senders_info[index]:
            incre_by_one = index * 5.8
            incre = 71.5 + incre_by_one
            pdf.set_xy(99, incre)
            pdf.cell(170, 6, f"{senders_info[index][key].ljust(30)}", 0, 1,'L')

    pdf.set_font('helvetica', '', 14.8)
    for index in range(len(receivers_info)):
        for key in receivers_info[index]:
            incre_by_one = index * 6
            incre = 119 + incre_by_one
            pdf.set_xy(118.5, incre)
            pdf.set_font('helvetica', '', 15.4)
            pdf.cell(100, 6, f"{receivers_info[index][key].ljust(30)}", 0, 1, align='L')

    pdf.line(98.55, 151.5, 252.45, 151.5)
    pdf.set_font('helvetica', 'B', 10.5)  
    pdf.text(155.4, 158, 'USPS TRACKING #EP')
    pdf.image("http://free-barcode.com/barcode.asp?bc1={}&bc2=12&bc3=4.72&bc4=1.2&bc5=0&bc6=1&bc7=Arial&bc8=14&bc9=1".format(barcode_target), x = 105.85, y = 162.95, w = 140.45, h = 26.4, type = '', link = '')
    pdf.set_font('helvetica', 'B', 13.5)  
    pdf.text(137.5, 196, "{}".format(number_data))

    pdf.line(98.55, 197.10, 252.45, 197.10)
    pdf.image("media/images/s.jpg", x = 164.35, y = 199, w = 22, h = 8.5, type = '', link = '')
    pdf.output('{}.pdf'.format(sender_name), 'F')
    return FileResponse(open('{}.pdf'.format(sender_name), 'rb'), as_attachment=True, content_type='application/pdf')


# Delete selected express with sig numbers
class GetData(APIView):
    # serializer_class = FileUploadSerializer3
    def post(self, request, selected=None):
        incomingData = request.data
        StoreData.my_store = incomingData

        # return Response('http://127.0.0.1:8000/report')
        return Response('https://texclusive.herokuapp.com/report')

        

        # x = s[0]
        # print(x)
        # serializer = LabelDataSerializer(data=request.data)
        # if serializer.is_valid():
        #     print(serializer)
        #     # serializer.save()
        #     return Response('http://127.0.0.1:8000/report')
#             return Response(serializer.data)
        # y =list(map(lambda x:{x[0]:x[1]},x.items() ))
        # print(y)
           
        



# Delete selected express with sig numbers
class GetDataSig(APIView):
    # serializer_class = FileUploadSerializer3
    def post(self, request, selected=None):
        incomingData = request.data
        StoreData.my_store = incomingData
           
        # return Response('http://127.0.0.1:8000/report/sig')
        return Response('https://texclusive.herokuapp.com/report/sig')


# Delete selected express with sig numbers
class GetDataExp(APIView):
    # serializer_class = FileUploadSerializer3
    def post(self, request, selected=None):
        incomingData = request.data
        StoreData.my_store = incomingData
           
        # return Response('http://127.0.0.1:8000/report/exp')

        return Response('https://texclusive.herokuapp.com/report/exp')


# Delete selected express with sig numbers
class GetDataFirstClass(APIView):
    # serializer_class = FileUploadSerializer3
    def post(self, request, selected=None):
        incomingData = request.data
        StoreData.my_store = incomingData
           
        # return Response('http://127.0.0.1:8000/report/fc')

        return Response('https://texclusive.herokuapp.com/report/fc')


































# "p", "in", [5.27, 7.98]
      # if len(output) > row_height_lines:
        #     row_height_lines = len(output)
                
        # for tlines , datum in zip(lines_in_row, row):
        #     # here you can hack-in the
        #     text =datum.rstrip('\n') + (1 + row_height_lines - tlines) * '\n'
        #     pdf.multi_cell(col_width, line_height, text, border=0, ln=3)
        # pdf.ln(row_height_lines * line_height)

    # for row in data:
    #     row_height_lines = 1
    #     lines_in_row = []
    #     for datum in row: # determine height of highest cell
    #         output = pdf.multi_cell(col_width, line_height, datum, border=0, ln=3, split_only=True)
    #         print(len(output))
    #         lines_in_row.append(len(output))
    #         if len(output) > row_height_lines:
    #             row_height_lines = len(output)

    #     for tlines , datum in zip(lines_in_row, row):
    #         # here you can hack-in the
    #         text =datum.rstrip('\n') + (1 + row_height_lines - tlines) * '\n'
    #         pdf.multi_cell(col_width, line_height, text, border=0, ln=3)
    #     pdf.ln(row_height_lines * line_height)
    # index = 0
    # for line in salesd: 
    #     for key in line:
    #         print(index)
    #         pdf.set_xy(20, 105)
    #         pdf.cell(170, 6, f"{line[key].ljust(30)}", 0, 1, )
    # for line in salesd: 
    #     pdf.set_xy(20, 105)
    #     pdf.cell(170, 6, f"{line['item'].ljust(30)}", 0, 1, )
    # pdf.cell(10, 50, txt = 'John Do', border = 0, ln = 0, align = '', fill = False, link = '')
    # pdf.cell(10, 65, txt = '64 Ajegunle', border = 0, ln = 0, align = '', fill = False, link = '')
    # pdf.cell(10, 55, f"{'Item'} {'Amount'}", 0, 0)
    # pdf.text(10, 75, 'Barv')
    # pdf.cell(10, 100, 'This is what you have sold this month so far:',0,0)
    # pdf.cell(40, 10, '',0,1)
    # pdf.set_font('courier', '', 12)
    
    # pdf.line(10, 30, 150, 30)
    # pdf.line(10, 38, 150, 38)
    # for line in sales:
    #     pdf.cell(200, 8, f"{line['item'].ljust(30)} {line['amount'].rjust(20)}", 0, 1)








#  line_height = pdf.font_size * 1.5
#     col_width = pdf.epw /6   # distribute content evenly
#     row_height_lines = 1

#     # pdf.multi_cell(col_width, line_height, f"{datum['item']}", border=0, ln=3)
#     for datum in salesd:
#         pdf.multi_cell(col_width, line_height, datum['item'], border=0, ln=3)

   # pdf.set_font('arial', 'B', 20)
#     pdf.write_html("""
#    <table border="0" align="center" width="50%">
#         <thead>
#             <tr>
#                 <th width="100%"><img src="media/images/1p.jpg"/></th>            
#             </tr>
#         </thead>
#         <tbody>
#         <tbody>
#             <tr>
#                 <td><img src="media/images/p2.png"/></td> 
#             </tr>
            
#         </tbody>

        
#     </table>
# """)