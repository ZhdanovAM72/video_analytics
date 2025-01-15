import datetime as dt


def year(request):
    """Добавляет переменную с текущим годом."""
    today = dt.date.today()
    return {
        'year': int(today.strftime('%Y'))
    }
