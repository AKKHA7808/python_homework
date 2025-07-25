from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

# Create your views here.

def home(request):
    """หน้าแรก (Home)"""
    return render(request, 'portfolio/home.html')

def about(request):
    """หน้าเกี่ยวกับ (About)"""
    return render(request, 'portfolio/about.html')

def contact(request):
    """หน้าติดต่อ (Contact)"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message')
        
        if name and email and message:
            # บันทึกข้อความลงฐานข้อมูล
            contact_message = ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            
            messages.success(request, f'ขอบคุณ {name} สำหรับข้อความของคุณ! เราจะติดต่อกลับเร็วๆ นี้')
        else:
            messages.error(request, 'กรุณากรอกข้อมูลให้ครบถ้วน')
    
    return render(request, 'portfolio/contact.html')
