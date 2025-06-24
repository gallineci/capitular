from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from cap.views import Login, Logout  # importa as views personalizadas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),  # <- ESSA LINHA É ESSENCIAL
    path('logout/', Logout.as_view(), name='logout'),
    path('historia/', include('historia.urls'), name='historia'),
    path('capitulo/', include('capitulo.urls'), name='capitulo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)