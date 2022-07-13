from django.contrib import admin #Этот документ содержит справочный материал по API для компонентов системы аутентификации Django.
from django.urls import path, include #Из django.urls можно импортировать функции для использования в URLconfs например path & include
from django.conf import settings #Импортируем настройки из settings.py
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('service.urls')),
    path('', include('api.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#Эта строка формирует корректный url для статики в браузере на время пока идет разработка и проект запускается через встроенный сервер.