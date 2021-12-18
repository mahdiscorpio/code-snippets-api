from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    # path('', views.snippet_list, name="snippet_list"),
    # path('<int:pk>/', views.snippet_detail, name="snippet_detail"),
    # path('', views.api_root),
    path('', include(router.urls)),
    # path('snippets/', views.SnippetList.as_view(), name="snippet-list"),
    # path('snippets/<int:pk>', views.SnippetDetail.as_view(), name='snippet-detail'),
    # path('snippets/<int:pk>/highlight', views.SnippetHighlight.as_view(), name="snippet-highlight"),
    # path('users/', views.UserList.as_view(), name="user-list"),
    # path('users/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
]

# urlpatterns = format_suffix_patterns(urlpatterns)