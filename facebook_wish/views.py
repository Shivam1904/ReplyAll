import os,facebook,requests
from datetime import date
from django.template import RequestContext, loader
from django.shortcuts import render,render_to_response
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from social.apps.django_app.default.models import *
from django.contrib.auth.models import User

SOCIAL_AUTH_FACEBOOK_KEY = '1609198282691297'
SOCIAL_AUTH_FACEBOOK_SECRET = 'adba82042e447ecb5e07b2f8f9c6fd3b'

def logout(request):
    auth_logout(request)
    return redirect('/')

def homepage(request):
	return render(request, 'index.html')

def details(request):
	details = {}
	facebook_profile = request.user
	user = User.objects.filter(username = facebook_profile)
	access_token = (UserSocialAuth.objects.filter(user = user))[0].extra_data['access_token']

	url = "https://graph.facebook.com/me?fields=first_name,name,picture,birthday"
	parameters = {'access_token': access_token}
	detail = requests.get(url, params = parameters).json()

	details['name'] = detail['name']
	details['first_name'] = detail['first_name']
	details['picture']= detail['picture']['data']['url']
	details['birthday'] = detail['birthday']
	return render(request, 'index.html',{ 'details' : details })