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

	bday = requests.get(url, params = parameters)
	bday =  detail['birthday']
	bday_date = str(bday.split('/')[1])
	bday_nextdate = str(int(bday.split('/')[1])+1)
	bday_month = str(bday.split('/')[0])
	current_year = str(date.today().year)

	current_bday = bday_month+"/"+bday_date+"/"+current_year
	next_day = bday_month+"/"+bday_nextdate+"/"+current_year

	print current_bday
	print next_day

	url = "https://graph.facebook.com/v2.4/me/feed?since="+"08/15/2015"+"&until="+"08/16/2015"
	# url = "https://graph.facebook.com/v2.4/me"
	parameters = {'access_token': access_token}
	related_list = requests.get(url, params = parameters)
	related_list = related_list.json()
	print related_list
	for msg in related_list['data']:
		try:
			print msg['id']
			url = "https://graph.facebook.com/"+msg['id']
			parameters = {'access_token': access_token}
			per_post = requests.get(url, params = parameters).json()
			print per_post
			# thanks(per_post['id'],access_token)
		except:
			print "Error "
	return render(request, 'index.html',{ 'details' : details })


def thanks(post_id,access_token):
	MESSAGE = ":/"
	parameters = {'access_token': access_token, 'message': MESSAGE}
	requests.post("https://graph.facebook.com/%s/comments" %(post_id), data = parameters)