from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.views.generic.base import View
import httplib2
from json import JSONDecoder
import urllib

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def search(request):
    return render(request, 'search.html', {})

def find_by_course(request):
    return render(request, 'intermediary.html', {})

def find_by_application(request):
    return render(request, 'intermediary.html', {})

def t_and_c(request):
    return render(request, 't_and_c.html', {})

def google_login(request):
    token_request_uri = "https://accounts.google.com/o/oauth2/auth"
    response_type = "code"
    client_id = '627357005421-47i7ujl3me1lb84k7lf2p9jt9rvu39bm.apps.googleusercontent.com'
    redirect_uri = "http://127.0.0.1:8000/login/google/auth"
    scope = "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"
    url = "{token_request_uri}?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}".format(
        token_request_uri = token_request_uri,
        response_type = response_type,
        client_id = client_id,
        redirect_uri = redirect_uri,
        scope = scope)
    return HttpResponseRedirect(url)

def google_authenticate(request):
    parser = httplib2.Http()
    login_failed_url = '/'
    if 'error' in request.GET or 'code' not in request.GET:
        return HttpResponseRedirect('{loginfailed}'.format(loginfailed = login_failed_url))

    access_token_uri = 'https://accounts.google.com/o/oauth2/token'
    redirect_uri = "http://127.0.0.1:8000/login/google/auth"
    params = urllib.urlencode({
        'code': request.GET['code'],
        'redirect_uri': redirect_uri,
        'client_id': '627357005421-47i7ujl3me1lb84k7lf2p9jt9rvu39bm.apps.googleusercontent.com',
        'client_secret': 'hpRg00WSMq8ghjuBYE4qrazT',
        'grant_type': 'authorization_code'
    })
    headers={'content-type':'application/x-www-form-urlencoded'}
    resp, content = parser.request(access_token_uri, method = 'POST', body = params, headers = headers)
    token_data = JSONDecoder().decode(content)
    resp, content = parser.request("https://www.googleapis.com/oauth2/v1/userinfo?access_token={accessToken}".format(accessToken=token_data['access_token']))
    google_profile = JSONDecoder().decode(content)
    return HttpResponseRedirect('/home')
