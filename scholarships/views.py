from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Scholarships

@csrf_exempt
def scholarship_list(request):
    scholarships = Scholarships.objects.all()
    scholarships_list = []

    for scholarship in scholarships:
        scholarship_dict = {
            "id": scholarship.id,
            "name": scholarship.scholarship_name,
            "about": scholarship.about_scholarship,
            "eligibility": scholarship.eligibility_scholarship,
            "amount": scholarship.amount_scholarship,
            "lastDate": scholarship.lastdate_scholarship,
            "gender" : scholarship.gender,
            "course" : scholarship.course,
            "institution" : scholarship.institution,
            "documents":scholarship.documents_required.split(",") if scholarship.documents_required else [],
            "website":scholarship.website,

        }
        scholarships_list.append(scholarship_dict)

    return JsonResponse({"scholarships": scholarships_list})

@csrf_exempt
def filter_scholarships(request):
    if request.method == 'GET':
        present_class = request.GET.get('course')
        gender = request.GET.get('gender')
        institution = request.GET.get('institution')

        print("Filter Parameters:")
        print("Course:", present_class)
        print("Gender:", gender)
        print("Institution:", institution)
        
        filtered_scholarships = Scholarships.objects.all()

        # Apply filters if present_class is not None
        if present_class:
            filtered_scholarships = filtered_scholarships.filter(course__iexact=present_class)

        # Apply filters if gender is not None
        if gender:
            filtered_scholarships = filtered_scholarships.filter(gender__iexact=gender)

        # Apply filters if institution is not None
        if institution:
            filtered_scholarships = filtered_scholarships.filter(institution__iexact=institution)
        
        scholarships_data = [{'id': scholarship.id, 
            'name': scholarship.scholarship_name,
            'about': scholarship.about_scholarship,
            'eligibility': scholarship.eligibility_scholarship,
            'amount': scholarship.amount_scholarship,
            'lastDate': scholarship.lastdate_scholarship,
            'gender' : scholarship.gender,
            'course' : scholarship.course,
            'institution' : scholarship.institution,
} for scholarship in filtered_scholarships]

        print("Filtered Scholarships:")
        print(scholarships_data)
        
        return JsonResponse(scholarships_data, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
@csrf_exempt    
def add_scholarship(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Assuming the data is JSON, parse it
        print(data)
        scholarship_name = data.get('scholarship_name')
        about_scholarship = data.get('about_scholarship')
        eligibility_scholarship = data.get('eligibility_scholarship')
        amount_scholarship = data.get('amount_scholarship')
        lastdate_scholarship = data.get('lastdate_scholarship')
        gender = data.get('gender')
        course = data.get('course')
        institution = data.get('institution')
        documents_required = data.get('documents_required')
        website = data.get('website')
        print(scholarship_name)
        
        # Create a new scholarship object
        scholarship = Scholarships.objects.create(
            scholarship_name=scholarship_name,
            about_scholarship=about_scholarship,
            eligibility_scholarship=eligibility_scholarship,
            amount_scholarship=amount_scholarship,
            lastdate_scholarship=lastdate_scholarship,
            gender=gender,
            course=course,
            institution=institution,
            documents_required=documents_required,
            website =website
        )

        # Return a success response
        return JsonResponse({'message': 'Scholarship added successfully', 'id': scholarship.id})
    else:
        # Return an error response for unsupported request methods
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def scholarship_detail(request, id):
    try:
        scholarship = Scholarships.objects.get(id=id)
        if request.method == 'PUT':
            data = json.loads(request.body)
            scholarship.scholarship_name = data.get('name', scholarship.scholarship_name)
            scholarship.about_scholarship = data.get('about', scholarship.about_scholarship)
            scholarship.eligibility_scholarship = data.get('eligibility', scholarship.eligibility_scholarship)
            scholarship.amount_scholarship = data.get('amount', scholarship.amount_scholarship)
            scholarship.lastdate_scholarship = data.get('lastDate', scholarship.lastdate_scholarship)
            scholarship.gender =data.get('gender',scholarship.gender)
            scholarship.course =data.get('course',scholarship.course)
            scholarship.institution = data.get('institution',scholarship.institution)
            scholarship.documents_required = data.get('documents',scholarship.documents_required)  
            scholarship.website = data.get('website',scholarship.website)         
            scholarship.save()
            return JsonResponse({'message': 'Scholarship updated successfully'})
        else:
            # Serialize the scholarship data into JSON format
            data = {
                "id": scholarship.id,
                "name": scholarship.scholarship_name,
                "about": scholarship.about_scholarship,
                "eligibility": scholarship.eligibility_scholarship,
                "amount": scholarship.amount_scholarship,
                "lastDate": scholarship.lastdate_scholarship,
                "gender":scholarship.gender,
                "course":scholarship.course,
                "institution":scholarship.institution,
                "documents":scholarship.documents_required,
                "website":scholarship.website
            }
            return JsonResponse(data)
    except Scholarships.DoesNotExist:
        return JsonResponse({'error': 'Scholarship not found'}, status=404)

@csrf_exempt
def delete_scholarship(request, id):
    if request.method == 'DELETE':
        try:
            scholarship = Scholarships.objects.get(id=id)
            scholarship.delete()
            return JsonResponse({'message': 'Scholarship deleted successfully'})
        except Scholarships.DoesNotExist:
            return JsonResponse({'error': 'Scholarship not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def edit_scholarship(request, id):
    if request.method == 'POST':
        data = json.loads(request.body)
        scholarship = get_object_or_404(Scholarships, id=id)
        # Update scholarship details based on data
        scholarship.scholarship_name = data.get('scholarship_name')
        scholarship.about_scholarship = data.get('about_scholarship')
        scholarship.eligibility_scholarship = data.get('eligibility_scholarship')
        scholarship.amount_scholarship = data.get('amount_scholarship')
        scholarship.lastdate_scholarship = data.get('lastdate_scholarship')
        scholarship.gender = data.get('gender')
        scholarship.course = data.get('course')
        scholarship.institution = data.get('institution')
        scholarship.documents_required = data.get('documents')
        scholarship.website = data.get('website') 
        scholarship.save()
        return JsonResponse({'message': 'Scholarship updated successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
