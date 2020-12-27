from django.shortcuts import render
from django.http import HttpResponse
from .models import logo,Skills,Project

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
    
    Skill=[skill1,skill2,skill3,skill4,skill5,skill6,skill7,skill8]
    
    projects1 = Project()
    projects1.topic = "Unit Conversion WebApp"
    projects1.year = 2018
    projects1.detail = "In this Application user can choose the property to co"
    
    projects2 = Project()
    projects2.topic = "Calculator Mobile Application"
    projects2.year = 2018
    projects2.detail = ""
    
    projects3 = Project()
    projects3.topic = "Quiz WebApplication "
    projects3.year = 2019
    projects3.detail = ""
    
    Projects = [projects1,projects2,projects3]
    
    return render(request,'index.html',{'Skill':Skill,'Logo':Logo, 'Projects':Projects})