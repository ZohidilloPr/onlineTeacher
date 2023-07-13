from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
# Create your views here.

def Profile(request):
    """ USER PROFILE UCHUN """
    return render(request, "users/profile.html")


class UserLoginView(LoginView):
    """ USERNI LOGIN QILISH UCHUN """
    redirect_authenticated_user = True
    template_name = "users/authenticated/login.html"
    
    def get_success_url(self):
        return reverse_lazy("users:user_profile")

    def form_invalid(self, form):
        messages.error(self.request, "Username yoki Passwordda xatolik bor.")
        return self.render_to_response(self.get_context_data(form=form))
    




