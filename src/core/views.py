from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from core.forms import EndpointRequestForm
from core.models import EndpointRequestPage


class Index(generic.TemplateView):
    template_name = 'core/index.html'


class EndpointRequestView(
    generic.DetailView, generic.FormMixin
):
    """Endpoint request page.

    Renders form to collect parameters for detail request
    to NASA API.

    TODO: render form, process request with form data
    """
    model = EndpointRequestPage
    template_name = 'core/endpoint_page.html'
    form_class = EndpointRequestForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            print(form.errors)
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('core:page_detail',
            kwargs={'slug': self.kwargs['slug']}
        )

    def form_valid(self, form):
        # TODO:
        return super().form_valid(form)
