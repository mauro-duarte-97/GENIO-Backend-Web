from django.contrib.contenttypes.models import ContentType
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.apps import apps
from django.shortcuts import redirect
from django.http import Http404, HttpResponseRedirect
from .forms import OpinionForm
from .models import Opinion
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


class OpinionListView(LoginRequiredMixin, FormMixin, ListView):
    model = Opinion
    form_class = OpinionForm
    template_name = 'opinion_historica.html'
    context_object_name = 'opiniones'

    def _get_model_and_instance(self):
        model_name = self.kwargs.get('model_name')
        entity_id = self.kwargs.get('entity_id')

        app_model_map = {
            'institucion': 'institucion',
            'carrera': 'carrera',
            'materia': 'materia',
            'profesor': 'profesor',
        }
        app_name = app_model_map.get(model_name)
        if not app_name:
            raise Http404(f"No application found for model {model_name}")

        Model = apps.get_model(app_name, model_name)
        if Model is None:
            raise Http404("Modelo no encontrado")
        
        instance = get_object_or_404(Model, id=entity_id)
        return Model, instance

    def get_queryset(self):
        Model, instance = self._get_model_and_instance()  # No need to catch instance here, just the model
        content_type = ContentType.objects.get_for_model(Model)
        return Opinion.objects.filter(content_type=content_type, object_id=instance.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Model, instance = self._get_model_and_instance()
        
        context['form'] = self.get_form()
        context['object_instance'] = instance
        context['model_name'] = self.kwargs.get('model_name')
        context['entity_id'] = self.kwargs.get('entity_id')
        return context
    
    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset() # Carga la lista de opiniones actuales
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        model_name = self.kwargs['model_name']
        entity_id = self.kwargs['entity_id']
        #app_name = self.kwargs.get('app_name', 'default_app')

        try:
            Model = apps.get_model(model_name, model_name)  # Uso model_name tanto para la app como para el modelo
            if Model is None:
                raise Http404("Modelo no encontrado")

            opinion = form.save(commit=False)
            opinion.content_object = Model.objects.get(id=entity_id)
            opinion.autor = self.request.user  # Asigna el usuario actual como autor
            opinion.save()

        except Model.DoesNotExist:
            raise Http404(f"No se encontró {model_name} con id {entity_id}")
        
        return redirect(self.get_success_url())
    
    def form_invalid(self, form):
        # Construir un diccionario de errores desde el formulario
        errors = {field: error.get_json_data() for field, error in form.errors.items()}
        return JsonResponse({'status': 'error', 'errors': errors}, status=400)
        #return JsonResponse({'errors': errors}, status=400)
    
    def get_success_url(self):
        return reverse_lazy('opiniones_por_entidad', kwargs={'model_name': self.kwargs['model_name'], 'entity_id': self.kwargs['entity_id']})


class OpinionDetailView(LoginRequiredMixin, DetailView):
    model = Opinion
    template_name = 'opinion_detail.html'
    context_object_name = 'opinion'

    def get_queryset(self):
        Model = apps.get_model(self.kwargs['model_name'], self.kwargs['model_name'])
        if Model is None:
            raise Http404("Modelo no encontrado")

        content_type = ContentType.objects.get_for_model(Model)
        return Opinion.objects.filter(content_type=content_type, object_id=self.kwargs['entity_id'], id=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        opinion = self.get_object()

        if request.user == opinion.autor:
            opinion.delete()
         # Redirigir a la página de opiniones por entidad
        return redirect('opiniones_por_entidad', model_name=self.kwargs['model_name'], entity_id=self.kwargs['entity_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Model = apps.get_model(self.kwargs['model_name'], self.kwargs['model_name'])
        if Model is None:
            raise Http404("Modelo no encontrado")

        # Pasar model_name y entity_id al contexto
        context['model_name'] = self.kwargs['model_name']
        context['entity_id'] = self.kwargs['entity_id']
        
        return context
    
