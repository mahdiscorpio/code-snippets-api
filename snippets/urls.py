from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'snippets'

urlpatterns = [
    # path('', views.snippet_list, name="snippet_list"),
    # path('<int:pk>/', views.snippet_detail, name="snippet_detail"),
    path('snippets/', views.SnippetList.as_view(), name='snippet_list'),
    path('snippets/<int:pk>', views.SnippetDetail.as_view(), name='snippet_detail'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)