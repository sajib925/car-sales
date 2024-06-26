from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import BrandForm

class AddBrandView(FormView):
    template_name = 'add_brand.html'
    form_class = BrandForm
    success_url = reverse_lazy('add_brand')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
