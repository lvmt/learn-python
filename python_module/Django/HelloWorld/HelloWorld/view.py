from django.http import HttpResponse
from django.shortcuts import render

# def hello(request):
#     return HttpResponse('Hello world!!') 

"""我们这里使用 render 来替代之前使用的 HttpResponse。render 还使用了一个字典 context 作为参数。
context 字典中元素的键值 "hello" 对应了模板中的变量 "{{ hello }}"。
"""
def hello(request):
    context = {}
    context['hello'] = 'hello world!aaaa'
    context['test'] = 'just a test'
    return render(request, 'hello.html', context)
    
# 完成了使用模板来输出数据，从而实现数据与视图分离。 

