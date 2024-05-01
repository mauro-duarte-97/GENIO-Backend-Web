from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import FormView
from .forms import FeedbackForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage




class FeedbackView(LoginRequiredMixin, FormView):
    template_name = 'feedback_box.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('user_home')  # Redirige aquí después de enviar el formulario correctamente

    def form_valid(self, form):
            feedback = form.save(commit=False)
            feedback.user = self.request.user  # Asocia el usuario autenticado con el feedback
            feedback.save()
            # Enviar correo electrónico
            email = EmailMessage(
                subject='Nuevo feedback',
                body=f'El usuario {feedback.user.nombre} de email {feedback.user.email} ha enviado un nuevo feedback:\n\n{feedback.mensaje}',
                to=['m.e.b.d.0904@ifts18.edu.ar'],)  # Cambiar por tu dirección de correo electrónico
            try:
                email.send()
                messages.success(self.request, 'Feedback enviado correctamente')

            except Exception as e:
                messages.error(self.request, 'No se pudo enviar el feedback')

            return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(FeedbackView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Añade el usuario actual a los kwargs del formulario
        return kwargs
    
class GmailView(LoginRequiredMixin, FormView):
    template_name = 'gmail_api.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('user_home')  # Redirige aquí después de enviar el formulario correctamente

    def form_valid(self, form):
            feedback = form.save(commit=False)
            feedback.user = self.request.user  # Asocia el usuario autenticado con el feedback
            feedback.save()
            # Enviar correo electrónico
            email = EmailMessage(
                subject='Nuevo feedback',
                body=f'El usuario {feedback.user.nombre} de email {feedback.user.email} ha enviado un nuevo feedback:\n\n{feedback.mensaje}',
                to=['m.e.b.d.0904@ifts18.edu.ar'],)