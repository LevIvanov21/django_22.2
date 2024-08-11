from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import BlogRecord


# Create your views here.

class BlogRecordCreate(CreateView):
    model = BlogRecord
    template_name = 'blog/blog_form.html'
    fields = ('title', 'body', 'preview', 'is_published')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_record = form.save()
            new_record.slug = slugify(new_record.title)
            new_record.save()

        return super().form_valid(form)


class BlogRecordUpdate(UpdateView):
    model = BlogRecord
    template_name = 'blog/blog_form.html'
    fields = ('title', 'body', 'preview', 'is_published')
    # success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_record = form.save()
            new_record.slug = slugify(new_record.title)
            new_record.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])

class BlogRecordIndexView(ListView):
    model = BlogRecord
    template_name = 'blog/blog_list.html'
    context_object_name = 'objects_list'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published = True)
        return queryset

class BlogRecordDeatilView(DetailView):
    model = BlogRecord
    template_name = 'blog/blog_detail.html'
    context_object_name = 'objects_list'

    def get_object(self, queryset=None):
        self.object = super().get_object()
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogRecordDeleteView(DeleteView):
        model = BlogRecord
        template_name = 'blog/blog_confirm_delete.html'
        success_url = reverse_lazy('blog:list')


def toggle_published(request, pk):
    record_item = get_object_or_404(BlogRecord, pk=pk)
    if record_item.is_published:
        record_item.is_published = False
    else:
        record_item.is_published = True

    record_item.save()

    return redirect(reverse('blog:list'))