from django.urls import path
from . import views

#app_name = 'posts'
urlpatterns = [
    path('', views.PostList.as_view(), name='posts'),
    path('new/', views.PostNew, name='postNew'),
    path('drafts/', views.DraftList, name='draft-posts'),
    path('edit/<slug:slug>/', views.PostEdit, name='postEdit'),
    path('<slug:slug>/', views.PostDetail, name='post'),
]

"""
path('posts/<category>/', views.CategoryListView.as_view(), name='category'),
"""
