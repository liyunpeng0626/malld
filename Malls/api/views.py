from django.shortcuts import render

from rest_framework.views import APIView
from api.serializers import *
from rest_framework.response import Response
from shopadmin.models import *
from datetime import datetime,time


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

        brand = PmsBrand.objects.all().order_by('price')[0:4]
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


class IndexSmsFlashPromotionSession(APIView): # 秒杀时间段(天)
    '''
    首页秒杀时间段
    '''
    def get(self,request):
        mes = {}
        # d = time.strftime("%Y/%m/%d")
        # print(d)
        # try:
        S = SmsFlashPromotionSession.objects.filter(status=1).all()[0:1]
        slist = []
        for i in S:
            sdict = {}
            sdict['id'] = i.id
            sdict['name'] = i.name
            sdict['start_time'] = i.start_time
            sdict['end_time'] = i.end_time
            aa = SmsFlashPromotionProductRelation.objects.filter(flash_promotion_session_id=i.id).all()
            sslist = []
            for j in aa:
                aaa = Pmsproduct.objects.filter(id=j.product_id)
                for l in aaa:
                    adict = {}
                    adict['id'] = l.id
                    adict['name'] = l.name
                    adict['price'] = l.price
                    adict['subTitle'] = l.subTitle
                    SMS = SmsFlashPromotionProductRelation.objects.filter(product_id=l.id).first()
                    adict['flash_promotion_price'] = SMS.flash_promotion_price
                    sslist.append(adict)
            sdict['list'] = sslist
            slist.append(sdict)
        mes['code'] = 200
        mes['message'] = '成功'
        mes['data'] = slist
        # except:

            # mes['code'] = 10010
            # mes['message'] = '失败'
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




































