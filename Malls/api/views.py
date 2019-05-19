from django.shortcuts import render

from rest_framework.views import APIView
from api.serializers import *
from rest_framework.response import Response
from shopadmin.models import *
from django_redis import get_redis_connection




# 连接
class Index(APIView):
    def get(self,request):
        conn = get_redis_connection('default')
        print(conn.get("name"))
        return Response('ok')



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
            aa = SmsFlashPromotionProductRelation.objects.filter(flash_promotion_session_id=i.id)
            sslist = []
            for j in aa:
                aaa = Pmsproduct.objects.filter(id=j.product_id).all()
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


# 分类页展示
class Product_category(APIView):
    '''
    分类页展示数据
    '''
    def get(self,request):
        category = PmsProductCategory.objects.filter(level_l=0).all()
        l_list = []
        for cate in category:
            l_dict = {}
            l_dict['id'] = cate.id
            l_dict['name'] = cate.name
            two_cate = PmsProductCategory.objects.filter(parent_id=cate.id).all()
            m_list = []
            for two in two_cate:
                m_dict = {}
                m_dict['id'] = two.id
                m_dict['name'] = two.name
                m_dict['image'] = two.image
                m_list.append(m_dict)
            l_dict['list'] = m_list
            l_list.append(l_dict)

        category_s =PmsProductCategoryModelSerializer(category,many=True)
        mes = {}
        mes['code'] = 200
        mes['advertising'] = l_list
        return Response(mes)



# 分类专题展示与专题
class Subject_category(APIView):
    '''
    专题分类与专题详情展示
    '''
    def get(self,request):
        l_list = []
        cate_show_detail = CmsSubjectCategory.objects.all()
        for item in cate_show_detail:
            l_dict = {}
            l_dict['id'] = item.id
            l_dict['name'] = item.name
            l_dict['icon'] = item.icon
            la = CmsSubject.objects.filter(category_id=item.id).all()
            j_list = []
            for j in la:
                j_dict = {}
                j_dict['title'] = j.title
                j_dict['pic'] = j.pic
                j_dict['category_name'] = j.category_name
                j_dict['subheading'] = j.subheading
                j_dict['price'] = j.price
                j_dict['read_count'] = j.read_count
                #收藏次数
                j_dict['collect_count'] = j.collect_count
                #评论次数
                j_dict['comment_count'] = j.comment_count
                j_list.append(j_dict)
        l_dict['list'] = j_list
        l_list.append(l_dict)
        mes = {}
        mes['code'] = 200
        mes['category'] = l_list
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

# 话题分类展示页
class Topic_category(APIView):
    '''
    话题分类展示页
    '''
    def get(self,request):

        topic_category = CmsTopicCategory.objects.all()
        topic_category_s = CmsTopicCategoryModelSerializer(topic_category,many=True)
        mes = {}
        mes['code'] = 200
        mes['topic_category'] = topic_category_s.data
        return Response(mes)

# 话题分类详情页
class Topic_category_details(APIView):
    '''
    话题分类详情页
    '''
    def get(self,request):

        l_list = []
        cate_show_detail = CmsTopicCategory.objects.all()
        for item in cate_show_detail:
            l_dict = {}
            l_dict['id'] = item.id
            l_dict['name'] = item.name
            l_dict['icon'] = item.icon
            la = CmsTopic.objects.filter(category_id=item.id).all()
            j_list = []
            for j in la:
                j_dict = {}
                j_dict['name'] = j.name
                j_dict['pic'] = j.pic
                j_dict['create_time'] = j.create_time
                j_dict['read_count'] = j.read_count
                j_dict['attention_count'] = j.attention_count
                j_dict['attend_count'] = j.attend_count
                j_dict['label'] = j.label

                j_list.append(j_dict)
            l_dict['topic_list'] = j_list
            l_list.append(l_dict)
        mes = {}
        mes['code'] = 200
        mes['category'] = l_list
        return Response(mes)
        
    
# 话题评论展示页
class Topic_comment(APIView):
    '''
    话题评论数据展示
    '''
    def get(self,request):

        topic_comment = CmsTopicComment.objects.all()
        topic_comment_s = CmsTopicCommentModelSerializer(topic_comment,many=True)
        mes = {}
        mes['code'] = 200
        mes['topic_comment'] = topic_comment_s.data
        return Response(mes)


# 话题分类与话题详情关联
class Topic_category_guan(APIView):
    '''
    话题分类与话题详情与话题评论关联
    '''
    def get(self,request):
        l_list = []
        cate_show_detail = CmsTopicCategory.objects.all()
        for item in cate_show_detail:
            l_dict = {}
            l_dict['id'] = item.id
            l_dict['name'] = item.name
            la = CmsTopic.objects.filter(category_id=item.id).all()
            j_list = []
            for j in la:
                j_dict = {}
                j_dict['id'] = j.id
                j_dict['name'] = j.name
                j_dict['pic'] = j.pic
                j_dict['create_time'] = j.create_time
                j_dict['read_count'] = j.read_count
                j_dict['attention_count'] = j.attention_count
                j_dict['attend_count'] = j.attend_count
                j_dict['label'] =j.label
                fen = CmsTopicComment.objects.filter(topic_id = j.id).order_by('-like_count')[:1]
                f_list = []
                for f in fen:   
                    f_dict = {}
                    f_dict['member_nick_name'] = f.member_nick_name
                    f_dict['member_icon'] = f.member_icon
                    f_dict['content'] = f.content
                    f_dict['create_time'] = f.create_time
                    f_dict['like_count'] = f.like_count
                    f_dict['comment_count'] = f.comment_count
                    f_list.append(f_dict)
                j_dict['comment_list'] = f_list
                j_list.append(j_dict)
            l_dict['topic_list'] = j_list
            l_list.append(l_dict)
        mes = {}
        mes['code'] = 200
        mes['topic_category'] = l_list
        return Response(mes)


# 品牌制造商详情页
class Brand_details(APIView):
    '''
    品牌制造商详情页
    '''
    def get(request,self):

        brand = PmsBrand.objects.all()
        brand_s = PmsbrandDetaileModelSerializer(brand,many=True)
        mes = {}    
        mes['code'] = 200
        mes['brand'] = brand_s.data 
        return Response(mes)

# 品牌详情相关商品
class Product_Count(APIView):
    '''
    品牌详情相关商品页面
    根据你点击的品牌ID获取数据，获取品牌下商品的总数量
    '''

    def get(self,request):
        id = request.GET.get('id')

        product = Pmsproduct.objects.filter(brandId = id).count()

        mes = {}    
        mes['code'] = 200
        mes['count'] = product
        return Response(mes)




# 品牌详情相关商品
class Product_XG(APIView):
    '''
    品牌详情相关商品页面
    根据你点击的品牌ID获取数据，id为1的数据比较全面
    '''

    def get(self,request):
        id = request.GET.get('id')

        product = Pmsproduct.objects.filter(brandId = id).all()
        product_s = PmsproductModelSerializer(product,many=True)
        mes = {}    
        mes['code'] = 200
        mes['XG'] = product_s.data 
        return Response(mes)



# 优选区展示优选推荐页面
class PrefrenceArea_recommend(APIView):
    '''
    优选区展示优选推荐页面
    '''
    def get(request,self):

        l_list = []
        cate_show_detail = CmsPrefrenceArea.objects.all()[:3]
        for item in cate_show_detail:
            l_dict = {}
            l_dict['id'] = item.id
            l_dict['name'] = item.name
            l_dict['sub_title'] = item.sub_title
            l_dict['pic'] = item.pic

            la = Pmsproduct.objects.filter(area_id=item.id,newStatus=1).all()[:4]
            j_list = []
            for j in la:
                j_dict = {}
                j_dict['pic'] = j.pic
                j_dict['name'] = j.name
                j_dict['subTitle'] = j.subTitle
                j_dict['price'] = j.price
                
                j_list.append(j_dict)
            l_dict['proudct_list'] = j_list
            l_list.append(l_dict)
        mes = {}
        mes['code'] = 200
        mes['area_list'] = l_list
        return Response(mes)



# 特惠详情页面展示
class Sales_price(APIView):
    '''
    特惠详情页面展示
    '''
    def get(request,self):

        l_list = []
        cate_show_detail = PmsSalesPrice.objects.all()
    
        for item in cate_show_detail:
            l_dict = {}
            l_dict['id'] = item.id
            l_dict['title'] = item.title
            l_dict['sub_title'] = item.sub_title

            la = Pmsproduct.objects.filter(sales_id=item.id).all()
            j_list = []
            for j in la:
                j_dict = {}
                j_dict['name'] = j.name
                j_dict['description'] = j.description
                j_dict['promotionPrice'] = j.promotionPrice
                j_list.append(j_dict)
            l_dict['proudct_list'] = j_list
            l_list.append(l_dict)
        mes = {}
        mes['code'] = 200
        mes['sales_list'] = l_list
        return Response(mes)

# 商品详情页
class Proudct_detail(APIView):
    '''
    商品详情页
    ，通过产品的id 查看产品的详情页
    '''
    def get(self,request):

        id = request.GET.get('id')

        product = Pmsproduct.objects.filter(id=id)
        product_s = PmsproductdetailModelSerializer(product,many=True)
        mes = {}
        mes['code'] = 200
        mes['dd'] = product_s.data
        return Response(mes)

# 产品相关专题页面
class Product_Subject(APIView):
    '''
    产品相关专题页面
    '''
    def get(self,request):

        id = request.GET.get('id')
        product = Pmsproduct.objects.filter(id = subjectId ).all()
        product_s = CmsSubjectModelSerializer(product,many=True)
        mes = {}
        mes['code'] = 200
        mes['subject'] = product_s.data
        return Response(mes)






















































                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
















































































