from django.shortcuts import render, redirect,reverse
from create.models import Create
from django_summernote.widgets import SummernoteInplaceWidget
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from create.forms import Title, BodyFrom
from create.models import Tag
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.


# class PostCreateView(CreateView):
#     model = Create
#     fields = ['text', 'blog']
#
#     def get_form(self, form_class=BodyFrom):
#         form = super(PostCreateView, self).get_form(BodyFrom)
#         form.fields['body'].widget = SummernoteInplaceWidget()
#         return form
#
#     def form_valid(self,form):
#         form.instance.author = self.request.user
#         keywords = self.request.POST['hidden-tags-value']
#
#         response = super().form_valid(form)
#
#         self.object.keywords = keywords
#         self.object.save()
#
#         keys = keywords.split(',')
#
#         for key in keys:
#             keyword = Tag.objects.create(post=self.object,tag=key,tag_upper_case=key.upper())
#
#
#         # return response
#         return redirect('index', pk=self.object.pk)

# def PostCreateView(requests):
#     return render(requests, 'create/create.html')

from tinymce.widgets import TinyMCE



class PostCreateView(CreateView):
    model = Create
    fields = ['text', 'blog', 'rank', 'category', 'metadata']

    def get_form(self, form_class=BodyFrom):
        form = super(PostCreateView, self).get_form(BodyFrom)
        form.fields['body'].widget = TinyMCE()
        return form

    def form_valid(self, form):

        form.instance.author = self.request.user
        response = super().form_valid(form)

        keywords = self.request.POST['hidden-category-value']
        self.object.category = keywords
        self.object.save()

        keys = keywords.split(', ')

        for key in keys:
            keyword = Tag.objects.create(post=self.object,tag=key,tag_upper_case=key.upper())

        return response

    # def get_success_url(self):
    #     return reverse('index')

    def form_invalid(self,form):
        errors = form.errors
        for error in errors:
            print(error)



def postcreateview(request):
    if request.method == 'POST':
        form = BodyFrom(request.POST, instance=request.user.users)

        if form.is_valid():
            rank = form.cleaned_data['rank']
            body = form.cleaned_data['body']
            title = form.cleaned_data['title']
            return redirect('index')
    form = BodyFrom()
    context = {
        'form': form
    }
    return render(request, 'create/create.html', context)


class PostDetailView(DetailView):
    model = Create


class PostUpdateView(View):
    template_name = 'create/create_form_edit.html'

    def get(self, request, post_id):
        post = get_object_or_404(Create, pk=post_id, author=request.user)

        form = BodyFrom(initial= {'title': post.title, 'body': post.body, 'rank': post.rank, 'category': post.category, 'metadata': post.metadata})

        form.fields['body'].widget = TinyMCE()

        context = {
            'post': post,
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, post_id):
        ## Only Authors can edit their own posts
        post = get_object_or_404(Create, pk=post_id, author=request.user)
        form = BodyFrom(request.POST)

        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.rank = form.cleaned_data['rank']
            # post.category = form.cleaned_data['category']
            post.metadata = form.cleaned_data['metadata']
            post.keywords = self.request.POST['hidden-category-value']
            post.modified_date = timezone.now()

            post.save()

            ## Saving the kewwords
            keywords = self.request.POST['hidden-category-value']
            ## The best way is to re create them
            keys = Tag.objects.filter(post=post)
            for key in keys:
                key.delete()

            keys = keywords.split(', ')

            for key in keys:
                keyword = Tag.objects.create(post=post,tag=key,tag_upper_case=key.upper())

        return redirect('index')


class PostDeleteView( LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Create
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False