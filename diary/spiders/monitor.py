# -*- coding: utf-8 -*-
import scrapy
from diary.items import DiaryItem
import urllib

class MonitorSpider(scrapy.Spider):
    csvPath = 'https://s3.amazonaws.com/shichaoji/diaryID.csv'

    name = 'monitor'
    allowed_domains = ['www.soyoung.com']
    link = 'http://www.soyoung.com/dpg'
    start_urls=[]

    opener = urllib.URLopener()
    fh = opener.open(csvPath)
    for line in fh.readlines():
        start_urls.append(link + line.strip())
    start_urls=start_urls[1:]
    
    #df = pd.read_csv(csvPath)
    #for l in df['group_id'].tolist():
        #start_urls.append(link+str(l))    
    

    print 'starting: ', len(start_urls), 'first: ', start_urls[0]

    def parse(self, response):
        
        dinfo = response.css('div.diary-info a')
        try:
            user=dinfo[1]
            hos=dinfo[2]
            doc=dinfo[3]
            prod=dinfo[4]
            img1=dinfo[5]
            img2=dinfo[6]
            img3=dinfo[7]
        except Exception as e:
            print e

        for i in response.css('div.diary-list > ul > li.diary-item'):
            item= DiaryItem()

            try:
                item['diary_link']= response.url
                item['user_name'] = user.css('::text').extract()[0].strip()
                item['user_link'] = user.css('::attr(href)').extract()[0].strip()
                item['hospital'] = hos.css('::text').extract()[0].strip()
                item['hospital_link'] = hos.css('::attr(href)').extract()[0].strip()    
                item['doctor_name'] = doc.css('::text').extract()[0].strip()
                item['doctor_link'] = doc.css('::attr(href)').extract()[0].strip()
                item['product_name'] = prod.css('::text').extract()[0].strip()
                item['product_link'] = prod.css('::attr(href)').extract()[0].strip()
                item['pre_surg_pic1'] = img1.css('::attr(href)').extract()[0].strip()    
                item['pre_surg_pic2'] = img2.css('::attr(href)').extract()[0].strip()    
                item['pre_surg_pic3'] = img3.css('::attr(href)').extract()[0].strip()    

            except Exception as e:
                print e    



            item['post_title'] = i.css('span.day::text').extract()[0]
            item['post_link'] = i.css('p.describe > a::attr(href)').extract()[0]
            item['post_text'] = i.css('p.describe > a::text').extract()[0]

            n=0
            for p in i.css('ul.photo-list > li > a > img::attr(data-img)').extract():
                n+=1
                item['post_image'+str(n)] = p
            tp='photo-diary'

            vid = i.css('div.video-poster > a > img::attr(data-img)').extract()
            if len(vid)>0:
                tp='video-diary'
                item['video_image'] = vid[0]

            item['post_type'] = tp

            coll = i.css('div.other-box a::text').extract()
            item['views']= coll[0]
            item['comments']= coll[1]
            item['favor']= coll[2]

