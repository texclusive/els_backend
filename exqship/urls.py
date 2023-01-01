from django.contrib import admin
from django.urls import path, include
# from backend.src.exqship.tracking.views import download_p
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
    FirstClasTrackingCount,
    ListFirstClassTracking,
    UploadFirstClassTracking,
    UploadSigPriorityTracking,
    ListSigPriorityTracking,
    DeleteSigPriorityTracking,
    SigExpressTrackingCount,
    UploadSigExpressPriorityTracking,
    ListSigExpressPriorityTracking,
    DeleteSigExpressPriorityTracking,
    PriorityTrackingSets,
    PriorityWithSigTrackingSets,
    ExpressPriorityTrackingSets,
    ExpressWithSigTrackingSets,
    FirstClassTrackingSets,
    DeleteAllPriorityNumber,
    DeleteAllFirstClassNumber,
    DeleteAllPriorityExpressNumber,
    DeleteAllPriorityWithSigNumber,
    DeleteAllExpressWithSigNumber,
    DeleteFromPriorityTrackingList,
    DeleteFromPriorityExpressTrackingList,
    DeleteFromPriorityWithSigNumber,
    DeleteFromExpressWithSigNumber,
    DeleteSingleFirstClassNumber,
    DeleteFirstClassTracking,
    GetData,
    GetDataSig,
    GetDataExp,
    GetDataExpressSig,
    GetDataFirstClass,
    GetDataBulk,
    download_p,
    download_ps,
    download_e,
    download_es,
    download_fc,
    FileCleanUp,
    download_p46,
    UploadPriorityBulk,
    DownloadPBulk,
    DownloadPPbulk

    )
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('rest-auth/password/change/', include('rest_auth.urls')),
    path('user-list/', UserList.as_view(), name='user-list'),
    # path('delete/user/<str:username>/', DeletePriorityTracking.as_view(), name='delete-item'),


    path('pbulk/', UploadPriorityBulk.as_view(), name='upload-bulk'),
    path('download/pbulk/', DownloadPBulk.as_view(), name='download-pbulk'),
    path('download/pbulk/p/<id>', DownloadPPbulk.as_view(), name='download-p-bulk'),


    # path('api/token/auth/', CustomAuthToken.as_view(), name="custom-auth"),
    path('tracking-count/', TrackingCount.as_view(), name='tracking-count'),
    path('p/list/', ListPriorityTracking.as_view(), name='test'),
    path('delete/item/<str:priority>/', DeletePriorityTracking.as_view(), name='delete-item'),
    path('upload/', UploadPriorityTracking.as_view(), name='upload-priority'),
   
   
    # express
    path('express-tracking-count/', ExpressTrackingCount.as_view(), name='express-tracking-count'),
    path('express-tracking-list/', ListExpressPriorityTracking.as_view(), name='express-tracking-list'),
    path('upload-express/', UploadExpressPriorityTracking.as_view(), name='upload-express'),
    path('delete/express/<str:express_priority>/', DeleteExpressPriorityTracking.as_view(), name='delete-express'),


    #priority with sig
    path('psig-tracking-count/', SigPriorityTrackingCount.as_view(), name='psig-tracking-count'),
    path('upload-priority-sig/', UploadSigPriorityTracking.as_view(), name='upload-prior-sig'),
    path('psig-tracking-list/', ListSigPriorityTracking.as_view(), name='psig-tracking-list'),
    path('delete/psig/<str:priority_with_sig>/', DeleteSigPriorityTracking.as_view(), name='delete-psig'),


    #express with sig
    path('sigexpress/tracking-count/', SigExpressTrackingCount.as_view(), name='sigexpress-tracking-count'),
    path('upload-sig-express/', UploadSigExpressPriorityTracking.as_view(), name='upload-sig-express'),
    path('express/sig/tracking-list/', ListSigExpressPriorityTracking.as_view(), name='sigexxprss-tracking-list'),
    path('delete/expwithsig/<str:express_priority_with_sig>/', DeleteSigExpressPriorityTracking.as_view(), name='delete-expsig'),
    path('priority/set/', PriorityTrackingSets.as_view(), name='priority_set'),
    path('priority/sig/set/', PriorityWithSigTrackingSets.as_view(), name='priority_with_sig_set'),
    path('express/set/', ExpressPriorityTrackingSets.as_view(), name='express_set'),
    path('express/sig/set/', ExpressWithSigTrackingSets.as_view(), name='express_sig_set'),
    path('first/class/set/', FirstClassTrackingSets.as_view(), name='first_class'),

    # first class
    path('first/class/tracking-count/', FirstClasTrackingCount.as_view(), name='first-class-tracking-count'),
    path('upload/first/class/', UploadFirstClassTracking.as_view(), name='upload-dirst-class'),
    path('delete/first/class/<str:selected>/', DeleteSingleFirstClassNumber.as_view(), name='deletefirstclass'),
    path('delete/all/first/class/', DeleteAllFirstClassNumber.as_view(), name='deleteallfirstclass'),
    path('first/class/list/', ListFirstClassTracking.as_view(), name='firstclassbyuser'),
    path('delete/fclass/<str:first_class>/', DeleteFirstClassTracking.as_view(), name='delete-fclass'),
    

    path('deletefromprioritylist/<str:selected>/', DeleteFromPriorityTrackingList.as_view(), name='deletefromprioritylist'),
    path('deleteallprioritynumbers/', DeleteAllPriorityNumber.as_view(), name='deletefromlist'),
    path('delete/all/express', DeleteAllPriorityExpressNumber.as_view(), name='deleteallexpressfromlist'),
    path('delete/express/number/<str:selected>/', DeleteFromPriorityExpressTrackingList.as_view(), name='deletefromexpresslist'),
    path('delete/all/priority/sig', DeleteAllPriorityWithSigNumber.as_view(), name='delete-all-express-list'),
    path('delete/priority/sig/<str:selected>/', DeleteFromPriorityWithSigNumber.as_view(), name='delete-priority-sig'),
    path('delete/all/express/sig', DeleteAllExpressWithSigNumber.as_view(), name='delete-all-express-sig'),
    path('delete/express/sig/<str:selected>/', DeleteFromExpressWithSigNumber.as_view(), name='delete-express-sig'),
    path('delete/verified-user/<int:user_id>/', DeleteUser.as_view(), name='user-delete'),  


    # Dowload links
    path('download/p/<id>', download_p, name='download_p'),
    path('download/ps/<id>', download_ps, name='download_ps'),
    path('download/e/<id>', download_e, name='download_e'),
    path('download/fc/<id>', download_fc, name='download_fc'),
    path('download/es/<id>', download_es, name='download_es'),

    
    # Links for getting data from user
    path('data/p', GetData.as_view(), name='datap'),  
    path('data/ps', GetDataSig.as_view(), name='dataps'),
    path('data/e', GetDataExp.as_view(), name='datapex'),
    path('data/fc', GetDataFirstClass.as_view(), name='datafcfc'),
    path('data/es', GetDataExpressSig.as_view(), name='dataes'),
    path('data/bp', GetDataBulk.as_view(), name='databp'),

 

    path('remove/store/files', FileCleanUp.as_view(), name='clear-data'), 

    # 4x6 links
    path('download/test', download_p46, name='clear-data'), 
]
