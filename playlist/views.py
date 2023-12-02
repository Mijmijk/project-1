from django.shortcuts import render
from .models import Video

# Create your views here.
def playlist (request):
    videos= Video.objects.all()
    return render (request, "playlist/playlist.html", {'videos':videos})



def new_video (request):
    if request.method == "POST": 
        embed_code = request.POST['embed_code']
        title = request.POST['title']
        Video.objects.create(
            title=title,
            embed_code=embed_code
        )

    return render (request, "playlist/new_video.html")
