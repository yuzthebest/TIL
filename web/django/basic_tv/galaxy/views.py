from django.shortcuts import render

# Create your views here.
def ping(request):
    return render(request, 'galaxy/ping.html')

def pong(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    elif request.method == 'GET':
        username = request.GET['username']
        password = request.GET['password']

    context= {
        "username" : username,
        "password" : password,
    }
    return render(request, 'galaxy/pong.html', context)

def pingpong(request):
    if request.method =="GET":
        return render(request, 'galaxy/form.html')
    elif request.method == "POST":
        c = int(request.POST['temperature'])
        f = c * 1.8 +32
        context={
            'f' : f,
        }
        return render(request, 'galaxy/result.html',context)