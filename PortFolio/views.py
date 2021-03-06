from django.shortcuts import render
from django.http import HttpResponse
from .models import logo,Skills,Project
from datetime import datetime
from django.core.mail import send_mail

# Create your views here.

def home(request):
    Logo = logo()
    Logo.img = 'logo.png'

    skill1 = Skills()
    skill1.name = 'HTML'
    skill1.exp = 'Expert'
    skill1.img = 'html.png'
    
    skill2 = Skills()
    skill2.name = 'CSS'
    skill2.exp = 'Intermediate'
    skill2.img = 'CSS.png'

    skill3 = Skills()
    skill3.name = 'JavaScript'
    skill3.exp = 'Intermediate'
    skill3.img = 'javascript.png'

    skill4 = Skills()
    skill4.name = 'Python'
    skill4.exp = 'Intermediate'
    skill4.img = 'Python.png'
    
    skill5 = Skills()
    skill5.name = 'C Language'
    skill5.exp = 'Intermediate'
    skill5.img = 'C.png'

    skill6 = Skills()
    skill6.name = 'CPP'
    skill6.exp = 'Intermediate'
    skill6.img = 'Cpp.png'
    
    skill7 = Skills()
    skill7.name = 'Django'
    skill7.exp = 'Intermediate'
    skill7.img = 'Django.jpg'
    
    skill8 = Skills()
    skill8.name = 'VSC'
    skill8.exp = 'Intermediate'
    skill8.img = 'Vsc.png'
    
    skill9 = Skills()
    skill9.name = 'SQL'
    skill9.exp = 'Intermediate'
    skill9.img = 'sql.png'
    
    skill10 = Skills()
    skill10.name = 'jQuery'
    skill10.exp = 'Beginner'
    skill10.img = 'jquery.png'
    
    
    Skill=[skill1,skill2,skill3,skill4,skill5,skill6,skill7,skill8,skill9,skill10]
    
    projects1 = Project()
    projects1.topic = "Unit Conversion WebApp"
    projects1.year = 2018
    projects1.detail = "Unit conversion is a multi-step process that involves multiplication or division by a numerical factor, selection of the correct number of significant digits, and rounding. The Application Was Developed using following Languages. "
    projects1.icon1 = "js"
    projects1.icon2 = "html5"
    projects1.icon3 = "css3-alt"
    
    projects2 = Project()
    projects2.topic = "Calculator Mobile Application"
    projects2.year = 2018
    projects2.detail = "This Calculator app is an application developed for android cells phones and tablets. It enables the users to perform fundamental mathematical operations such as addition, subtraction, multiplication and division on their phone. Being installed on phone, it always remains with the user, helps in daily life calculations and works as a typical android calculator app."
    projects2.icon1 = "java"
    projects2.icon2 = "android"
    
    projects3 = Project()
    projects3.topic = "Quiz WebApplication "
    projects3.year = 2019
    projects3.detail = "The Online Quiz is a web application for candidate to appear for an online test in an effective way and there is no loss of time to check the paper. The chief aim of Online Quiz is to effectively estimate the candidate completely via a totally automated system which besides preserving time, offers swifter outcomes. The Application was Developed using following languages"
    projects3.icon1 = "js"
    projects3.icon2 = "html5"
    projects3.icon3 = "css3-alt"
    projects3.icon4 = "php"
    projects3.icon5 = "database"
    
     
    Projects = [projects1,projects2,projects3]
    
    if request.method == "POST":
           
        email = request.POST['email']
        name = request.POST['name']
        phone = request.POST["phone"]
        message = request.POST["message"]
        full_Message = ("From : " + email
                    + "\nName : " + name 
                    + "\nContact No : " + phone
                    + "\nMessage : " + message)
        send_mail(
                    name,
                    full_Message,
                    email,
                    ['rohitbyadav786@gmail.com'],
        )
        return render(request, 'index.html', {'Skill':Skill,'Logo':Logo, 'Projects':Projects,'senders_name': name})
    else:
        return render(request,'index.html',{'Skill':Skill,'Logo':Logo, 'Projects':Projects})
