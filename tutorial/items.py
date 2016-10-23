# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MedicationItem(scrapy.Item):
	# 批准文号	国药准字Z14020687 
	license = scrapy.Field()
	# 产品名称	龟龄集 
	product = scrapy.Field()
	# 英文名称
	english = scrapy.Field()
	# 商品名称
	item = scrapy.Field()
	# 剂型	胶囊剂
	form = scrapy.Field()
	# 规格	每粒装0.3g
	standard = scrapy.Field()
	# 生产单位	山西广誉远国药有限公司
	corporation = scrapy.Field()
	# 生产地址	山西省晋中市太谷县新建路171号
	address = scrapy.Field()
	#产品类别	中药 
	category = scrapy.Field()
	# 批准日期	2015-09-28
	date = scrapy.Field()
	# 原批准文号
	original = scrapy.Field()
	# 药品本位码 86902884000629
	code = scrapy.Field()
	# 药品本位码备注
	comment = scrapy.Field()
	
	# 时间
	now = scrapy.Field()	
	# 分页
	page = scrapy.Field()
	# 序列号
	mid = scrapy.Field()	
	
	 
class CorporationItem(scrapy.Item):
	# 编号	陕20160089
	serialnumber = scrapy.Field()
	# 分类码	HbZb
	# 省市	陕西省
	# 企业名称	陕西海天制药有限公司
	# 法定代表人	王春
	# 企业负责人	王誉
	# 注册地址	陕西省西咸新区沣东新城世纪大道东
	# 生产地址	咸阳市永寿县新西兰大街,陕西省西咸新区沣东新城世纪大道东
	# 生产范围	片剂，硬胶囊剂，颗粒剂，合剂，栓剂，搽剂，洗剂 
	# 发证日期	20160622
	# 有效期至	20201231
	# 发证机关	陕西省食品药品监督管理局
	# 签发人	胡小平
	# 日常监管机构	咸阳市食品药品监督管理局
	# 日常监管人员	孙进宝、孙博；李忠、邓召
	# 社会信用代码/组织机构代码	91611104732667919X
	# 监督举报电话	12331
	# 质量负责人	赵荣
	# 备注
	comment = scrapy.Field()
	
