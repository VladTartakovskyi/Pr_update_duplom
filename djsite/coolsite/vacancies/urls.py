from django.urls import path, re_path
from . import views
from .views import *
from django.contrib.auth.forms import UserCreationForm





urlpatterns = [
    path('', VacanciesHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('cursu/', CursuHome.as_view(), name='cursu'),
    path('admin/', AddPage.as_view(), name='add_page'),
    path('search/', Search.as_view(), name='search'),
    path('sear/', Sear.as_view(), name='sear'),
    path('cursu/sr/', Sr, name='sr'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('profession/<int:pr_id>/', show_profession, name='profession'),
    path('proff/', parse_article, name='proff'),
    path('category/<int:pr_id>/', show_category, name='category'),

]