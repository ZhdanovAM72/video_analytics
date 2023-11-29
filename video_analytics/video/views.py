from django.shortcuts import render
from django.core.paginator import Paginator

from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404

from video.services import open_file
from video.models import Video
from video_analytics.settings import VIDEO_PER_PAGE


# Create your views here.
def index(request):
    post_list = Video.objects.all()
    paginator = Paginator(post_list, VIDEO_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'video/index.html', context)


def get_list_video(request):
    return render(request, 'video/index.html', {'video_list': Video.objects.all()})


def get_video(request, pk: int):
    _video = get_object_or_404(Video, id=pk)
    return render(request, "video/video.html", {"video": _video})


def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response
