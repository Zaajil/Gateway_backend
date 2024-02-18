from django.shortcuts import render
from .models import Scholarships
from django.http import JsonResponse

def view(request):
     scholarships = Scholarships.objects.all()
     scholarships_list =[]

     for s in scholarships:
          s_dict ={
               "name": s.scholarship_name,
               "about": s.about_scholarship,
               "eligibility":s.eligibility_scholarship,
               "amount" : s.amount_scholarship,
               "lastDate":s.lastdate_scholarship
          } 
          scholarships_list.append(s_dict)

     return JsonResponse({"scholarships":scholarships_list})
