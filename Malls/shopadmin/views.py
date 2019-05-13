from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from rest_framework.response import Response
from shopadmin.models import *
from django.views import View   
from django.contrib import messages
import json,os
from rest_framework.views import APIView
from Mall import settings
from django.core.paginator import Paginator
from shopadmin.serializers import *
import time
# Create your views here.

# 带蝴蝶好好的
# 后返回回复
from rest_framework.pagination import PageNumberPagination
""" 分页"""
class GoodsPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    page_query_param = 'pageNum'
    max_page_size = 100


"""
产品模块
"""
#产品           
class Goodslist(APIView):
    def get(self,request):


        pageSize = request.GET.get('pageSize')
       
        pageNum = request.GET.get('pageNum')
        pages=GoodsPagination()
        pages.page_size =int(pageSize)
       

        goods = Pmsproduct.objects.all()
        page_goods = pages.paginate_queryset(queryset=goods,request=request, view=self)
        goods_serializer = PmsproductModelSerializer(goods,many=True)

       mes={}
       mes['code']=200
       mes['list']=goods_serializer.data
       
       return Response(mes)

class Del_goods(APIView):
    def get(self,request):

        id = request.GET.get('id')
        Pmsproduct.objects.filter(id=id).delete()

        mes = {}
        mes['code'] = 200
        return Response(mes)



#商品属性展示
class Catelist_attr(APIView):
    def get(self,request):
        #  pageSize = request.GET.get('pageSize')
        # pageSize =int(pageSize)
        # pageNum = request.GET.get('pageNum')

        # print(pageNum,pageSize)
        # pg = PageNumberPagination()#创建分页 对象 
        # pg.page_size=pageSize
       goods = Pmsproduct.objects.all()
       goods_serializer = PmsproductModelSerializer(goods,many=True)
       mes={}
       mes['code']=200
       mes['list']=goods_serializer.data
       
       
       return Response(mes)
#商品分类的搜索显示
class Goods_cate(APIView):
    def get(self,request,formate=None):
        mes={}
        one = PmsProductCategory.objects.filter(parent_id=0).all()
        alist=[]
        for i in one:
            dicta = i.to_dict()
            id = dicta['id']
            two  = PmsProductCategory.objects.filter(parent_id=id).all()
            blist=[]
            for j in two:
                dictb = j.to_dict()
                blist.append(dictb)
            dicta['children']=blist
            alist.append(dicta)
        # print(alist)  
        mes['list']=alist     
        return Response(mes)  

#商品添加
# class Add_goods(APIView):
#     def get(self,request):
#         goods = PmsBrand.objects.all()
#         goods_serializer = PmsBrandModelSerializer(goods,many=True)
#         mes={}
#         mes['code']=200
#         mes['list']=goods_serializer.data
       
        # goods = GoodsSerializer(data=request.data)
        # print(goods)
        # if goods.is_valid():
        #     goods.save()
        #     print(goods.errors)
        #     mes['code']=200
        #     mes['message']='0k'
        #     print("rrrrrrrrrrrrrrrr")
        # else:
        #     mes['code']=20010
        #     mes['message']='必须添加数据'
        #     print("llllllllllllllllll")
        # return Response({'code':200})

#添加商品
class Add_goods(APIView):
    def post(self,request):
        mes={}
        data=request.data
        print(data)
        #如果等于零是没有优惠
        goods=Pmsproduct(brandId=data['brandId'],    #商品品牌
        productCategoryId=data['productCategoryId'],    #商品分类id
        feightTemplateId=data['feightTemplateId'],     
        productAttributeCategoryId=data['productAttributeCategoryId'],     #属性类型id
        name=data['name'],    #商品名字
        pic=data['pic'],      #图片链接
        productSn=data['productSn'],    # 货号
        deleteStatus=data['deleteStatus'],     # 删除状态: 0.未删除 1.已删除
        publishStatus=data['publishStatus'],  # 上架状态：0->下架；1->上架
        newStatus=data['newStatus'],   # 新品状态:0->不是新品；1->新品
        recommandStatus=data['recommandStatus'],   # 推荐状态；0->不推荐；1->推荐
        verifyStatus=data['verifyStatus'],   # 审核状态：0->未审核；1->审核通过
        sort=data['sort'],   # 排序
        sale=data['sale'],    # 销量
        price=data['price'],    #价格
        giftGrowth=data['giftGrowth'],    # 赠送的成长值
        giftPoint=data['giftPoint'],    # 赠送的积分
        usePointLimit=data['usePointLimit'],   # 限制使用的积分数
        subTitle=data['subTitle'],    # 副标题
        description=data['description'],    # 商品描述
        originalPrice=data['originalPrice'],  # 市场价
        stock=data['stock'],   # 库存
        lowStock=data['lowStock'],    # 库存预警值
        unit=data['unit'],   # 单位
        weight=data['weight'],   # 商品重量，默认为克
        previewStatus=data['previewStatus'],   # 是否为预告商品：0->不是；1->是
        serviceIds=str(data['serviceIds'].strip(',').split(',')),   # 以逗号分割的产品服务：1->无忧退货；2->快速退款；3->免费包邮
        keywords=data['keywords'],   #关键字
        note=data['note'],    #商品备注
        albumPics=data['albumPics'],    # 画册图片，连产品图片限制为5张，以逗号分割
        detailTitle=data['detailTitle'],      #详细页标题
        detailDesc=data['detailDesc'],     #详细页描述
        detailHtml=data['detailHtml'],     #电脑端详情
        detailMobileHtml=data['detailMobileHtml'],     #移动端详情
        promotionType=data['promotionType'],    # 促销类型：0->没有促销使用原价;1->使用促销价；2->使用会员价；3->使用阶梯价格；4->使用满减价格；5->限时购
        brandName=data['brandName'],      # 品牌名称
        productCategoryName=data['productCategoryName'])   # 产品分类名称
        goods.save()
        if data['promotionType']==1:       #type等于1 说明是特惠价格  入特惠价格表
            print(data['promotionEndTime'])
            print(data['promotionStartTime'])
            data['promotionEndTime']=time.localtime()
            data['promotionEndTime']=time.strftime('%Y-%m-%d %H:%M:%S',data['promotionEndTime'])
            #转换时间格式
            data['promotionStartTime']=time.localtime()
            data['promotionStartTime']=time.strftime('%Y-%m-%d %H:%M:%S',data['promotionStartTime'])
            print(data['promotionStartTime'])
            print(data['promotionEndTime'])
            
            goods_sales_price=PmsSalesPrice(goods_id=goods.id,promotionPrice=data['promotionPrice'],promotionStartTime=data['promotionStartTime'],promotionEndTime=data['promotionEndTime'])
            goods_sales_price.save()
        elif data['promotionType']==2:       #type等于2   是会员价格  入会员价格表
            for i in data['memberPriceList']:
                #商品会员价格表  PmsMemberPrice
                goods_member=PmsMemberPrice(goods_id=goods.id,member_level_id=i['memberLevelId'],price=i['memberPrice'],Member_level_name=i['memberLevelName'])
                goods_member.save()

        elif data['promotionType']==3:   #type等于3   是阶梯价格   入阶梯价格表
            for i in data['productLadderList']:
                #PmsProductLadder 产品价格阶梯表
                goods_fight=PmsProductLadder(product_id=goods.id,
                pro_count=int(i['count']),
                discount=float(i['discount']),
                price=float(i['discount'])*goods.price)
                goods_fight.save()
        elif data['promotionType']==4:   #type等于4   是满减价格    入满减价格表
            for i in data['productFullReductionList']:
                #满减价格表  PmsProductFullReduction
                goods_full_price=PmsProductFullReduction(product_id=goods.id,full_price=i['fullPrice'],reduce_price=i['reducePrice'])
                goods_full_price.save()
        mes['code']=200
        return Response(mes)


#商品添加中品牌渲染      
class Brandget(APIView):
    def get(self,request):
        id = request.GET.get('id')
        cate =PmsBrand.objects.filter(id=id).all()
        ser = PmsBrandModelSerializer(cate,many=True)
        mes={}
        mes['code']=200
        mes['list']= ser.data
        return JsonResponse(mes)


"""
登录
"""
class Login(APIView):
    def get(self,request):
        return JsonResponse({'code':200})



def index(request):
    return render(request,'admin/index.html')


# #上传所有图片
def upload_allimg(img):
    f = open(os.path.join(settings.UPLOAD_ROOT,'',img.name),'wb')
    #写文件 遍历图片文件流
    for chunk in img.chunks():
        f.write(chunk)
    #关闭文件流
        f.close()

#图片上传
class Upload_img(APIView):
    def post(self,request):
        img = request.FILES.get('img')
       
        if img:
            upload_allimg(img)  
            img1 = "/upload/"+img.name
           
        mes={}
        mes['path'] = "http://127.0.0.1:8000/sadmin"+img1
        mes['code'] = 200
        return JsonResponse(mes)
        

"""
品牌模块
"""
#品牌展示
class Brandlist(APIView):
    def get(self,request):
        mes={}
        keyword = request.GET.get('keyword','')
        pageSize = request.GET.get('pageSize')
       
        pageNum = request.GET.get('pageNum')
        pages=GoodsPagination()
        pages.page_size =int(pageSize)
       

        if keyword:
            # 模糊匹配用到name__contains
            brand = PmsBrand.objects.filter(name__contains=keyword).order_by('-name','-first')
        else:  
            brand = PmsBrand.objects.all()
        
        #获取分页的数据
        page_brand = pages.paginate_queryset(queryset=brand,request=request,view=self)
        ser = PmsBrandModelSerializer(page_brand,many=True)
        mes['code']=200
        mes['list']= ser.data
        return pages.get_paginated_response(ser.data)
        # return JsonResponse(mes)


#是否显示品牌制造商
class Show_brand_factoryStatus(APIView):

    def post(self,request):
       
        s = request.POST.get('ids')
        a = request.POST.get('is_company')
        
        if s:
            PmsBrand.objects.filter(id=s).update(is_company=a)
        return JsonResponse({'code':200})

#是否显示
class Show_brand_show(APIView):

    def post(self,request):
        mes={}
        data = request.data
        id = data['ids'].strip(',').split(',')
        
        try:
            PmsBrand.objects.filter(id__in = id).update(is_show=data['showStatus'])
            mes['code']=200
        except:
            mes['code']=20010   
        return JsonResponse(mes)

#编辑品牌制造商       
class Edit_brand(APIView):
    
    def post(self,request):
        mes={}
        id = request.GET.get('id')
        dict1=request.data
        
        PmsBrand.objects.filter(id=id).update(name=dict1['name'],first=dict1['first'],sort=dict1['sort'],is_company=dict1['is_company'],is_show=dict1['is_show'],logo=dict1['logo'],b_logo=dict1['b_logo'],story=dict1['story'])
        mes['code']=200
        return JsonResponse(mes)   
#渲染页面        
class Edit_brand_get(APIView):
    
    def post(self,request):
        id = request.GET.get('id')
        
        cate =PmsBrand.objects.filter(id=id).all()
        ser = PmsBrandModelSerializer(cate,many=True)
        
        mes={}
        mes['code']=200
        mes['list']= ser.data
        return JsonResponse(mes)

#添加品牌
class Add_brand(APIView):
   
    def post(self,request):
        mes={}
      
        brand = PmsBrandSerializer(data=request.data)
        if brand.is_valid():
            brand.save()
            
            mes['code']=200
            mes['message']='0k'
            print("rrrrrrrrrrrrrrrr")
        else:
            mes['code']=20010
            mes['message']='必须添加数据'
            print("llllllllllllllllll")
            
        return JsonResponse(mes)   

#删除品牌
class Delbrand(APIView):
    def get(self,request):
        id = request.GET.get('id')
        PmsBrand.objects.filter(id=id).delete()
        return JsonResponse({'code':200})


"""
商品分类模块
"""
#商品分类展示
class Categorylist(APIView):
    def get(self,request):

        pageSize = request.GET.get('pageSize')
       
        pageNum = request.GET.get('pageNum')
        pages=GoodsPagination()
        pages.page_size =int(pageSize)


        id = request.GET.get("id")
        if int(id) == 0:
            cate = PmsProductCategory.objects.filter(level_l=0,parent_id=0).all()
        else:
            cate = PmsProductCategory.objects.filter(level_l=1,parent_id=id).all()
        mes={}
        page_cate = pages.paginate_queryset(queryset=cate,request=request,view=self)
        ser = PmsProductCategoryModelSerializer(page_cate,many=True)
      
        mes['code']=200
        mes['list']= ser.data
       
        return pages.get_paginated_response(ser.data)
       
  

#二级属性联动
class Withchilden(APIView):
    def get(self,request):
        mes={}
        one = PmsProductAttributeCategory.objects.all()
        alist=[]
        blist=[]
        for i in one:
            dicta = i.to_dict()
             
            # id = dicta['id']
            # print(id)
            two  = PmsProductAttribute.objects.filter(type_id=i.id,type1=1).all()
            for j in two:
                dictb = j.to_dict1()
                blist.append(dictb)
            dicta['productAttributeList']=blist
            alist.append(dicta) 
        # print(alist)  
        mes['list']=alist     
        return Response(mes)  

#添加商品分类
class Add_Category(APIView):
    def get(self,request):
        mes={}
        goods = PmsProductAttributeCategory.objects.all()
    
        g = PmsProductAttributeCategoryModelSerializer(goods, many=True)
    
        mes['code'] = 200
        mes['list'] = g.data
       
        # print(mes)
        return Response(mes)
    def post(self,request):
        mes={}
        
        brand = PmsProductCategorySerializer(data=request.data)
        print(brand)
        if brand.is_valid():
            brand.save()
            mes['code']=200
            mes['message']='0k'
            print("rrrrrrrrrrrrrrrr")    
        else:
            mes['code']=20010
            mes['message']='必须添加数据'
            print("yyyyyyyyyyyyyyyyyyyyyyyyy")
        return JsonResponse(mes)   
        
#获取id       
class Categoryget(APIView):
    def get(self,request):
        id = request.GET.get('id')
        mes={}
        mes['code']=200
        return JsonResponse(mes)
#商品属性中心
class Pro_attrInfo(APIView):
    def get(self,request):
        id = request.GET.get('id')
        mes={}
        mes['code']=200
        return JsonResponse(mes)        


#编辑商品分类        
class Edit_Category(APIView):
    def post(self,request):
        id = request.GET.get('id')
        print(id,"wwww")
        cate =PmsProductCategory.objects.filter(id=id).all()
        ser = PmsProductCategoryModelSerializer(cate,many=True)
        mes={}
        mes['code']=200
        mes['list']= ser.data
        return JsonResponse(mes)
#删除商品分类
class DElCategory(APIView):
    def get(self,request):
        id = request.GET.get('id')
        print(id)
        PmsProductCategory.objects.filter(id=id).delete()
        return JsonResponse({'code':200})

#是否显示导航栏
class Update_navStatus(APIView):
    def post(self,request):
           
        s = request.POST.get('ids')
        a = request.POST.get('is_nav_status')
        
        if s:
            PmsProductCategory.objects.filter(id=s).update(is_nav_status=a)
        return JsonResponse({'code':200})

#是否显示
class Update_Status(APIView):
    def post(self,request):
           
        s = request.POST.get('ids')
        a = request.POST.get('status')
        print(s,a)
        if s:
            PmsProductCategory.objects.filter(id=s).update(status=a)
        return JsonResponse({'code':200})        
""" 
商品类型模块
"""

#商品类型展示
class Goods_typelist(APIView):
    def get(self,request):

        pageSize = request.GET.get('pageSize')
       
        pageNum = request.GET.get('pageNum')
        pages=GoodsPagination()
        pages.page_size =int(pageSize)

        goods = PmsProductAttributeCategory.objects.all()
        # goods_serializer = Goods_typeModelSerializer(goods,many=True)
        mes={}
        page_coods_type = pages.paginate_queryset(queryset=goods,request=request,view=self)
        ser = PmsProductAttributeCategoryModelSerializer(page_coods_type,many=True)
       
        mes['code']=200
        mes['list']= ser.data
        return pages.get_paginated_response(ser.data)
       

#添加商品类型
class Add_Goods_type(APIView):
    def post(self,request):
        mes={}
        brand = PmsProductAttributeCategorySerializer(data=request.data)
        if brand.is_valid():
            brand.save()
            mes['code']=200
            mes['message']='0k'
        else:
            mes['code']=20010
            mes['message']='必须添加数据'
        print(request.data)
        return JsonResponse(mes)   


#编辑商品类型
class Edit_Goods_type(APIView):
    def post(self,request):
        mes={}
        id = request.GET.get('id')
        name= request.POST.get('name')
        goods_type=PmsProductAttributeCategory.objects.filter(id=id).update(name=name)
        mes={}
        mes['code']=200
        return JsonResponse(mes)

#删除商品类型
class DEl_goods_type(APIView):
    def get(self,request):
        id = request.GET.get('id')
        PmsProductAttributeCategory.objects.filter(id=id).delete()
        return JsonResponse({'code':200})

'''
商品属性
'''

#商品属性展示
class Goods_type_attribute1(APIView):
    def get(self,request):

        type=request.GET.get('type')
        id = request.GET.get('id')
        pageSize = request.GET.get('pageSize')
       
        pageNum = request.GET.get('pageNum')
        pages=GoodsPagination()
        pages.page_size =int(pageSize)

        cid = request.GET.get('id')
     
        goods = PmsProductAttribute.objects.filter(type1=type,type_id=id)
    #    goods_serializer = PmsProductAttributeModelSerializer(goods,many=True)
        mes={}
        page_cate = pages.paginate_queryset(queryset=goods,request=request,view=self)
        ser = PmsProductAttributeModelSerializer(page_cate,many=True)
       
        mes['code']=200
        mes['list']= ser.data
        return pages.get_paginated_response(ser.data)

#添加商品属性
class Add_Goods_type_attribute(APIView):
    def get(self,request):
        goods = PmsProductAttributeCategory.objects.all()
        goods_serializer = PmsProductAttributeCategoryModelSerializer(goods,many=True)
        mes={}
        mes['code']=200
        mes['list']=goods_serializer.data
       
        return Response(mes)
    def post(self,request):
        mes={}
        goods_type_attribute = PmsProductAttributeSerializer(data=request.data)
       
        if goods_type_attribute.is_valid():
           
            goods_type_attribute.save()
            print(goods_type_attribute.errors)
            mes['code']=200
            mes['message']='0k'
           
        else:
            mes['code']=20010
            mes['message']='必须添加数据'
         
        return JsonResponse(mes)   

#编辑商品属性
class Edit_goods_type_attribute(APIView):
   def post(self,request):
    mes={}
    id = request.GET.get('id')
    dict1=request.data
    
    goods = PmsProductAttributeSerializer(data=request.data)
    PmsProductAttribute.objects.filter(id=id).update(name=dict1['name'],type_id=dict1['productAttributeCategoryId'],filter_type=dict1['filterType'],is_select= dict1['searchType'],related_status= dict1['relatedStatus'],select_type=dict1['selectType'],input_type= dict1['inputType'],input_list= dict1['inputList'],hand_add_status= dict1['handAddStatus'],sort=dict1['sort'],type1=dict1['type'])
    mes={}
    mes['code']=200
    return JsonResponse(mes)


#编辑商品属性
class Edit_goods_type_attribute_get(APIView):
    def get(self,request):
        id = request.GET.get('id')
        
        list1 = PmsProductAttribute.objects.filter(id=id).all()
        a=[]
        for i in list1:
            dict1={}
            dict1['name']=i.name
            dict1['productAttributeCategoryId']=i.type_id
            dict1['filterType']=i.filter_type
            dict1['searchType']=i.is_select
            dict1['relatedStatus']=i.related_status
            dict1['selectType']=i.select_type
            dict1['inputType']=i.input_type
            dict1['inputList']=i.input_list
            dict1['handAddStatus']=i.hand_add_status
            dict1['sort']=i.sort
            dict1['type']=i.type1
            a.append(dict1)
            
       
        mes={}
        mes['code']=200
        mes['list']=a
        
        return JsonResponse(mes)
   

#删除商品属性
class DEl_goods_type_attribute(APIView):
    def get(self,request):
        id = request.GET.get('ids')
        id1=id.strip(',').split(',')

        PmsProductAttribute.objects.filter(id__in=id1).delete()
        return JsonResponse({'code':200})


"""
优惠券
"""
#优惠券展示 SmsCoupon
class Coupon1_list(APIView):
    def get(self,request):
        mes = {}
        name = request.GET.get('name')
        type =request.GET.get('type')
        pageSize = request.GET.get('pageSize')
        pageNum = request.GET.get('pageNum')
        pages=GoodsPagination()
        pages.page_size =int(pageSize)
        if name:
            coupon = SmsCoupon.objects.filter(name=name).all()
           
        elif type:
            coupon = SmsCoupon.objects.filter(type=type).all()
            
        elif type and name:
            coupon = SmsCoupon.objects.filter(type=type,name=name).all()
            
        else:
            coupon = SmsCoupon.objects.all()
           
        page_brand = pages.paginate_queryset(queryset=coupon,request=request,view=self)
        ser = SmsCouponModelSerializer(page_brand,many=True)
        mes['code']=200
        mes['list'] = ser.data
        return pages.get_paginated_response(ser.data)

       
      
#添加优惠券
class Add_coupon(APIView):
    def post(self,request):
        mes={}
        time = SmsCouponSerializer(data=request.data)
        print(time)
        if time.is_valid():
            time.save()
            mes['code'] = 200
            mes['message'] = '添加成功' 
        else:
            mes['code'] = 10011
            mes['message'] = '添加失败'
        return JsonResponse(mes)



#删除优惠券
class Delete_coupon(APIView):
    def get(self,request):
        id = request.GET.get('id')
        SmsCoupon.objects.filter(id=id).delete()
        return JsonResponse({'code':200})
    
#点击查看
class Find_coupon(APIView):
    def get(self,request):
        # id = request.GET.get('id')
        # SmsCoupon.objects.filter(id=id).delete()
        return JsonResponse({'code':200})
#获取id
class Find_coupon_id(APIView):
    def get(self,request):
        # id = request.GET.get('id')
        # SmsCoupon.objects.filter(id=id).delete()
        return JsonResponse({'code':200})


'''
人气推荐
'''
#推荐页
class Product_recommend(APIView):
    def get(self,request):

        # activity = SmsHomeRecommendProduct.objects.all()
        # a = SmsHomeRecommendProduct_modelser(activity,many=True)
        # mes={}
        # mes['code']=200
        # mes['list']=a.data
        # return JsonResponse(mes)
        mes = {}
        pageSize = request.GET.get('pageSize')
        pageNum = request.GET.get('pageNum')
        product_name=request.GET.get('product_name')
        recommend_status = request.GET.get('recommend_status')
        print(recommend_status,product_name)
        pages=GoodsPagination()
        pages.page_size =int(pageSize)
        if recommend_status:
            coupon = SmsHomeRecommendProduct.objects.filter(recommend_status__in = recommend_status)
        elif product_name:
            coupon = SmsHomeRecommendProduct.objects.filter(product_name__in = product_name)
        elif product_name and recommend_status:
            coupon = SmsHomeRecommendProduct.objects.filter(product_name__in = product_name,recommend_status__in = recommend_status)  
        else:    
            coupon = SmsHomeRecommendProduct.objects.all()
        page_brand = pages.paginate_queryset(queryset=coupon,request=request,view=self)
        ser = SmsHomeRecommendProduct_modelser(page_brand,many=True)
        mes['code']=200
        mes['list'] = ser.data
        # return JsonResponse(mes)
        return pages.get_paginated_response(ser.data)

#添加人气推荐
class Add_Product_recommend(APIView):
    def post(self,request):
        mes={}
        print(request.data)
        for i in request.data:
            SmsHome1 = SmsHomeRecommendProduct_serilazer(data=i)
            if SmsHome1.is_valid():
                SmsHome1.save()
                mes['code'] = 200
                mes['message'] = '添加成功'
            else:
                mes['code'] = 10011
                mes['message'] = '添加失败'
                print(SmsHomeBrand.errors)
            return JsonResponse(mes)


#更新状态
class Update_product_status(APIView):
    def post(self,request):
        mes={}
        ids = request.POST.get('ids')
        status = request.POST.get('recommend_status')
        print(ids,status)
        id=ids.split(',')
        SmsHomeRecommendProduct.objects.filter(id__in=id).update(recommend_status=status)
        mes['code'] = 200
        mes['message'] = '修改成功'
        return JsonResponse(mes)

#更新排序
class Update_Sort1(APIView):
    def post(self,request):
        return JsonResponse({'code':200})

#删除成功
class Delete_Recommend_product(APIView):
    def post(self,request):
        id = request.POST.get('ids')
        print(id)
        SmsHomeRecommendProduct.objects.filter(id=id).delete()
        return JsonResponse({'code':200})


"""
品牌推荐

"""
#品牌推荐页
class Show_brand_recommend(APIView):
    def get(self,request):
        activity = SmsHomeBrand.objects.all()
        a = SmsHomeBrand_modelser(activity,many=True)
        mes={}
        mes['code']=200
        mes['list']=a.data
        return JsonResponse(mes)
        

#添加品牌推荐
class Add_brand_recommend(APIView):
    def post(self,request):
        mes={}
        print(request.data)
        for i in request.data:
            SmsHomeBrand = SmsHomeBrand_serilazer(data=i)
            if SmsHomeBrand.is_valid():
                SmsHomeBrand.save()
                mes['code'] = 200
                mes['message'] = '添加成功'
            else:
                mes['code'] = 10011
                mes['message'] = '添加失败'
                print(SmsHomeBrand.errors)
            return JsonResponse(mes)


#更新状态
class Update_brand_status(APIView):
    def post(self,request):
        mes={}
        ids = request.POST.get('ids')
        status = request.POST.get('recommend_status')
        print(ids,status)
        id=ids.split(',')
        SmsHomeBrand.objects.filter(id__in=id).update(recommend_status=status)
        mes['code'] = 200
        mes['message'] = '修改成功'
        return JsonResponse(mes)

#更新排序
class Recommend_sort(APIView):
    def post(self,request):
        return JsonResponse({'code':200})

#删除成功
class Delete_Recommend(APIView):
    def post(self,request):
        id = request.POST.get('ids')
        print(id)
        SmsHomeBrand.objects.filter(id=id).delete()
        return JsonResponse({'code':200})
"""
专题推荐
"""
#专题推荐
class Product_recommend_Sub(APIView):
    def get(self,request):
        activity = SmsHomeRecommendSubject.objects.all()
        a = SmsHomeRecommendSubject_modelser(activity,many=True)
        mes={}
        mes['code']=200
        mes['list']=a.data
        return JsonResponse(mes)
#添加专题推荐
class Add_Product_recommend_Sub(APIView):
    def post(self,request):
        mes={}
        print(request.data)
        for i in request.data:
            SmsHomeBrand = SmsHomeRecommendSubject_serilazer(data=i)
            if SmsHomeBrand.is_valid():
                SmsHomeBrand.save()
                mes['code'] = 200
                mes['message'] = '添加成功'
            else:
                mes['code'] = 10011
                mes['message'] = '添加失败'
                print(SmsHomeBrand.errors)
            return JsonResponse(mes)


#更新状态
class Update_product_status_Sub(APIView):
    def post(self,request):
        mes={}
        ids = request.POST.get('ids')
        status = request.POST.get('recommend_status')
        print(ids,status)
        id=ids.split(',')
        SmsHomeRecommendSubject.objects.filter(id__in=id).update(recommend_status=status)
        mes['code'] = 200
        mes['message'] = '修改成功'
        return JsonResponse(mes)

#更新排序
class Recommend_sort1_Sub(APIView):
    def post(self,request):
        return JsonResponse({'code':200})

#删除成功
class Delete_Recommend_product_Sub(APIView):
    def post(self,request):
        id = request.POST.get('ids')
        print(id)
        SmsHomeRecommendSubject.objects.filter(id=id).delete()
        return JsonResponse({'code':200})

"""
新品推荐
"""
#新品展示
class New_recommend(APIView):
    def get(self,request):
        mes = {}
        pageSize = request.GET.get('pageSize')
        pageNum = request.GET.get('pageNum')
        productName=request.GET.get('name')
        recommend_status = request.GET.get('recommend_status')
      
        pages=GoodsPagination()
        pages.page_size =int(pageSize)
        if recommend_status:
            coupon = SmsHomeNewProduct.objects.filter(recommend_status__in = recommend_status)
        elif productName:
            coupon = SmsHomeNewProduct.objects.filter(productName__in = productName)
        elif productName and recommend_status:
            coupon = SmsHomeNewProduct.objects.filter(productName__in = productName,recommend_status__in = recommend_status)  
        else:    
            coupon = SmsHomeNewProduct.objects.all()
        page_brand = pages.paginate_queryset(queryset=coupon,request=request,view=self)
        ser = SmsHomeNewProduct_Modelseri(page_brand,many=True)
        mes['code']=200
        mes['list'] = ser.data
        # return JsonResponse(mes)
        return pages.get_paginated_response(ser.data)


#选择新品
class Select_Newgoods(APIView):
    def post(self,request):
        mes = {}
        # print(request.data)
        for i in request.data:
            add = SmsHomeNewProduct_serializers(data=i)
            if add.is_valid():
                add.save()
                mes['code'] = 200
                mes['message'] = '添加成功' 
            else:
                mes['code'] = 10011
                mes['message'] = '添加失败'
                print(add.errors)
        return JsonResponse(mes)

#删除新品
class Delete_Newgoods(APIView):
    def get(self,request):  
        mes = {}
        id = request.GET.get('ids')
        # print(id)
        SmsHomeNewProduct.objects.filter(id=id).delete()
        mes['code'] = 200
        return JsonResponse(mes)

#多选修改状态和删除
class Update_Newgoods(APIView):
    def post(self,request):
        mes = {}
        id = request.POST.get('ids')
        recommend_status=request.POST.get('recommend_status')
        id=id.split(',')
        # print(id)
        SmsHomeNewProduct.objects.filter(id__in=id).update(recommend_status=recommend_status)



        mes['code'] = 200
        return JsonResponse(mes)

#更新排序
class Update_Sort(APIView):
    def get(self,request):
        sort=request.GET.get('sort')
        print(sort)
        SmsHomeNewProduct.objects.filter(sort=sort).order_by('sort').all()

        return JsonResponse({'code':200})
"""
秒杀活动表
"""
#添加活动
class Activity1(APIView):
    def post(self,request):
        mes={}
        activity = SmsFlashPromotionSerializer(data=request.data)
       
      
        if activity.is_valid():
            activity.save()
            mes['code'] = 200
            mes['message'] = '添加成功'
        else:
            mes['code'] = 10011
            mes['message'] = '添加失败'

        return JsonResponse(mes)
#展示活动
class Show_activity(APIView):
    def get(self,request):
        mes={}
        keyword = request.GET.get('keyword')
        pageSize = request.GET.get('pageSize')
        pageNum = request.GET.get('pageNum')
        pages=GoodsPagination()
        pages.page_size =int(pageSize)
        if keyword:
            activity = SmsFlashPromotion.objects.filter(name=keyword).all()
            
        else:
            activity = SmsFlashPromotion.objects.all()
            
       
        page_brand = pages.paginate_queryset(queryset=activity,request=request,view=self)
        ser = SmsFlashPromotionModelSerializer(page_brand,many=True)
        mes['code']=200
        mes['list'] = ser.data
        return pages.get_paginated_response(ser.data)

#删除活动
class Delete_activity(APIView):
    def get(self,request):
        id = request.GET.get('id')
        SmsFlashPromotion.objects.filter(id=id).delete()
        return JsonResponse({'code':200})

#改变上下线状态
class Update_status(APIView):
    def get(self,request):
        id = request.GET.get('id')
        status = request.GET.get('status')
        SmsFlashPromotion.objects.filter(id=id).update(status=status)
        return JsonResponse({'code':200})
#编辑活动
class Edit_activity(APIView):
       def post(self,request):
        mes={}
        id = request.GET.get('id')
        dict1=request.data
        
      
        SmsFlashPromotion.objects.filter(id=id).update(name=dict1['name'],start_time=dict1['start_time'],end_time=dict1['end_time'],status=dict1['status'])
      
        mes['code']=200
        return JsonResponse(mes)

#设置商品 
class Setting_goods(APIView):
       def get(self,request):
        mes={}
        show = SmsFlashPromotionSession.objects.all()

        show1 = SmsFlashPromotionSessionModelSerializer(show,many=True)
        goods = PmsBrand.objects.all().count()
        mes['code'] = 200
        mes['list'] = show1.data
        mes['count']=goods
        return JsonResponse(mes)



#商品列表
class show_goodslist(APIView):
       def get(self,request):
        mes={}
        show = SmsFlashPromotionProductRelation.objects.all()
        for i in show:
            print(i.flash_promotion_id)
            w=SmsFlashPromotion.objects.filter(id=i.flash_promotion_id).all()
            print(w)
            # print("=="*50)
            # print(i.product_id)

        show1 = SmsFlashPromotionProductRelationSerializer(show,many=True)
        mes['code'] = 200
        mes['list'] = show1.data
        # print(show1.data)
        return JsonResponse(mes)    
#添加秒杀时间段表
class Add_flasssession(APIView):
    def post(self,request):
        mes={}
        time = SmsFlashPromotionSessionSerializer(data=request.data)
       
        if time.is_valid():
            time.save()
            mes['code'] = 200
            mes['message'] = '添加成功' 
        else:
            mes['code'] = 10011
            mes['message'] = '添加失败'
        return JsonResponse(mes)

#秒杀时间段展示
class Show_flass(APIView):
    def get(self,request):
        mes = {}
        show = SmsFlashPromotionSession.objects.all()

        show1 = SmsFlashPromotionSessionModelSerializer(show,many=True)
       
        mes['code'] = 200
        mes['list'] = show1.data
        return JsonResponse(mes)

#删除秒杀时间段
class Delete_flass(APIView):
    def get(self,request):
        id = request.GET.get('id')
        SmsFlashPromotionSession.objects.filter(id=id).delete()
        return JsonResponse({'code':200})


#编辑时间段表
class Edit_flass(APIView):
       def post(self,request):
        mes={}
        id = request.GET.get('id')
        dict1=request.data
        
      
        SmsFlashPromotionSession.objects.filter(id=id).update(name=dict1['name'],start_time=dict1['start_time'],end_time=dict1['end_time'],status=dict1['status'])
        mes={}
        mes['code']=200
        return JsonResponse(mes)



#秒杀时间段是否启用
class Update_stime(APIView):
    def get(self,request):
        mes={}
        id = request.GET.get('id')
        status = request.GET.get('status')
        print(status)
        SmsFlashPromotionSession.objects.filter(id=id).update(status=status)
        mes['code'] = 200
        mes['message'] = '修改成功'
        return JsonResponse(mes)

"""
广告图
"""

# 广告列表
class Advertising_list(APIView):
    def get(self,request):
        print(request.GET)
        name = request.GET.get('name','').strip()
        type = request.GET.get('type','').strip()
        end_time = request.GET.get('end_time','').strip()
        pageSize = request.GET.get('pageSize')
        pageNum = request.GET.get('pageNum')
        pages=GoodsPagination()
        pages.page_size =int(pageSize)
        print(end_time)
        id = request.GET.get('id')

        if id:
            advertising = SmsHomeAdvertise.objects.filter(id=id).all()
        else:
            if type and end_time and name:
                advertising = SmsHomeAdvertise.objects.filter(end_time__lte = end_time).filter(type = type).filter(name__contains = name).all()
            elif type and end_time:
                advertising = SmsHomeAdvertise.objects.filter(end_time__lte = end_time).filter(type = type).all()
            elif name and end_time:
                advertising = SmsHomeAdvertise.objects.filter(end_time__lte = end_time).filter(name__contains = name).all()
            elif name and type:
                advertising = SmsHomeAdvertise.objects.filter(type = type).filter(name__contains = name).all()
            elif end_time:
                advertising = SmsHomeAdvertise.objects.filter(end_time__lte = end_time)  
            elif type:
                advertising = SmsHomeAdvertise.objects.filter(type = type)
            elif name:
                advertising = SmsHomeAdvertise.objects.filter(name__contains = name)
            else:
                advertising = SmsHomeAdvertise.objects.all()
        # advertising_s = SmsHomeAdvertiseModelSerializer(advertising,many=True)
        page_brand = pages.paginate_queryset(queryset=advertising,request=request,view=self)
        ser = SmsHomeAdvertiseModelSerializer(page_brand,many=True)
        mes = {}
        mes['code'] = 200
        mes['list'] = ser.data

        return pages.get_paginated_response(ser.data)        
       


  
# 添加广告
class Add_advertising(APIView):
    def post(self,request):
        mes = {}
        advertising = SmsHomeAdvertiseSerializer(data=request.data)
        print(advertising)
        if advertising.is_valid():

            advertising.save()
            mes['code'] = 200
        else:
            print(advertising.errors)
            mes['code'] = 300
        return JsonResponse(mes)
   
# 修改广告
class Edit_advertising(APIView):
    def post(self,request):
        res = request.data
        print(res['id'])
        SmsHomeAdvertise.objects.filter(id=res['id']).update(name=res['name'],type=res['type'],pic=res['pic'],start_time=res['start_time'],end_time=res['end_time'],status=res['status'],click_count=res['click_count'],order_count=res['order_count'])

        mes = {}
        mes['code'] = 200
        return Response(mes)
    
# 修改广告状态
class Edit_ad_status(APIView):
    def post(self,request):
        id = request.GET.get('id')
        status = request.GET.get('status')
        # print(id,status)

        SmsHomeAdvertise.objects.filter(id=id).update(status=status)
        return Response({'code':200})

#获取id渲染页面

class GetHomeAdvertise(APIView):
    def get(self,request):
        mes={}
        id = request.GET.get('id')
        advertising= SmsHomeAdvertise.objects.filter(id=id).all()
        advertising_s = SmsHomeAdvertiseModelSerializer(advertising,many=True)
        mes['code']=200
        mes['list'] = advertising_s.data
        return JsonResponse(mes)
        # class Edit_brand_get(APIView):
        
    # def post(self,request):
    #     id = request.GET.get('id')
        
    #     cate =PmsBrand.objects.filter(id=id).all()
    #     ser = PmsBrandModelSerializer(cate,many=True)
        
    #     mes={}
    #     mes['code']=200
    #     mes['list']= ser.data
        # return JsonResponse(mes)
# 批量选择 删除
class DElAdvertising(APIView):
    def post(self,request):
            data=request.data
            # print(data)
            id1=data['ids'].split(',')
            print(id1)
            mes = {}
            SmsHomeAdvertise.objects.filter(id__in=id1).delete()
            mes['code'] = 200
      
            return Response(mes)

"""
项目
"""
#项目列表
class Subject_list(APIView):
    def get(self,request):
        
        mes={}
        mes['code']=200
      
        return JsonResponse(mes)

"""
会员等级  memberLevel
"""  
class MemberLevel_list(APIView):
    def get(self,request):
        
        mes={}
        mes['code']=200
      
        return JsonResponse(mes)

"""
prefrenceArea  默认地区
"""        
class PrefrenceArea_list(APIView):
    def get(self,request):
        
        mes={}
        mes['code']=200
      
        return JsonResponse(mes)