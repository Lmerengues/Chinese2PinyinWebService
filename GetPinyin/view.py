# encoding: utf-8
from xpinyin import Pinyin
from django.http import HttpResponse
p = Pinyin()
 
def hello(request):

    source = request.GET["str"]
    pinyin = p.get_pinyin(source)
    return HttpResponse(pinyin)