from django.contrib.auth import get_user_model
from django.db import models


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


class CheckList(models.Model):
    """Модель чек-листов."""
    name = models.CharField(
        verbose_name='Название чек-листа',
        help_text='Название чек-листа проверки видео',
        max_length=50,
        unique=True,
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
        verbose_name='Лицо производящее переключение',
        help_text='Лицо непосредственно производящее переключение',
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

    class Meta:
        verbose_name = 'Чек лист'
        verbose_name_plural = 'Чек листы'

    def __str__(self) -> str:
        return self.name
