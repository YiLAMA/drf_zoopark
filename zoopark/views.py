from django.shortcuts import render
# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Variety, Place, Human, Animal
from .serializers import VarietySerializer, PlaceSerializer, HumanSerializer, AnimalSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .service import AnimalFilter
from rest_framework import generics, status


class VaruetyViewID(generics.RetrieveAPIView):
    """Вид животного по ID"""
    serializer_class = VarietySerializer

    def get(self, request, pk):
        variety = Variety.objects.get(id=pk)
        serializer = VarietySerializer(variety)
        return Response({"Variety": serializer.data})

    def put(self, request, pk):
        saved_zoopark = get_object_or_404(Variety.objects.all(), pk=pk)
        # partial=True - даёт возможность обновлять только некоторые поля, но не обязательно все сразу.
        serializer = VarietySerializer(instance=saved_zoopark, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            variety_saved = serializer.save()
        return Response({
            "success": "Variety '{}' updated successfully".format(variety_saved.name)
        })

    def delete(self, request, pk):
        zoopark = get_object_or_404(Variety.objects.all(), pk=pk)
        zoopark.delete()
        return Response({
            "message": "Variety with id `{}` has been deleted.".format(pk)
        }, status=204)


class VarietyView(generics.ListAPIView):
    """Вид животного"""
    serializer_class = VarietySerializer

    def get(self, request):
        zoopark = Variety.objects.all()
        # параметр many сообщает сериализатору, что он будет сериализовать более одной статьи.
        serializer = VarietySerializer(zoopark, many=True)
        return Response({"Variety": serializer.data})

    def post(self, request):
        serializer = VarietySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlaceViewID(generics.RetrieveAPIView):
    """Место животного по ID"""
    serializer_class = PlaceSerializer

    def get(self, request, pk):
        places = Place.objects.get(id=pk)
        serializer = PlaceSerializer(places)
        return Response({"Place": serializer.data})

    def put(self, request, pk):
        saved_zoopark = get_object_or_404(Place.objects.all(), pk=pk)
        serializer = PlaceSerializer(instance=saved_zoopark, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            place_saved = serializer.save()
        return Response({
            "success": "Place '{}' updated successfully".format(place_saved.name)
        })

    def delete(self, request, pk):
        zoopark = get_object_or_404(Place.objects.all(), pk=pk)
        zoopark.delete()
        return Response({
            "message": "Place with id `{}` has been deleted.".format(pk)
        }, status=204)


class PlaceView(generics.ListAPIView):
    """Место животного"""
    serializer_class = PlaceSerializer
    filter_backends = (DjangoFilterBackend,)

    # filterset_class = PlaceFilter

    def get_queryset(self):
        place = Place.objects.all()
        return place

    def post(self, request):
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HumanViewID(generics.RetrieveAPIView):
    """Сотрудник по ID"""
    serializer_class = HumanSerializer

    def get(self, request, pk):
        humans = Human.objects.get(id=pk)
        serializer = HumanSerializer(humans)
        return Response({"Human": serializer.data})

    def put(self, request, pk):
        saved_zoopark = get_object_or_404(Human.objects.all(), pk=pk)
        serializer = HumanSerializer(instance=saved_zoopark, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            human_saved = serializer.save()
        return Response({
            "success": "Human '{}' updated successfully".format(human_saved.name)
        })

    def delete(self, request, pk):
        zoopark = get_object_or_404(Human.objects.all(), pk=pk)
        zoopark.delete()
        return Response({
            "message": "Human with id `{}` has been deleted.".format(pk)
        }, status=204)


class HumanView(generics.ListAPIView):
    """Сотрудники"""
    serializer_class = HumanSerializer

    def get(self, request):
        humans = Human.objects.all()
        serializer = HumanSerializer(humans, many=True)
        return Response({"Human": serializer.data})

    def post(self, request):
        serializer = HumanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnimalViewID(generics.RetrieveAPIView):
    """Животное по ID"""
    serializer_class = AnimalSerializer

    def get(self, request, pk):
        animals = Animal.objects.get(id=pk)
        serializer = AnimalSerializer(animals)
        return Response({"Animal": serializer.data})

    def put(self, request, pk):
        saved_zoopark = get_object_or_404(Animal.objects.all(), pk=pk)
        serializer = AnimalSerializer(instance=saved_zoopark, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            zoopark_saved = serializer.save()
        return Response({
            "success": "Animal '{}' updated successfully".format(zoopark_saved.animal)
        })

    def delete(self, request, pk):
        zoopark = get_object_or_404(Animal.objects.all(), pk=pk)
        zoopark.delete()
        return Response({
            "message": "Animal with id `{}` has been deleted.".format(pk)
        }, status=204)


class AnimalView(generics.ListAPIView):
    """Животные"""
    serializer_class = AnimalSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnimalFilter

    def get_queryset(self):
        animals = Animal.objects.all().order_by('-month_human')  # '-' отвечает за порядок обратный (реверс короче)
        return animals

    # def get(self, request):
    #     animals = Animal.objects.all()
    #     serializer = AnimalSerializer(animals, many=True)
    #     return Response({"Animal": serializer.data})

    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ZooparkView(generics.ListAPIView):
    """Зоопарк"""

    def get(self, request):
        animal = Animal.objects.all()
        animal_serial = AnimalSerializer(animal, many=True)
        variety = Variety.objects.all()
        variety_serial = VarietySerializer(variety, many=True)
        place = Place.objects.all()
        place_serial = PlaceSerializer(place, many=True)
        human = Human.objects.all()
        human_serial = HumanSerializer(human, many=True)
        return Response({"Zoopark":
            {
                "Animal": animal_serial.data,
                "Variety": variety_serial.data,
                "Place": place_serial.data,
                "Human": human_serial.data,
            }
        })
