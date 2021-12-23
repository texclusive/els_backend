from django.contrib import admin
from django.urls import path, include
from tracking.views import (
    ListPriorityTracking, 
    DeletePriorityTracking, 
    UploadPriorityTracking, 
    TrackingCount, 
    UserList, 
    DeleteUser,
    ListExpressPriorityTracking,
    DeleteExpressPriorityTracking,
    UploadExpressPriorityTracking,
    ExpressTrackingCount,
    SigPriorityTrackingCount,
    UploadSigPriorityTracking,
    ListSigPriorityTracking
    )
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', ListPriorityTracking.as_view(), name='test' ),
    path('delete/item/<str:priority>/', DeletePriorityTracking.as_view(), name='delete-item' ),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('api/token/auth/', CustomAuthToken.as_view(), name="custom-auth"),
    path('upload/', UploadPriorityTracking.as_view(), name='upload-priority'),
    path('tracking-count/', TrackingCount.as_view(), name='tracking-count'),
    path('user-list/', UserList.as_view(), name='user-list'),
    path('delete/user/<str:username>/', DeletePriorityTracking.as_view(), name='delete-item' ),

    # express

     path('express-tracking-count/', ExpressTrackingCount.as_view(), name='express-tracking-count'),
     path('express-tracking-list/', ListExpressPriorityTracking.as_view(), name='express-tracking-list' ),
     path('upload-express/', UploadExpressPriorityTracking.as_view(), name='upload-express'),
     path('delete/express/<str:express_priority>/', DeleteExpressPriorityTracking.as_view(), name='delete-express'),


     #priority
     path('psig-tracking-count/', SigPriorityTrackingCount.as_view(), name='psig-tracking-count'),
     path('upload-priority-sig/', UploadSigPriorityTracking.as_view(), name='upload-prior-sig'),
     path('psig-tracking-list/', ListSigPriorityTracking.as_view(), name='psig-tracking-list' ),


     
    
]
