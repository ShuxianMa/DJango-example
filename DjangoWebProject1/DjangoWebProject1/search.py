from django.http import HttpResponse
from django.shortcuts import render


# 表单
def search_form(request):
    return render(request, 'index.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'draw' in request.GET and request.GET['draw']:
        #message = '你绘图的内容为: ' + request.GET['draw']
        return render(request, 'pic.html',{'category':request.GET['draw']})
    else:
        message = '你提交了空表单'
        return HttpResponse(message)
