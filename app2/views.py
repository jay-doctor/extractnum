from tkinter import Y
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import Flupld

abcd = "abcdefghijklmnopqrstuvwxyz"

def home(request):
    if request.method == "POST":
        file2 = request.FILES["file"]
        document = Flupld.objects.create(file=file2)
        document.save()
        print(file2)
        img_url = './media1/{}'.format(file2)
        # return HttpResponse(" its uploaded")

     #######################################################   
       
    
        with open(img_url, 'r') as file:
            var = file.read()
            print(var)

            var = var.lower()
            for x in range(len(abcd)):
                var = var.replace(abcd[x],(" "+abcd[x]+" "))
                print(var)
                y = var.replace('.',',').replace(' ',',')
                z = y.split(',')
                print(z)
            li = []
            for i in range(len(z)):
                if len(z[i]) == 10:
                    print(z[i])
                    li.append(z[i])
            print(li)
        with open(img_url, 'w') as file:
            file.writelines("\n".join(li))
            pass
        file.close    

       

     #######################################################
        
        return render(request, "index.html", {'img_url': img_url})
    return render(request, "index.html")


def delete_matrix(request):
    if request.method == "POST":
        documents = Flupld.objects.all().delete()
        return render(request, "index.html", {'delete': documents})
    return render(request, "index.html")
    
    
    
# Create your views here.
