from django.urls import path

from .views import ListZadanie, DetailZadanie, LoginView, UserList, UserDetail, ListZadanieUser, DetailZadanieUser

urlpatterns = [
    path('', ListZadanie.as_view()),
    path('<int:pk>/', DetailZadanie.as_view()),
    path('login/', LoginView.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:user_id>/', ListZadanieUser.as_view()),
    path('users/<int:user_id>/<int:pk>/', DetailZadanieUser.as_view()),
]