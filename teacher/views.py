from django.shortcuts import render

from django.db.models import Q
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from django.shortcuts import render,get_object_or_404,redirect
from teacher.models import Teacher
from django.contrib.auth.models import User
from django.contrib import messages
import datetime
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect,JsonResponse,Http404, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import io,csv

# Create your views here.
def index(request):
    return render(request, 'index.html')

def teacher_list(request):
    t_list = Teacher.objects.all()
    paginator=Paginator(t_list, 5)
    page_number=request.GET.get('page')
    query=request.GET.get("q")
    if query:
        t_list=t_list.filter(Q(last_name__icontains=query) | Q(subject_taught__icontains=query)).distinct()   
    try:
        t_list=paginator.page(page_number)
    except PageNotAnInteger:
        t_list=paginator.page(1)
    except EmptyPage:
        t_list=paginator.page(paginator.num_pages)
    return render(request, 'teacher_list.html', {'t_list':t_list,})


def teacher_detail(request,pk):
    t_obj = Teacher.objects.get(id=pk)
    return render(request, 'details.html', {'t_obj':t_obj,})   


from tablib import Dataset
from .resources import PersonResource

# @login_required
# def simple_upload(request):
#     if request.method == 'POST':
#         person_resource = PersonResource()
#         dataset = Dataset()
#         new_persons = request.FILES['myfile']
        
#         imported_data = Dataset().load(new_persons.read().decode('utf-8'), format='csv', headers=False)
#         print(imported_data)

#         #imported_data = dataset.load(new_persons.read())
#         result = person_resource.import_data(dataset, dry_run=True)  # Test the data import
#         print(result)

#         if not result.has_errors():
#             person_resource.import_data(dataset, dry_run=False)  # Actually import now
#             print(person_resource)

#     return render(request, 'index.html')

@login_required
def import_data(request):
    return render(request, "import.html")   


def simple_upload(request):
    user = request.user #get the current login user details
    paramFile = io.TextIOWrapper(request.FILES['myfile'].file)
    portfolio1 = csv.DictReader(paramFile)
    list_of_dict = list(portfolio1)
    print(list_of_dict,"lllllllllllllllllllllllll")
    objs = [ Teacher(
            first_name=row['First Name'],
            last_name=row['Last Name'],
            email_address=row['Email Address'],
            profile_picture=row['Profile picture'],
            mobile_number=row['Phone Number'],
            room_number=row['Room Number'],
            subject_taught=row['Subjects taught'],
           # created_by=user, #This is foreignkey value
           
        )
        for row in list_of_dict
        ]
    try:
        msg = Teacher.objects.bulk_create(objs)
        returnmsg = {"status_code": 200}
        print('imported successfully')
        return render(request, 'index.html')
    except Exception as e:
        print('Error While Importing Data: ',e)
        returnmsg = {"status_code": 500}
       
    #return JsonResponse(returnmsg)
    return render(request, 'import.html')    