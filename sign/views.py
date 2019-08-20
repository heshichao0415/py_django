from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from sign.models import Basic, Statistics, Detail, testdetails
from django.forms.models import model_to_dict     #类用于将数据库中读取的数据转化为字典
from django.contrib.auth import authenticate, login
# Create your views here.
def test(request):
    return HttpResponse("Hello heshichao")

def login(request):
    return render(request, 'login.html')

# def home(request):
#     return render(request, 'home.html')

# def logout(request):
#     auth.logout(request)
#     return render(request, 'login.html')

#登录验证
def action_login(request):
    if request.method == 'POST':                  #通过request.method方法得到客户端的请求方式
        username = request.POST.get('username', '')   #通过request.POST来获取POST请求，通过get()来获取'username,和password，/此处的username和password为/
        password = request.POST.get('password', '')   #form表单对应的input属性
        user = auth.authenticate(username=username, password=password)    # 用于登录认证
        if user is not None:
            auth.login(request, user)      #调用登录
            request.session['user'] = username         #将session信息记录到浏览器
            response = HttpResponseRedirect('/py_test/')
            return response
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误请问超哥'})
    # return render(request, 'mytest.html')

#报告页面
"""
导入Model中的Basic类，通过Basic.objects.all()来获取数据库信息；
并通过render()方法附加在mytest.html页面返回给客户端
"""
@login_required
def py_test(request):
    userOBJ = Statistics.objects.get(id=1)    #获取单条数据
    data = model_to_dict(userOBJ)             #转化为字典
    del data['id']                            #删除id键对值
    data.update({'成功': data.pop('success_cases')})         #替换键
    data.update({'失败': data.pop('fail_cases')})
    data.update({'错误': data.pop('error_cases')})
    data.update({'跳过': data.pop('skip_cases')})
    test_list = Basic.objects.all()
    statis_list = Statistics.objects.all()
    detail_list = Detail.objects.all()
    username = request.session.get('user', '')
    return render(request, 'mytest.html', {'user': username, 'basics': test_list, 'data': data, 'statis': statis_list,
                                           'detail': detail_list}) #返回到前端

def py_details(request):
    username = request.session.get('user', '')
    test_name = request.GET.get('name', '')
    test_list = testdetails.objects.filter(name__contains=test_name)
    return render(request, 'details.html', {'user': username, 'tests': test_list})

