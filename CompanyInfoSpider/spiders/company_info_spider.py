import scrapy
import xlrd
from lxml import etree

from scrapy.http import Request

from CompanyInfoSpider.items import CompanyInfoItem


class CompanyInfoSpider(scrapy.Spider):
    name = "companyspider"
    allowed_domains = ["s.askci.com"]
    bash_url = "http://s.askci.com/stock/summary/"
    bash_url_suffix = "/"
    table = xlrd.open_workbook("F://毕业论文资料//股票代码.xlsx").sheet_by_index(0)
    company_code_list = []
    for i in range(table.nrows):
        company_code_list.append(table.cell(i, 0).value)

    def start_requests(self):
        for company_code in self.company_code_list:
            url = self.bash_url + company_code + self.bash_url_suffix
            yield Request(url, callback=self.parse)

    def parse(self, response):
        tree = etree.HTML(response.text)
        company_name = tree.xpath("/html/body/div[2]/div[3]/div[2]/div[2]/table/tr[1]/td[2]/text()")
        company_web_site = tree.xpath("/html/body/div[2]/div[3]/div[2]/div[2]/table/tr[6]/td[2]/a/@href")
        company_main_business = tree.xpath("/html/body/div[2]/div[3]/div[2]/div[2]//table/tr[7]/td[2]/text()")
        company_industry = tree.xpath(
            "/html/body/div[2]/div[3]/div[2]/div[2]/table/tr[5]/td[2]/a[1]/text()") + tree.xpath(
            "/html/body/div[2]/div[3]/div[2]/div[2]/table/tr[5]/td[2]/a[2]/text()")
        item = CompanyInfoItem()
        url_array = response.url.split("/")
        item['company_code'] = str(url_array[len(url_array) - 2])
        item['company_name'] = (company_name, "")[company_name is None]
        item['company_web_site'] = (company_web_site, "")[company_web_site is None]
        item['company_industry'] = (company_industry, "")[company_industry is None]
        item['company_main_business'] = (company_main_business, "")[company_main_business is None]
        yield item
