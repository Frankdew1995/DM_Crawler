# -*- coding: utf-8 -*-
from DM_Bot.items import DmBotItem
import scrapy
import json
# from scrapy_splash import SplashRequest



class DmspiderSpider(scrapy.Spider):
    name = 'DasGesundePlus'
    allowed_domains = ['dm.de']
    # headers = {
    #     'Accept': 'application/json, text/plain, */*'
    # }
    page = 1
    api_url = "https://services.dm.de/websearch/search/pues?type=product&tenant=de_mcr&q=das%20gesunde%20plus&categoryId=&pageSize=48&sort=relevance&cp={}&productQuery=&initialProductQuery=&hiddenFacets="
    start_urls = [api_url.format(page)]

    # def start_requests(self):
    #
    #     yield SplashRequest( url = 'https://www.dm.de/search/468652.html?type=product&tenant=de_mcr&targetSystem=live&q=alverde&categoryId=&pageSize=48&sort=relevance&cp=1&productQuery=&hiddenFacets=',
    #                          callback = self.parse,)

    def parse(self, response):
        data = json.loads(response.text)
        item = DmBotItem()
        for product in data['serviceProducts']:
            item['name'] = product['name']
            item['EAN'] = product['gtin']
            item['IMG'] = product['links'][0]['href']
            item['Price'] = product['priceLocalized']
            yield item
        api_url = "https://services.dm.de/websearch/search/pues?type=product&tenant=de_mcr&q=das%20gesunde%20plus&categoryId=&pageSize=48&sort=relevance&cp={}&productQuery=&initialProductQuery=&hiddenFacets="
        # pos = 1
        # base_list_url = "https://www.dm.de/search/468652.html?type=product&tenant=de_mcr&targetSystem=live&q=alverde&categoryId=&pageSize=48&sort=relevance&cp={}&productQuery=&hiddenFacets="
        # next_list_url = base_list_url.format(pos + 1)
        # if next_list_url:
        #     next_api_url = api_url.format(pos + 1)
        #     yield scrapy.Request(url=next_api_url, callback=self.parse)


        for i in range(2,7):
            next_page = i
            next_url = api_url.format(next_page)
            yield scrapy.Request(url = next_url, callback = self.parse)
