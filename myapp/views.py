from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from django.template import loader
from myapp.models import *
from django import forms

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee1
        fields=['name','language','company']
# Create your views here.

def hello(request):
    text = "<H1>Hello Django, this is my first HTML static code<H1>"
    return HttpResponse(text)

def validation(request):
    a=1
    if a==2:
        return HttpResponseNotFound("<h1>PAGE NOT FOUND</h1>")
    else:
        return HttpResponse("<h1>You are at the correct page</h1>")
    
#def index(request):
#   template=loader.get_template('index.html')
#    return HttpResponse(template.render())

def index(request):
    data= Employee1.objects.all()
    return render(request,'index.html',{'emp_data':data})

def del_emp(request,id):
    data=Employee1.objects.get(pk=id)
    data.delete()
    return redirect('Index')

def add_company(request):
    if(request.method=='POST'):
        get_name=request.POST.get('name')
        get_date=request.POST.get('date')
        temp=Company(name=get_name,c_date=get_date)
        temp.save()
        return redirect('msg')
    else:
        return render(request,'add_company.html')

def add_language(request):
    if(request.method=='POST'):
        get_name=request.POST.get('name')
        get_founder=request.POST.get('founder')
        temp=Language(name=get_name,founder=get_founder)
        temp.save()
        return redirect('msg')
    else:
        return render(request,'add_language.html')
def add_employee(request):
    if(request.method=='POST'):
        '''
        get_name=request.POST.get('name')
        get_company=request.POST.get('company')
        get_language=request.POST.get('language')
        company_obj=Company.objects.get(pk=int(get_company))
        language_obj=Language.objects.get(pk=int(get_language))
        temp=Employee(name=get_name,
                      company=company_obj,
                      language=language_obj)
        temp.save()
        return redirect('msg')'''
    else:
        '''company=Company.objects.all()
        #language=Language.objects.all()'''
        form=AddEmployeeForm()
        return render(request,'add_employee.html',
                      {'form':form})

def msg(request):
    return render(request,'msg.html')