from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.PostList.as_view(), name='post-list'),
    path("<int:id>/", views.PostDetail.as_view(), name='post-detail'),
    path("write/", views.PostWrite.as_view(), name='post-write'),
    path("edit/<int:id>/", views.PostEdit.as_view(), name='post-edit'),
    path("delete/<int:id>/", views.PostDelete.as_view(), name='post-delete'),
    path("search/<str:tag>/", views.PostSearch.as_view(), name='post-search'),
    path("<int:id>/comment/write/", views.CommentWrite.as_view(), name='cm-write'),
    path("comment/delete/<int:id>/", views.CommentDelete.as_view(), name='cm-delete'),
]