# 🏥 VAIDYAM — Doctor Appointment Management System

**A full-stack web application that simplifies doctor appointment booking and management by connecting patients, doctors, and administrators on a single platform.**

VAIDYAM is designed to digitize the appointment management process, reduce manual work, and provide patients with a convenient way to find doctors, schedule appointments, manage medical records, and access digital prescriptions.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [System Modules](#-system-modules)
- [Application Workflow](#-application-workflow)
- [Database Design](#-database-design)
- [Project Structure](#-project-structure)
- [Installation and Setup](#-installation-and-setup)
- [Environment Configuration](#-environment-configuration)
- [Running the Project](#-running-the-project)
- [Deployment](#-deployment)
- [Security Considerations](#-security-considerations)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📖 Overview

Managing doctor appointments manually can lead to scheduling conflicts, inefficient communication, and difficulty maintaining patient records.

**VAIDYAM** addresses these challenges through a centralized, web-based appointment management system.

The application provides separate interfaces for patients, doctors, and administrators. Patients can discover doctors and request appointments, doctors can manage appointment requests and consultations, and administrators can oversee the platform.

The system also supports digital prescription generation, including PDF downloads, to make prescription management more convenient.

### 🎯 Project Objectives

- Digitize the doctor appointment booking process.
- Provide separate dashboards for different user roles.
- Simplify appointment scheduling and status management.
- Maintain organized patient and appointment information.
- Enable digital prescription generation and downloading.
- Build a scalable foundation for future healthcare-related features.

---

## ✨ Key Features

### 👤 Patient Module

- Patient registration and login.
- Secure session-based authentication.
- Search and browse available doctors.
- View doctor information and relevant details.
- Book doctor appointments.
- Track appointment status.
- View appointment history.
- Access digital prescriptions where available.

### 🩺 Doctor Module

- Dedicated doctor dashboard.
- View appointment requests.
- Approve or reject appointment requests.
- Manage scheduled appointments.
- Mark consultations as completed.
- Generate digital prescriptions for patients.
- Download prescriptions in PDF format.

### 🛡️ Admin Module

- Dedicated administrator dashboard.
- Manage doctor records.
- Oversee platform operations.
- Monitor relevant appointment and user information.

*The exact administrative actions depend on the permissions implemented in the application.*

### 📄 Digital Prescription Management

- Generate digital prescriptions.
- Associate prescriptions with relevant patient and consultation records.
- Download prescriptions as PDF documents.
- Reduce dependence on handwritten prescription records.

### 🔐 Authentication and Access Control

- Session-based authentication.
- Role-specific dashboards.
- Separation of patient, doctor, and administrator functionality.
- Server-side access control for protected operations.

---

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Frontend | HTML5, CSS3, JavaScript |
| UI Framework | Bootstrap |
| Backend | Python |
| Web Framework | Django |
| Database | TiDB Cloud / MySQL-compatible database |
| Authentication | Django authentication and sessions |
| Version Control | Git and GitHub |
| Deployment | Vercel and configured backend/database services |
| Document Generation | PDF generation functionality |

### How the Technologies Work Together

- **HTML, CSS, Bootstrap and JavaScript:** Build the user interface and responsive web pages.
- **Python and Django:** Handle business logic, authentication, requests, and database operations.
- **TiDB Cloud:** Provides cloud-hosted database capabilities when configured with the application.
- **Git and GitHub:** Support version control and collaborative development.
- **Deployment services:** Make the configured application accessible online.

*The exact deployment architecture depends on how the Django backend, frontend, and database are connected in the deployed version.*

---

## 🧩 System Modules

| Module | Responsibility |
|---|---|
| Authentication | Login, registration, sessions and access control |
| Patient Management | Patient accounts and relevant records |
| Doctor Management | Doctor information and administration |
| Appointment Management | Booking, approval, rejection and completion |
| Prescription Management | Digital prescription creation and PDF downloads |
| Admin Dashboard | Administrative operations and oversight |

---

## 🔄 Application Workflow

1. **User Registration:** Patients and doctors access the system through their respective accounts.
2. **Authentication:** Users log in and access the appropriate dashboard.
3. **Doctor Discovery:** Patients browse or search for doctors.
4. **Appointment Booking:** Patients submit appointment requests.
5. **Appointment Management:** Doctors review and approve or reject requests.
6. **Consultation:** The appointment progresses through its relevant status.
7. **Prescription Generation:** The doctor generates a digital prescription when applicable.
8. **PDF Download:** The prescription can be downloaded for future reference.

---

## 🗄️ Database Design

The application uses a relational database to organize users, doctors, appointments, and prescription information.

The following entities represent the conceptual data model. Actual table names and relationships may differ in the implementation.

| Entity | Purpose |
|---|---|
| User | Stores authentication and account information |
| Doctor | Stores doctor-specific information |
| Patient | Stores patient-specific information |
| Appointment | Stores booking details, scheduling information and status |
| Prescription | Stores prescription details associated with a consultation |

### Important Relationships

- A patient can have multiple appointments.
- A doctor can receive multiple appointment requests.
- An appointment connects a patient with a doctor.
- A prescription can be associated with the relevant patient, doctor, and appointment.

These relationships help maintain consistency and organize healthcare-related information efficiently.

---

## 📁 Project Structure

The following is an illustrative Django project structure. Adjust the names to match your actual repository.

```text
VAIDYAM/
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── apps/
│   ├── accounts/
│   ├── doctors/
│   ├── patients/
│   ├── appointments/
│   └── prescriptions/
│
├── templates/
│   ├── base.html
│   ├── accounts/
│   ├── doctors/
│   ├── patients/
│   └── appointments/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── media/
    └── prescriptions/
```

**Note:** This tree illustrates a possible organization, not a verified listing of the actual repository. Your existing Django app names and directory structure should take precedence.

---

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### Prerequisites

Install the following:

- Python 3.10 or a version compatible with your project dependencies.
- pip.
- Git.
- A configured MySQL-compatible database or the project's existing TiDB Cloud connection.

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_DIRECTORY>
```

Replace the placeholders with your actual repository URL and directory name.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

If the repository includes a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If it does not, install the dependencies required by your actual Django project and create a dependency file before sharing the repository.

### 4. Configure Environment Variables

Create a `.env` file in the project's root directory if your settings use environment variables.

Add the required Django secret, database connection details, and other settings based on your implementation.

Do not commit real credentials to GitHub.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

Ensure that the configured database is accessible before running migrations.

### 6. Create an Administrator Account

```bash
python manage.py createsuperuser
```

Follow the prompts to create an administrator account if Django Admin is enabled in your project.

### 7. Start the Development Server

```bash
python manage.py runserver
```

Open the following address in your browser:

http://127.0.0.1:8000/

The application should now be accessible locally, provided that the configuration and dependencies are correct.

---

## 🔑 Environment Configuration

Keep sensitive configuration outside the source code.

Example configuration keys may include:

```env
DJANGO_SECRET_KEY=replace-with-a-secure-secret
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=3306
```

These are illustrative variable names. Your application must explicitly load and use them in Django settings, and the names must match your actual database configuration.

**Important:** Never upload production credentials, database passwords, API keys, or private environment files to a public repository.

---

## 🚀 Deployment

VAIDYAM has been developed with deployment in mind.

The deployed configuration may include:

- **Application hosting:** Vercel or the configured backend hosting platform.
- **Database hosting:** TiDB Cloud or another compatible configured database service.
- **Source code:** GitHub repository.
- **Production configuration:** Environment variables and deployment-specific settings.

### Production Checklist

Before deploying or redeploying, verify:

- `DEBUG` is disabled in production.
- A secure `SECRET_KEY` is configured through environment variables.
- `ALLOWED_HOSTS` contains the appropriate hostnames.
- Database credentials are configured securely.
- Static files are collected and served correctly.
- Database migrations have been applied.
- HTTPS and secure session settings are configured appropriately.
- The deployment platform supports the Django application's runtime requirements.

A Django application may require additional configuration or a separate backend hosting service depending on the deployment platform. Confirm that your actual hosting setup supports the project's WSGI/ASGI application and database connectivity.

**Live Demo:** Add your working deployment URL here.

**GitHub Repository:** Add your repository URL here.

---

## 🔐 Security Considerations

Because VAIDYAM handles patient and appointment information, security and privacy are important.

- Use Django's authentication and authorization mechanisms appropriately.
- Enforce role-based permissions on the server, not only in the frontend.
- Validate user input and appointment-related requests.
- Keep secrets and database credentials out of version control.
- Use HTTPS and secure cookie settings in production.
- Restrict access to prescriptions and patient records to authorized users.
- Avoid exposing real patient data in screenshots, demonstrations, or test fixtures.
- Follow applicable data protection requirements before using real healthcare information.

This project should not be considered a certified medical or healthcare compliance system unless it has undergone the relevant reviews and assessments.

---

## 🔮 Future Enhancements

Potential improvements for future versions include:

- 📅 Doctor availability calendars and conflict prevention.
- 🔔 Email or SMS appointment reminders.
- 💳 Online appointment payments.
- 📹 Video consultation integration.
- ⭐ Patient feedback and doctor ratings.
- 📊 Analytics dashboards for appointments and platform usage.
- 🧾 Improved prescription templates and printable medical summaries.
- 📱 Progressive Web App (PWA) support.
- 🔍 Advanced doctor search and filtering.
- 🧪 Automated unit, integration, and end-to-end tests.
- 🐳 Docker-based development and deployment.
- 🤖 AI-assisted healthcare information features with appropriate clinical safeguards.

These are proposed enhancements and are not claimed to be implemented in the current version.

---

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork the repository.
2. Create a feature branch.

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes.
4. Test your changes locally.
5. Commit your work.

   ```bash
   git commit -m "Add: describe your feature"
   ```

6. Push your branch.

   ```bash
   git push origin feature/your-feature-name
   ```

7. Open a Pull Request describing your changes.

Please avoid including real patient data, credentials, or other sensitive information in contributions.

---

## 📄 License

This project does not currently specify a license.

If you want others to reuse, modify, or distribute your source code, choose an appropriate open-source license and add a `LICENSE` file to the repository. Do not assume that public availability alone grants permission to reuse the code.

---

## 👨‍💻 Author

**Atharv Shukla**

Computer Science Engineering

Project: **VAIDYAM — Doctor Appointment Management System**

GitHub: https://github.com/Atharv7518

LinkedIn: https://www.linkedin.com/in/atharv-shukla-20bb0633b?utm_source=share_via&utm_content=profile&utm_medium=member_ios

---

<p align="center">
  <strong>VAIDYAM — Simplifying Doctor Appointments Through Technology 🏥</strong>
</p>
