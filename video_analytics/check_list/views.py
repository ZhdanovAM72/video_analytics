from django.shortcuts import render
from django.core.paginator import Paginator

from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from video.services import open_file
from video.models import Video
from video.forms import VideoForm
from check_list.models import PersonnelActionsValue, CheckList
from check_list.forms import CheckListForm
from video_analytics.settings import VIDEO_PER_PAGE
from django.shortcuts import render, get_object_or_404
from check_list.forms import CheckListForm
import logging
from django.shortcuts import get_object_or_404
from check_list.models import PersonnelActions

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
