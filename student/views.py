from django.shortcuts import render, HttpResponse, redirect
import pyrebase
from django.contrib import auth


config = {
'apiKey': "AIzaSyB7NcY3z-0aR8teABnfAV7K8pR0J8qC8Ww",
'authDomain': "software-development-pro-29d1b.firebaseapp.com",
'databaseURL': "https://software-development-pro-29d1b.firebaseio.com",
'projectId': "software-development-pro-29d1b",
'storageBucket': "software-development-pro-29d1b.appspot.com",
'messagingSenderId': "1046913742869"
}

firebase = pyrebase.initialize_app(config)

firebaseauth = firebase.auth()
database = firebase.database()



def home(request):
	return render(request, 'student/home.html')




def signup(request):
	return render(request, 'student/signup.html')


def signupsubmit(request):
	username = request.POST.get('username')
	email = request.POST.get('email')
	phonenumber = request.POST.get('phonenumber')
	password = request.POST.get('password')
	try:
		user = firebaseauth.create_user_with_email_and_password(email, password)
	except Exception as ex:
		message = "Unable to create account. Try again!"
		return render(request, 'student/home.html', {'msg': message})
	uid = user['localId']
	data = {
		'username': username,
		'email': email,
		'phonenumber': phonenumber,
	}
	database.child('Users').child('Students').child(uid).child('Details').set(data)
	message = "Your account has created successfully"
	return render(request, 'student/home.html', {'msg': message})




def login(request):
	return render(request, 'student/login.html')


def loginsubmit(request):
	email = request.POST.get('email')
	password = request.POST.get('password')
	try:
		user = firebaseauth.sign_in_with_email_and_password(email, password)
	except Exception as ex:
		return HttpResponse(ex)
		message = "Invalid Username and password"
		return render(request, 'student/home.html',{'msg':message})
	session_id = user['idToken']
	request.session['uid'] = str(session_id)
	idToken = request.session['uid']
	a = firebaseauth.get_account_info(idToken)
	a = a['users']
	a = a[0]['localId']
	data = database.child('Users').child('Students').child(a).child('Details').get().val()
	message = 'You are logged in successfully'
	return render(request, 'student/home.html', {'msg': message,'data':data})



def logout(request):
	auth.logout(request)
	return redirect(home)


