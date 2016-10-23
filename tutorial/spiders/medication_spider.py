# -*- coding: utf-8 -*-

import scrapy
import datetime
import re

from tutorial.items import MedicationItem

class MedicationSpider(scrapy.Spider):
    
    name = 'medication'
    allowed_domains=['app1.sfda.gov.cn','app2.sfda.gov.cn']
    start_urls = ['http://app1.sfda.gov.cn/datasearch/face3/search.jsp?tableId=25&curstart=1']

    def parse(self, response):
	
	# <td width=200 align=center>第 1 页 共10949页 共164230条</td>         
	page = response.xpath('//td[@align="center"]/text()').extract_first().encode('utf-8').strip()
	reg = re.search(r'第\s*(.+?)页\s+共\s*(.+?)页',page,re.I)
 	current_page = reg.group(1)
 	all_page = reg.group(2)
	
        # follow links to author pages
        for href  in response.css('a::attr(href)').extract():
	    # <a href=javascript:commitForECMA(callbackC,'content.jsp?tableId=25&tableName=TABLE25&tableView=国产药品&Id=190135',null)></a>
	    foo = re.search( r"&Id=(\d+)\'",href, re.I)
	    mid = foo.group(1)
	    # uri = 'http://app2.sfda.gov.cn/datasearchp/index1.do?tableId=25&tableName=TABLE25&Id=%s'%(str(mid))
	    uri = 'http://app1.sfda.gov.cn/datasearch/face3/content.jsp?tableId=25&tableName=TABLE25&Id=%d&page=%d' %( int(mid), int(current_page))
            yield scrapy.Request( response.urljoin(uri), callback=self.parse_medication)

        # follow pagination links
        #if int(current_page) < int(all_page):
	if int(current_page) < 2 :
            next_page = response.urljoin('http://app1.sfda.gov.cn/datasearch/face3/search.jsp?tableId=25&curstart=%d' %(1+(int(current_page))))
	    yield scrapy.Request( next_page, callback=self.parse)

    def parse_medication(self, response):
	
	def extract_with_xpath(query):
	    foo = response.xpath(u"//td[text()=\'%s\']/following-sibling::td[1]/text()" %(query)).extract_first()
	    if not foo or re.match( r'^-{1,}$',foo,0) :
		return None
	    return foo

	item = MedicationItem()
	
	foo = re.search( r'&Id=(\d+?)&page=(\d+)', response.url, re.I)
	item['page'] = int(foo.group(2))
	item['mid']  = int(foo.group(1))

	# 批准文号
	item_license = extract_with_xpath(u'批准文号')
	if item_license : 
	    item['license'] = item_license
	# 产品名称
	item_product = extract_with_xpath(u'产品名称')
	if item_product :
	    item['product'] = item_product
	# 英文名称
	item_english = extract_with_xpath(u'英文名称')
	if item_english :
	    item['english'] = item_english
	# 商品名
	item_item = extract_with_xpath(u'商品名')
	if item_item :
	    item['item'] = item_item
	# 剂型
	item_form = extract_with_xpath(u'剂型')
	if item_form :
	    item['form'] = item_form
	# 规格
	item_standard = extract_with_xpath(u'规格')
	if item_standard :
	    item['standard'] = item_standard
	# 生产单位
	item_corporation = response.xpath('//td/a[1]/text()').extract_first()
	if item_corporation :
	    item['corporation'] = item_corporation
	# 生产地址
	item_address = extract_with_xpath(u'生产地址')
	if item_address :
	    item['address'] = item_address
	# 产品类别
	item_category = extract_with_xpath(u'产品类别')
	if item_category :
	    item['category'] = item_category
	# 批准日期
	item_date = extract_with_xpath(u'批准日期')
	if item_date :
	    item['date'] = item_date
	# 原批准文号
	item_original = extract_with_xpath(u'原批准文号')
	if item_original :
	    item['original'] = item_original
	# 药品本位码
	item_code = extract_with_xpath(u'药品本位码')
	if item_code :
	    item['code'] = item_code
	# 药品本位码备注
	item_comment = extract_with_xpath(u'药品本位码备注')
	if item_comment :
	    item['comment'] = item_comment
	
	# 当前时间
	item['now'] = datetime.datetime.utcnow()
	
	yield item
	
