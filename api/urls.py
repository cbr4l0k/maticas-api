from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


from .views import *

urlpatterns = [
    # ==== Org related
    path("org/new/",          OrgAPICreate.as_view(),       name="create_org"),        # POST
    path("org/<str:pk>/",     OrgAPIDetail.as_view(),       name="orgs_detail"),       # GET
    path("org/mod/<str:pk>/", OrgAPIDetailModify.as_view(), name="orgs_detail"),       # PUT
    path("org/del/<str:pk>/", OrgAPIDetailDelete.as_view(), name="orgs_detail"),       # DELETE

    # ==== Crop related
    path("crop/new/",          CropAPICreate.as_view(),       name="crop_create"),     # POST
    path("crop/<str:pk>/",     CropAPIDetail.as_view(),       name="crop_detail"),     # GET
    path("crop/mod/<str:pk>/", CropAPIDetailModify.as_view(), name="crop_modify"),     # PUT
    path("crop/del/<str:pk>/", CropAPIDetailDelete.as_view(), name="crop_delete"),     # DELETE

    # ==== Actuator related
    path("actuator/new/",          ActuatorAPICreate.as_view(),       name="actuator_create"),     # POST
    path("actuator/<str:pk>/",     ActuatorAPIDetail.as_view(),       name="actuator_detail"),     # GET
    path("actuator/mod/<str:pk>/", ActuatorAPIDetailModify.as_view(), name="actuator_modify"),     # PUT
    path("actuator/del/<str:pk>/", ActuatorAPIDetailDelete.as_view(), name="actuator_delete"),     # DELETE

    # ==== Actuator_type related
    path("actuatortype/new/",          Actuator_typeAPICreate.as_view(),       name="actuatortype_create"),     # POST
    path("actuatortype/<str:pk>/",     Actuator_typeAPIDetail.as_view(),       name="actuatortype_detail"),     # GET
    path("actuatortype/mod/<str:pk>/", Actuator_typeAPIDetailModify.as_view(), name="actuatortype_modify"),     # PUT
    path("actuatortype/del/<str:pk>/", Actuator_typeAPIDetailDelete.as_view(), name="actuatortype_delete"),     # DELETE

    # ==== Condition related
    path("condition/new/",          ConditionAPICreate.as_view(),       name="condition_create"),     # POST
    path("condition/<str:pk>/",     ConditionAPIDetail.as_view(),       name="condition_detail"),     # GET
    path("condition/mod/<str:pk>/", ConditionAPIDetailModify.as_view(), name="condition_modify"),     # PUT
    path("condition/del/<str:pk>/", ConditionAPIDetailDelete.as_view(), name="condition_delete"),     # DELETE

    # ==== Measurement related
    path("measurement/new/",          MeasurementAPICreate.as_view(),       name="measurement_create"),     # POST
    path("measurement/<str:pk>/",     MeasurementAPIDetail.as_view(),       name="measurement_detail"),     # GET
    path("measurement/mod/<str:pk>/", MeasurementAPIDetailModify.as_view(), name="measurement_modify"),     # PUT
    path("measurement/del/<str:pk>/", MeasurementAPIDetailDelete.as_view(), name="measurement_delete"),     # DELETE

    # ==== Variable related
    path("variable/new/",          VariableAPICreate.as_view(),       name="variable_create"),     # POST
    path("variable/<str:pk>/",     VariableAPIDetail.as_view(),       name="variable_detail"),     # GET
    path("variable/mod/<str:pk>/", VariableAPIDetailModify.as_view(), name="variable_modify"),     # PUT
    path("variable/del/<str:pk>/", VariableAPIDetailDelete.as_view(), name="variable_delete"),     # DELETE

    # ==== User related
    path('user/new/',        CreateUserView.as_view(), name='user_create'),
    path('user/login/',      UserLoginView.as_view(),  name='user_login'),
    path('user/token_auth/', obtain_auth_token,        name='user_api_token_auth'),
]

