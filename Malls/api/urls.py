"""Mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
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
from rest_framework.documentation import include_docs_urls
from api import views
from Mall.settings import UPLOAD_ROOT
from django.views.static import serve




urlpatterns = [

    # path('',views.Index.as_view()),
    # 轮播图展示路由
    path('advertising_list',views.Advertising_list.as_view()),
    # 新闻展示路由
    path('news_list',views.News_list.as_view()),
    # 品牌展示路由
    path('brand_list',views.Brand_list.as_view()),
    # 品牌详情展示路由
    path('brand_detail',views.Brand_details.as_view()),
    # 秒杀活动展示路由
    path('activity_list',views.Activity_list.as_view()),
    # 秒杀活动时间路由
    # path('activity_time_list',views.Activity_time_list.as_view()),
    # 首页秒杀时间段
    path('indexSmsFlashPromotionSession',views.IndexSmsFlashPromotionSession.as_view()),
    # 新鲜好物路由
    path('goods_list',views.Goods_list.as_view()),
    # 人气推荐路由
    path('goodss_list',views.Goodss_list.as_view()),
    # 专题精选路由
    path('subject_list',views.Subject_list.as_view()),
    # 猜你喜欢
    path('cai_list',views.Cai_list.as_view()),
    
    # 商品分类展示路由
    path('proudct_category',views.Product_category.as_view()),
    # 专题分类路由
    path('subject_category',views.Subject_category.as_view()),
    # 话题详情路由
    path('topic_list',views.Topic_list.as_view()),
    # 话题分类路由
    path('topic_category',views.Topic_category.as_view()),
    # 话题评论路由
    path('topic_comment',views.Topic_comment.as_view()),
    # 话题分类详情页路由
    path('topic_category_detaile',views.Topic_category_details.as_view()),
    # 话题分类与话题与话题评论关联路由
    path('topic_category_guan',views.Topic_category_guan.as_view()),
    # 优选区展示优选推荐路由
    path('prefrenceArea_recommend',views.PrefrenceArea_recommend.as_view()),
    # 特惠详情展示路由
    path('sales_price',views.Sales_price.as_view()),
    # 相关商品的路由
    path('product_xg',views.Product_XG.as_view()),
    # 相关商品总个数路由
    path('product_count',views.Product_Count.as_view()),
    # 商品详情页路由
    path('product_detail',views.Proudct_detail.as_view()),
    
    

]