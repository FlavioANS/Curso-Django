from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video Aperitvo: Motivação'}
    return render(request, 'aperitivos/video.html', context={'video': video})
