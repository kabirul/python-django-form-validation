from django.shortcuts import render, HttpResponse
from . forms import EmpDetailsForm

def emp_form(request):  
    if request.method == "POST":  
        form = EmpDetailsForm(request.POST)  
        if form.is_valid():  
            try: 
               form.save()               
               #return HttpResponse('The file is saved')  
               return render(request,'form.html',{'error_message': "The information has been saved."})      

            except:  
                pass  
    else:  
        form = EmpDetailsForm()  
    return render(request,'form.html',{'form':form})  
