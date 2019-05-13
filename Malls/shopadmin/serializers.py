from rest_framework import serializers
from shopadmin.models  import *
"""
添加商品
"""
# 商品表 PmsMemberPrice
class PmsproductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =Pmsproduct
        fields='__all__'
       

#添加商品
class PmsProductSerializer(serializers.Serializer):
    brandId = serializers.IntegerField(required=True) #品牌id
    productCategoryId = serializers.IntegerField(required=True) #商品分类id
    feightTemplateId = serializers.IntegerField(required=True) #
    productAttributeCategoryId = serializers.IntegerField(required=True) #属性类型id
    name = serializers.CharField(max_length=64,required=True)
    pic = serializers.CharField(max_length=255,required=True) #图片
    productSn = serializers.CharField(max_length=64,required=True) # 货号
    deleteStatus = serializers.IntegerField(required=True) # 删除状态: 0.未删除 1.已删除
    publishStatus = serializers.IntegerField(required=True) # 上架状态：0->下架；1->上架
    newStatus = serializers.IntegerField(required=True) # 新品状态:0->不是新品；1->新品
    recommandStatus = serializers.IntegerField(required=True) # 推荐状态；0->不推荐；1->推荐
    verifyStatus = serializers.IntegerField(required=True) # 审核状态：0->未审核；1->审核通过
    sort = serializers.IntegerField(required=True)# 排序
    sale = serializers.IntegerField(required=True) # 销量
    price = serializers.DecimalField(max_digits=10, decimal_places=2,required=True) 
    promotionPrice = serializers.DecimalField(max_digits=10, decimal_places=2,required=True) # 促销价格
    giftGrowth = serializers.IntegerField(required=True) # 赠送的成长值
    giftPoint = serializers.IntegerField(required=True) # 赠送的积分
    usePointLimit = serializers.IntegerField(required=True) # 限制使用的积分数
    subTitle = serializers.CharField(max_length=255,required=True) # 副标题
    description = serializers.CharField(required=True) # 商品描述
    originalPrice = serializers.DecimalField(
    max_digits=10, decimal_places=2, required=True) # 市场价
    stock = serializers.IntegerField(required=True) # 库存
    lowStock = serializers.IntegerField(required=True) # 库存预警值
    unit = serializers.CharField(max_length=16,required=True) # 单位
    weight = serializers.DecimalField(
    max_digits=10, decimal_places=2, required=True) # 商品重量，默认为克
    previewStatus = serializers.IntegerField(required=True) # 是否为预告商品：0->不是；1->是
    serviceIds = serializers.CharField(max_length=64,required=True)
    # 以逗号分割的产品服务：1->无忧退货；2->快速退款；3->免费包邮
    keywords = serializers.CharField(max_length=255, required=True) #关键字
    note = serializers.CharField(max_length=255, required=True) #商品备注
    albumPics = serializers.CharField(
    max_length=255,required=True) # 画册图片，连产品图片限制为5张，以逗号分割
    detailTitle = serializers.CharField(max_length=255,required=True)
    detailDesc = serializers.CharField(required=True)
    detailHtml = serializers.CharField(required=True) # 产品详情网页内容
    detailMobileHtml = serializers.CharField(required=True) # 移动端网页详情
    promotionStartTime = serializers.DateTimeField(required=True) # 促销开始时间
    promotionEndTime = serializers.DateTimeField(required=True) # 促销结束时间
    promotionPerLimit = serializers.IntegerField(required=True) # 活动限购数量
    promotionType = serializers.IntegerField(required=True)
    # 促销类型：0->没有促销使用原价;1->使用促销价；2->使用会员价；3->使用阶梯价格；4->使用满减价格；5->限时购
    brandName = serializers.CharField(max_length=255, required=True) # 品牌名称
    productCategoryName = serializers.CharField(max_length=255,required=True)# 产品分类名称

    def create(self,data):
        return Pmsproduct.objects.create(**data)   

#新品推荐
class SmsHomeNewProduct_serializers(serializers.Serializer):
    productId =serializers.IntegerField(required=True)
    productName = serializers.CharField(required=True)
    recommend_status = serializers.IntegerField(required=False)
    sort = serializers.IntegerField(required=False)
    def create(self,data):
        return SmsHomeNewProduct.objects.create(**data)
#展示新品推荐
class SmsHomeNewProduct_Modelseri(serializers.ModelSerializer):
    class Meta:
        model =SmsHomeNewProduct
        fields='__all__'
 
 #添加品牌推荐
class SmsHomeBrand_serilazer(serializers.Serializer):
    brandName = serializers.CharField(required=True)
    brandId = serializers.IntegerField(required=True)
    recommend_status = serializers.IntegerField(required=False)
    sort = serializers.IntegerField(required=False)
    def create(self,data):
        return SmsHomeBrand.objects.create(**data)

#展示品牌推荐
class SmsHomeBrand_modelser(serializers.ModelSerializer):
    class Meta:
        model = SmsHomeBrand
        fields = '__all__'

#添加人气推荐
class SmsHomeRecommendProduct_serilazer(serializers.Serializer):
    product_name = serializers.CharField(required=True)
    product_id = serializers.IntegerField(required=True)
    recommend_status = serializers.IntegerField(required=False)
    sort = serializers.IntegerField(required=False)
  
    def create(self,data):
        return SmsHomeRecommendProduct.objects.create(**data)

#展示人气推荐
class SmsHomeRecommendProduct_modelser(serializers.ModelSerializer):
    class Meta:
        model = SmsHomeRecommendProduct     
        fields = '__all__'

#添加专题推荐
class SmsHomeRecommendSubject_serilazer(serializers.Serializer):
    subject_name = serializers.CharField(required=True)
    subject_id = serializers.IntegerField(required=True)
    recommend_status = serializers.IntegerField(required=False)
    sort = serializers.IntegerField(required=False)
    

   
    def create(self,data):
        return SmsHomeRecommendSubject.objects.create(**data)

#展示专题推荐
class SmsHomeRecommendSubject_modelser(serializers.ModelSerializer):
    class Meta:
        model = SmsHomeRecommendSubject     
        fields = '__all__'



# 商品价格会员表 PmsMemberPrice
class PmsMemberPriceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =PmsMemberPrice
        fields='__all__'
        # fields=("name") 

#添加会员商品表
class PmsMemberPriceSerializer(serializers.Serializer):
    
    product_id = serializers.IntegerField(required=True)
    member_level_id = serializers.IntegerField(required=True)
    #会员价格
    member_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    member_level_name = serializers.CharField(required=True)

    def create(self,data):
        return PmsMemberPrice.objects.create(**data)    



# 商品满减表
class PmsProductFullReductionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =PmsProductFullReduction
        fields='__all__'
        # fields=("name") 

#添加商品满减表
class PmsProductFullReductionSerializer(serializers.Serializer):
    
    product_id = serializers.IntegerField(required=True)
    full_price = serializers.DecimalField(required=True,max_digits=10, decimal_places=2,)
    reduce_price = serializers.DecimalField(required=True,max_digits=10, decimal_places=2,)


    def create(self,data):
        return PmsProductFullReduction.objects.create(**data) 




# 商品阶梯价格表(只针对同商品)
class PmsProductLadderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =PmsProductLadder
        fields='__all__'
        # fields=("name") 

#添加阶梯价格表
class PmsProductLadderSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(required=True)
    #满足的商品数量
    count = serializers.IntegerField(required=True)
    #折扣
    discount = serializers.DecimalField(required=True,max_digits=10, decimal_places=2,)
    #折后价格
    price = serializers.DecimalField(required=True,max_digits=10, decimal_places=2,)

    def create(self,data):
        return PmsProductLadder.objects.create(**data) 


# 商品特惠价格表
class PmsSalesPriceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =PmsSalesPrice
        fields='__all__'
        # fields=("name") 

#添加特惠价格表
class PmsSalesPriceSerializer(serializers.Serializer):
    promotionStartTime = serializers.DateTimeField(required=True) # 促销开始时间
    promotionEndTime = serializers.DateTimeField(required=True) # 促销结束时间
    promotionPrice = serializers.DecimalField(max_digits=10, decimal_places=2,required=True) # 促销价格
    brandId = serializers.IntegerField(required=True) #品牌id


    def create(self,data):
        return PmsSalesPrice.objects.create(**data) 





'''
品牌
'''

#获取品牌
class PmsBrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =PmsBrand
        fields='__all__'
        # fields=("name") 

#添加品牌 反序列化
class PmsBrandSerializer(serializers.Serializer):
    name = serializers.CharField(required=True,max_length=50)
    first = serializers.CharField(required=True,max_length=10)
    logo = serializers.CharField(required=True,max_length=255)
    b_logo = serializers.CharField(required=True,max_length=255)
    story = serializers.CharField(required=True,max_length=255)
    sort = serializers.IntegerField(required=True)
    is_show = serializers.IntegerField(required=True)   #是否显示 1显示 0不显示
    is_company = serializers.IntegerField(required=True)   #是否为品牌制造商 0 不是 1是
    
    def create(self,data):
        return PmsBrand.objects.create(**data)     
    
        
'''分类'''
#获取商品分类
class PmsProductCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =PmsProductCategory
        fields='__all__'
        # fields=("name") 

#添加商品分类 反序列化
class PmsProductCategorySerializer(serializers.Serializer):
    name = serializers.CharField(required=True,max_length=50)
    icon = serializers.CharField(required=True,source='image')
    description = serializers.CharField(required=True,max_length=255,source='descrip')
    keywords = serializers.CharField(required=True,max_length=255,source='keyword')
    sort = serializers.IntegerField(required=True)
    level_l = serializers.IntegerField(required=True)     
    parentId = serializers.IntegerField(required=True,source='parent_id')  
    navStatus = serializers.IntegerField(required=True,source='is_nav_status')  
    showStatus = serializers.IntegerField(required=True,source='status')
    count = serializers.IntegerField(required=False)
    productUnit = serializers.CharField(required=True,max_length=50,source='danwei')
    productAttributeIdList= serializers.CharField(required=True,max_length=255)
    def create(self,data):
        return PmsProductCategory.objects.create(**data)   
 
'''轮播图'''

#获取轮播图列表
class SmsHomeAdvertiseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =SmsHomeAdvertise
        fields='__all__'
        

#添加轮播图反序列化
class SmsHomeAdvertiseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=True)
    type = serializers.IntegerField(required=True)
    #'轮播位置：0->PC首页轮播；1->app首页轮播'
    pic = serializers.CharField(max_length=500, required=True)
    start_time = serializers.DateTimeField(required=True)
    end_time = serializers.DateTimeField(required=True)
    #上下线状态：0->下线；1->上线
    status = serializers.IntegerField(required=True)
    #点击数
    click_count = serializers.IntegerField(required=False)
    #下单数
    order_count = serializers.IntegerField(required=False)
    #链接地址
    url = serializers.CharField(max_length=500, required=True)
    #备注
    note = serializers.CharField(max_length=500, required=True)
    #排序
    sort = serializers.IntegerField(required=True)
    def create(self,data):
        return SmsHomeAdvertise.objects.create(**data)   
 
'''类型'''
#获取商品类型
class PmsProductAttributeCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =PmsProductAttributeCategory
        fields='__all__'
        # fields=("name") 

#添加商品类型
class PmsProductAttributeCategorySerializer(serializers.Serializer):
    name = serializers.CharField(required=True,max_length=50)
    # attribute_count = serializers.IntegerField(required=True)
    # param_count = serializers.IntegerField(required=True)
    def create(self,data):
        return PmsProductAttributeCategory.objects.create(**data)   
  
'''属性'''
#获取商品属性
class  PmsProductAttributeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =PmsProductAttribute
        fields='__all__'
        

#添加商品属性  PmsProductAttribute
class PmsProductAttributeSerializer(serializers.Serializer):
    name = serializers.CharField(required=True,max_length=50)
    productAttributeCategoryId = serializers.IntegerField(required=True,source='type_id')
    filterType = serializers.IntegerField(required=True,source='filter_type') 
    #分类筛选方式 1 尺寸 2 颜色
    
    searchType = serializers.IntegerField(required=True,source='is_select')  
    #检索类型 0不与要进行检索，1关键字检索，2范围检索
    relatedStatus = serializers.IntegerField(required=True,source='related_status')  
    #相同属性产品是否关联 0不关联，1是关联
    selectType = serializers.IntegerField(required=True,source='select_type') 
    #属性选择类型：0唯一，1单选，2是多选
    inputType = serializers.IntegerField(required=True,source='input_type')   
    #属性值的录入方式：0手动录入，1是从列表选取
    inputList = serializers.CharField(required=True,max_length=50,source='input_list') 
    #可选值列表，以逗号隔开
    handAddStatus = serializers.IntegerField(required=True,source='hand_add_status')   
    #是否支持手动新增： 0不支持，1是支持
    sort = serializers.IntegerField(required=True)
    
    type = serializers.IntegerField(required=True,source='type1')

    def create(self,data):
        return PmsProductAttribute.objects.create(**data)   
  
    # def update(self, instance, validated_data):
    #     """更新，instance为要更新的对象实例"""
    #     instance.type_id = validated_data.get('productAttributeCategoryId', instance.type_id)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.filter_type = validated_data.get('filterType', instance.filter_type)
    #     instance.select_type = validated_data.get('searchType', instance.select_type)
    #     instance.save()
    #     return instance
  



'''优惠券'''
# SmsCoupon
   
class SmsCouponModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =SmsCoupon
        fields='__all__'
        # fields=("name") 

#添加优惠券
class SmsCouponSerializer(serializers.Serializer):
   
    name = serializers.CharField(required=True,max_length=50)
    type = serializers.IntegerField(required=True)
     #'使用平台：0->全部；1->移动；2->PC'
    platform = serializers.IntegerField(required=True)
   
    count = serializers.IntegerField(required=True)
    #金额
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    #每人限领张数
    per_limit = serializers.IntegerField(required=True)
     #使用门槛；0表示无门槛
    min_point = serializers.DecimalField(max_digits=10, decimal_places=2)
    start_time = serializers.DateTimeField(required=True)
    end_time = serializers.DateTimeField(required=True)
    #'使用类型：0->全场通用；1->指定分类；2->指定商品
    use_type = serializers.IntegerField(required=True)
    #备注
    note = serializers.CharField(required=True,max_length=200)
    #发行数量
    publish_count = serializers.IntegerField(required=True)
    #已使用数量
    use_count =serializers.IntegerField(required=True)
    #领取数量
    receive_count = serializers.IntegerField(required=True)
    #可以领取的日期
    enable_time = serializers.DateTimeField(required=True)
    #优惠码
    code = serializers.CharField(required=True,max_length=50)
    #可领取的会员类型：0->无限时
    member_level = serializers.IntegerField(required=True)
    
    def create(self,data):
        return SmsCoupon.objects.create(**data)   

'''活动表'''
#活动表   SmsFlashPromotion
class SmsFlashPromotionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =SmsFlashPromotion
        fields='__all__'
        # fields=("name") 

#添加活动
class SmsFlashPromotionSerializer(serializers.Serializer):
   
    name = serializers.CharField(required=True,max_length=50)
    #开始日期
    start_time = serializers.DateTimeField(required=True)
    #结束日期
    end_time = serializers.DateTimeField(required=True)
    #上下线状态
    status = serializers.IntegerField(required=True)
    #秒杀时间段名称
    create_time = serializers.DateTimeField(required=False)

     #用于post请求
    def create(self,data):
        return SmsFlashPromotion.objects.create(**data)   

'''时间段表'''
#活动时间段表   SmsFlashPromotionSession
class SmsFlashPromotionSessionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =SmsFlashPromotionSession
        fields='__all__'
        # fields=("name") 

#添加时间段
class SmsFlashPromotionSessionSerializer(serializers.Serializer):
    
    name = serializers.CharField(required=True,max_length=50)
    #开始日期
    start_time = serializers.DateTimeField(required=True)
    end_time = serializers.DateTimeField(required=True)
    #启用状态 0->不启用；1->启用
    status = serializers.IntegerField(required=True)
    #秒杀时间段名称
    create_time = serializers.DateTimeField(required=False)
     
     
    def create(self,data):
        return SmsFlashPromotionSession.objects.create(**data)  




#活动时间段关系表  SmsFlashPromotionProductRelation
class SmsFlashPromotionProductRelationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =SmsFlashPromotionProductRelation
        fields='__all__'
        # fields=("name") 

#添加时间段
class SmsFlashPromotionProductRelationSerializer(serializers.Serializer):
    
  
    flash_promotion_id = serializers.IntegerField(required=True)
    #编号
    flash_promotion_session_id = serializers.IntegerField(required=True)

    product_id = serializers.IntegerField(required=True)
    #限时购价格
    flash_promotion_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    #限时购数量
    flash_promotion_count = serializers.IntegerField(required=True)
    #每人限购数量
    flash_promotion_limit = serializers.IntegerField(required=True)
    #排序
    sort = serializers.IntegerField(required=True)
     
     
    def create(self,data):
        return SmsFlashPromotionProductRelation.objects.create(**data)  


   
