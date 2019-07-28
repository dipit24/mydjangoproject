from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def session(request):
    if request.method == 'POST':
        messages.success(request,message='THIS IS A SUCCESS MESSAGE')
        request.session['name'] = "DipitSession"
        request.session.set_expiry(5)
    try:
        name = request.session['name']
    except:
        name = None
    print(type(name))
    return render(request,'sessionmanagement/index.html',{'name':name})