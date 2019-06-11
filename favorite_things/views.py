from django.shortcuts import render
from create.models import Create
from django.contrib.auth.models import User
# Create your views here.
from django.views import View
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



class Home(View):
    template_name = 'favorite_things/index.html'

    def get(self, request):
        my_favorites = Create.objects.filter(author=request.user).order_by('rank')

        paginator = Paginator(my_favorites, 5)
        page = request.GET.get('page')
        my_posts = paginator.get_page(page)
        context = {
            'fav_item': my_posts
        }
        return render(request, self.template_name, context)
