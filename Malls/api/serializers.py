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
# 新闻展示
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



# 首页秒杀列表
class FlashProductModelSerializer(serializers.ModelSerializer):
    product_detail = serializers.SerializerMethodField()

    class Meta:
        model = SmsFlashPromotionProductRelation
        fields = ('__all__')

        def get_product_detail(self, obj):
            product = Pmsproduct.objects.get(id=obj.product_id)
            product_serializer = ProductDetailModelSerializer(product)
            return product_serializer.data  



# 首页各种活动展示的商品
class ProductDetailModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pmsproduct
        fields = ("sub_title", "name", "pic", "price")


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




        


