from django.shortcuts import render
from userapp.forms import UserForm
from userapp.forms  import EmployeeForm
# Create your views here.
def gethomepage(request):
    return render(request, 'home.html')

def getnewuserpage(request):
    form = UserForm()
    return render(request, 'user.html', {'form': form})

def getnewemppage(request):
    form = EmployeeForm()
    return render(request, 'emp.html', {'form':form})
