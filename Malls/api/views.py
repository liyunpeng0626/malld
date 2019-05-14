from django.shortcuts import render

from rest_framework.views import APIView
from api.serializers import *
from rest_framework.response import Response
from shopadmin.models import *


# 轮播图列表页
class Advertising_list(APIView):
    '''
 轮播图列表页
    '''
    def get(self,request):

        advertising = SmsHomeAdvertise.objects.all()
        advertising_s =SmsHomeAdvertiseModelSerializer(advertising,many=True)
        mes = {}
        mes['code'] = 200
        mes['advertising'] = advertising_s.data
        return Response(mes)

# 新闻展示页
class News_list(APIView):
    '''
 新闻展示页
    '''
    def get(self,request):

        news = News.objects.all()
        news_s = NewsModelSerializer(news,many=True)
        mes = {}
        mes['code'] = 200
        mes['news'] = news_s.data
        return Response(mes)



# 品牌列表页
class Brand_list(APIView):
    
    '''
 品牌列表页
    '''
    def get(self,request):

        brand = PmsBrand.objects.all().order_by('price')[0:6]
        brand_s =PmsbrandModelSerializer(brand,many=True)
        mes = {}
        mes['code'] = 200
        mes['brand'] = brand_s.data 
        return Response(mes)

# 秒杀活动展示页
class Activity_list(APIView):
    '''
 秒杀活动展示页
    '''
    def get(self,request):

        activity = SmsFlashPromotion.objects.all()
        activity_s =SmsFlashPromotionModelSerializer(activity,many=True)
        mes = {}
        mes['code'] = 200
        mes['activity'] = activity_s.data
        return Response(mes)


# 秒杀活动时间展示页
class Activity_time_list(APIView):
    '''
 秒杀活动时间展示页
    '''
    def get(self,request):

        activity_time = SmsFlashPromotionSession.objects.all()
        activity_time_s = SmsFlashPromotionSessionModelSerializer(activity_time,many=True)
        mes = {}
        mes['code'] = 200
        mes['activity_time'] = activity_time_s.data
        return Response(mes)


# 新鲜好物展示页
class Goods_list(APIView):
    '''
    新鲜好物展示页
    '''
    def get(self,request):

        goods = Pmsproduct.objects.all()[0:2]
        goods_s = PmsproductModelSerializer(goods,many=True)
        mes = {}
        mes['code'] = 200
        mes['goods'] = goods_s.data
        return Response(mes)


# 人气推荐
class Goodss_list(APIView):
    '''
    人气推荐
    '''
    def get(self,request):

        goods = Pmsproduct.objects.all()[0:3]
        goods_s = PmsproductModelSerializer(goods,many=True)
        mes = {}
        mes['code'] = 200
        mes['goods'] = goods_s.data
        return Response(mes)

# 专题推荐
class Subject_list(APIView):
    '''
    专题推荐
    '''
    def get(self,request):

        subject = CmsSubject.objects.all()[0:1]
        subject_s = CmsSubjectModelSerializer(subject,many=True)
        mes = {}
        mes['code'] = 200
        mes['subject'] = subject_s.data
        return Response(mes)



# 猜你喜欢
class Cai_list(APIView):
    '''
    猜你喜欢
    '''
    def get(self,request):

        goods = Pmsproduct.objects.all()[0:4]
        goods_s = PmsproductModelSerializer(goods,many=True)
        mes = {}
        mes['code'] = 200
        mes['goods'] = goods_s.data
        return Response(mes)


# 话题详情表展示
class Topic_list(APIView):
    '''
    话题详情表展示
    '''
    def get(self,request):

        topic = CmsTopic.objects.all()
        topic_s = CmsTopicModelSerializer(topic,many=True)
        mes = {}
        mes['code'] = 200
        mes['topic'] = topic_s.data
        return Response(mes)








































