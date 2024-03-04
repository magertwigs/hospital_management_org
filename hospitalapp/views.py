
from django.shortcuts import render,redirect
from hospitalapp.models import Member,Contact,Users,Product,ImageModel
from hospitalapp.forms import ImageUploadForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        messages = Contact(name=request.POST['name'],
                           email=request.POST['email'],
                           subject=request.POST['subject'],
                           message=request.POST['message'])
        messages.save()
        return redirect('/')
    else:
        return render(request, 'index.html')

def inner(request):
    return render(request, 'inner-page.html')

def register(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        member.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def detail(request):
    details = Contact.objects.all()
    return render(request, 'details.html', {'details':details})

def users(request):
    users = Users.objects.all()
    return render(request, 'users.html', {'users':users})

def adminhome(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],
                                 password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'],
                                        password=request.POST['password'])
            return render(request, 'adminhome.html', {'member':member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})


def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'showimages.html', {'images': images})


def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')