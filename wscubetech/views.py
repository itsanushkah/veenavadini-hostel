from django.shortcuts import render


def homePage(request):
    return render(request, "index.html")


def aboutUS(request):
    return render(request, "aboutus.html")


FACILITIES = [
    {"title": "Comfortable Rooms", "icon": "bi-house-heart", "img": "room_imgh9.JPG",
     "text": "Spacious, well-ventilated rooms with beds, storage and study tables."},
    {"title": "Mess Food", "icon": "bi-egg-fried", "img": "veenamess.JPG",
     "text": "Nutritious and hygienic meals served daily in a clean, organised dining area."},
    {"title": "24/7 CCTV Surveillance", "icon": "bi-camera-video", "img": "outer14v.JPG",
     "text": "Round-the-clock CCTV cameras and security staff keep the hostel safe and secure."},
    {"title": "Open Garden", "icon": "bi-tree", "img": "garden2h.JPG",
     "text": "A beautifully kept garden in front of the hostel for relaxing and evening walks."},
    {"title": "Water Purifier", "icon": "bi-droplet", "img": "water.JPG",
     "text": "Safe, clean drinking water from an advanced purification system."},
    {"title": "Daily Housekeeping", "icon": "bi-stars", "img": "room_imgh4.JPG",
     "text": "Rooms and common areas are cleaned regularly to keep everything hygienic."},
    {"title": "Personal Storage", "icon": "bi-lock", "img": "almariv.JPG",
     "text": "Lockable steel cupboards so every resident can keep her things safe."},
    {"title": "Peaceful Study Environment", "icon": "bi-book", "img": "room_imgv12.JPG",
     "text": "Quiet spaces that let students focus and study effectively."},
    {"title": "Friendly Office", "icon": "bi-person-check", "img": "office1v.JPG",
     "text": "Staff on hand from 9am to 10pm for parents, visitors and any help you need."},
]


def service(request):
    return render(request, "service.html", {"facilities": FACILITIES})


def contactus(request):
    return render(request, "contactus.html")


GALLERY_SECTIONS_RAW = [
    ('Building', [
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
    ('Mess & more', [
        'almariv2.JPG',
        'almariv.JPG',
        'office1v.JPG',
        'office2v.JPG',
        'veenamess.JPG',
        'water.JPG',
    ]),
]


GALLERY_SECTIONS = [
    {"title": title, "slug": slug, "images": images}
    for (title, images), slug in zip(GALLERY_SECTIONS_RAW, ["building", "garden", "rooms", "more"])
]


def Gallery(request):
    total = sum(len(s["images"]) for s in GALLERY_SECTIONS)
    return render(request, "gallery.html", {"sections": GALLERY_SECTIONS, "total": total})
