# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this u
# :
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

#帮助表
class CmsHelp(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.BigIntegerField(blank=True, null=True)
    icon = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    show_status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    read_count = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_help'

#帮助分类表
class CmsHelpCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    #分类图标
    icon = models.CharField(max_length=500, blank=True, null=True)
    #专题数量
    help_count = models.IntegerField(blank=True, null=True)
    show_status = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_help_category'

#用户举报表
class CmsMemberReport(models.Model):
    id = models.BigIntegerField(primary_key=True)
    #0 商品评价 1 话题内容  2：用户评论
    report_type = models.IntegerField(blank=True, null=True)
    #举报人
    report_member_name = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    report_object = models.CharField(max_length=100, blank=True, null=True)
    #举报状态： 0：未处理  1：已处理
    report_status = models.IntegerField(blank=True, null=True)
    #处理结果 0：无效  1：有效  2：恶意
    handle_status = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_member_report'

#优选专区
class CmsPrefrenceArea(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    #展示图片
    pic = models.CharField(max_length=500, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    show_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_prefrence_area'

#优选专区和产品关系表
class CmsPrefrenceAreaProductRelation(models.Model):
    id = models.AutoField(primary_key=True)
    prefrence_area_id = models.BigIntegerField(blank=True, null=True)
    product_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_prefrence_area_product_relation'

#专题表
class CmsSubject(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    #专题主图
    pic = models.CharField(max_length=500, blank=True, null=True)
    #关联产品数量
    product_count = models.IntegerField(blank=True, null=True)
    recommend_status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    collect_count = models.IntegerField(blank=True, null=True)
    read_count = models.IntegerField(blank=True, null=True)
    comment_count = models.IntegerField(blank=True, null=True)
    #画册图片用逗号分割
    album_pics = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    #显示状态：0->不显示；1->显示'
    show_status = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    #转发数
    forward_count = models.IntegerField(blank=True, null=True)
    #专题分类名称'
    category_name = models.CharField(max_length=200, blank=True, null=True)
    # 副标题
    subheading = models.CharField(max_length=200, blank=True, null=True)
    # 价格
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_subject'

#专题分类表
class CmsSubjectCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    #分类图标
    icon = models.CharField(max_length=500, blank=True, null=True)
    #专题数量
    subject_count = models.IntegerField(blank=True, null=True)
    show_status = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_subject_category'

#专题评论表
class CmsSubjectComment(models.Model):
    id = models.AutoField(primary_key=True)
    subject_id = models.BigIntegerField(blank=True, null=True)
    member_nick_name = models.CharField(max_length=255, blank=True, null=True)
    member_icon = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    show_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_subject_comment'

#专题商品关系表
class CmsSubjectProductRelation(models.Model):
    id = models.AutoField(primary_key=True)
    subject_id = models.BigIntegerField(blank=True, null=True)
    product_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_subject_product_relation'

#话题表
class CmsTopic(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    #参与人数
    attend_count = models.IntegerField(blank=True, null=True)
    #关注人数
    attention_count = models.IntegerField(blank=True, null=True)
    read_count = models.IntegerField(blank=True, null=True)
    #奖品名称
    award_name = models.CharField(max_length=100, blank=True, null=True)
    #参与方式
    attend_type = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_topic'

#话题分类表
class CmsTopicCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    #分类图标
    icon = models.CharField(max_length=500, blank=True, null=True)
    #专题数量
    subject_count = models.IntegerField(blank=True, null=True)
    show_status = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_topic_category'

#专题评论表
class CmsTopicComment(models.Model):
    id = models.AutoField(primary_key=True)
    member_nick_name = models.CharField(max_length=255, blank=True, null=True)
    topic_id = models.BigIntegerField(blank=True, null=True)
    member_icon = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    show_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_topic_comment'

#购物车表
class OmsCartItem(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    product_sku_id = models.BigIntegerField(blank=True, null=True)
    member_id = models.BigIntegerField(blank=True, null=True)
    #购买数量
    quantity = models.IntegerField(blank=True, null=True)
    #添加到购物车的价格
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #销售属性1
    sp1 = models.CharField(max_length=200, blank=True, null=True)
    #销售属性2
    sp2 = models.CharField(max_length=200, blank=True, null=True)
    #销售属性3
    sp3 = models.CharField(max_length=200, blank=True, null=True)
    #商品主图
    product_pic = models.CharField(max_length=1000, blank=True, null=True)
    #商品名称
    product_name = models.CharField(max_length=500, blank=True, null=True)
    #商品副标题（卖点）
    product_sub_title = models.CharField(max_length=500, blank=True, null=True)
    #商品sku条码
    product_sku_code = models.CharField(max_length=200, blank=True, null=True)
    #会员昵称
    member_nickname = models.CharField(max_length=500, blank=True, null=True)
    #创建时间
    create_date = models.DateTimeField(blank=True, null=True)
    #修改时间
    modify_date = models.DateTimeField(blank=True, null=True)
    #是否删除
    delete_status = models.IntegerField(blank=True, null=True)
    #商品分类
    product_category_id = models.BigIntegerField(blank=True, null=True)
    product_brand = models.CharField(max_length=200, blank=True, null=True)
    product_sn = models.CharField(max_length=200, blank=True, null=True)
    #商品销售属性:[{"key":"颜色","value":"颜色"},{"key":"容量","value":"4G"}]
    product_attr = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_cart_item'

#公司收发货地址表
class OmsCompanyAddress(models.Model):
    id = models.AutoField(primary_key=True)
    #地址名称
    address_name = models.CharField(max_length=200, blank=True, null=True)
    #默认发货地址：0->否；1->是'
    send_status = models.IntegerField(blank=True, null=True)
    #是否默认收货地址：0->否；1->是'
    receive_status = models.IntegerField(blank=True, null=True)
    #收发货人姓名
    name = models.CharField(max_length=64, blank=True, null=True)
    #收货人电话
    phone = models.CharField(max_length=64, blank=True, null=True)
    #省/直辖市
    province = models.CharField(max_length=64, blank=True, null=True)
    #市
    city = models.CharField(max_length=64, blank=True, null=True)
    #区
    region = models.CharField(max_length=64, blank=True, null=True)
    #详细地址
    detail_address = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_company_address'

#订单表
class OmsOrder(models.Model):
    #订单id
    id = models.AutoField(primary_key=True)
    member_id = models.BigIntegerField()
    coupon_id = models.BigIntegerField(blank=True, null=True)
    #订单编号
    order_sn = models.CharField(max_length=64, blank=True, null=True)
    #提交时间
    create_time = models.DateTimeField(blank=True, null=True)
    #用户帐号
    member_username = models.CharField(max_length=64, blank=True, null=True)
    #订单总金额
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #应付金额（实际支付金额）
    pay_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #运费金额
    freight_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #促销优化金额（促销价、满减、阶梯价）
    promotion_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #积分抵扣金额
    integration_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #优惠券抵扣金额
    coupon_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #管理员后台调整订单使用的折扣金额
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #'支付方式：0->未支付；1->支付宝；2->微信'
    pay_type = models.IntegerField(blank=True, null=True)
    #'订单来源：0->PC订单；1->app订单'
    source_type = models.IntegerField(blank=True, null=True)
    #'订单状态：0->待付款；1->待发货；2->已发货；3->已完成；4->已关闭；5->无效订单'
    status = models.IntegerField(blank=True, null=True)
    #'订单类型：0->正常订单；1->秒杀订单'
    order_type = models.IntegerField(blank=True, null=True)
    #物流公司(配送方式)
    delivery_company = models.CharField(max_length=64, blank=True, null=True)
    #物流单号
    delivery_sn = models.CharField(max_length=64, blank=True, null=True)
    #自动确认时间（天）'
    auto_confirm_day = models.IntegerField(blank=True, null=True)
    #可以获得的积分
    integration = models.IntegerField(blank=True, null=True)
    #可以活动的成长值
    growth = models.IntegerField(blank=True, null=True)
    #活动信息
    promotion_info = models.CharField(max_length=100, blank=True, null=True)
    #'发票类型：0->不开发票；1->电子发票；2->纸质发票'
    bill_type = models.IntegerField(blank=True, null=True)
    #发票抬头
    bill_header = models.CharField(max_length=200, blank=True, null=True)
    #发票内容
    bill_content = models.CharField(max_length=200, blank=True, null=True)
    #收票人电话
    bill_receiver_phone = models.CharField(max_length=32, blank=True, null=True)
    #收票人邮箱
    bill_receiver_email = models.CharField(max_length=64, blank=True, null=True)
    #收货人姓名
    receiver_name = models.CharField(max_length=100)
    #收货人电话
    receiver_phone = models.CharField(max_length=32)
    #收货人邮编
    receiver_post_code = models.CharField(max_length=32, blank=True, null=True)
    #省份/直辖市
    receiver_province = models.CharField(max_length=32, blank=True, null=True)
    #城市
    receiver_city = models.CharField(max_length=32, blank=True, null=True)
    #区
    receiver_region = models.CharField(max_length=32, blank=True, null=True)
    #详细地址
    receiver_detail_address = models.CharField(max_length=200, blank=True, null=True)
    #订单备注
    note = models.CharField(max_length=500, blank=True, null=True)
    #'确认收货状态：0->未确认；1->已确认'
    confirm_status = models.IntegerField(blank=True, null=True)
    #删除状态：0->未删除；1->已删除'
    delete_status = models.IntegerField()
    #下单时使用的积分
    use_integration = models.IntegerField(blank=True, null=True)
    #支付时间
    payment_time = models.DateTimeField(blank=True, null=True)
    #发货时间
    delivery_time = models.DateTimeField(blank=True, null=True)
    #确认收货时间
    receive_time = models.DateTimeField(blank=True, null=True)
    ##评价时间
    comment_time = models.DateTimeField(blank=True, null=True)
    #修改时间
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_order'

#订单中所包含的商品
class OmsOrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    #订单id
    order_id = models.BigIntegerField(blank=True, null=True)
    #订单编号
    order_sn = models.CharField(max_length=64, blank=True, null=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    product_pic = models.CharField(max_length=500, blank=True, null=True)
    product_name = models.CharField(max_length=200, blank=True, null=True)
    product_brand = models.CharField(max_length=200, blank=True, null=True)
    product_sn = models.CharField(max_length=64, blank=True, null=True)
    #销售价格
    product_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #购买数量
    product_quantity = models.IntegerField(blank=True, null=True)
    #商品sku编号
    product_sku_id = models.BigIntegerField(blank=True, null=True)
    #商品sku条码
    product_sku_code = models.CharField(max_length=50, blank=True, null=True)
    #商品分类id
    product_category_id = models.BigIntegerField(blank=True, null=True)
    #商品的销售属性
    sp1 = models.CharField(max_length=100, blank=True, null=True)

    sp2 = models.CharField(max_length=100, blank=True, null=True)
    sp3 = models.CharField(max_length=100, blank=True, null=True)
    #商品促销名称
    promotion_name = models.CharField(max_length=200, blank=True, null=True)
    #商品促销分解金额
    promotion_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #优惠券优惠分解金额
    coupon_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ##积分优惠分解金额
    integration_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #该商品经过优惠后的分解金额
    real_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #
    gift_integration = models.IntegerField(blank=True, null=True)
    gift_growth = models.IntegerField(blank=True, null=True)
    #商品销售属性:[{"key":"颜色","value":"颜色"},{"key":"容量","value":"4G"}]'
    product_attr = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_order_item'

#订单操作历史记录
class OmsOrderOperateHistory(models.Model):
    id = models.AutoField(primary_key=True)
    #订单id
    order_id = models.BigIntegerField(blank=True, null=True)
    #操作人：用户；系统；后台管理员
    operate_man = models.CharField(max_length=100, blank=True, null=True)
    #操作时间
    create_time = models.DateTimeField(blank=True, null=True)
    #'订单状态：0->待付款；1->待发货；2->已发货；3->已完成；4->已关闭；5->无效订单'
    order_status = models.IntegerField(blank=True, null=True)
    #备注
    note = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_order_operate_history'

#订单退货申请
class OmsOrderReturnApply(models.Model):
    id = models.AutoField(primary_key=True)
    #订单id
    order_id = models.BigIntegerField(blank=True, null=True)
    #收货地址表id
    company_address_id = models.BigIntegerField(blank=True, null=True)
    #退货商品id
    product_id = models.BigIntegerField(blank=True, null=True)
    #订单编号
    order_sn = models.CharField(max_length=64, blank=True, null=True)
    #申请时间
    create_time = models.DateTimeField(blank=True, null=True)
    #会员用户名
    member_username = models.CharField(max_length=64, blank=True, null=True)
    #退款金额
    return_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #退货人姓名
    return_name = models.CharField(max_length=100, blank=True, null=True)
    #退货人电话
    return_phone = models.CharField(max_length=100, blank=True, null=True)
    #'申请状态：0->待处理；1->退货中；2->已完成；3->已拒绝
    status = models.IntegerField(blank=True, null=True)
    #处理时间
    handle_time = models.DateTimeField(blank=True, null=True)
    #商品图片
    product_pic = models.CharField(max_length=500, blank=True, null=True)
    #商品名称
    product_name = models.CharField(max_length=200, blank=True, null=True)
    #商品品牌
    product_brand = models.CharField(max_length=200, blank=True, null=True)
    #商品销售属性：颜色：红色；尺码：xl
    product_attr = models.CharField(max_length=500, blank=True, null=True)
    #退货数量
    product_count = models.IntegerField(blank=True, null=True)
    #商品单价
    product_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #商品实际支付单价
    product_real_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #原因
    reason = models.CharField(max_length=200, blank=True, null=True)
    #描述
    description = models.CharField(max_length=500, blank=True, null=True)
    #凭证图片，以逗号隔开
    proof_pics = models.CharField(max_length=1000, blank=True, null=True)
    #处理备注
    handle_note = models.CharField(max_length=500, blank=True, null=True)
    #处理人员
    handle_man = models.CharField(max_length=100, blank=True, null=True)
    #收货人
    receive_man = models.CharField(max_length=100, blank=True, null=True)
    #收货时间
    receive_time = models.DateTimeField(blank=True, null=True)
    #收货备注
    receive_note = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_order_return_apply'

#退货原因表
class OmsOrderReturnReason(models.Model):
    id = models.AutoField(primary_key=True)
    #退货类型
    name = models.CharField(max_length=100, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    #状态：0->不启用；1->启用
    status = models.IntegerField(blank=True, null=True)
    #添加时间
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_order_return_reason'

#订单设置表
class OmsOrderSetting(models.Model):
    id = models.AutoField(primary_key=True)
    #秒杀订单超时关闭时间(分)
    flash_order_overtime = models.IntegerField(blank=True, null=True)
    #正常订单超时时间(分)
    normal_order_overtime = models.IntegerField(blank=True, null=True)
    #发货后自动确认收货时间（天）
    confirm_overtime = models.IntegerField(blank=True, null=True)
    #自动完成交易时间，不能申请售后（天）
    finish_overtime = models.IntegerField(blank=True, null=True)
    #订单完成后自动好评时间（天）
    comment_overtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oms_order_setting'

#相册表
class PmsAlbum(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    cover_pic = models.CharField(max_length=1000, blank=True, null=True)
    pic_count = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pms_album'

#画册图片表
class PmsAlbumPic(models.Model):
    id = models.AutoField(primary_key=True)
    album_id = models.BigIntegerField(blank=True, null=True)
    pic = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pms_album_pic'

#品牌表

class PmsBrand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    first = models.CharField(max_length=8, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    is_company = models.IntegerField(blank=True, null=True)
    is_show = models.IntegerField(blank=True, null=True)
    product_count = models.IntegerField(default=1,blank=True)
    product_comment_count = models.IntegerField(default=1,blank=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    b_logo = models.CharField(max_length=255, blank=True, null=True)
    story = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pms_brand'



#商品评价表
class PmsComment(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    member_nick_name = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    #评价星数：0->5
    star = models.IntegerField(blank=True, null=True)
    #评价的ip
    member_ip = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    show_status = models.IntegerField(blank=True, null=True)
    #购买时的商品属性
    product_attribute = models.CharField(max_length=255, blank=True, null=True)
    collect_couont = models.IntegerField(blank=True, null=True)
    read_count = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    #上传图片地址，以逗号隔开
    pics = models.CharField(max_length=1000, blank=True, null=True)
    #评论用户头像
    member_icon = models.CharField(max_length=255, blank=True, null=True)
    replay_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pms_comment'

#产品评价回复表
class PmsCommentReplay(models.Model):
    id = models.AutoField(primary_key=True)
    comment_id = models.BigIntegerField(blank=True, null=True)
    member_nick_name = models.CharField(max_length=255, blank=True, null=True)
    member_icon = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    #评论人员类型；0->会员；1->管理员
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pms_comment_replay'

#运费模版
class PmsFeightTemplate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    #'计费类型:0->按重量；1->按件数'
    charge_type = models.IntegerField(blank=True, null=True)
    #首重kg
    first_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #首费（元）
    first_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    continue_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    continme_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #目的地（省、市）
    dest = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pms_feight_template'

#商品会员价格表
class PmsMemberPrice(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    member_level_id = models.BigIntegerField(blank=True, null=True)
    #会员价格
    member_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    member_level_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pms_member_price'

#商品特惠价格表
class PmsSalesPrice(models.Model):
    id = models.AutoField(primary_key=True)
    promotionStartTime = models.DateTimeField() # 促销开始时间
    promotionEndTime = models.DateTimeField() # 促销结束时间
    promotionPrice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) # 促销价格
    brandId = models.BigIntegerField(blank=True, null=True) #品牌id

    class Meta:
        managed = False
        db_table = 'pms_sales_price'



# 商品表
class Pmsproduct(models.Model):
    id = models.AutoField(primary_key=True)
    brandId = models.BigIntegerField(blank=True, null=True) #品牌id
    productCategoryId = models.BigIntegerField(blank=True, null=True) #商品分类id
    feightTemplateId = models.BigIntegerField(blank=True, null=True) #
    productAttributeCategoryId = models.BigIntegerField(blank=True, null=True) #属性类型id
    name = models.CharField(max_length=64)
    pic = models.CharField(max_length=255, blank=True, null=True) #图片
    productSn = models.CharField(max_length=64) # 货号
    deleteStatus = models.IntegerField(blank=True, null=True) # 删除状态: 0.未删除 1.已删除
    publishStatus = models.IntegerField(
    blank=True, null=True) # 上架状态：0->下架；1->上架
    newStatus = models.IntegerField(
    blank=True, null=True) # 新品状态:0->不是新品；1->新品
    recommandStatus = models.IntegerField(
    blank=True, null=True) # 推荐状态；0->不推荐；1->推荐
    verifyStatus = models.IntegerField(
    blank=True, null=True) # 审核状态：0->未审核；1->审核通过
    sort = models.IntegerField(blank=True, null=True)# 排序
    sale = models.IntegerField(blank=True, null=True) # 销量
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) 
    promotionPrice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) # 促销价格
    giftGrowth = models.IntegerField(blank=True, null=True) # 赠送的成长值
    giftPoint = models.IntegerField(blank=True, null=True) # 赠送的积分
    usePointLimit = models.IntegerField(blank=True, null=True) # 限制使用的积分数
    subTitle = models.CharField(max_length=255, blank=True, null=True) # 副标题
    description = models.TextField(blank=True, null=True) # 商品描述
    originalPrice = models.DecimalField(
    max_digits=10, decimal_places=2, blank=True, null=True) # 市场价
    stock = models.IntegerField(blank=True, null=True) # 库存
    lowStock = models.IntegerField(blank=True, null=True) # 库存预警值
    unit = models.CharField(max_length=16, blank=True, null=True) # 单位
    weight = models.DecimalField(
    max_digits=10, decimal_places=2, blank=True, null=True) # 商品重量，默认为克
    previewStatus = models.IntegerField(
    blank=True, null=True) # 是否为预告商品：0->不是；1->是
    serviceIds = models.CharField(max_length=64, blank=True, null=True)
    # 以逗号分割的产品服务：1->无忧退货；2->快速退款；3->免费包邮
    keywords = models.CharField(max_length=255, blank=True, null=True) #关键字
    note = models.CharField(max_length=255, blank=True, null=True) #商品备注
    albumPics = models.CharField(
    max_length=255, blank=True, null=True) # 画册图片，连产品图片限制为5张，以逗号分割
    detailTitle = models.CharField(max_length=255, blank=True, null=True)
    detailDesc = models.TextField(blank=True, null=True)
    detailHtml = models.TextField(blank=True, null=True) # 产品详情网页内容
    detailMobileHtml = models.TextField(blank=True, null=True) # 移动端网页详情
    promotionStartTime = models.DateTimeField() # 促销开始时间
    promotionEndTime = models.DateTimeField() # 促销结束时间
    promotionPerLimit = models.IntegerField(blank=True, null=True) # 活动限购数量
    promotionType = models.IntegerField(blank=True, null=True)
    # 促销类型：0->没有促销使用原价;1->使用促销价；2->使用会员价；3->使用阶梯价格；4->使用满减价格；5->限时购
    brandName = models.CharField(max_length=255, blank=True, null=True) # 品牌名称
    productCategoryName = models.CharField(max_length=255, blank=True, null=True)# 产品分类名称


    class Meta:
        db_table = 'pms_product'




#商品属性参数表
class PmsProductAttribute(models.Model):
    id = models.AutoField(primary_key=True)
    type_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    #'属性选择类型：0->唯一；1->单选；2->多选'
    select_type = models.IntegerField(blank=True, null=True)
    #'属性录入方式：0->手工录入；1->从列表中选取'
    input_type = models.IntegerField(blank=True, null=True)
    #'可选值列表，以逗号隔开'
    input_list = models.CharField(max_length=255, blank=True, null=True)
    #排序字段：最高的可以单独上传图片
    sort = models.IntegerField(blank=True, null=True)
   #'分类筛选样式：1->普通；1->颜色
    filter_type = models.IntegerField(blank=True, null=True)
    # '检索类型；0->不需要进行检索；1->关键字检索；2->范围检索
    is_select = models.IntegerField(blank=True, null=True)
    #'相同属性产品是否关联；0->不关联；1->关联'
    related_status = models.IntegerField(blank=True, null=True)
    #'是否支持手动新增；0->不支持；1->支持'
    hand_add_status = models.IntegerField(blank=True, null=True)
    #'属性的类型；0->规格；1->参数',
    type1 = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pms_product_attribute'
    def to_dict1(self):
        udict = {'id':self.id,'name':self.name}
        return udict      

#产品属性分类表
class PmsProductAttributeCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    #属性数量
    attribute_count = models.IntegerField(blank=True, null=True)
    #参数数量
    param_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pms_product_attribute_category'
    def to_dict(self):
        udict = {'id':self.id,'name':self.name}
        return udict      

#存储产品参数信息的表
class PmsProductAttributeValue(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    product_attribute_id = models.BigIntegerField(blank=True, null=True)
    #手动添加规格或参数的值，参数单值，规格有多个时以逗号隔开
    value = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pms_product_attribute_value'

# #产品分类
class PmsProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    #上机分类的编号：0表示一级分类
    parent_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    #'分类级别：0->1级；1->2级'
    level_l = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    danwei = models.CharField(max_length=64, blank=True, null=True)
    #'是否显示在导航栏：0->不显示；1->显示'
    is_nav_status = models.IntegerField(blank=True, null=True)
    #'显示状态：0->不显示；1->显示'
    status = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    #图标
    image = models.CharField(max_length=255, blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    productAttributeIdList= models.CharField(max_length=255)
    #描述
   

    class Meta:
        managed = False
        db_table = 'pms_product_category'
    def to_dict(self):
        udict = {'id':self.id,'name':self.name}
        return udict        
    
#产品的分类和属性的关系表，用于设置分类筛选条件（只支持一级分类）
class PmsProductCategoryAttributeRelation(models.Model):
    id = models.AutoField(primary_key=True)
    product_category_id = models.BigIntegerField(blank=True, null=True)
    product_attribute_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pms_product_category_attribute_relation'

#产品满减表(只针对同商品)
class PmsProductFullReduction(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    full_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reduce_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pms_product_full_reduction'

#产品阶梯价格表(只针对同商品)
class PmsProductLadder(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    #满足的商品数量
    count = models.IntegerField(blank=True, null=True)
    #折扣
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #折后价格
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pms_product_ladder'

#
class PmsProductOperateLog(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    price_old = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_new = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sale_price_old = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sale_price_new = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #赠送的积分
    gift_point_old = models.IntegerField(blank=True, null=True)
    gift_point_new = models.IntegerField(blank=True, null=True)
    use_point_limit_old = models.IntegerField(blank=True, null=True)
    use_point_limit_new = models.IntegerField(blank=True, null=True)
    #操作人
    operate_man = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pms_product_operate_log'

#商品审核记录
class PmsProductVertifyRecord(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    #审核人
    vertify_man = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    #反馈详情
    detail = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pms_product_vertify_record'

#sku的库存
class PmsSkuStock(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    #sku编码
    sku_code = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #库存
    stock = models.IntegerField(blank=True, null=True)
    #预警库存
    low_stock = models.IntegerField(blank=True, null=True)
    #销售属性1
    sp1 = models.CharField(max_length=64, blank=True, null=True)
    sp2 = models.CharField(max_length=64, blank=True, null=True)
    sp3 = models.CharField(max_length=64, blank=True, null=True)
    #展示图片
    pic = models.CharField(max_length=255, blank=True, null=True)
    #销量
    sale = models.IntegerField(blank=True, null=True)
    #单品促销价格
    promotion_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #锁定库存
    lock_stock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pms_sku_stock'

#优惠卷表
class SmsCoupon(models.Model):
    id = models.AutoField(primary_key=True)
    #'优惠卷类型；0->全场赠券；1->会员赠券；2->购物赠券；3->注册赠券'
    type = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    #'使用平台：0->全部；1->移动；2->PC'
    platform = models.IntegerField(blank=True, null=True)
    #数量
    count = models.IntegerField(blank=True, null=True)
    #金额
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #每人限领张数
    per_limit = models.IntegerField(blank=True, null=True)
    #使用门槛；0表示无门槛
    min_point = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    #'使用类型：0->全场通用；1->指定分类；2->指定商品
    use_type = models.IntegerField(blank=True, null=True)
    #备注
    note = models.CharField(max_length=200, blank=True, null=True)
    #发行数量
    publish_count = models.IntegerField(blank=True, null=True)
    #已使用数量
    use_count = models.IntegerField(blank=True, null=True)
    #领取数量
    receive_count = models.IntegerField(blank=True, null=True)
    #可以领取的日期
    enable_time = models.DateTimeField(blank=True, null=True)
    #优惠码
    code = models.CharField(max_length=64, blank=True, null=True)
    #可领取的会员类型：0->无限时
    member_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_coupon'

#优惠券使用、领取历史表
class SmsCouponHistory(models.Model):
    id = models.AutoField(primary_key=True)
    coupon_id = models.BigIntegerField(blank=True, null=True)
    member_id = models.BigIntegerField(blank=True, null=True)
    coupon_code = models.CharField(max_length=64, blank=True, null=True)
    #领取人昵称
    member_nickname = models.CharField(max_length=64, blank=True, null=True)
    #'获取类型：0->后台赠送；1->主动获取',
    get_type = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    #'使用状态：0->未使用；1->已使用；2->已过期'
    use_status = models.IntegerField(blank=True, null=True)
    #使用时间
    use_time = models.DateTimeField(blank=True, null=True)
    #订单编号
    order_id = models.BigIntegerField(blank=True, null=True)
    #订单号码
    order_sn = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_coupon_history'

#优惠券和产品分类关系表
class SmsCouponProductCategoryRelation(models.Model):
    id = models.AutoField(primary_key=True)
    coupon_id = models.BigIntegerField(blank=True, null=True)
    product_category_id = models.BigIntegerField(blank=True, null=True)
    #产品分类名称
    product_category_name = models.CharField(max_length=200, blank=True, null=True)
    #父分类名称
    parent_category_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_coupon_product_category_relation'

#优惠券和产品的关系表
class SmsCouponProductRelation(models.Model):
    id = models.AutoField(primary_key=True)
    coupon_id = models.BigIntegerField(blank=True, null=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    #商品名称
    product_name = models.CharField(max_length=500, blank=True, null=True)
    #商品编码
    product_sn = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_coupon_product_relation'

#限时购表 活动表
class SmsFlashPromotion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    #开始日期
    start_time = models.DateField(blank=True, null=True)
    #结束日期
    end_time = models.DateField(blank=True, null=True)
    #上下线状态
    status = models.IntegerField(blank=True, null=True)
    #秒杀时间段名称
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'sms_flash_promotion'

#限时购通知记录
class SmsFlashPromotionLog(models.Model):
    member_id = models.IntegerField(blank=True, null=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    member_phone = models.CharField(max_length=64, blank=True, null=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)
    #会员订阅时间
    subscribe_time = models.DateTimeField(blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_flash_promotion_log'

#商品限时购与商品关系表
class SmsFlashPromotionProductRelation(models.Model):
    #编号
    id = models.AutoField(primary_key=True)
    flash_promotion_id = models.BigIntegerField(blank=True, null=True)
    #编号
    flash_promotion_session_id = models.BigIntegerField(blank=True, null=True)

    product_id = models.BigIntegerField(blank=True, null=True)
    #限时购价格
    flash_promotion_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #限时购数量
    flash_promotion_count = models.IntegerField(blank=True, null=True)
    #每人限购数量
    flash_promotion_limit = models.IntegerField(blank=True, null=True)
    #排序
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_flash_promotion_product_relation'

#限时购场次表  时间段表
class SmsFlashPromotionSession(models.Model):
    #编号
    id = models.AutoField(primary_key=True)
    #场次名称
    name = models.CharField(max_length=200, blank=True, null=True)
    #每日开始时间
    start_time = models.DateTimeField()
    #每日结束时间
    end_time = models.DateTimeField()
    #启用状态：0->不启用；1->启用
    status = models.IntegerField(blank=True, null=True)
    #创建时间
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'sms_flash_promotion_session'

#首页轮播广告表
class SmsHomeAdvertise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    #'轮播位置：0->PC首页轮播；1->app首页轮播'
    pic = models.CharField(max_length=500, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    #上下线状态：0->下线；1->上线
    status = models.IntegerField(blank=True, null=True)
    #点击数
    click_count = models.IntegerField(blank=True, null=True)
    #下单数
    order_count = models.IntegerField(blank=True, null=True)
    #链接地址
    url = models.CharField(max_length=500, blank=True, null=True)
    #备注
    note = models.CharField(max_length=500, blank=True, null=True)
    #排序
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_home_advertise'

#首页推荐品牌表
class SmsHomeBrand(models.Model):
    id = models.AutoField(primary_key=True)
    brandId = models.BigIntegerField(blank=True, null=True)
    brandName = models.CharField(max_length=64, blank=True, null=True)
    recommend_status = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_home_brand'

#新鲜好物表 新品推荐
class SmsHomeNewProduct(models.Model):
    id = models.AutoField(primary_key=True)
    productId = models.IntegerField(blank=True, null=True)
    productName = models.CharField(max_length=64, blank=True, null=True)
    recommend_status = models.IntegerField(blank=True, null=True,default=0)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_home_new_product'

#人气推荐商品表
class SmsHomeRecommendProduct(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=64, blank=True, null=True)
    recommend_status = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_home_recommend_product'

#首页推荐专题表
class SmsHomeRecommendSubject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_id = models.BigIntegerField(blank=True, null=True)
    subject_name = models.CharField(max_length=64, blank=True, null=True)
    recommend_status = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_home_recommend_subject'

#后台用户表
class UmsAdmin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    #头像
    icon = models.CharField(max_length=500, blank=True, null=True)
    #邮箱
    email = models.CharField(max_length=100, blank=True, null=True)
    #昵称
    nick_name = models.CharField(max_length=200, blank=True, null=True)
    #备注信息
    note = models.CharField(max_length=500, blank=True, null=True)
    #创建时间
    create_time = models.DateTimeField(blank=True, null=True)
    #最后登录时间
    login_time = models.DateTimeField(blank=True, null=True)
    #帐号启用状态：0->禁用；1->启用
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_admin'

#后台用户登录日志表
class UmsAdminLoginLog(models.Model):
    id = models.AutoField(primary_key=True)
    admin_id = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    #浏览器登录类型
    user_agent = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_admin_login_log'

#后台用户和权限关系表(除角色中定义的权限以外的加减权限)
class UmsAdminPermissionRelation(models.Model):
    id = models.AutoField(primary_key=True)
    admin_id = models.BigIntegerField(blank=True, null=True)
    permission_id = models.BigIntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_admin_permission_relation'

#
class UmsAdminRoleRelation(models.Model):
    id = models.AutoField(primary_key=True)
    admin_id = models.BigIntegerField(blank=True, null=True)
    role_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_admin_role_relation'

#后台用户和角色关系表
class UmsGrowthChangeHistory(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    change_type = models.IntegerField(blank=True, null=True)
    change_count = models.IntegerField(blank=True, null=True)
    operate_man = models.CharField(max_length=100, blank=True, null=True)
    operate_note = models.CharField(max_length=200, blank=True, null=True)
    source_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_growth_change_history'

#成长值变化历史记录表
class UmsIntegrationChangeHistory(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    #改变类型：0->增加；1->减少'
    change_type = models.IntegerField(blank=True, null=True)
    #积分改变数量
    change_count = models.IntegerField(blank=True, null=True)
    #操作人员
    operate_man = models.CharField(max_length=100, blank=True, null=True)
    #操作备注
    operate_note = models.CharField(max_length=200, blank=True, null=True)
    #'积分来源：0->购物；1->管理员修改'
    source_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_integration_change_history'

#积分消费设置
class UmsIntegrationConsumeSetting(models.Model):
    id = models.AutoField(primary_key=True)
    #每一元需要抵扣的积分数量
    deduction_per_amount = models.IntegerField(blank=True, null=True)
    #每笔订单最高抵用百分比
    max_percent_per_order = models.IntegerField(blank=True, null=True)
    #每次使用积分最小单位100
    use_unit = models.IntegerField(blank=True, null=True)
    #'是否可以和优惠券同用；0->不可以；1->可以'
    coupon_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_integration_consume_setting'

#会员表
class UmsMember(models.Model):
    id = models.AutoField(primary_key=True)
    member_level_id = models.BigIntegerField(blank=True, null=True)
    #用户名
    username = models.CharField(unique=True, max_length=64, blank=True, null=True)
    #密码
    password = models.CharField(max_length=64, blank=True, null=True)
    #昵称
    nickname = models.CharField(max_length=64, blank=True, null=True)
    #手机号码
    phone = models.CharField(unique=True, max_length=64, blank=True, null=True)
    #帐号启用状态:0->禁用；1->启用
    status = models.IntegerField(blank=True, null=True)
    #注册时间
    create_time = models.DateTimeField(blank=True, null=True)
    #头像
    icon = models.CharField(max_length=500, blank=True, null=True)
    #性别：0->未知；1->男；2->女
    gender = models.IntegerField(blank=True, null=True)
    #生日
    birthday = models.DateField(blank=True, null=True)
    #所在城市
    city = models.CharField(max_length=64, blank=True, null=True)
    #职业
    job = models.CharField(max_length=100, blank=True, null=True)
    #个性签名
    personalized_signature = models.CharField(max_length=200, blank=True, null=True)
    #用户来源
    source_type = models.IntegerField(blank=True, null=True)
    #积分
    integration = models.IntegerField(blank=True, null=True)
    #成长值
    growth = models.IntegerField(blank=True, null=True)
    #剩余抽奖次数
    luckey_count = models.IntegerField(blank=True, null=True)
    #历史积分数量
    history_integration = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_member'

#会员等级表
class UmsMemberLevel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    growth_point = models.IntegerField(blank=True, null=True)
    #是否为默认等级：0->不是；1->是'
    default_status = models.IntegerField(blank=True, null=True)
    #免运费标准
    free_freight_point = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #每次评价获取的成长值
    comment_growth_point = models.IntegerField(blank=True, null=True)
    #是否有免邮特权
    priviledge_free_freight = models.IntegerField(blank=True, null=True)
    #是否有签到特权
    priviledge_sign_in = models.IntegerField(blank=True, null=True)
    #是否有评论获奖励特权
    priviledge_comment = models.IntegerField(blank=True, null=True)
    #是否有专享活动特权
    priviledge_promotion = models.IntegerField(blank=True, null=True)
    #是否有会员价格特权
    priviledge_member_price = models.IntegerField(blank=True, null=True)
    #是否有生日特权
    priviledge_birthday = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_member_level'

#会员登录记录
class UmsMemberLoginLog(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.BigIntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    #登录类型：0->PC；1->android;2->ios;3->小程序
    login_type = models.IntegerField(blank=True, null=True)
    province = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_member_login_log'

#用户和标签关系表
class UmsMemberMemberTagRelation(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.BigIntegerField(blank=True, null=True)
    tag_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_member_member_tag_relation'

#会员与产品分类关系表（用户喜欢的分类）
class UmsMemberProductCategoryRelation(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.BigIntegerField(blank=True, null=True)
    product_category_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_member_product_category_relation'

#会员收货地址表
class UmsMemberReceiveAddress(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.BigIntegerField(blank=True, null=True)
    #收货人名称
    name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=64, blank=True, null=True)
    #是否为默认
    default_status = models.IntegerField(blank=True, null=True)
    #邮政编码
    post_code = models.CharField(max_length=100, blank=True, null=True)
    #省份/直辖市
    province = models.CharField(max_length=100, blank=True, null=True)
    #城市
    city = models.CharField(max_length=100, blank=True, null=True)
    #区
    region = models.CharField(max_length=100, blank=True, null=True)
    #详细地址(街道)
    detail_address = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_member_receive_address'

#会员积分成长规则表
class UmsMemberRuleSetting(models.Model):
    id = models.AutoField(primary_key=True)
    #连续签到天数
    continue_sign_day = models.IntegerField(blank=True, null=True)
    #连续签到赠送数量
    continue_sign_point = models.IntegerField(blank=True, null=True)
    #每消费多少元获取1个点
    consume_per_point = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #最低获取点数的订单金额
    low_order_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #每笔订单最高获取点数
    max_point_per_order = models.IntegerField(blank=True, null=True)
    #类型：0->积分规则；1->成长值规则
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_member_rule_setting'

#会员统计信息
class UmsMemberStatisticsInfo(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.BigIntegerField(blank=True, null=True)
    #累计消费金额
    consume_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    #订单数量
    order_count = models.IntegerField(blank=True, null=True)
    #优惠券数量
    coupon_count = models.IntegerField(blank=True, null=True)
    #评价数
    comment_count = models.IntegerField(blank=True, null=True)
    #退货数量
    return_order_count = models.IntegerField(blank=True, null=True)
    #登录次数
    login_count = models.IntegerField(blank=True, null=True)
    #关注数量
    attend_count = models.IntegerField(blank=True, null=True)
    #粉丝数量
    fans_count = models.IntegerField(blank=True, null=True)

    collect_product_count = models.IntegerField(blank=True, null=True)
    collect_subject_count = models.IntegerField(blank=True, null=True)
    collect_topic_count = models.IntegerField(blank=True, null=True)
    collect_comment_count = models.IntegerField(blank=True, null=True)
    invite_friend_count = models.IntegerField(blank=True, null=True)
    #最后一次下订单时间
    recent_order_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_member_statistics_info'

#用户标签表
class UmsMemberTag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    #自动打标签完成订单数量
    finish_order_count = models.IntegerField(blank=True, null=True)
    #自动打标签完成订单金额
    finish_order_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_member_tag'

#会员任务表
class UmsMemberTask(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    #赠送成长值
    growth = models.IntegerField(blank=True, null=True)
    #赠送积分
    intergration = models.IntegerField(blank=True, null=True)
    #'任务类型：0->新手任务；1->日常任务
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_member_task'

#后台用户权限表
class UmsPermission(models.Model):
    id = models.AutoField(primary_key=True)
    #父级权限id
    pid = models.BigIntegerField(blank=True, null=True)
    #名称
    name = models.CharField(max_length=100, blank=True, null=True)
    #权限值
    value = models.CharField(max_length=200, blank=True, null=True)
    #图标
    icon = models.CharField(max_length=500, blank=True, null=True)
    #'权限类型：0->目录；1->菜单；2->按钮（接口绑定权限）
    type = models.IntegerField(blank=True, null=True)
    #前端资源路径
    uri = models.CharField(max_length=200, blank=True, null=True)
    #启用状态；0->禁用；1->启用'
    status = models.IntegerField(blank=True, null=True)
    #创建时间
    create_time = models.DateTimeField(blank=True, null=True)
    #排序
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_permission'

#后台用户角色表
class UmsRole(models.Model):
    id = models.AutoField(primary_key=True)
    #名称
    name = models.CharField(max_length=100, blank=True, null=True)
    #描述
    description = models.CharField(max_length=500, blank=True, null=True)
    #后台用户数量
    admin_count = models.IntegerField(blank=True, null=True)
    #创建时间
    create_time = models.DateTimeField(blank=True, null=True)
    #启用状态：0->禁用；1->启用'
    status = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_role'

#后台用户角色和权限关系表
class UmsRolePermissionRelation(models.Model):
    id = models.AutoField(primary_key=True)
    role_id = models.BigIntegerField(blank=True, null=True)
    permission_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ums_role_permission_relation'


# 新闻表
class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)

    


    class Meta:
        managed = False
        db_table = 'news'

