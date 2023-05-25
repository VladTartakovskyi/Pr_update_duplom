from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .forms import AddPostForm, RegisterUserForm, LoginUserForm, UnemployedF
from .utils import *
import requests
from bs4 import BeautifulSoup
from django.db.models import Count
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.forms import UserCreationForm


class VacanciesHome(DataMixin,ListView):
    paginate_by = 3
    model = Vacancies
    template_name = 'vacancies/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(kilkbez_count=Count('unemployed'))
        return queryset


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Головна сторінка")

        context.update(c_def)
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)
        '''context['menu'] = user_menu'''
        if not self.request.user.is_superuser:
            '''user_menu.pop(1)'''
            user_menu.pop(2)


        context['menu'] = user_menu

        return context
def parse_article(request):
    # Код з отриманням результатів
    url = "https://uakino.club/"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Accept-Language": "uk-UA,uk;q=0.8,en-US;q=0.5,en;q=0.3"
    }
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return HttpResponse("Error conect to site: " + str(r.status_code))

    soup = BeautifulSoup(r.content, 'html.parser')
    sc = soup.findAll('div', class_="movie-item short-item")

    result = ""
    movies = []
    for i in sc:
        a = i.find("a", class_="movie-title")
        img = i.find("img")
        name = a.contents[0].strip()
        href = a["href"]
        src = img["src"]
        movies.append({'name': name, 'href': href, 'src': src})


    return render(request, "vacancies/parser.html", {"movies": movies})


def about(request):
    user_menu = menu.copy()
    if not request.user.is_authenticated:
        user_menu.pop(2)
    if not request.user.is_superuser:

        user_menu.pop(2)
    return render(request, 'vacancies/about.html', {'menu': user_menu, 'title': 'Про сайт'})

'''def cursu(request):
    user_menu = menu.copy()
    if not request.user.is_authenticated:
        user_menu.pop(2)
    return render(request, 'vacancies/about.html', {'menu': user_menu, 'title': 'Курси'})'''

class CursuHome(DataMixin,ListView):
    paginate_by = 3
    model = Cursu
    template_name = 'vacancies/indexcursu.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Курси")

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)
        '''context['menu'] = user_menu'''
        if not self.request.user.is_superuser:
            '''user_menu.pop(1)'''
            user_menu.pop(2)

        context['menu'] = user_menu

        return context





class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'vacancies/post.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавлення вакансії'
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)
        if not self.request.user.is_superuser:
            user_menu.pop(2)
        context['menu'] = user_menu
        return context




def contact(request):
    if request.method == 'POST':
        form = UnemployedF(request.POST, request.FILES)

        user_menu = menu.copy()
        if not request.user.is_superuser:
            user_menu.pop(3)
        if form.is_valid():

            try:
                unemployed = form.save(commit=False)
                unemployed.kor = request.user  # Присвоєння значення kor
                unemployed.save()
                return redirect('home')




                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Помилка добавлення')

    else:
        form = UnemployedF()


    return render(request, 'vacancies/contact.html', {'form': form, 'menu': menu, 'title': 'Добавлення даних про користувача'})





def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінка не знайдена</h1>')


def show_post(request, post_id):
    post = get_object_or_404(Vacancies, pk=post_id)



    context = {
        'post': post,
        'menu': menu,
        'title': post.posada,
        'cat_selected': post.pr_id,
    }

    return render(request, 'vacancies/post.html', {'title': 'Добавити дані про себе'})


def show_profession(request, pr_id):

    posts = Vacancies.objects.filter(pr_id=pr_id)

    user_menu = menu.copy()
    if not request.user.is_authenticated:
        user_menu.pop(2)
    if not request.user.is_superuser:
        user_menu.pop(2)
    context = {
        'posts': posts,
        'menu': user_menu,
        'title': 'Відображення по професіях',
        'cat_selected': pr_id,
    }


    return render(request, 'vacancies/index.html', context=context)

def show_category(request, pr_id):
    posts = Cursu.objects.filter(pr_id=pr_id)

    user_menu = menu.copy()
    if not request.user.is_authenticated:
        user_menu.pop(2)
    if not request.user.is_superuser:
        user_menu.pop(2)
    context = {
        'posts': posts,
        'menu': user_menu,
        'title': 'Відображення за видом послуг',

        'cat_selected': pr_id,
    }

    return render(request, 'vacancies/indexcursu.html', context=context)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'vacancies/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Реєстрація")

        return dict(list(context.items()) + list(c_def.items()))




class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'vacancies/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизація")


        return dict(list(context.items())+list(c_def.items()))

    def get_success_url(self):
        return  reverse_lazy('home')


def logout_user(request):
    logout(request)
    return  redirect('login')


class Search(ListView):
    model = Vacancies
    template_name = 'vacancies/index.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Vacancies.objects.filter(city=self.request.GET.get("search"))


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["search"] = self.request.GET.get("search")
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)
        '''context['menu'] = user_menu'''
        if not self.request.user.is_superuser:
            '''user_menu.pop(1)'''
            user_menu.pop(2)

        context['menu'] = user_menu

        return context





class Sear(ListView):
    model = Vacancies
    template_name = 'vacancies/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Vacancies.objects.filter(salary__gt=self.request.GET.get("sear"), salary__lt=self.request.GET.get("s"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["sear"] = self.request.GET.get("sear")
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)
        '''context['menu'] = user_menu'''
        if not self.request.user.is_superuser:
            '''user_menu.pop(1)'''
            user_menu.pop(2)

        context['menu'] = user_menu

        return context



'''class Sr(ListView):
    model = Cursu
    template_name = 'cursu/indexcursu.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Vacancies.objects.filter(city=self.request.GET.get("sr"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["sr"] = self.request.GET.get("sr")

        user_menu = menu.copy()
        if not self.request.user.is_superuser:
            user_menu.pop(2)
        context['menu'] = user_menu
        return context'''
def Sr(request):
    posts = Cursu.objects.filter(city=request.GET.get("sr"))

    user_menu = menu.copy()
    if not request.user.is_authenticated:
        user_menu.pop(2)
    '''context['menu'] = user_menu'''
    if not request.user.is_superuser:
        '''user_menu.pop(1)'''
        user_menu.pop(2)




    context = {
        'posts': posts,
        'menu': user_menu,
        'title': 'Відображення за видом послуг',

        'cat_selected': request.GET.get("sr")
    }

    return render(request, 'vacancies/indexcursu.html', context=context)





def category_avg_salary(request):
    # Отримати середню зарплату для кожної категорії
    categories = Category.objects.annotate(avg_salary=Avg('vacancy__salary'))

    # Передати список категорій та їх середню зарплату до шаблону
    return render(request, 'list_categories.html', {'categories': categories})

