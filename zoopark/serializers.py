from rest_framework import serializers
from .models import Variety, Place, Human, Animal


class VarietySerializer(serializers.ModelSerializer):
    """Вид животного"""

    class Meta:
        model = Variety
        # fields = ("id", "variety", "food", "behavior", "recommendation", "created_at", "updated_at")
        fields = "__all__"

    def create(self, validated_data):
        return Variety.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.variety = validated_data.get('variety', instance.variety)
        instance.food = validated_data.get('food', instance.food)
        instance.behavior = validated_data.get('behavior', instance.behavior)
        instance.recommendation = validated_data.get('recommendation', instance.recommendation)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance


class HumanSerializer(serializers.ModelSerializer):
    """Сотрудники"""

    class Meta:
        model = Human
        # fields = ("id", "name", "gender", "age", "experience", "phone", "email", "created_at", "updated_at")
        fields = "__all__"

    def create(self, validated_data):
        return Human.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.age = validated_data.get('age', instance.age)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance


class AnimalSerializer(serializers.ModelSerializer):
    """Животные"""
    variety_id = serializers.IntegerField()
    place_id = serializers.IntegerField()
    human_id = serializers.IntegerField()

    class Meta:
        model = Animal
        fields = ("id", "animal", "gender", "variety_id", "place_id", "human_id",
                  "month_human", "created_at", "updated_at")
        # fields = "__all__"

    def create(self, validated_data):
        return Animal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.animal = validated_data.get('animal', instance.animal)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.variety_id = validated_data.get('variety_id', instance.variety_id)
        instance.place_id = validated_data.get('place_id', instance.place_id)
        instance.human_id = validated_data.get('human_id', instance.human_id)
        instance.month_human = validated_data.get('month_human', instance.month_human)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance


class PlaceSerializer(serializers.ModelSerializer):
    """Место животных"""

    class Meta:
        model = Place
        # fields = ("id", "place", "length", "width", "height", "material", "capacity", "created_at", "updated_at")
        fields = "__all__"

    def create(self, validated_data):
        return Place.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.place = validated_data.get('place', instance.place)
        instance.length = validated_data.get('length', instance.length)
        instance.width = validated_data.get('width', instance.width)
        instance.height = validated_data.get('height', instance.height)
        instance.material = validated_data.get('material', instance.material)
        instance.capacity = validated_data.get('capacity', instance.capacity)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance
