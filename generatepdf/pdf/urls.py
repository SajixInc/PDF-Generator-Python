from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .htmltopdfconverter import *


    

urlpatterns = [
    path('generation/', Generatepdf.as_view()),
    path('gen/', htmltopdfview.as_view()),
    # path('get', downloadfile.as_view()),
    
     path('index/',index),
   # path('index1/', index1),
    path('read/',read),
   

] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)