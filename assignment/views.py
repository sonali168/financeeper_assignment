from django.shortcuts import render

from .models import Login

# Create your views here.
def Indexpage(request):
    if request.method == 'POST':
        email_id= request.POST.get('email_id')
        password= request.POST.get('password')
        form = Login(email_id=email_id,password=password)
        form.save()
    return render(request, 'assignment/base.html')

def Records(request):
    form = Login.objects.all()
    return render(request, 'assignment/records.html', {"Forms": form})