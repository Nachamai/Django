from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from BLOG_POSTS.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['blognum', 'title', 'slug', 'author', 'content', 'status']

def blog_list(request, template_name='BLOG_POSTS/blog_list.html'):
    blog = Post.objects.all()
    data = {}
    data['object_list'] = blog
    print(blog)
    return render(request, template_name, data)

def blog_view(request, blognum, template_name='BLOG_POSTS/blog_detail.html'):
    blog = get_object_or_404(Post, blognum=blognum)
    return render(request, template_name, {'object':blog})

def blog_create(request, template_name='BLOG_POSTS/blog_form.html'):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog_list')
    return render(request, template_name, {'form':form})

def blog_update(request, blognum , template_name='BLOG_POSTS/blog_form.html'):
    blog = get_object_or_404(Post, blognum=blognum)
    form = PostForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('blog_list')
    return render(request, template_name, {'form':form})

def blog_delete(request, blognum , template_name='BLOG_POSTS/blog_confirm_delete.html'):
    blog = get_object_or_404(Post, blognum=blognum)
    if request.method=='POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, template_name, {'object':blog})
