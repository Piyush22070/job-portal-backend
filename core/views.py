import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Company, JobPost, Applicant
from django.shortcuts import get_object_or_404

@csrf_exempt
def create_company(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get("name")
        location = data.get("location")
        description = data.get("description")
        if not all([name, location, description]):
            return JsonResponse({"error": "Missing fields"}, status=400)
        company = Company.objects.create(name=name, location=location, description=description)
        return JsonResponse({"id": company.id, "status": "Company created"})

@csrf_exempt
def post_job(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            company = Company.objects.get(id=data.get("company_id"))
        except Company.DoesNotExist:
            return JsonResponse({"error": "Company not found"}, status=404)
        job = JobPost.objects.create(
            company=company,
            title=data.get("title"),
            description=data.get("description"),
            salary=data.get("salary"),
            location=data.get("location")
        )
        return JsonResponse({"id": job.id, "status": "Job posted"})

def list_jobs(request):
    jobs = JobPost.objects.select_related("company").all()
    data = [{
        "id": job.id,
        "title": job.title,
        "company": job.company.name,
        "location": job.location
    } for job in jobs]
    return JsonResponse(data, safe=False)

@csrf_exempt
def apply_job(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            job = JobPost.objects.get(id=data.get("job_id"))
        except JobPost.DoesNotExist:
            return JsonResponse({"error": "Job not found"}, status=404)
        applicant = Applicant.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            resume_link=data.get("resume_link"),
            job=job
        )
        return JsonResponse({"id": applicant.id, "status": "Applied successfully"})

def get_applicants(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    applicants = Applicant.objects.filter(job=job)
    data = [{
        "name": a.name,
        "email": a.email,
        "resume_link": a.resume_link,
        "applied_at": a.applied_at
    } for a in applicants]
    return JsonResponse(data, safe=False)
