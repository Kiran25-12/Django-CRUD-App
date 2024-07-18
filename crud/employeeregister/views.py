from django.shortcuts import render
from .models import EmployeeData
from django.http import HttpResponseRedirect
from .froms import EmployeeRegister
from loginSignup.models import userdata
from django.contrib.auth.decorators import login_required

def employeeregister(request):
    form = EmployeeRegister()
    if request.method == 'POST':
        form = EmployeeRegister(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard')
    return render(request,'employeeregister.html',{'form':form})


def getallemployee(request):
    if request.session.get('id'):
        username = request.session.get('username')
        image = userdata.objects.get(id= request.session.get('id'))
        fetch_data = EmployeeData.objects.all()
        return render(request,'index.html',{'fetch_data' : fetch_data,'username':username,'image':image})
    else:
        return HttpResponseRedirect('/user_login')

def deleteemployee(request,id):
    employee_id = EmployeeData.objects.get(id=id)
    print(employee_id)
    employee_id.delete()
    return HttpResponseRedirect('/dashboard')

def updateemployee(request, id):
    form = EmployeeRegister()
    obj = EmployeeData.objects.get(id=id)
    form = EmployeeRegister(instance=obj)
    if request.method == 'POST':
        form = EmployeeRegister(request.POST,request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard')
    return render(request,'editemployee.html', {'form':form})











# def editemployee(request,id):
#     EmployeeDetails = EmployeeData.objects.get(id=id)
#     return render(request,'editemployee.html',{'emp':EmployeeDetails})

# def updateemployee(request,id):
#     # print("update ",id)
#     name = request.POST.get('name')
#     email = request.POST.get('email')
#     department = request.POST.get('department')
#     contact = request.POST.get('contact')
#     address = request.POST.get('address')
#     print("1")
#     image = request.FILES['image']
#     emp_update = EmployeeData.objects.filter(id=id).update(name=name,email=email,department=department,contact=contact,address=address,image= image)
#     # emp_update.name = name
#     # EmployeeDetails = emp_update(name=name,email=email,department=department,contact=contact,address=address,image=image)
#     # emp_update.save()
#     return HttpResponseRedirect('/dashboard')


