import json
import urllib
from bs4 import BeautifulSoup
import datetime
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from PIL import Image
from predict import prediction
from django.http import HttpResponse
from Django_demo1.settings import MEDIA_ROOT

#pip3 install --default-timeout=100 tensorflow -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
def main(request):
    return render(request, 'main.html', {})

@xframe_options_exempt
def getImageModule(request):
    return render(request,'uploadImage_module.html',{})

#------------------------函数名结尾的R为Recognization-------------------

#-------------------车牌识别-------------
def vehicleLicensePlateR(request):
    return render(request,'vehicleLicensePlateR.html', {})


def get_VLPR_info(request):
    img=request.FILES['img']
    print(img)
    print(img.size)
    print(type(img))

    imgName='%s%s'%(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-'),img.name)
    save_path = "%s/%s" % (MEDIA_ROOT,imgName)
    with open(save_path, 'wb') as f:
        # img.chunks()为图片的一系列数据，它是一一段段的，所以要用for逐个读取
        for content in img.chunks():
            f.write(content)

    result={
        'vehicleLicense':'aaa',
        'vl_address':'北京',
        'vl_bgColor':'红',
        'vl_fontColor':'黄',
        'vehicleInfo':'军用卡车'
    }
    return HttpResponse(json.dumps(result))

#根据车牌号分析出车辆信息
def getPlateInfo(plateStr):
    url="https://chepai.911cha.com/"

    data_dict={"q":plateStr}                          #post参数
    data_string=urllib.parse.urlencode(data_dict)     #使用urlencode将字典参数序列化成字符串
    last_data=bytes(data_string,encoding='utf-8')     #将序列化后的字符串转换成二进制数据，因为post请求携带的是二进制参数

    req = urllib.request.Request(url,data=last_data)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0")

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    soup=BeautifulSoup(html,'html.parser')
    p=soup.find_all("p")                              #使用bs4将所有的<p></p找出来>

    type=str(p[1]).replace('</p>','').replace('<p>类型：','')          #车牌类型
    province=str(p[2]).replace('</p>','').replace('<p>省份：','')      #车牌省份
    city=str(p[3]).replace('</p>','').replace('<p>城市：','')          #车牌城市

    return type,province,city

#-----------------车型识别------------------
def vehicleTypeR(request):
    return render(request, 'vehicleTypeR.html', {})

def get_VTR_info(request):
    img = request.FILES['img']

    imgName = '%s%s' % (datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-'), img.name)
    save_path = "%s/%s" % (MEDIA_ROOT, imgName)
    with open(save_path, 'wb') as f:
        # img.chunks()为图片的一系列数据，它是一一段段的，所以要用for逐个读取
        for content in img.chunks():
            f.write(content)

    image=Image.open(save_path)
    result=prediction(image)
    return HttpResponse(json.dumps(result))