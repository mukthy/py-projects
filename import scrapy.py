import scrapy


class TestSpider(scrapy.Spider):
      name = 'test'

    def start_requests(self):

           yield scrapy.Request(url="http://books.toscrape.com/", callback=self.parse,
                                 meta={
                                     "zyte_api": {
                                         "browserHtml": True,
                                         # You can set any GEOLocation region you want.
                                         "geolocation": "US",
                                         "javascript": True,
                                         "echoData": {"something": True}
                                     }
                                 })

        def parse(self, response):
            yield{
                'URL': response.url,
                'status': response.status,
                'HTML': response.body
            }
