from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy

from . import views

urlpatterns = [
    
    url(r'^login/google$', views.google_login, name='google login'),
    url(r'^login/google/auth$', views.google_authenticate, name='google authenticate'),
    
    url(r'^$', views.index, name='home'),
    url(r'^.*home/$', RedirectView.as_view(url=reverse_lazy('home')), name='redirect_home'),
    
    url(r'^about/$', views.about, name='about'),
    url(r'^.*about/$', RedirectView.as_view(url=reverse_lazy('about')), name='redirect_about'),
    
    url(r'^search/$', views.search, name='search'),
    url(r'^.*search/$', RedirectView.as_view(url=reverse_lazy('search')), name='redirect_search'),
    
    url(r'^course/$', views.find_by_course, name='find by course name'),
    url(r'^.*course/$', RedirectView.as_view(url=reverse_lazy('course')), name='redirect_course'),
    
    url(r'^use/$', views.find_by_application, name='find by use'),
    url(r'^.*use/$', RedirectView.as_view(url=reverse_lazy('use')), name='redirect_use'),
    
    url(r'^t&c/$', views.t_and_c, name='terms and conditions'),
    url(r'^.*t&c/$', RedirectView.as_view(url=reverse_lazy('terms and conditions')), name='redirect_t_and_c'),
]