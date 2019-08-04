from django.shortcuts import render
import pyrebase
from django.contrib import auth

config = {
	
	'apiKey': "AIzaSyAkUYQ51_t6T-qE_lJBMS3bVy-iuN_9AeI",
    'authDomain': "smartcampus-a19e2.firebaseapp.com",
    'databaseURL': "https://smartcampus-a19e2.firebaseio.com",
    'projectId': "smartcampus-a19e2",
    'storageBucket': "smartcampus-a19e2.appspot.com",
    'messagingSenderId': "945557570664",
    'appId': "1:945557570664:web:cfd73a02caa0538e"
  }

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def signIn(request):

	return render(request, "signIn.html")

def postsign(request):
	email=request.session.get('username')
	passw=request.session.get('password')
	try:
		user=authe.sign_in_with_email_and_password(email,passw)
	except:
		message="invalid credentials"
		return render(request, "signIn.html",{"messg":message})
	session_id=user['idToken']
	request.session['uid']=str(session_id)
	return render(request, "postsign.html")

def logout(request):
	auth.logout(request)
	return render(request, "signIn.html")

def signUp(request):
	return render(request, "signUp.html")

def postsignup(request):
	name=request.POST.get('name')
	email=request.POST.get('email')
	passw=request.POST.get('pass')
	try:
		user=authe.create_user_with_email_and_password(email,passw)
	except:
		message="Unable to create account. Try again."
		return render(request,"signUp.html",{"messg":message})	
		uid = user['localId']
	data={"name":name,"status":"1"}
	database.child("users").child(uid).child("details").set(data)
	return render(request,"signIn.html")

def home(request):
	email=request.POST.get('email')
	passw=request.POST.get('pass')
	return render(request,"home.html", {"username":email}, {"password":passw})