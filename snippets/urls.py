from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'snippets'

urlpatterns = [
    # path('', views.snippet_list, name="snippet_list"),
    # path('<int:pk>/', views.snippet_detail, name="snippet_detail"),
    path('', views.SnippetList.as_view(), name='snippet_list'),
    path('<int:pk>', views.SnippetDetail.as_view(), name='snippet_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)