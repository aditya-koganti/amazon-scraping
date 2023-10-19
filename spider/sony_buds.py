# -*- coding: utf-8 -*-
import scrapy
import logging
class SonyBudsSpider(scrapy.Spider):
    name = 'sony_buds'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/s?k=sony+wf-1000xm4']
   
    # Global Variables
    
    def parse(self, response):
        item_names = []
        item_prices = []
        item_links = []
        # 2
        item_blocks = response.xpath("//text()[contains(., 'Results')]/following::div[@data-index]//text()[contains(., 'WF-1000XM4')]/ancestor-or-self::div[5]")
        
        for item in item_blocks:
            item_name = item.xpath(".//text()[contains(., 'Sony')]").get()
            item_names.append(item_name)
            item_price = item.xpath('.//descendant::span[@class="a-offscreen"][1]//text()').get()
            item_prices.append(item_price)
            item_link = item.xpath(".//text()[contains(., 'Sony')]/ancestor-or-self::a[1]/@href").get()
            item_links.append(item_link)
            
            absolute_url = f"https://www.amazon.com{item_link}"
            yield scrapy.Request(url=absolute_url, callback=self.parse_item, meta={'item_name': item_name, 'item_price': item_price})
            
        next_page = response.xpath('//*[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]/@href').get()
        full_url = f"https://www.amazon.com{next_page}"
        
        if next_page:
            yield scrapy.Request(url=full_url, callback=self.parse)
        
       
    def parse_item(self, response):
       item_name = response.request.meta['item_name']
       item_price = response.request.meta['item_price']
       review_data = [item_name, {'Price': item_price}]
       reviews = response.xpath('//*[@data-hook="review"]')

       for review in reviews:
           commented_names_text = review.xpath('(.//descendant::*[@class="a-profile-name"]//text())[1]').get()           
           commented_rating = review.xpath('(.//descendant::*[contains(@class, "a-icon a-icon-star")]//text())[1]').get()

           review_data.append({
               'commented name': commented_names_text,
               'commented rating': commented_rating
           })                                                                                 
    #    print("\n------------------")
    #    print("\n Reviews Data: ", review_data)
       
       yield{
           'review_data': review_data
       }