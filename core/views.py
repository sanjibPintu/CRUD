from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistrations
from .models import User

# Create your views here.
# adding and showing the item
def index(request):
    if request.method=="POST":
        fm=StudentRegistrations(request.POST)
        if fm.is_valid():
            # accessing the clean data
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            print(nm,em,ps)
            # crerating the model class object
            u=User(name=nm,email=em,password=ps)
            # saving  the model class object data
            u.save()
            fm=StudentRegistrations()# for genaratig the blank form

       
    else:
        fm=StudentRegistrations()
        # getting all the data from database
    user_obj=User.objects.all()
       

    return render(request,'core/add_show.html',{'form':fm,'user':user_obj})

# update and delete the data
def update_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=StudentRegistrations(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        pi=User.objects.get(pk=id)
    fm=StudentRegistrations(instance=pi)

    return render(request,'core/update.html',{'form':fm})


# deleting the data
def delete_data(requst,id):
    if requst.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        print('data deleted')
        return HttpResponseRedirect('/')
