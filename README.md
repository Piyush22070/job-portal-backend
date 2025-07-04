# Job Portal API

A Django-based backend for a job portal built using **core Django only** — no Django REST Framework (DRF).  
It allows companies to post jobs and applicants to apply, returning JSON responses manually using `JsonResponse`.

---

##  Features

-  Create companies
-  Post jobs
-  Apply to jobs
-  View job listings
-  View applicants for a specific job

---

##  Tech Stack

- **Backend**: Django (no DRF)
- **Database**: SQLite
- **Views**: Function-based views
- **API**: Manual JSON response using `JsonResponse`

---

##  Setup Instructions

```bash
git clone https://github.com/Piyush22070/job-portal-backend
cd job_portal_api

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create database tables
python manage.py makemigrations
python manage.py migrate

# Run the development server
python manage.py runserver

```

| Method | Endpoint                    | Description                    |
| ------ | --------------------------- | ------------------------------ |
| POST   | `/api/create-company/`      | Create a new company           |
| POST   | `/api/post-job/`            | Post a new job under a company |
| GET    | `/api/jobs/`                | List all job posts             |
| POST   | `/api/apply/`               | Apply to a job                 |
| GET    | `/api/applicants/<job_id>/` | List all applicants for a job  |


Base URL: Base URL: http://127.0.0.1:8000/

API Endpoints + Sample JSON
1. Create Company
POST /api/create-company/
```bash
{
  "name": "Google",
  "location": "Bangalore",
  "description": "Tech company"
}
```
```bash
{
  "id": 1,
  "status": "Company created"
}
```
2. Post Job
POST /api/post-job/
```bash
{
  "company_id": 1,
  "title": "Backend Developer",
  "description": "Experience with Django",
  "salary": 60000,
  "location": "Remote"
}
```
Response:
```bash
{
  "id": 1,
  "status": "Job posted"
}
```
3. Get All Jobs
GET /api/jobs/

Response:
```bash
[
  {
    "id": 1,
    "title": "Backend Developer",
    "company": "Google",
    "location": "Remote"
  }
]
```
4. Apply for Job
POST /api/apply/
```bash
{
  "name": "John Doe",
  "email": "john@example.com",
  "resume_link": "https://example.com/resume.pdf",
  "job_id": 1
}
```
Response:
```bash
{
  "id": 1,
  "status": "Applied successfully"
}
```
5. Get Applicants for a Job
GET /api/applicants/1/
Response
```bash
[
  {
    "name": "John Doe",
    "email": "john@example.com",
    "resume_link": "https://example.com/resume.pdf",
    "applied_at": "2025-07-04T17:42:00Z"
  }
]
```
Testing
Use Thunder Client or Postman

Set Content-Type: application/json
