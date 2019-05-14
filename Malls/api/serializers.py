from rest_framework import serializers
from shopadmin.models  import *

# 商品展示
class PmsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Pmsproduct
        fields='__all__'

# 轮播图展示
class SmsHomeAdvertiseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =SmsHomeAdvertise
        fields = ('pic',)
        # fields='__all__'

class NewsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =News
        fields='__all__'

# 品牌展示
class PmsbrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =PmsBrand
        fields = ('name','price','logo')
        # fields='__all__'


# 秒杀活动展示
class SmsFlashPromotionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =SmsFlashPromotion
        fields='__all__'    


# 秒杀活动时间展示
class SmsFlashPromotionSessionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =SmsFlashPromotionSession
        fields='__all__'
        # fields=("name")

# 新鲜好物展示页面
class PmsproductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =Pmsproduct
        # fields='__all__'
        fields=("pic",'name','subTitle','originalPrice')

# 专题优选展示页面
class CmsSubjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =CmsSubject
        # fields='__all__'
        fields=("pic",'title','subheading','price')

class CmsTopicModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =CmsTopic
        fields='__all__'
        # fields=("pic",'name','','price')



        


