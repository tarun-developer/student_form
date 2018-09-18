from django.shortcuts import render

from forms_create.forms import FormName

def index(request):
    return render(request, "forms_create/index.html")



def form_name_view(request):
        form  = FormName()
        
        if request.method=="POST":
            form = FormName(request.POST)
            if form.is_valid():
                
                return index(request)
            else:
                print("Error Information Invalid")
        return render(request,"forms_create/form_page.html",{'form':form})