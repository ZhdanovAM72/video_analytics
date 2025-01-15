from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db import models
from video.models import Video


User = get_user_model()


HN = 'ПрЭО "Холмогорнефть"'
MN = 'ПрЭО "Муравленковскнефть"'
PN = 'ПрЭО "Приобскнефть"'
ON = 'ПО "Оренбургнефть"'
VN = 'ПрЭО "Востокнефть"'
YAMAL = 'ПрЭО "Ямал"'
TYMEN = 'ПрЭО "Тюмень"'


STRUCTURAL_SUBDIVISION = (
    (HN, 'ХН'),
    (MN, 'МН'),
    (PN, 'ПН'),
    (ON, 'ОН'),
    (VN, 'ВН'),
    (YAMAL, 'Ямал'),
    (TYMEN, 'Тюмень'),
)

GOOD_QUALITY = 'Хорошее качество видео/звука'
NORMAL_QUALITY = 'Удовлетворительное качество видео/звука'
BAD_QUALITY = 'Плохое качество видео/звука'

RECORDING_QUALITY = (
    (GOOD_QUALITY, 'Хорошее'),
    (NORMAL_QUALITY, 'Удовлетворительное'),
    (BAD_QUALITY, 'Плохое'),
)

YES = 'ДА'
NO = 'НЕТ'

ACTION_VALUE = (
    (YES, 'ДА'),
    (NO, 'НЕТ'),
)


class PersonnelActions(models.Model):
    """Модель действий персонала."""
    number = models.CharField(
        verbose_name='Номер замечания',
        help_text='Номер замечания из чек-листа',
        max_length=6,
        unique=True,
    )
    personnel_action_description = models.TextField(
        verbose_name='Описание замечания',
        help_text='Описание замечания из чек-листа',
        max_length=500,
        unique=True,
    )

    class Meta:
        ordering = ('number',)
        verbose_name = 'Действие персонала'
        verbose_name_plural = 'Действия персонала'

    def __str__(self) -> str:
        return f'№{self.number}: {self.personnel_action_description}'


class CheckList(models.Model):
    """Модель чек-листов."""
    name = models.CharField(
        verbose_name='Название чек-листа',
        help_text='Название чек-листа проверки видео',
        max_length=50,
        unique=True,
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name='check_lists',
        verbose_name='Видео',
        help_text='Видео, к которому относится чек-лист',
    )
    structural_subdivision = models.CharField(
        verbose_name='Название ПрЭО/ПО',
        help_text='Название подразделения',
        max_length=50,
        choices=STRUCTURAL_SUBDIVISION,
    )
    working_place = models.CharField(
        verbose_name='Рабочее место',
        help_text='Место производства работ',
        max_length=100,
    )
    record_date = models.DateTimeField(
        verbose_name='Дата видео',
        help_text='Дата записи видео',
        default=timezone.now,
    )
    bp_number = models.CharField(
        verbose_name='Номер бланка переключений',
        help_text='Номер бланка переключений с описанием',
        max_length=100,
    )
    working_person = models.CharField(
        verbose_name='Лицо производящее переключение',
        help_text='Лицо непосредственно производящее переключение',
        max_length=100,
    )
    controlling_person = models.CharField(
        verbose_name='Лицо контролирующее переключение',
        help_text='Лицо непосредственно контролирующее переключение',
        max_length=100,
    )
    recording_quality = models.CharField(
        verbose_name='Качество видео',
        help_text='Качество видеозаписи (картинка, звук)',
        max_length=50,
        choices=RECORDING_QUALITY,
    )
    inspector = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='check_list',
        verbose_name='Проверяющий',
        help_text='Лицо заполняющее чек-лист',
    )
    brif_conclusion = models.TextField(
        verbose_name='Краткий вывод о проверке',
        help_text='Краткий вывод о произведенной проверке видео',
        max_length=500,
    )
    offer = models.TextField(
        verbose_name='Предложение',
        help_text='Предложения по результату проверки',
        max_length=500,
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Чек лист'
        verbose_name_plural = 'Чек листы'

    def __str__(self) -> str:
        return self.name


class PersonnelActionsValue(models.Model):
    """Модель пунктов чек листа."""
    check_list_id = models.ForeignKey(
        CheckList,
        on_delete=models.CASCADE,
    )
    personnel_action = models.ForeignKey(
        PersonnelActions,
        on_delete=models.CASCADE,
    )
    value = models.CharField(
        verbose_name='Отметка действия',
        help_text='Выбор из значений ДА/НЕТ',
        max_length=3,
        choices=ACTION_VALUE,
        blank=True,
    )
    description = models.CharField(
        verbose_name='Описание действия',
        help_text='Краткое описание действия',
        max_length=500,
        blank=True,
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'пункт в чек-листе'
        verbose_name_plural = 'пункты в чек-листах'

    def __str__(self) -> str:
        return f'{self.check_list_id, self.personnel_action, self.value, self.description}'
