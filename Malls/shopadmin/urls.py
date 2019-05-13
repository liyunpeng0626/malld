"""Mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views\
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from shopadmin import views
from Mall.settings import UPLOAD_ROOT
from django.views.static import serve

urlpatterns = [   
    path('index/',views.index),

    path('Login/',views.Login.as_view()),    
    #商品添加
    path('brand/',views.Brandget.as_view()),#添加页品牌的渲染
    path('product/create',views.Add_goods.as_view()),
    path('productAttribute/create',views.Add_Goods_type_attribute.as_view()),
    path('productAttribute/delete/',views.DEl_goods_type_attribute.as_view()),
    path('productAttribute/catelist',views.Catelist_attr.as_view()),
    # path('productAttribute/catelist',views.Catelist_attr.as_view()),
    #商品展示
    path('product/list/',views.Goodslist.as_view()),
    path('productCategory/list/withChildren',views.Goods_cate.as_view()),
    path('product/del/',views.Del_goods.as_view()),

    # path('productAttribute/create',views.Goods_brand.as_view()),
    # path('productAttribute/delete/',views.DEl_goods_type_attribute.as_view()),
    #品牌
    path('brand/create',views.Add_brand.as_view()),
    path('brand/list',views.Brandlist.as_view()),
    path('upload/',views.Upload_img.as_view()),
    re_path('^upload/(?P<path>.*)$',serve,{'document_root':UPLOAD_ROOT}),
    path('brand/delete/',views.Delbrand.as_view()),
    path('brand/update/factoryStatus/',views.Show_brand_factoryStatus.as_view()),  
    path('brand/update/showStatus/',views.Show_brand_show.as_view()),  
    path('brand/update',views.Edit_brand.as_view()),
    path('brand/get',views.Edit_brand_get.as_view()),
    
    #商品分类
    path('productCategory/',views.Categoryget.as_view()), 
    path('productCategory/list/',views.Categorylist.as_view()),     
    path('productCategory/create',views.Add_Category.as_view()),
    path('productCategory/update/',views.Edit_Category.as_view()),
    path('productCategory/delete/',views.DElCategory.as_view()),    
    path('productCategory/update/navStatus',views.Update_navStatus.as_view()),
    path('productCategory/update/showStatus',views.Update_Status.as_view()),
    path('productAttribute/category/list/withAttr',views.Withchilden.as_view()), 
    #商品类型
    path('productAttribute/category/list',views.Goods_typelist.as_view()),
    path('productAttribute/category/create',views.Add_Goods_type.as_view()),
    path('productAttribute/category/update/',views.Edit_Goods_type.as_view()),
    path('productAttribute/category/delete/',views.DEl_goods_type.as_view()),
    #商品属性/参数 
    path('productAttribute/list/',views.Goods_type_attribute1.as_view()),
    path('productAttribute/create',views.Add_Goods_type_attribute.as_view()),
    path('productAttribute/delete/',views.DEl_goods_type_attribute.as_view()),
    path('productAttribute/update/',views.Edit_goods_type_attribute.as_view()),    
    path('productAttribute/',views.Edit_goods_type_attribute_get.as_view()),
    path('productAttribute/attrInfo/',views.Pro_attrInfo.as_view()),
    #优惠券
    path('coupon/list',views.Coupon1_list.as_view()),
    path('coupon/create',views.Add_coupon.as_view()),
    path('coupon/delete/',views.Delete_coupon.as_view()),
    path('coupon/update/',views.Edit_goods_type_attribute.as_view()),
    path('productAttribute/',views.Edit_goods_type_attribute_get.as_view()),   
    path('couponHistory/list',views.Find_coupon.as_view()),   
     path('coupon/',views.Find_coupon_id.as_view()),
    #活动秒杀
    path('flash/list',views.Show_activity.as_view()),
    path('flash/create',views.Activity1.as_view()),
    path('flash/update/status/',views.Update_status.as_view()),
    path('flash/update/',views.Edit_activity.as_view()),  
    path('flash/delete/',views.Delete_activity.as_view()),
    path('flashSession/list',views.Show_flass.as_view()),
    path('flashSession/update/',views.Edit_flass.as_view()),
    path('flashSession/delete/',views.Delete_flass.as_view()),
    path('flashSession/update/status/',views.Update_stime.as_view()),  
    path('flashSession/create',views.Add_flasssession.as_view()),
    #设置商品
    path('flashSession/selectList',views.Setting_goods.as_view()),   
    path('flashProductRelation/list',views.show_goodslist.as_view()),#商品列表展示
    

    path('',views.Show_flass.as_view()),    

    #项目列表
    path('subject/listAll',views.Subject_list.as_view()),
    #会员等级  
    path('memberLevel/list',views.MemberLevel_list.as_view()),
    #优先地区
    path('prefrenceArea/listAll',views.PrefrenceArea_list.as_view()), 
    #轮播图
    path('home/advertise/delete',views.DElAdvertising.as_view()),
    path('home/advertise/update/status/',views.Edit_ad_status.as_view()),   
    path('home/advertise/update/',views.Edit_advertising.as_view()),
    path('home/advertise/create',views.Add_advertising.as_view()),  
    path('home/advertise/list',views.Advertising_list.as_view()), 
    path('home/advertise/',views.GetHomeAdvertise.as_view()), #获取广告id
    # path('add_coupon_type',views.add_coupon1),    New_recommend
    #新品推荐
    path('home/newProduct/list',views.New_recommend.as_view()), 
    path('home/newProduct/create',views.Select_Newgoods.as_view()),
    path('home/newProduct/delete/',views.Delete_Newgoods.as_view()),  
    path('home/newProduct/update/recommendStatus/',views.Update_Newgoods.as_view()),  
    path('home/newProduct/update/sort/',views.Update_Sort.as_view()),    

    #品牌推荐
    path('home/brand/list',views.Show_brand_recommend.as_view()), 
    path('home/brand/create',views.Add_brand_recommend.as_view()),
    path('home/brand/delete',views.Delete_Recommend.as_view()),  
    path('home/brand/update/recommendStatus',views.Update_brand_status.as_view()),  
    path('home/brand/update/sort',views.Update_Sort.as_view()),    

    #人气推荐
    path('home/recommendProduct/list',views.Product_recommend.as_view()), 
    path('home/recommendProduct/create',views.Add_Product_recommend.as_view()),
    path('home/recommendProduct/delete',views.Delete_Recommend_product.as_view()),  
    path('home/recommendProduct/update/recommendStatus',views.Update_product_status.as_view()),  
    path('home/recommendProduct/update/sort/',views.Update_Sort1.as_view()),  

    #专题推荐
     #人气推荐
    path('home/recommendSubject/list',views.Product_recommend_Sub.as_view()), 
    path('home/recommendSubject/create',views.Add_Product_recommend_Sub.as_view()),
    path('home/recommendSubject/delete',views.Delete_Recommend_product_Sub.as_view()),  
    path('home/recommendSubject/update/recommendStatus',views.Update_product_status_Sub.as_view()),  
    path('home/recommendSubject/update/sort/',views.Recommend_sort1_Sub.as_view()),  
]

