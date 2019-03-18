# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyinfospiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CompanyInfoItem(scrapy.Item):
    # 股票代码
    company_code = scrapy.Field()
    # 公司名称
    company_name = scrapy.Field()
    # 公司网址
    company_web_site = scrapy.Field()
    # 公司所属行业
    company_industry = scrapy.Field()
    # 公司主营业务
    company_main_business = scrapy.Field()
