import scrapy
#from scrapy.http import Request, FormRequest

class IntrospiderSpider(scrapy.Spider):
    name = "introspider"
    allowed_domains = ["tesco.com"]
    start_urls = ["https://www.tesco.com/groceries/en-GB/search?query=nutella"] ###you can change the product name Like 'nutella' to 'bread' 


    def parse(self, response):
        products = response.css("div.styles__StyledVerticalTileWrapper-dvv1wj-0.dtCNPH")

        for product in products:
            yield{
                'Product_name' : product.css("h3.styles__H3-oa5soe-0.gbIAbl span.styled__Text-sc-1i711qa-1.xZAYu.ddsweb-link__text::text").get(),
                'prduct_price' : product.css("div.base-components__RootElement-sc-1mosoyj-1.styled__Container-sc-8qlq5b-0.jptQqM.bgZrjw.styled__StyledPrice-sc-6nhkzi-5.iYHeik.beans-buybox__price.beans-price__container p.styled__StyledHeading-sc-119w3hf-2.jWPEtj.styled__Text-sc-8qlq5b-1.lnaeiZ.beans-price__text::text").get(),
                'product_link' : product.css("h3 a").attrib['href']

            }
        next_page = response.css("li.pagination-btn-holder a::attr(href)").get()
        if next_page is not None:
            next_page_url = 'https://www.tesco.com' + next_page
            yield response.follow(next_page_url, callback = self.parse, headers={'cookie': COOKIES, 'user-agent': USER_AGENT})