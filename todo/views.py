from django.http import request
from django.shortcuts import render
from todo.models import sotasks

# Create your views here.

def addtask(request):
    context = {'success' : False}
    if request.method == "POST":
        #handle the form
        title = request.POST.get('task')
        print(title)
        ins = sotasks(hellotask=title)
        ins.save()
        context = {'success' : True}
        
    return render(request, 'todo/addtask.html',context)
def tasks(request):
    alltasks = sotasks.objects.all()
    # print(alltasks)
    # for item in alltasks:
    #     print(item.hellotask)
    context = {
        'tasks' : alltasks
    }
    return render(request, 'todo/tasks.html', context)
