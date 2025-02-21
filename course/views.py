from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
courses=[
    {"id":1,"name":"python","teacher":"AR"}
]
def course_list(request):
    data=""
    for item in courses:
        data=data+f"id={item['id']},name={item['name']},teacher={item['teacher']}"+"<br>"
    return HttpResponse(data)