from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': '682069825?h=6282c4b3f3'}
    return render(request, 'aperitivos/video.html', context={'video': video})
