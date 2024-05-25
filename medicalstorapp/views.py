from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from .forms import medicalform 
from .models import medicalstore
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('retrive')
        
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

@login_required
def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    
    context = {
        'user': request.user
    }

    return render(request,'logout.html',context)

@login_required
def medical_create(request):
    if request.method == 'POST':
        form = medicalform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retrive')
        
    else:
        form = medicalform()
    return render(request,'create.html',{'form':form})

@login_required
def retrive_medi(request):
    medic = medicalstore.objects.all()
    return render(request,'retrive.html',{'medic':medic})

@login_required
def update_medi(request, id):
    medic = medicalstore.objects.get(pk=id)
    if request.method == 'POST':
        form = medicalform(request.POST, instance=medic)
        if form.is_valid():
            form.save()
            return redirect('retrive')
        
    else:
        form = medicalform(instance=medic)
    return render(request,'update.html',{'form':form})

@login_required
def delete_medi(request, id):
    medic = medicalstore.objects.get(pk=id)
    if request.method == 'POST':
        medic.delete()
        return redirect('retrive')
    
    return render(request,'delete.html',{'medic':medic})


@login_required
def medicine_search(request):
    if request.method == 'POST':
        query = request.POST.get('search_query')
        if query:
            return redirect('search_results', query=query)
    
    return redirect('retrive')
 

@login_required
def search_results(request, query):
    medicine = medicalstore.objects.filter(name__istartswith=query)
    return render(request, 'results.html', {'medicine': medicine})


