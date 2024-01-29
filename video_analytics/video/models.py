from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import FileExtensionValidator, RegexValidator

# from django.urls import reverse

User = get_user_model()

GREEN = '#008000'
ORANGE = '#FF9900'
RED = '#f44336'

CHOICE_STATUS = (
    (GREEN, 'зеленый'),
    (ORANGE, 'оранжевый'),
    (RED, 'красный'),
)

GROUPS_CHOISE = {}


class Status(models.Model):
    """Модель статусов видео с выбором цвета."""
    name = models.CharField(
        verbose_name='Статус',
        help_text='Статус просмотра видео',
        max_length=50,
        unique=True,
    )
    color = models.CharField(
        verbose_name='Цвет статуса',
        help_text='Цвет в формате HEX',
        max_length=7,
        validators=(
            RegexValidator(
                regex=r'#[A-F\d]{6}',
                message='Цвет толжен быть в формате HEX!'
            ),
        ),
        choices=CHOICE_STATUS,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name='Слаг статуса',
        help_text='уникальный слаг статуса до 100 символов',
        max_length=100,
        unique=True,
    )

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self) -> str:
        return self.name


class Group(models.Model):
    """Модель для описания групп."""
    name = models.CharField(
        max_length=50,
        verbose_name='Название группы',
        help_text='название группы видео',
    )
    slug = models.SlugField(
        verbose_name='Уникальный slug',
        help_text='slug группы',
        max_length=20,
        unique=True,
    )
    description = models.TextField(
        max_length=200,
        verbose_name='Описание',
        help_text='Описание группы',
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self) -> str:
        return self.name


class Video(models.Model):
    """Модель видеозаписей."""
    name = models.CharField(
        max_length=50,
        null=False,
        verbose_name='название',
        help_text='название видео',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='videos',
        verbose_name='автор видео',
        help_text='Сотрудник загрузивший видео',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
        help_text='Дата публикации в формате "ДД название месяца ГГГГ"',
    )
    description = models.CharField(
        max_length=200,
        verbose_name='описание',
        help_text='описание видео',
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        related_name='videos',
        verbose_name='статус',
        help_text='статус видео'
    )
    video = models.FileField(
        upload_to='video/',
        blank=False,
        unique=True,
        validators=(
            FileExtensionValidator(
                allowed_extensions=('MOV', 'avi', 'mp4', 'webm', 'mkv'),
                code='неверное расширение',
            ),
        ),
        verbose_name='Видеозапись',
        help_text='видеофайл',
    )
    image = models.ImageField(
        upload_to='video/',
        blank=True,
        verbose_name='Картинка',
        help_text='Изображение поста',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.DO_NOTHING,
        verbose_name='группа',
        help_text='группа видео',
    )

    class Meta:
        verbose_name = 'Видеозапись'
        verbose_name_plural = 'Видеозаписи'

    def __str__(self) -> str:
        return self.name
