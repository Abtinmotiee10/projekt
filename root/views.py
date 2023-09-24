from django.shortcuts import render






def home(request):
    return render(request,"root/index.html")


def about(request):
    return render(request,"root/inner-page.html")



def contact(request):
    return render(request,"root/portfolio-details.html")


