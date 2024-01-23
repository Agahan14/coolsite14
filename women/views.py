from django.shortcuts import render, redirect
from django.views.generic import ListView
from women.models import Women, Category
from women.forms import AddPostForm


menu = [
    {"name": "Главная страница", "url": "index"},
    {"name": "О нас", "url": "about"},
    {"name": "Наши контакты", "url": "contacts"},
    {"name": "Вопросы", "url": "questions"},
    {"name": "Добавить статью", "url": "add-post"}
]


class WomenHome(ListView):
    model = Women
    template_name = "index.html"
    context_object_name = "women"
    extra_context = {"title": "Главная страница"}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        context["menu"] = menu
        context["category"] = category
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)

# def index(request):
#     women = Women.objects.all()
#     new_women = {'women': women, 'menu': menu}
#     return render(request, 'index.html', context=new_women)


def about(request):
    new_women = {'menu': menu}
    return render(request, 'about.html', context=new_women)


def contacts(request):
    new_women = {'menu': menu}
    return render(request, 'contacts.html', context=new_women)


def questions(request):
    new_women = {'menu': menu}
    return render(request, 'questions.html', context=new_women)


def add_women(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddPostForm()
    new_women = {'menu': menu, 'form': form}
    return render(request, 'add_women.html', context=new_women)


def delete_women(request, women_id):
    if request.method == "POST":
        Women.objects.filter(id=women_id).delete()
        return redirect('index')


def detail_women(request, women_slug):
    woman = Women.objects.filter(slug=women_slug).first()
    new_women = {'menu': menu, 'woman': woman}
    return render(request, 'women_detail.html', context=new_women)
