from django.shortcuts import render
import mainwebsite.templates.utilities.DataAccess as data
import datetime

# Create your views here.
def index(request):
    return render(request, 'mainwebsite/index.html')

def dashboard(request):
    x = datetime.datetime.now()
    todaysDate = x.strftime("%A")

    return render(request, 'mainwebsite/dashboard.html', {'todaysDate': todaysDate})

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')



    return render(request, 'mainwebsite/signup.html')