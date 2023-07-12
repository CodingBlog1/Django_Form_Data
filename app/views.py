from django.shortcuts import render
from app.models import Member
from app.form import MemberForm
import random
li = ['soyab@g.com','how@f.com','where@f.com','for@f.com']
# Create your views here.
def home(request):
    db_data = Member.objects.all()
    email = random.choice(li)
    obj = MemberForm(auto_id=True,label_suffix=' ',initial={'memail':email})
    return render(request,'home.html',{'data':db_data,'mform':obj})


