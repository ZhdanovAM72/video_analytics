from django.shortcuts import render
from django.core.paginator import Paginator

from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from video.services import open_file
from video.models import Video
from video.forms import VideoForm
from check_list.models import PersonnelActionsValue
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


def index(request):
    post_list = Video.objects.all()
    paginator = Paginator(post_list, VIDEO_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'video/index.html', context)


def new_index(request):
    post_list = Video.objects.filter(status__name='Новое')
    paginator = Paginator(post_list, VIDEO_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for video in page_obj.object_list:
        video.status_name = video.status.name
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'video/new_index.html', context)


def done_index(request):
    post_list = Video.objects.filter(status__name='Просмотрено')
    logging.info(f'{post_list}')
    paginator = Paginator(post_list, VIDEO_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for video in page_obj.object_list:
        video.status_name = video.status.name
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'video/done_index.html', context)


def get_list_video(request):
    return render(
        request, 'video/index.html', {'video_list': Video.objects.all()}
    )


@login_required
def create_video(request):
    form = VideoForm(request.POST, request.FILES or None)
    if request.method != 'POST':
        form = VideoForm()
    if form.is_valid():
        video = form.save(commit=False)
        video.save()
        return index(request)
    return render(request, 'video/create_video.html', {'form': form})


def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(
        file, status=status_code, content_type='video/mp4'
    )

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response


def get_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    video.checklist = video.check_lists.all()
    for checklists in video.checklist:
        checklists.actions = checklists.personnelactionsvalue_set.all()
    if request.method == 'POST':
        form = CheckListForm(request.POST)
        form.video = video
        if form.is_valid():
            # logging.info('>>>>>>>>>>>>after valid')
            check_list_instance = form.save(commit=False)
            check_list_instance.save()

            formset = form.formset
            for i, formset_form in enumerate(formset.forms):
                value = request.POST.get(
                    f'personnelactionsvalue_set-{i}-value'
                )
                logging.info(f'{value}')
                logging.info(f'{value}')

                description = request.POST.get(
                    f'personnelactionsvalue_set-{i}-description'
                )
                logging.info(f'{description}')

                personnel_action_id = request.POST.get(
                    f'personnelactionsvalue_set-{i}-personnel_action'
                )
                logging.info(f'{personnel_action_id}')

                personnel_action_instance = get_object_or_404(
                    PersonnelActions,
                    id=personnel_action_id
                )

                PersonnelActionsValue.objects.create(
                    value=value,
                    description=description,
                    check_list_id=check_list_instance,
                    personnel_action=personnel_action_instance,
                )

        return index(request)
    else:
        # logging.info('>>>>>>>>>>>>else')
        form = CheckListForm(initial={'video': video})

    return render(request, 'video/video.html', {'form': form, 'video': video})
