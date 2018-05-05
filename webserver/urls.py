from django.contrib import admin
from django.urls import path
from mainapp import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
))
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.index),
    path('index/',v.index),
    path('challenge/',v.challenges),
    path('problems/',v.problemstatement), #problem statement
    path('keyword/',v.keywords),
    path('solution/',v.solution),
    path('about/',v.aboutpage),
    path('contact/',v.contact),
    path('search/',v.searchbox),
    path('log/',v.download),
]