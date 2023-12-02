from django.contrib import admin
from django.urls import path
from Blog.views import post_list, post_like
from playlist.views import playlist
from django.conf.urls.static import static 
from django.conf import settings
from playlist.views import new_video
from firstapp.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', post_list, name='post_list' ),
    path('playlist/', playlist, name='playlist'),
    path('new_video/', new_video, name='new_video'),
    path('', signup, name='signup'),
    path('blog/post_like/',post_like, name='post_like'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
