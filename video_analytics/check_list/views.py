from django.shortcuts import render
from django.core.paginator import Paginator

from django.shortcuts import render
from django.db.models import Count, Q

from video.models import Video
from check_list.models import CheckList
from django.shortcuts import render
import logging


logging.basicConfig(
    level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s'
)


def get_check_list_info(request):
    check_lists = CheckList.objects.all()
    paginator = Paginator(check_lists, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for check_list in page_obj.object_list:
        check_list.personnel_actions_value = (
            check_list.personnelactionsvalue_set.filter(value='НЕТ').count()
        )

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'check_list/check_list_info.html', context)


def get_video_base_stats(request):
    check_lists = CheckList.objects.all()
    count_all = check_lists.count()

    videos_stats = Video.objects.aggregate(
        videos_all=Count('id'),
        videos_done=Count('id', filter=Q(status__name='Новое'))
    )

    personnel_actions_value = check_lists.annotate(
        no_actions_count=Count(
            'personnelactionsvalue',
            filter=Q(personnelactionsvalue__value='НЕТ')
        )
    ).aggregate(
        total_no_actions=Count('no_actions_count')
    )['total_no_actions'] or 0

    context = {
        'count_all': count_all,
        'videos_all': videos_stats['videos_all'],
        'videos_done': videos_stats['videos_done'],
        'personnel_actions_value': personnel_actions_value,
    }
    return render(request, 'stats/base_stats.html', context)
