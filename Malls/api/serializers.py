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

# 品牌详情展示
class PmsbrandDetaileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PmsBrand
        fields = ('b_logo','logo','name','describe','location','like_count','attention_count','story')


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

# 商品分类页面
class PmsProductCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PmsProductCategory
        fields = '__all__'
        # fields = ("name","icon")


# 专题分类页面
class CmsSubjectcategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CmsSubjectCategory
        # fields = '__all__'
        fields = ("name","icon")



# 话题详情展示页面
class CmsTopicModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =CmsTopic
        fields='__all__'
        # fields=("pic",'name','','price')


# 话题分类展示页面
class CmsTopicCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =CmsTopicCategory
        # fields='__all__'
        fields=("name",'icon')

# 话题评论展示页面
class CmsTopicCommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =CmsTopicComment
        # fields='__all__'
        fields=("member_nick_name",'member_icon','content','create_time','like_count','comment_count')








        


