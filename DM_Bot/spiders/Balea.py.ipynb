{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# -*- coding: utf-8 -*-\n",
    "import scrapy\n",
    "import json\n",
    "from DM_Bot.items import DmBotItem\n",
    "\n",
    "\n",
    "class DmspiderSpider(scrapy.Spider):\n",
    "    name = 'Balea'\n",
    "    allowed_domains = ['dm.de']\n",
    "    # headers = {\n",
    "    #     'Accept': 'application/json, text/plain, */*'\n",
    "    # }\n",
    "    page = 1\n",
    "    api_url = \"https://services.dm.de/websearch/search/pues?type=product&tenant=de_mcr&q=balea&categoryId=&pageSize=48&sort=relevance&cp={}&productQuery=&initialProductQuery=&hiddenFacets=\"\n",
    "    start_urls = [api_url.format(page)]\n",
    "\n",
    "    def parse(self, response):\n",
    "        data = json.loads(response.text)\n",
    "        item = DmBotItem()\n",
    "        for product in data['serviceProducts']:\n",
    "            item['name'] = product['name']\n",
    "            item['EAN'] = product['gtin']\n",
    "            item['IMG'] = product['links'][0]['href']\n",
    "            item['Price'] = product['priceLocalized']\n",
    "            yield item\n",
    "            api_url = \"https://services.dm.de/websearch/search/pues?type=product&tenant=de_mcr&q=balea&categoryId=&pageSize=48&sort=relevance&cp={}&productQuery=&initialProductQuery=&hiddenFacets=\"\n",
    "\n",
    "        for i in range(2,13):\n",
    "            next_page = i\n",
    "            next_url = api_url.format(next_page)\n",
    "            yield scrapy.Request(url = next_url, callback = self.parse)\n",
    "            # if len(data['serviceProducts']) == 48 :\n",
    "            #     page = 1\n",
    "            #     next_url = api_url.format(page + 1)\n",
    "            #     yield scrapy.Request(url = next_url, callback = self.parse)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
