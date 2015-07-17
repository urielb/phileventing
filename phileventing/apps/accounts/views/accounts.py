from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template import RequestContext
from django.conf import settings

from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        post = request.POST
        try:
            username = post["username"]
            email = post["email"]
            password = post["password"]
            c_password = post["c_password"]
        except:
            error = "Failed to get required fields."
            return render_to_response("default_error.html", locals(), context_instance=RequestContext(request))
            
        if username == "" or email == "" or password == "" or c_password == "":
            error = "Some required fields were empty, please fix this and submit the form again."
            return render_to_response("default_error.html", locals(), context_instance=RequestContext(request))
            
        user = User(username=username, email=email)
        
        if password != c_password:
            error = "Given password doesn't match the confirmation password."
            return render_to_response("default_error.html", locals(), context_instance=RequestContext(request))
        
        try:
            user.set_password(password)
            user.save()
        except:
            error = "Username or email already registered in the database."
            return render_to_response("default_error.html", locals(), context_instance=RequestContext(request))
        
    return render_to_response("accounts/register.html", locals(), context_instance=RequestContext(request))