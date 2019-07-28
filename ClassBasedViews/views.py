from django.shortcuts import render,reverse
from django.views import View
from django.views.generic import ListView
from .models import Blogs
from django.views.generic.edit import CreateView

# Create your views here.
'''def index(request):
    return render(request,'ClassBasedViews/index.html',{})'''
    
class BlogCreateView(CreateView):
    model=Blogs
    fields=['title','desc']
    template_name='ClassBasedViews/blogs_form.html'
    def get_success_url(self):
        return reverse('blog')
            
class BlogsListView(ListView):
    model=Blogs
    context_object_name='blogs'
    template_name='ClassBasedViews/blogs_list.html'
    paginate_by = 2
class IndexView(View):
    def get(self,request):
        return render(request,'ClassBasedViews/index.html',{})
    def post(self,request):
        return render(request,'ClassBasedViews/index.html',{
            'is_post':True,
            'post_msg':"THis is a response to POST request"})

        