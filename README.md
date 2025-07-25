# Python Homework + Django Portfolio

สำหรับส่งการบ้านวิชาเขียนโปรแกรมของ อ.พิศาล สุขขี

## 🌟 Django Portfolio Website

Portfolio เว็บไซต์ที่สร้างด้วย Django Framework พร้อม Bootstrap และ Glass-morphism Effects

### ✨ Features

- **3 หน้าหลัก**: หน้าแรก, เกี่ยวกับ, ติดต่อ
- **Responsive Design**: ใช้งานได้ดีในทุกอุปกรณ์
- **Glass-morphism Effects**: เอฟเฟกต์แก้วที่สวยงาม
- **Bootstrap Carousel**: แสดงภาพสไลด์โชว์
- **Contact Form**: ฟอร์มติดต่อที่ทำงานได้จริง
- **Thai Language Support**: รองรับภาษาไทยอย่างสมบูรณ์
- **Modern Gradient Background**: พื้นหลังไล่สีที่สวยงาม

### 🚀 Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd python_homework
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

5. **Start development server**
   ```bash
   python manage.py runserver
   ```

6. **Open in browser**
   ```
   http://localhost:8000
   ```

### 🌐 Vercel Deployment

การ deploy ไปยัง Vercel สำหรับ Django:

1. **Push ไปยัง GitHub**
   ```bash
   git add .
   git commit -m "Django Portfolio ready for deployment"
   git push origin main
   ```

2. **Connect to Vercel**
   - ไปที่ [Vercel Dashboard](https://vercel.com/dashboard)
   - Click "New Project"
   - Import จาก GitHub repository

3. **Configuration**
   - Framework Preset: `Other`
   - Build Command: `chmod +x build_files.sh && ./build_files.sh`
   - Output Directory: `staticfiles`

4. **Environment Variables** (ถ้าจำเป็น)
   ```
   DEBUG=False
   DJANGO_SETTINGS_MODULE=portfolio_site.settings
   ```

### 📁 Project Structure

```
portfolio_site/
├── portfolio/                 # Django app
│   ├── templates/portfolio/   # HTML templates
│   │   ├── base.html         # Base template
│   │   ├── home.html         # หน้าแรก
│   │   ├── about.html        # เกี่ยวกับ
│   │   └── contact.html      # ติดต่อ
│   ├── views.py              # View functions
│   └── urls.py               # URL routing
├── portfolio_site/           # Django project settings
│   ├── settings.py           # Configuration
│   ├── urls.py               # Main URL routing
│   └── wsgi.py               # WSGI application
├── static/                   # Static files
├── requirements.txt          # Python dependencies
├── vercel.json              # Vercel configuration
└── build_files.sh           # Build script for Vercel
```

### 🎨 Design Features

- **Glass-morphism**: พื้นหลังโปร่งใสแบบแก้ว
- **Gradient Animation**: พื้นหลังไล่สีเคลื่อนไหว
- **Responsive Grid**: ใช้ Bootstrap Grid System
- **Thai Typography**: ฟอนต์ Kanit สำหรับภาษาไทย
- **Interactive Elements**: ปุ่มและฟอร์มที่ตอบสนอง

### 📧 Contact Form

ฟอร์มติดต่อมีฟีเจอร์:
- การตรวจสอบข้อมูล (Validation)
- แสดงข้อความยืนยัน
- รองรับภาษาไทย
- CSRF Protection

### 🛠️ Technologies Used

- **Backend**: Django 5.2.4
- **Frontend**: Bootstrap 5.3, HTML5, CSS3
- **Icons**: Font Awesome 6.0
- **Fonts**: Google Fonts (Kanit)
- **Deployment**: Vercel
- **Database**: SQLite (development)

---

สร้างโดย Django Framework พร้อม deploy บน Vercel 🚀
