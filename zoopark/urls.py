from django.urls import path

from .views import (ZooparkView,
                    AnimalView, AnimalViewID,
                    HumanView, HumanViewID,
                    PlaceView, PlaceViewID,
                    VarietyView, VaruetyViewID)

app_name = "zoopark"

# app_name поможет выполнить обратный поиск.
urlpatterns = [
    path('zoopark/', ZooparkView.as_view()),
    path('zoopark/variety/', VarietyView.as_view()),
    path('zoopark/variety/<int:pk>', VaruetyViewID.as_view()),
    path('zoopark/place/', PlaceView.as_view()),
    path('zoopark/place/<int:pk>', PlaceViewID.as_view()),
    path('zoopark/human/', HumanView.as_view()),
    path('zoopark/human/<int:pk>', HumanViewID.as_view()),
    path('zoopark/animal/', AnimalView.as_view()),
    path('zoopark/animal/<int:pk>', AnimalViewID.as_view()),
]
