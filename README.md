# 🎓 Online Course Platform

A modern and scalable web platform for hosting and selling online courses, built with **Django**, **HTMX**, **Bootstrap**, and **Cloudinary**. The platform supports email-based user authentication, responsive design, and efficient media handling — providing both instructors and learners with a smooth and dynamic experience.

---

## 🚀 Features

- ✅ User authentication via email (secure login/signup)
- 🎥 Course creation & management
- 📂 Upload and host media via **Cloudinary**
- 📱 Mobile-first responsive UI using **Bootstrap**
- ⚡️ Dynamic interactions without full-page reloads using **HTMX**
- 🧠 Clean, readable code structure (MVC pattern with Django)
- 🛡️ CSRF protection and security best practices
- 🌐 SEO-friendly design & metadata-ready
- 📧 Email confirmation system (customizable)

---

## 🛠️ Built With

- [Django](https://www.djangoproject.com/) — Backend framework
- [HTMX](https://htmx.org/) — Lightweight AJAX & dynamic UI
- [Bootstrap 5](https://getbootstrap.com/) — UI components and layout
- [Cloudinary](https://cloudinary.com/) — Media hosting and transformation
---

⚙️ Getting Started
1. Clone the project
git clone https://github.com/yourusername/course-website-django.git
cd course-website-django

2. Create a virtual environment and install dependencies
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Set up environment variables
Create a .env file and add your secret keys and Cloudinary credentials:
SECRET_KEY=your-secret-key
DEBUG=True
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

4. Run migrations
python manage.py migrate

5. Start the development server
python manage.py runserver
Now visit http://localhost:8000 to see your site live locally.

📬 Contact
Built with 💙 by [Sina Hozhabri]
For questions, suggestions or collaboration, feel free to reach out at:
📧 sinahzdev@gmail.com




