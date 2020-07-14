from django.db import models
#导入Django自带用户模块
from django.contrib.auth.models import User

# Create your models here.

#车牌识别信息类
class VLPR_Info():
    #车牌
    vehicleLicense=''
    #车牌申请地
    vl_address=''
    #车牌底色
    vl_bgColor=''
    #车牌字体颜色
    vl_fontColor=''
    #车辆类型及说明
    vehicleInfo=''
