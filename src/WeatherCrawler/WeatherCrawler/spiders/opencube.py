# -*- coding: utf-8 -*-
import scrapy
import json
from datetime import datetime,timedelta
from ..items import WeathercrawlerItem

class OpencubeSpider(scrapy.Spider):
    name = 'opencube'
    allowed_domains = ['opencube.tw']
    start_urls = ['https://api.opencube.tw']

    def parse(self, response):
        date = datetime(2019,5,1)
        for i in range(90): 
            print(date.strftime('%Y-%m-%d')) 
            api_url = 'https://api.opencube.tw/weather?date=%s&city=台北市' % date.strftime('%Y-%m-%d')
            yield scrapy.Request(
                    api_url,
                    callback=self.getData
            )
            date += timedelta(days=1)

    def getData(self, response):
        print response.url
        resp = json.loads(response.body_as_unicode())
        data = resp['data']
        raw_data = data['台北市'.decode('utf-8')]
        print raw_data

        date = WeathercrawlerItem()
        date['url'] = response.url
        date['city'] = raw_data['city']
        date['weather'] = raw_data['weather']
        date['maxTemperature'] = raw_data['maxTemperature']
        date['minTemperature'] = raw_data['minTemperature']
        date['notice'] = raw_data['notice']
        date['pop'] = raw_data['pop']
        date['date'] = raw_data['date']
        date['created_datetime'] = datetime.now()
        yield date