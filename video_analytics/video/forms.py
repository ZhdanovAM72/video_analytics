from django import forms
from video.models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
