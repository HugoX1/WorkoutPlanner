from django.shortcuts import redirect, render
import mainwebsite.templates.utilities.DataAccess as data
import datetime

# Create your views here.
def index(request):
    if request.method == 'POST':
       
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        verify_details = data.verify_user(username, password)
        userID = data.getUserID(username)

        if verify_details == False:
            return render(request, 'mainwebsite/index.html', {'verify_details': verify_details}) 
        elif verify_details == True:
           request.session['userID'] = userID
           return redirect('dashboard')
       
    else:
        return render(request, 'mainwebsite/index.html')

    return render(request, 'mainwebsite/index.html')

def dashboard(request):
    x = datetime.datetime.now()
    todaysDate = x.strftime("%A")

    return render(request, 'mainwebsite/dashboard.html', {'todaysDate': todaysDate})

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(name, email, password)

        verify_details = data.sign_up(name, email, password)

        if verify_details == False:
            return render(request, 'mainwebsite/signup.html', {'verify_details': verify_details})
        else:
            return redirect('mainwebsite/index.html')  
        
    return render(request, 'mainwebsite/signup.html')