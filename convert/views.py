from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from convert.utils import Convert


def upload(request):
    context = {}
    if request.method == 'POST':
        if 'action' in request.POST:
            if request.POST['action'] == 'upload':
                uploaded_file = request.FILES['file']
                fs = FileSystemStorage()
                name = fs.save(uploaded_file.name, uploaded_file)
                url = fs.url(name)
                context['url'] = url
                return render(request, 'convert/upload.html', context)
            elif request.POST['action'] == 'convert':
                if context['url']:
                    url = context['url']
                    converter = Convert()
                    converter.shapeToJson(url)
                    context['convert'] = True
                    return render(request,'convert/upload.html', context)
    return render(request, 'convert/upload.html')
