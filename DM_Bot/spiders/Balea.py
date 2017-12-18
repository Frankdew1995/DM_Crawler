# -*- coding: utf-8 -*-
import scrapy
import json
from DM_Bot.items import DmBotItem


class DmspiderSpider(scrapy.Spider):
    name = 'Balea'
    allowed_domains = ['dm.de']
    # headers = {
    #     'Accept': 'application/json, text/plain, */*'
    # }
    page = 1
    api_url = "https://services.dm.de/websearch/search/pues?type=product&tenant=de_mcr&q=balea&categoryId=&pageSize=48&sort=relevance&cp={}&productQuery=&initialProductQuery=&hiddenFacets="
    start_urls = [api_url.format(page)]

    def parse(self, response):
        data = json.loads(response.text)
        item = DmBotItem()
        for product in data['serviceProducts']:
            item['name'] = product['name']
            item['EAN'] = product['gtin']
            item['IMG'] = product['links'][0]['href']
            item['Price'] = product['priceLocalized']
            yield item
            api_url = "https://services.dm.de/websearch/search/pues?type=product&tenant=de_mcr&q=balea&categoryId=&pageSize=48&sort=relevance&cp={}&productQuery=&initialProductQuery=&hiddenFacets="

        for i in range(2,13):
            next_page = i
            next_url = api_url.format(next_page)
            yield scrapy.Request(url = next_url, callback = self.parse)
            # if len(data['serviceProducts']) == 48 :
            #     page = 1
            #     next_url = api_url.format(page + 1)
            #     yield scrapy.Request(url = next_url, callback = self.parse)
