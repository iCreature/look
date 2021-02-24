"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from app.models import *
import mysql.connector

from operator import itemgetter
import re
import os
from .forms import BookForm
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from io import BytesIO
from django.template.loader import render_to_string
import pdfkit

import tempfile
from django.template.loader import get_template
config=pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")

    #pass
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
def T_Info(request):
    """Admin add test info and take sessions"""
    examiner=""
    error=""
    if request.session.get('admin'):
        examiner+="{0}".format(request.session.get('admin'))
    if request.method=='POST':
        subject = request.POST['subject']
        tot=request.POST['totMarks']
        duration= request.POST['duration']
        date=request.POST['date']
        time=request.POST['time']
        num=request.POST['num_q']
        type=request.POST['type']
        tint=int(tot)
       
        
        if tint>100:
            error="Total marks not to exceed 100"
        else:
            #pass
            x = test_info.objects.all().count()
            y = list(subject_list.objects.filter(module=subject).values('course_id'))
            y=str(y)
            r=y.replace("[{","")
            o=r.replace("}]","")
            v=o.replace("'","")
            w=v.replace(':','')
            s=w.replace('course_id','')
            m=s.replace(",","")
            n_s=m
            x=str(x)
            test_id=m+x
            request.session['subject']=subject
            request.session['tot']=tot
            request.session['test_id']=test_id
            request.session['duration']=duration
            request.session['date']=date
            request.session['time']=time
            request.session['num_q']=num
            request.session['type']=type
            request.session['course_id']=m
            return HttpResponseRedirect('/testCreate')
        #create sessions for all fields

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/testinfo.html',
        {
             'title':'Test/Exam',
             'year':datetime.now().year,
             'error':error
            }
        )#Test information
#Create test
def T_Create(request):
    _var=False
    examiner=""
    test_id=""
    tot=""
    subject=""
    date=""
    time=""
    type=""
    duration=""
    num_q=""
    co_id=""
    if request.session.get('course_id'):
        co_id+="{0}".format(request.session.get('course_id'))
    if request.session.get('admin'):
        examiner+="{0}".format(request.session.get('admin'))
    if request.session.get('num_q'):
        num_q+="{0}".format(request.session.get('num_q'))
    if request.session.get('subject'):
        subject+="{0}".format(request.session.get('subject'))
    if request.session.get('duration'):
        duration+="{0}".format(request.session.get('duration'))
    if request.session.get('type'):
        type+="{0}".format(request.session.get('type'))
    if request.session.get('date'):
        date+="{0}".format(request.session.get('date'))
    if request.session.get('time'):
        time+="{0}".format(request.session.get('time'))
    if request.session.get('test_id'):
        test_id+="{0}".format(request.session.get('test_id'))
    if request.session.get('tot'):
        tot+="{0}".format(request.session.get('tot'))
    num_q=int(num_q)
    if num_q==5:
        _var=False
    elif num_q==10:
        _var=True

    if request.method=='POST':
        if not _var:
            q1= request.POST['q1']
            q2= request.POST['q2']
            q3= request.POST['q3']
            q4= request.POST['q4']
            q5= request.POST['q5']
            user=test_info.objects.create(examiner=examiner,module=subject,mark_tot=tot,test_id=test_id,type=type,date=date,duration=duration,time=time,course_id=co_id)
            u = exams.objects.create(question=q1,test_id=test_id)
            y = exams.objects.create(question=q2,test_id=test_id)
            r = exams.objects.create(question=q3,test_id=test_id)
            t = exams.objects.create(question=q4,test_id=test_id)
            f = exams.objects.create(question=q5,test_id=test_id)
            return HttpResponseRedirect('/success')
            
        elif _var:
            q1= request.POST['q1']
            q2= request.POST['q2']
            q3= request.POST['q3']
            q4= request.POST['q4']
            q5= request.POST['q5']
            q6= request.POST['q6']
            q7= request.POST['q7']
            q8= request.POST['q8']
            q9= request.POST['q9']
            q10= request.POST['q10']
            user=test_info.objects.create(examiner=examiner,module=subject,mark_tot=tot,test_id=test_id,type=type,date=date,duration=duration,time=time,course_id=co_id)
            u = exams.objects.create(question=q1,test_id=test_id)
            y = exams.objects.create(question=q2,test_id=test_id)
            r = exams.objects.create(question=q3,test_id=test_id)
            t = exams.objects.create(question=q4,test_id=test_id)
            f = exams.objects.create(question=q5,test_id=test_id)
            i = exams.objects.create(question=q6,test_id=test_id)
            b = exams.objects.create(question=q7,test_id=test_id)
            q = exams.objects.create(question=q8,test_id=test_id)
            a = exams.objects.create(question=q9,test_id=test_id)
            x = exams.objects.create(question=q10,test_id=test_id)
            return HttpResponseRedirect('/success')

    

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/setTest.html',
        {
            'title':'Test/Exam',
            'name':'Name and Surname',
            'year':datetime.now().year,
            'q':_var,
            'question':'Question'
            
            }
        )
def success(request):
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/success.html',
        {
            'title':success,
            'year':datetime.now().year
        }
        )

#test info 
def testList(request):
    #get student session
    student=""
    ref=""
    user=""
    examiner=""
    mod=""
    msg=""
   
    if request.session.get('student_no'):
        student+="{0}".format(request.session.get('student_no'))
    u=list(student_info.objects.filter(student_no=student).values('course_id'))
    student_info.objects.filter(student_no=student).update(status='online')
    y=str(u)
    r=y.replace("[{","")
    o=r.replace("}]","")
    v=o.replace("'","")
    w=v.replace(':','')
    s=w.replace('course_id','')
    id=s.replace(",","")
    #get from test list
    #get all test that equal to
    
    if test_info.objects.filter(course_id=id):
        user =test_info.objects.filter(course_id=id,date=datetime.now()).all()
        msg=""
        temp= list(test_info.objects.filter(course_id=id,date=datetime.now()).values('test_id'))
        y=str(temp)
        r=y.replace("[{","")
        o=r.replace("}]","")
        v=o.replace("'","")
        w=v.replace(':','')
        s=w.replace('test_id','')
        p=s.replace(",","")
        request.session['test_id']=p       
        dat=datetime.now()
        te= list(test_info.objects.filter(test_id=p,date=dat).values('module'))
        q=str(te)
        d=p.replace("[{","")
        m=r.replace("}]","")
        c=m.replace("'","")
        x=c.replace(':','')
        z=x.replace('test_id','')
        l=z.replace(",","")
        mod=l
        request.session['module']=mod
    else:
        if request.session.get('student'):
            student+="{0}".format(request.session.get('student'))
        msg="*Nothing scheduled for you today"+student
    

    assert isinstance(request,HttpRequest)
    return render(
            request,
            'app/testList.html',
            {
                'title':'Test/Exams',
                'year':datetime.now().year, 
                'name':'Name and Surname',
                'test_info':user,
                'message':msg
                
            }
           
        )

#admin log
def login_admin(request):
    msg=""
    if request.method=='POST':
        u = request.POST['txtuser']
        p = request.POST['txtpass']
        if admin_info.objects.filter(lecture_id=u):
            _p=list(admin_info.objects.filter(lecture_id=u).values('password'))
            _p=str(_p)
            x=_p.replace("[{","")
            y=x.replace("}]","")
            t=y.replace("'","")
            d=t.replace(':','')
            e=d.replace('password','') 
            z=e.replace(" ","")
            r=z
            if r==p:
                f=list(admin_info.objects.filter(lecture_id=u).values('fname','surname'))
                stu_no=u
                f=str(f)
                r=f.replace("[{","")
                o=r.replace("}]","")
                v=o.replace("'","")
                w=v.replace(':','')
                s=w.replace('fname','')
                g=s.replace('surname','')
                m=g.replace(",","")
                n_s=m
                msg=n_s
                request.session['lect_no']=u
                request.session['admin']=msg
                return HttpResponseRedirect('/adminDash')
            else:
                msg="invalid credentails"
        else:
            msg="invalid credentails"
        #return HttpResponseRedirect('/adminDash')
  
    assert isinstance(request,HttpRequest)
    return render(
            request,
            'app/Admin.html',
            {
                'title':'Login',
                'error':msg,
                'year':datetime.now().year, 
            }
        
        )

#student login
def login_student(request):

    data=[]
    msg=""
    n_s=""
    data = student_info.objects.all()
    
    if request.method=='POST':    
        u= request.POST['txtuser']
        p= request.POST['txtpass']   
              
        if student_info.objects.filter(student_no=u):   
            _p=list(student_info.objects.filter(student_no=u).values('password'))
            _p=str(_p)
            x=_p.replace("[{","")
            y=x.replace("}]","")
            t=y.replace("'","")
            d=t.replace(':','')
            e=d.replace('password','') 
            z=e.replace(" ","")
            r=z
            if r == p:
                f=list(student_info.objects.filter(student_no=u).values('fname','surname'))
                stu_no=u
                f=str(f)
                r=f.replace("[{","")
                o=r.replace("}]","")
                v=o.replace("'","")
                w=v.replace(':','')
                s=w.replace('fname','')
                g=s.replace('surname','')
                m=g.replace(",","")
                n_s=m
                msg=n_s
                request.session['student_no']=u
                request.session['student']=msg
                #student_info.objects.filter(student_no=u).update(status='online')
                return HttpResponseRedirect('/studentDash')           
            else:
                 msg="invalid credentails"

        else:
            msg="invalid credentails"
    #GET method
    assert isinstance(request,HttpRequest)
    return render(
                request,
                'app/login.html',
                {
                    'error':msg,
                    'title':'Login',
                    'year':datetime.now().year, 
                }
            )
def SetS(request):
    name=""
    id=""
    msg=""
    error=""
    
    
    if request.session.get('student'):
        name+="{0}".format(request.session.get('student'))
    if request.session.get('student_no'):
        id+="{0}".format(request.session.get('student_no'))
    #fields
    
    if request.method=='POST':
        pwd = request.POST['txtPass']
        pwd2= request.POST['txtRePass']
        #pass
        #regex = '(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])'
        regex='[A-Za-z0-9@?!#]'
        #regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex,pwd):
            if len(pwd)<8:
                error="Password is to short"
            elif pwd==pwd2:
            #pass
                 student_info.objects.filter(student_no=id).update(password=pwd)
                 msg="You have successfully updated your password!"
            else:
                error="Passwords you have entered do not match"
        else:
            error="Password doesn't meet requirements stated above"

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/S_set.html',
         {
            'title':'Settings',
            'year':datetime.now().year,
            'message':msg,
            'error':error
         }
      )
#reset password Admin side
def SetA(request):
    name =""
    id=""
    msg=""
    error=""
   
    
    if request.session.get('lect_no'):
        id+="{0}".format(request.session.get('lect_no'))
    if request.method=='POST':
        pwd=request.POST['txtPass']
        pwd2=request.POST['txtRePass']
        regex='[A-Za-z0-9@?!#]'
        if re.search(regex,pwd):
            #check length
            if len(pwd)<8:
                error="Password entered is too short"
            elif pwd==pwd2:
                admin_info.objects.filter(lecture_id=id).update(password=pwd)
                msg="You have successfully updated your password!"
        else:
          error="Password doesn't meet requirements stated above"


    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/A_set.html',
        {
            'year':datetime.now().year,
            'title':'Settings',
            'name':name,
            'error':error,
            'message':msg,
                
            }
        )
def Add(request):
   """Admin"""
   msg=""
   error=""
   name=""
   if request.session.get('admin'):
       name+="{0}".format(request.session.get('admin'))
   if  request.method=='POST': 
        #e =admin_info.objects.all()
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        secx='[a-zA-Z]'
        #res = list(map(itemgetter(0),e))
        d_pass="12345678"
        l_id=""
        #Get values from form
        nam= request.POST['txtnam']
        surn= request.POST['txtsur']
        email=request.POST['txtemail']
        tit= request.POST['title']
        ad= request.POST['type']
        lect=request.POST['lectId']
        pwd= d_pass
        
        #validate  email address entered
        if re.search(regex,email):
            #eValid=True    
            if admin_info.objects.filter(email=email):
                msg="email address has been taken"
            elif admin_info.objects.filter(lecture_id=lect):
                msg="lecture Id already exist"   
            elif nam.isalpha()== False:
                 error="Name has to be a non-numeric and no special characters"
            elif surn.isalpha() == False:
                 error="Surname has to be a non-numeric and no special characters"
            elif len(nam)<3:
                error="Name is too short"
            elif len(surn)<3:
                error="Surname is too short"
            else:
               user = admin_info.objects.create(fname=nam,surname=surn,email=email,lecture_id=lect,title=tit,ad_type=ad,password=pwd)
                #user.save(force_insert=True)  
               error="You have successfully added a new user"    
        else:
            msg="the email you have entered is not valid"
            #messages.info(request,msg)   
   assert isinstance(request,HttpRequest)
   return render(
           request,
           'app/AddUser.html',
               {
                'title':'Add User' ,
                'year':datetime.now().year,
                'name':name,
                'task':msg,
                'error':error
               }
        )
def addstudent(request):
    #add student
    error=""
    msg=""
    student="student"
    name=""
    pwd="12345678"
    course_id=""
    #st_no="130840"
    if request.session.get('admin'):
        name+="{0}".format(request.session.get('admin'))
    if request.method=='POST':
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        secx='[a-zA-Z]'
        nam = request.POST['txtnam']
        surn = request.POST['txtsurnam']
        email_ = request.POST['txtemail']
        #pic = request.POST['image']
        id_no = request.POST['txtid']
        co= request.POST['course']
        yr=request.POST['year']
        id_no=id_no[::-1]

        #course_id
        if co=="BSc" and yr =="1st":
            course_id="FBSC#"
        elif co=="BSc" and yr=="2nd":
            course_id="TBSC#"
        elif co=="BSc" and yr=="3rd":
            course_id="LBSC#"
        elif co=="DIT" and yr =="1st":
            course_id="FDIT#"
        elif co=="DIT" and yr=="2nd":
            course_id="SDIT#"
        elif co=="DIT" and yr=="3rd":
            course_id="LDIT#"
      
        if re.search(regex,email_):
            if student_info.objects.filter(email=email_):
                error="Email Address already exist"
            elif student_info.objects.filter(student_no=id_no):
                error="Student already exists!"
            elif len(id_no)!=13:
                error="Id number is invalid"
            elif nam.isalpha()== False:
                 error="Name has to be a non-numeric and no special characters"
            elif surn.isalpha() == False:
                 error="Surname has to be a non-numeric and no special characters"
            elif len(surn)<3:
                 error="Surname has to be a non-numeric and no special characters"
            elif len(nam)<3:
                 error="Surname has to be a non-numeric and no special characters"
            else:
                user = student_info.objects.create(student_no=id_no,email=email_,password=pwd,fname=nam,surname=surn,course=co,year=yr,course_id=course_id,type=student)
                msg="You have successfully added a new user"
        else:
            error="Invalid email format"
    assert isinstance(request,HttpRequest) 
    return render(
           request,
            'app/Add.html',
            {
                'title':'Add Student',
                'year':datetime.now().year,
                'name':name,
                'error':error,
                'message':msg,
            }
        )
def _view(request):
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/view.html',
        {
            'title':'View',
            'year': datetime.now().year,
            'name':'Name and Surname'
        }
        
  )


def OptionAdd(request):
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/Option.html',
        {
            'title':' Select User',
            'year':datetime.now().year,
            'name':'Name and Surname'
        }   
    )

def sDash(request):
   """Student dashboard"""
   name=""
   id=""
   tip=""
   default="12345678"
   if request.session.get('student'):
       name+="{0}".format(request.session.get('student'))
   if request.session.get('student_no'):
       id+="{0}".format(request.session.get('student_no'))

   student_info.objects.filter(student_no=id).update(status='online')
   x= list(student_info.objects.filter(student_no=id).values('password'))
   #f=list(student_info.objects.filter(student_no=u).values('fname','surname'))
   #stu_no=u
   x=str(x)
   r=x.replace("[{","")
   o=r.replace("}]","")
   v=o.replace("'","")
   w=v.replace(':','')
   s=w.replace('password','')
   m=s.replace(",","")
   n_s=m
   mg=n_s
   if mg== default:
       tip="Oh Looks like You need a more secure password then that buddy. Best you change it by clicking the settings icon"
   else:
       tip="Not bad your password is a bit secure but If  were you i would change it ever 14 days"
   
   if request.method=='POST':
        student_info.objects.filter(student_no=id).update(status='offline')
        #delete sessions
        return HttpResponseRedirect('/login')
   assert isinstance(request,HttpRequest)
   return render(
       request,
       'app/studentDash.html',
           {
            'title':'Dashboard',
            'year':datetime.now().year,
            'user':name,
            'tip':tip
           }
    )
def menu(request):
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/menu.html',
        {
            'title':'Menu',
            'year': datetime.now().year,
            'name':'Name and Surname'
            }
        )
def aDash(request):
    name=""
    if request.session.get('admin'):
        name+="{0}".format(request.session.get('admin'))

    obj=""
    e="Exam"
    t="Test"
    obj=exams.objects.all()
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/adminDash.html',
        {
            'title':'Dashboard',
            'year':datetime.now().year,
            'name':name,
            'obj':obj,
            'exam':e,
            'test':t,
         }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )
def Write(request,test):
    """Renders the contact page."""
    #floating button with time
    name=""
    id=""
    testid="" 
    e=""
    ex=""
    mod=""
    
    if request.session.get('examiner'):
        ex+="{0}".format(request.session.get('examiner'))
    
    if request.session.get('module'):
        mod+="{0}".format(request.session.get('module'))
    if request.session.get('test_id'):
        testid+="{0}".format(request.session.get('test_id'))
    if request.session.get('student'):
       name+="{0}".format(request.session.get('student'))
    if request.session.get('student_no'):
       id+="{0}".format(request.session.get('student_no'))
    student_info.objects.filter(student_no=id).update(status='writing')
    if exams.objects.filter(test_id=test):
        e=list(exams.objects.filter(test_id=test).all())
    #exams.objects.filter(test_id=testid).all()
    #get module
    x=str(request.get_full_path)
    if request.method=='POST':
        
        projectUrl = request.get_host() + x
        pdf = pdfkit.from_url(projectUrl, False)
        response = HttpResponse(pdf,content_type='application/pdf')
        response['Content-Dispostion']='attachment; filename=Schedule'+\
            str(datetime.now())+'.pdf'
 
        return response
    else: 
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/w.html',
            {
                'title':'Exam',
                'year':datetime.now().year,
                'name':name,
                'student_no':id,
                'date':datetime.now().date,
                'details':e,
                'examiner':ex,
                'module':testid
            }
        )
#forget password student
def _forgetStudent(request):
    error=""
    msg=""
    if request.method=='POST':
        #email= request.POST['txtemail']
        id=request.POST['txtno']
        pwd=request.POST['txtpass']
        pwd2=request.POST['txtrepass']
        regex='[a-zA-Z0-9]'
        #check if email exists
        if student_info.objects.filter(student_no=id):
            if re.search(regex,pwd):
              if len(pwd)<8:
                 error="Passowrd is too short"
              elif pwd==pwd2:
                  student_info.objects.filter(student_no=id).update(password=pwd)
                  msg="You have sucessfully reset your password!"
              elif pwd != pwd2:
                  errror="Passwords don't match"
              
            else:
                error="Password does not meet the standards mentioned above"
        else:
         error="Invalid Student Number"
    assert isinstance(request,HttpRequest)
    return render(request,'app/F_student.html',
                  {
                      'title':'Reset',
                      'year':datetime.now().year,
                      'error':error,
                      'message':msg,
                  }
                  
                  )
#forget admin
def _forgetAdmin(request):
    error=""
    msg=""
    if request.method=='POST':
        id= request.POST['txtno']
        pwd= request.POST['txtpass']
        pwd2=request.POST['txtrepass']
        regex='^[A-Za-z0-9]'
        if admin_info.objects.filter(lecture_id=id):
            if re.search(regex,pwd):
                if len(pwd)<8:
                    error="Password is too short"
                elif pwd==pwd2:
                    admin_info.objects.filter(lecture_id=id).update(password=pwd)
                    msg="You have sucessfully updated your password"
                elif pwd != pwd2:
                    error="Passwords Don't match"
            else:
                error="Password does not meet the mentioned above standards above"   
        else:
            error="Invalid Lecture Id"
    assert isinstance(request,HttpRequest)
    return render( request,'app/F_admin.html',
                  {
                      'title':'Reset',
                      'year':datetime.now().year,
                      'error':error,
                      'message':msg                     
})
def settings(request):
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/settings.html',
        {
            'title':'Settings' ,
            'year':datetime.now().year,
             'name':'Name and Surname'
            
        }
        
        )
 
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
#view all students in the db for admin
def studentView(request):
    student=""
    #c = request.GET['course']   
    #y = request.GET['year']
    if request.method=='POST':
        c=request.POST['course']
        y=request.POST['year']

        if c=="default" and y=="default":
            student=student_info.objects.all()
        elif c=="BSc" and y=="default":
            student=student_info.objects.filter(course='BSc').all()
        elif c=="BSc" and y=="1st":
            student=student_info.objects.filter(course='BSc',year='1st').all()
        elif c=="BSc" and y=="2nd":
            student=student_info.objects.filter(course='BSc',year='2nd').all()
        elif c=="BSc" and y=="3rd":
            student=student_info.objects.filter(course='BSc',year='3rd').all()
        elif c=="DIT" and y=="1st":
            student=student_info.objects.filter(course='DIT',year='1st').all()
        elif c=="DIT" and y=="2nd":
            student=student_info.objects.filter(course='DIT',year='2nd').all()
        elif c=="DIT" and y=="3rd":
            student=student_info.objects.filter(course='DIT',year='3rd').all() 
        elif c=="DIT":
            student=student_info.objects.filter(course='DIT').all()
        elif c=="BSC":
            student=student_info.objects.filter(course='BSc').all()
        elif y=="1st":
            student=student_info.objects.filter(year='1st').all()
        elif y=="2nd":
            student=student_info.objects.filter(year=y).all()
        elif y=="3rd":
            student=student_info.objects.filter(year=y).all()
    else:
        student=student_info.objects.all()
    assert isinstance(request,HttpRequest)
    return render(
        request, 'app/students.html',
        {
            'title':'Students',
            'year':datetime.now().year,
            'student':student
            }
        )
#view for schedule exams/test
def schedule(request):
    dule=""
    html=""
    options={}
    dule=test_info.objects.all()
   
    assert isinstance(request,HttpRequest)
    return render(
        request, 'app/schedule.html',
        {
            'title':'Schedule',
            'year':datetime.now().year,
            'schedule':dule
            }
        )
#submitted exam
def submit(request):
    sub=""
    msg=""
    if submitted.objects.all():
        sub=submitted.objects.all()
        msg=""
    else:
        msg="*No submitted documents yet"
    assert isinstance(request,HttpRequest)
    return render(
        request,'app/submitted.html',
        {
            'title':'Submitted',
            'year':datetime.now().year,
            'submit':sub,
            'msg':msg
            }
        )
def dule(request):
    #scheduleV

    pdfkit.from_file("w.html","paper.pdf")
    #response = HttpResponse(pdf,content_type='application/pdf')
    #response['Content-Dispostion']='attachment; filename=Schedule'+\
        #str(datetime.now())+'.pdf'
 
    return response

#upload document
def upload(request):
    x=""

    if request.method=='POST':
        upload_doc=request.FILES['file']
        fs = FileSystemStorage()
        fs.save(upload_doc.name,upload_doc)
        x="You have successfully uploaded a document"
    assert isinstance(request,HttpRequest)
    return render(
        request,'app/upload.html',{
        'title':'Upload',
        'year':datetime.now().year,
        'message':x
        })

def upload_list(request):
    return render(request,'app/upload_list.html')

def upload_pdf(request):
    if request.method =='POST':
        form =BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=BookForm()
    return render(request,'app/upload_pdf.html',{
        'form':form,
        'title':'upload',
        'year':datetime.now().year
        })
def current(request):
    current=""
    status=""
    if student_info.objects.filter(status='writing'):
        current=student_info.objects.filter(status='writing').all()
        status=""
    else:
        current=student_info.objects.filter(status='writing').all()
        status="No student is writing"

    assert isinstance(request,HttpRequest)
    return render(
        request,'app/current.html',
        {
          'title':'Writing',
          'year':datetime.now().year,
          'write':current,
          'status':status
            
         }
        
 )