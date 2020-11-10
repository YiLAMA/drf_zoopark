from django.db import models


# Create your models here.


class Variety(models.Model):
    """Вид животного"""
    variety = models.CharField("Вид", max_length=30)
    food = models.CharField("Питание", max_length=30, help_text="написать, что кушает животное")
    behavior = models.TextField("Описание вида", )
    recommendation = models.TextField("Рекомендации по работе", )
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True)

    def __str__(self):
        return self.variety

    class Meta:
        verbose_name = "Вид животного"
        verbose_name_plural = "Видов животных"


class Human(models.Model):
    """Сотрудники"""
    name = models.CharField("Фамилия", max_length=30, help_text="на пейджике будет")
    CHOICES = (
        ('М', 'мужской'),
        ('Ж', 'женский'),
        ('В', 'вертолёт'),
        ('?', 'лгбт')
    )
    gender = models.CharField("Пол", max_length=10, choices=CHOICES)
    age = models.PositiveSmallIntegerField("Возраст", )
    experience = models.PositiveSmallIntegerField("Стаж",
                                                  help_text="в годах")  # Сколько лет сотрудник работает в зоопарке
    phone = models.CharField("номер телефона", max_length=15, help_text="не более 15 символов")
    email = models.EmailField("Электронная почта", max_length=30)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Animal(models.Model):
    """Животные"""
    animal = models.CharField("Животное", max_length=50)
    CHOICES = (
        ('М', 'мужской'),
        ('Ж', 'женский'),
        ('Х', 'бесполый'),
    )
    gender = models.CharField("Пол", max_length=10, choices=CHOICES)
    variety = models.ForeignKey('Variety', related_name='zoopark', on_delete=models.CASCADE)  # Вид
    place = models.ForeignKey('Place', related_name='zoopark', on_delete=models.CASCADE)  # Место
    human = models.ForeignKey('Human', related_name='zoopark', on_delete=models.CASCADE)  # Сотрудник
    month_human = models.PositiveSmallIntegerField("Сколько месяцев уже закреплён сотрудник", help_text="в месяцах")
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True)

    def __str__(self):
        return self.animal

    class Meta:
        verbose_name = "Животное"
        verbose_name_plural = "Животные"


class Place(models.Model):
    """Место животного"""
    place = models.CharField("Место", max_length=30)
    length = models.IntegerField("Длина", help_text="в метрах")
    width = models.IntegerField("Ширина", help_text="в метрах")
    height = models.IntegerField("Высота", help_text="в метрах")
    material = models.CharField("Материал", max_length=30, help_text="основной материал защиты")
    capacity = models.IntegerField("Вместимость животных", help_text="сколько влезет животных")
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True)

    def __str__(self):
        return self.place

    class Meta:
        verbose_name = "Место животного"
        verbose_name_plural = "Места животных"
