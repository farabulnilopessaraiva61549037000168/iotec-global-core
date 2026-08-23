import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import scrapy

class OportunidadesSpider(scrapy.Spider):
    name = "oportunidades"
    start_urls = [
        "https://seusite.com"
    ]

    def parse(self, response):
        text = response.text  # Usa o `response.text` para garantir que Scrapy lida com encoding interno

        for oportunidade in response.xpath("//div"):
            yield {
                "titulo": oportunidade.xpath(".//h2/text()").get(default="TÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tulo nÃƒÆ'Ã†â€™o encontrado"),
                "link": oportunidade.xpath(".//a/@href").get(default="Link nÃƒÆ'Ã†â€™o disponÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel"),
                "data_limite": oportunidade.xpath(".//span[@class='data']/text()").get(default="Data nÃƒÆ'Ã†â€™o especificada"),
                "categoria": oportunidade.xpath(".//span[@class='categoria']/text()").get(default="Categoria nÃƒÆ'Ã†â€™o identificada"),
            }


