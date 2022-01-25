import io, csv, pandas as pd
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status, mixins
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializer import (
    PriorityTrackingSerializer, 
    FileUploadSerializer, 
    FileUploadSerializer1, 
    FileUploadSerializer2, 
    FileUploadSerializer3, 
    UserListSerializer, 
    ExpressPriorityTrackingSerializer, 
    SigPriorityTrackingSerializer, 
    SigExpressTrackingSerializer
    )
from rest_framework.permissions import IsAuthenticated
from .models import (
    User,
    PriorityTracking,  
    ExpressPriorityTracking, 
    PriorityWithSigTracking, 
    ExpressWithSigPriorityTracking
    )
from django.db import IntegrityError
from rest_framework.authentication import (
    SessionAuthentication, 
    BasicAuthentication, 
    TokenAuthentication)                                                            
from rest_framework.pagination import PageNumberPagination



class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 1000



#Delete all express with sig numbers
class DeleteAllExpressWithSigNumber(APIView):
    def delete(self, request, *args, **kwargs):
        qs = ExpressWithSigPriorityTracking.objects.all()
        # qs.delete()
        print(qs)
        return Response('You have sucessfully deleted all express with sig numbers')


#Delete selected express with sig numbers
class DeleteFromExpressWithSigNumber(APIView):
    def delete(self, request, selected=None):
        selectedNumber = selected.split(",") 
        for index in range(0, len(selectedNumber)):
            qs = ExpressWithSigPriorityTracking.objects.filter(express_priority_with_sig=selectedNumber[index])
            print(qs, 'working')
            # qs.delete()
            print(selectedNumber[index])
        return Response('Working.....now on express with sig numbers')


class ExpressWithSigTrackingSets(generics.ListAPIView):
    # queryset = ExpressWithSigPriorityTracking.objects.all()
    serializer_class = SigExpressTrackingSerializer
    pagination_class = StandardResultsSetPagination


    def get_queryset(self):
        user_id = self.request.user.id
        return ExpressWithSigPriorityTracking.objects.filter(user_id=user_id)



#Delete all priority with sig numbers
class DeleteAllPriorityWithSigNumber(APIView):
    def delete(self, request, *args, **kwargs):
        qs = PriorityWithSigTracking.objects.all()
        # qs.delete()
        print(qs)
        return Response('You have sucessfully deleted all priority with sig numbers')


#Delete selected priority with sig numbers
class DeleteFromPriorityWithSigNumber(APIView):
    def delete(self, request, selected=None):
        selectedNumber = selected.split(",") 
        for index in range(0, len(selectedNumber)):
            qs = PriorityWithSigTracking.objects.filter(priority_with_sig=selectedNumber[index])
            print(qs, 'working')
            # qs.delete()
            print(selectedNumber[index])
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
            print(qs)
            # qs.delete()
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
        # qs.delete()
        print(qs)
        return Response('You have sucessfully deleted all numbers')


# Delete selected priority numbers
class DeleteFromPriorityTrackingList(APIView):
    def delete(self, request, selected=None):
        authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
        permission_classes = [IsAuthenticated]
        
        selectedNumber = selected.split(",") 
        for index in range(0, len(selectedNumber)):
            qs = PriorityTracking.objects.filter(priority=selectedNumber[index])
            print(qs)
            # qs.delete()
            print(selectedNumber[index])
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
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, user_id=None):
        try:
            qs = User.objects.get(user_id=user_id)
            qs.delete()
            return Response('User has been deleted')
        except PriorityTracking.DoesNotExist:
            return Response('User does not exist')



class UserList(APIView):
    def get(self, request, *args, **kwargs):
        qs = User.objects.all()
        print(qs)
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
            if len(new_file.priority) < 26:
                return Response({"status": "forbidden",
                                "priority": f"{new_file.priority}"}, status.HTTP_403_FORBIDDEN)
            try:
                # new_file.save()
                PriorityTracking.objects.bulk_create([new_file])
            except IntegrityError as e:
                if 'UNIQUE constraint' in str(e.args):
                    return Response({"status": "duplicate found"}, status.HTTP_403_FORBIDDEN)
                    
        return Response({"status": "success"}, status.HTTP_201_CREATED)


class DeletePriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, priority=None):
        try:
            qs = PriorityTracking.objects.get(priority=priority)
            qs.delete()
            return Response('Tracking deleted')
        except PriorityTracking.DoesNotExist:
            return Response('Tracking not found')


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
            if len(new_file.priority_with_sig) < 26:
                return Response({"status": "forbidden",
                                "priority_with_sig": f"{new_file.priority_with_sig}"}, status.HTTP_403_FORBIDDEN)

            elif PriorityWithSigTracking.objects.filter(priority_with_sig=new_file.priority_with_sig).exists():
                print(PriorityWithSigTracking.objects.filter(priority_with_sig=new_file.priority_with_sig).exists())

            try:
                PriorityWithSigTracking.objects.bulk_create([new_file])
                # new_file.save()
            except IntegrityError as e:
                if 'UNIQUE constraint' in str(e.args):
                    return Response({"status": "duplicate found"}, status.HTTP_403_FORBIDDEN)

        return Response({"status": "success"}, status.HTTP_201_CREATED)


class DeleteSigPriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, priority_with_sig=None):
        try:
            qs = PriorityWithSigTracking.objects.get(priority_with_sig=priority_with_sig)
            qs.delete()
            return Response('Tracking deleted')
        except PriorityWithSigTracking.DoesNotExist:
            return Response('Tracking not found')



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
            if len(new_file.express_priority) < 26:
                return Response({"status": "forbidden",
                                "express_priority": f"{new_file.express_priority}"}, status.HTTP_403_FORBIDDEN)
            try:
                ExpressPriorityTracking.objects.bulk_create([new_file])
                # new_file.save()
            except IntegrityError as e:
                if 'UNIQUE constraint' in str(e.args):
                    return Response({"status": "duplicate found"}, status.HTTP_403_FORBIDDEN)

        return Response({"status": "success"}, status.HTTP_201_CREATED)


class DeleteExpressPriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, express_priority=None):
        try:
            qs = ExpressPriorityTracking.objects.get(express_priority=express_priority)
            qs.delete()
            return Response('Tracking deleted')
        except ExpressPriorityTracking.DoesNotExist:
            return Response('Tracking not found')




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
                    #    priority = row['priority'],
                       user = requested_user
                       )
            if len(new_file.express_priority_with_sig) < 26:
                return Response({"status": "forbidden",
                                "express_priority_with_sig": f"{new_file.express_priority_with_sig}"}, status.HTTP_403_FORBIDDEN)
            try:
                ExpressWithSigPriorityTracking.objects.bulk_create([new_file])
                # new_file.save()
            except IntegrityError as e:
                if 'UNIQUE constraint' in str(e.args):
                    return Response({"status": "duplicate found"}, status.HTTP_403_FORBIDDEN)

        return Response({"status": "success"}, status.HTTP_201_CREATED)


class DeleteSigExpressPriorityTracking(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, express_priority_with_sig=None):
        try:
            qs = ExpressWithSigPriorityTracking.objects.get(express_priority_with_sig=express_priority_with_sig)
            qs.delete()
            return Response('Tracking deleted')
        except ExpressWithSigPriorityTracking.DoesNotExist:
            return Response('Tracking not found')




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















