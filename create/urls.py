from django.urls import path
from create import views


urlpatterns = [
    path('', views.PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post-detail"),
    path('update/<int:post_id>/', views.PostUpdateView.as_view(), name="post-edit"),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name="post-delete")

    # path('', views.postcreateview, name='create')
]