from django.shortcuts import render


def homePage(request):
    return render(request, "index.html")


def aboutUS(request):
    return render(request, "aboutus.html")


def service(request):
    return render(request, "service.html")


def contactus(request):
    return render(request, "contactus.html")


GALLERY_SECTIONS = [
    ('Building & Exterior', [
        'outer1v.JPG',
        'outer2h.JPG',
        'outer3h.JPG',
        'outer4h.JPG',
        'outer5h.JPG',
        'outer6h.JPG',
        'outer7h.JPG',
        'outer9h.JPG',
        'outer10h.JPG',
        'outer11h.JPG',
        'outer12h.JPG',
        'outer13v.JPG',
        'outer14v.JPG',
        'outer15v.JPG',
        'outer16h.JPG',
        'outer17h.JPG',
    ]),
    ('Garden', [
        'garden1v.JPG',
        'garden2h.JPG',
        'garden3v..JPG',
        'garden4v..JPG',
        'garden5h.JPG',
        'garden6h.JPG',
        'garden7v..JPG',
        'garden8h.JPG',
        'garden9v.JPG',
        'garden10.JPG',
        'garden11v.JPG',
        'garden12v.JPG',
        'garden13v.JPG',
        'garden14v.JPG',
        'garden15v.JPG',
        'garden16h.JPG',
        'garden17v.JPG',
        'garden18v.JPG',
    ]),
    ('Rooms', [
        'room_imgh4.JPG',
        'room_imgh8.JPG',
        'room_imgh9.JPG',
        'room_imgv1.JPG',
        'room_imgv2.JPG',
        'room_imgv3.JPG',
        'room_imgv5.JPG',
        'room_imgv6.JPG',
        'room_imgv7.JPG',
        'room_imgv10.JPG',
        'room_imgv11.JPG',
        'room_imgv12.JPG',
    ]),
    ('Mess, Office & More', [
        'almariv2.JPG',
        'almariv.JPG',
        'office1v.JPG',
        'office2v.JPG',
        'veenamess.JPG',
        'water.JPG',
    ]),
]


def Gallery(request):
    return render(request, "gallery.html", {"sections": GALLERY_SECTIONS})
