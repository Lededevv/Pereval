from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=30, blank=True, null=True)
    otc = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=16, blank=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='группы',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="custom_user_groups",
        related_query_name="custom_user_group",
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='разрешения пользователя',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_permissions",
        related_query_name="custom_user_permission",
    )

    def __str__(self):
        return self.username or self.email


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.latitude}, {self.longitude}, Высота: {self.height} м"


class Pereval_added(models.Model):
    STATUS_CHOICES = (("new", "новый"),
                      ("pending", "на рассмотрении"),
                      ("accept", "принят"),
                      ("reject", "отклонен"))
    beauty_title = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    other_titles = models.TextField(blank=True)
    connect = models.TextField(null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")

    def __str__(self):
        return self.title


class Images(models.Model):
    pereval = models.ForeignKey(Pereval_added, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=128)
    # data = models.CharField(max_length=128)
    data = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.title


class Level(models.Model):
    pereval = models.OneToOneField(Pereval_added, on_delete=models.CASCADE)
    winter = models.CharField(max_length=10, blank=True, default='')
    summer = models.CharField(max_length=10, blank=True, default='')
    autumn = models.CharField(max_length=10, blank=True, default='')
    spring = models.CharField(max_length=10, blank=True, default='')