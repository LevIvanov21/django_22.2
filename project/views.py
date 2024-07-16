from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from project.forms import ProductAddForm, VersionForm, ProductManagerForm
from project.models import Product, Version, Category
from project.services import get_category_from_cache



class indexListView(ListView, LoginRequiredMixin):
    model = Product
    template_name = 'project/home.html'
    context_object_name = 'objects_list'


class contactsPageView(TemplateView):
    template_name = 'project/contacts.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(f"You have new feedback! Info: \n"
                  f"Subject_name: {name} \n"
                  f"Subject_phone: {phone} \n"
                  f"Subject_message: {message}")
        return render(request, self.template_name)


class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product
    template_name = 'project/product.html'
    context_object_name = 'objects_list'


class CategoryListView(ListView, LoginRequiredMixin):
    model = Category
    template_name = 'project/category_list.html'
    context_object_name = 'objects_list'

    def get_queryset(self):
        return get_category_from_cache()


class CategoryDetailView(DetailView, LoginRequiredMixin):
    model = Category
    template_name = 'project/category_detail.html'
    context_object_name = 'objects_list'


class ProductAddView(CreateView, LoginRequiredMixin):
    model = Product
    template_name = 'project/add_product.html'
    form_class = ProductAddForm
    success_url = reverse_lazy('project:index')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    template_name = 'project/product_form.html'
    form_class = ProductAddForm
    success_url = reverse_lazy('project:index')
    perms = ('project.edit_publication', 'project.edit_description', 'project.edit_categories')

    def get_form_class(self):
        if self.request.user.is_staff or self.request.user.has_perms(perm_list=self.perms) \
                and not self.request.user.is_superuser:
            return ProductManagerForm
        else:
            if self.request.user != self.get_object().owner:
                raise PermissionDenied
            else:
                return ProductAddForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        Versionformset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = Versionformset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = Versionformset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        self.object.owner = self.request.user
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProudctDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'project/product_confirm_delete.html'
    success_url = reverse_lazy('project:index')