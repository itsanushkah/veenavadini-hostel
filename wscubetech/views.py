from django.http import HttpResponse
from django.shortcuts import render

#html page render 
def homePage(request):
    #How to Pass Data From Django View to Template from here to
    # data={
    #     "title":" welcome to my Home Page",
    #     "bdata":"This is a ran designed homepage using only HTML and CSS..",
    #     "clist":["php","java", "c++"],
    #     "student_details":[
    #         {"name":"pradeep","phone":1234567890},
    #          {"name":"jeetu","phone":67890}
    #         ],
    #     "numbers":[14,23,33,42,25,55]
    # }
    # #here

    return render(request,'index.html')
#static call url
def aboutUS(request):
   return render(request,'aboutus.html')
def service(request):
   return render(request,'service.html')
def Course(request):
    return HttpResponse("Welcome checkout our Course")
def contactus(request):
    return render(request,'contactus.html')
def Gallery(request):
   return render(request,'gallery.html')

#dynamic url call
def CourseDetails(request,courseid):
    return HttpResponse(courseid)

# Use a list in the view and pass it to the template. Step 1: In your view function (views.py), pass the image numbers as a list:
# views.py
def Gallery(request):
    image_list = [
       
    "outer6h.JPG", "outer7h.JPG", "outer9h.JPG", "outer10h.JPG",
    "outer11h.JPG", "outer12h.JPG","outer2h.JPG", "outer3h.JPG", "outer16h.JPG", "outer17h.JPG",
    "garden2h.JPG", "garden5h.JPG",
    "garden16h.JPG", "room_imgh4.JPG", "garden6h.JPG","outer4h.JPG", "outer5h.JPG", "garden8h.JPG", "room_imgh8.JPG", "room_imgh9.JPG"

    ]
    return render(request, 'gallery.html', {'image_list': image_list})
