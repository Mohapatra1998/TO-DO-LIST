from django.shortcuts import render
from django.http.response import JsonResponse
from TO_DO_APP.models import work
# Create your views here.
def homePage(request):
    all_work=work.objects.all().order_by('-created_at')
    # wid = request.GET['id']
    # if wid:
    #     work_detail=work.objects.get(pk=wid)
    # else:
    work_list=work.objects.all().order_by('-created_at')[:1:]
    for list in work_list:
        list_id=list.id
        work_detail=work.objects.get(pk=list_id)
    
    return render(request, 'home.html', {'all_work': all_work, 'work_detail':work_detail})
def workFilter(request):
    try:
        wstatus = request.GET['work_status']
        if wstatus:
            if work.objects.filter(work_status__icontains=wstatus):
                all_work=work.objects.filter(work_status__icontains=wstatus).order_by('-created_at')
                work_list=work.objects.filter(work_status__icontains=wstatus).order_by('-created_at')[:1:]
            else:
                pass
        else:
            all_work=work.objects.all().order_by('-created_at')
            work_list=work.objects.all().order_by('-created_at')[:1:]
        for list in work_list:
            list_id=list.id
            work_detail=work.objects.get(pk=list_id)
        return render(request, 'home.html', {'all_work': all_work, 'work_detail':work_detail})
    except Exception as e:
         return render(request, 'home.html')


def workAdd(request):
    if request.method=="POST":
        name=request.POST.get('work_name')
        date=request.POST.get('work_date')
        status=request.POST.get('work_status')
        des=request.POST.get('work_des')
        print(name, date, status, des)
        try:
            if name != '' and date != '' and status != '': 
                work_task = work(name=name, date=date,  work_status=status, discription=des)
                work_task.save()
                task=work.objects.values().order_by("-created_at")
                all_work=list(task)
                return JsonResponse({'status': 'Save', 'all_work': all_work})
            else:
                print('fail_1')
                return JsonResponse({'status': '0'})
        except Exception as ex:
          return JsonResponse({'status': '0'})
          
    else:
       return JsonResponse({'status': '0'})

def workUpdate(request):
    if request.method=="POST":
        wid=request.POST.get('work_id')
        name=request.POST.get('work_name')
        date=request.POST.get('work_date')
        status=request.POST.get('work_status')
        des=request.POST.get('work_des')
        print(name, date, status, des)
        try:
            if wid != '': 
                work_task = work.objects.get(id=wid)
                work_task.name=name
                work_task.date=date
                work_task.work_status=status
                work_task.discription=des
                work_task.save()
                task=work.objects.values().order_by("-created_at")

                all_work=list(task)
                return JsonResponse({'status': 1, 'all_work': all_work, 'name': work_task.name, 'date':work_task.date, 'task_status': work_task.work_status, 'des': work_task.discription})
            else:
                print('fail_1')
                return JsonResponse({'status': 0})
        except Exception as ex:
          return JsonResponse({'status': '0'})
          
    else:
       return JsonResponse({'status': '0'})

def deleteWork(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('wid')
            work_d = work.objects.get(pk=id)
            work_d.delete()
            return JsonResponse({'status': 1})
        except Exception as e:
            return JsonResponse({'status': 0})
def workDetails(request):
    id=request.GET['wid']
    print(id, 'widddd')
    if id != '': 
        work_task = work.objects.get(pk=id)
        return JsonResponse({'status': 1, 'name': work_task.name, 'date':work_task.date, 'task_status': work_task.work_status, 'des': work_task.discription})
    else:
         return JsonResponse({'status': 0})
    
       