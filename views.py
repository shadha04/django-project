from django.shortcuts import render,redirect
from app.models import Student,Teacher,User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import check_password,make_password


# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        n=request.POST['name']
        e=request.POST['email']
        p=request.POST['password']
        c=request.POST['conf']
        a=request.POST['address']
        ph=request.POST['phno']
        g=request.POST['gname']
        i=request.FILES['image']
        if p==c:
            x=User.objects.create_user(username=n,password=p,email=e,is_active=False,usertype='student')
            y=Student.objects.create(student_id=x,confirm_password=c,address=a,phno=ph,image=i,guardian=g)
            y.save()
            return HttpResponse('<script>alert("Succesfully registered");window.location.href="http://127.0.0.1:8000//register";</script>')
        else:
            return HttpResponse('<script>alert("password incorrect");window.history.back();</script>')
    else:
        return render(request,'reg.html')
    
def log(request):
    if request.method=='POST':
        us=request.POST['name']
        ps=request.POST['pass']
        x=authenticate(username=us,password=ps)
        if x is not None and x.is_superuser==1:
            return redirect(admin)
        elif x is not None and x.is_staff==1:
            login(request,x)
            request.session['teacher']=x.id
            return redirect('tr')
        elif x is not None and x.is_active==1:
            login(request,x)
            request.session['student']=x.id
            return redirect(student)
        else:
            return HttpResponse('invalid')
    else:
        return render(request,'login.html')
        
def admin(request):
    return render(request,'admin.html')

def teacher(request):
    return render(request,'teacher.html')

def student(request):
    x=request.session.get('student')
    s=Student.objects.get(student_id_id=x)
    return render(request,'student.html',{'s':s})


def tradd(request):
    if request.method=='POST':
        na=request.POST['name']
        e=request.POST['email']
        pa=request.POST['password']
        cpwd=request.POST['conf']
        add=request.POST['address']
        ph=request.POST['phno']
        sal=request.POST['sal']
        exp=request.POST['exp']
        if pa == cpwd:
            x=User.objects.create_user(username=na,email=e,is_active=True,password=pa,is_staff=True,usertype='teacher')
            x.save()
            y=Teacher.objects.create(teacher_id=x,confirm_password=cpwd,address=add,phno=ph,salary=sal,experience=exp)
            y.save()
            return HttpResponse('<script>alert("successfully added");window.location.href="http://127.0.0.1:8000//addtr";</script>')
        else:
            return HttpResponse('<script>alert("password doesnot matching");window.history.back();</script>')
    else:
        return render(request,'tradd.html')
    

def viewtr(request):
    x=Teacher.objects.all()
    return render(request,'trview.html',{'data':x})

def deltr(request,id):
    x=Teacher.objects.get(id=id)
    z=x.teacher_id.id
    x.delete()
    u=User.objects.get(id=z)
    u.delete()
    return HttpResponse('<script>alert("successfully Deleted..");window.location.href="http://127.0.0.1:8000//trview";</script>')


def viewstud(request):
    x=Student.objects.all()
    return render(request,'studview.html',{'data':x})

def apprstud(request,id):
    x=Student.objects.get(id=id)
    x.student_id.is_active=True
    x.student_id.save()
    return HttpResponse('<script>alert("successfully Approved..");window.location.href="http://127.0.0.1:8000//studview";</script>')

def rejstud(request,id):
    x=Student.objects.get(id=id)
    y=x.student_id.id
    x.delete()
    u=User.objects.get(id=y)
    u.delete()
    return redirect('studview')

def out(request):
    logout(request)
    return redirect(log)


def tredit(request,id):
    x=Teacher.objects.get(id=id)
    y=x.teacher_id.id
    z=User.objects.get(id=y)
    if request.method=='POST':
        z.username=request.POST['name']
        z.email=request.POST['email']
        z.save()
        x.address=request.POST['address']
        x.phno=request.POST['phno']
        x.salary=request.POST['sal']
        x.experience=request.POST['exp']
        x.save()
        return HttpResponse('<script>alert("successfully edited..");window.location.href="http://127.0.0.1:8000//trview";</script>')
    else:
        return render(request,'tredit.html',{'tr':x,'us':z})
    
def viewprofiletr(request):
    s=request.session.get('teacher')
    t=Teacher.objects.get(teacher_id_id=s)
    x=t.teacher_id.id
    u=User.objects.get(id=x)
    return render(request,'viewtrprofile.html',{'t':t,'u':u})

def viewstudtr(request):
    s=Student.objects.all()
    return render(request,'viewstudtr.html',{'data':s})

def editstud(request,id):
    x=Student.objects.get(id=id)
    z=x.student_id.id
    u=User.objects.get(id=z)
    if request.method=='POST':
        u.username=request.POST['name']
        u.email=request.POST['email']
        x.address=request.POST['address']
        x.address=request.POST['address']
        x.phno=request.POST['phno']
        x.guardian=request.POST['gud']
        u.save()
        x.save()
        return  HttpResponse('<script>alert("successfully edited..");window.location.href="http://127.0.0.1:8000//studviewtr";</script>')
    return render(request,'editstud.html',{'s':x,'u':u})

def trpass(request):
    s=request.session.get('teacher')
    t=Teacher.objects.get(teacher_id_id=s)
    x=t.teacher_id.id
    u=User.objects.get(id=x)
    if request.method=='POST':
        p=request.POST['pass']
        c=request.POST['conpass']
        if p!=c:
            return  HttpResponse('<script>alert("password doesnot match..try again");window.history.back();</script>')

            
        if check_password(p, u.password):
            return HttpResponse(
                '<script>alert("New password cannot be same as old password");window.history.back();</script>'
            )
        else:
            u.set_password(p)
            u.save()
            t.confirm_password = c
            t.save()
            return  HttpResponse('<script>alert("Password changed...");window.location.href="http://127.0.0.1:8000//login";</script>')

    return render(request,'trpass.html',{'t':t,'u':u})

def studpass(request):
    r=request.session.get('student')
    s=Student.objects.get(student_id_id=r)
    y=s.student_id.id
    u=User.objects.get(id=y)  
    if request.method=='POST':
        p=request.POST['pass'] 
        c=request. POST['conpass']
        if p!=c:
            return  HttpResponse('<script>alert("password doesnot match..try again");window.history.back();</script>')
        if check_password(p,u.password):
            return HttpResponse(
                '<script>alert("New password cannot be same as old password");window.history.back();</script>'
            )
        else:
            u.set_password(p)
            u.save()
            s.confirm_password=c
            s.save()
            return HttpResponse('<script>alert("Password changed...");window.location.href="http://127.0.0.1:8000//login";</script>')
    return render(request,'studpass.html')


def viewstudprof(request):
    x=request.session.get('student')
    s=Student.objects.get(student_id_id=x)
    z=s.student_id.id
    u=User.objects.get(id=z)
    return render(request,'studprofile.html',{'s':s,'u':u})

def edit(request):
    x=request.session.get('student')
    s=Student.objects.get(student_id_id=x)
    if request.method=='POST':
        img=request.FILES['image']
        s.image=img
        s.save()
        return HttpResponse('<script>alert("Profile changed...");window.location.href="http://127.0.0.1:8000//st";</script>')
    return render(request,'edit.html',{'s':s})

def viewtrstud(request):
    t=Teacher.objects.all()
    return render(request,'viewtrstud.html',{'data':t})
