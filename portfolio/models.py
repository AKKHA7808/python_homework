from django.db import models
from django.utils import timezone

# Create your models here.

class ContactMessage(models.Model):
    """Model สำหรับเก็บข้อความจากฟอร์มติดต่อ"""
    name = models.CharField(max_length=100, verbose_name="ชื่อ-นามสกุล")
    email = models.EmailField(verbose_name="อีเมล")
    subject = models.CharField(max_length=200, blank=True, verbose_name="หัวข้อ")
    message = models.TextField(verbose_name="ข้อความ")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="วันที่ส่ง")
    is_read = models.BooleanField(default=False, verbose_name="อ่านแล้ว")
    
    class Meta:
        verbose_name = "ข้อความติดต่อ"
        verbose_name_plural = "ข้อความติดต่อ"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject or 'ไม่มีหัวข้อ'}"
