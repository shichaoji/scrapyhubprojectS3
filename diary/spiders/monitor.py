# -*- coding: utf-8 -*-
import scrapy
from diary.items import DiaryItem

class MonitorSpider(scrapy.Spider):
    name = 'monitor'
    allowed_domains = ['www.soyoung.com']
    link = 'http://www.soyoung.com/dpg'
    start_urls=[]
    with open('/home/shj16110/notebook/download_soyoung/did17_7.csv','r') as fh:
	for line in fh.readlines():
		start_urls.append(link + line.strip())
    print 'starting: ', len(start_urls), 'first: ', start_urls[0]

    def parse(self, response):
	
	for i in response.css('li.diary-item'):
		item= DiaryItem()
		item['dlink']= response.url
        	item['title']= i.css('span.day::text').extract()[0]
         	item['plink']= i.css('p.describe a::attr(href)').extract()[0]
         	item['time']= i.css('div.date::text').extract()[0]
         	coll = i.css('div.other-box a::text').extract()
		item['views']= coll[0]
		item['comments']= coll[1]
		item['favor']= coll[2]
	yield item
