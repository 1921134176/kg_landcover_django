from django.shortcuts import render, HttpResponse
import json
from firstWEB.models import User


# Create your views here.
def index(request):
    data = {
        'patient_name': '张三',
        'age': '25',
        'patient_id': '19000347',
        '诊断': '上呼吸道感染',
    }
    # return render(request, 'index.html')
    return HttpResponse(json.dumps(data))


def calPage(request):
    return render(request, 'cal.html')


def cal(request):
    v1 = request.POST.get('value1')
    v2 = request.POST.get('value2')
    result = int(v1) + int(v2)
    print(v1, v2)
    return render(request, 'result.html', context={'data': result})
    # return render(request, 'result.html')


def login(request):
    '''
    用户登录验证
    '''
    userdata = json.loads(request.body.decode('utf-8'))
    username = userdata.get('username')
    password = userdata.get('password')
    if len(User.objects.filter(name=username, password=password)) == 1:
        data = {
            'msg': '登录成功',
            'status': 200
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    elif len(User.objects.filter(name=username)) == 1:
        data = {
            'msg': '密码错误',
            'status': 403
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    elif len(User.objects.filter(password=password)) == 1:
        data = {
            'msg': '用户名错误',
            'status': 403
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        data = {
            'msg': '无此用户信息',
            'status': 403
        }
        return HttpResponse(json.dumps(data), content_type='application/json')


def register(request):
    '''
    用户注册
    '''
    userdata = json.loads(request.body.decode('utf-8'))
    username = userdata.get('username')
    password = userdata.get('password')
    if len(User.objects.filter(name=username)) == 0:
        User.objects.create(name=username,
                            password=password,
                            role='OrdinaryUser')
        data = {
            'msg': '创建用户成功',
            'status': 201
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        data = {
            'msg': '用户已存在，创建用户失败',
            'status': 422
        }
        return HttpResponse(json.dumps(data), content_type='application/json')