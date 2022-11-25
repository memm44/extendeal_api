from app.scrappers.bot_handler.bot_controller import BotController


class HomeDisco:
    def __init__(self):
        self.driver = None
        self.bot = None
        self.url = "https://www.disco.com.ar/electro/informatica?page=1"
        self.xpath_names = '//div[contains(@class,"vtex-product-summary-2-x-productBrandContainer")]'
        self.xpath_descriptions = '//h2[contains(@class,"vtex-product-summary-2-x-productNameContainer")]/span'
        self.xpath_prices = '//div[contains(@class,"contenedor-precio")]'
        self.show_more_btn_xpath = '//div[contains(@class,"vtex-search-result-3-x-buttonShowMore")]/button'

    def __load_items_from_page(self, driver, page_number=1):
        self.bot = BotController(your_driver=driver)
        self.bot.get_page(self.url, delay_after=2)
        if page_number > 1:
            for times in range(page_number):
                self.click_show_more()
        self.scroll_botton_page()
        final_dict = {"records": [{"marca": e[0], "descripcion": e[1], "precio": self.__clean_price(e[2])} for e in
                                  list(zip(self.get_name_from_items(), self.get_description_from_items(),
                                           self.get_all_prices_from_items()))]}
        return final_dict

    @staticmethod
    def __clean_price(price):
        return price.strip("$")

    def get_name_from_items(self):
        all_name_elements = self.bot.find_elements_xpath(
            xpath_exp=self.xpath_names)
        return [e.text for e in all_name_elements]

    def get_description_from_items(self):
        all_descriptions = self.bot.find_elements_xpath(xpath_exp=self.xpath_descriptions)
        return [e.text for e in all_descriptions]

    def get_all_prices_from_items(self):
        all_prices = self.bot.find_elements_xpath(xpath_exp=self.xpath_prices)
        return [p.text for p in all_prices]

    def click_show_more(self):
        elem = self.bot.find_element_xpath(self.show_more_btn_xpath)
        self.bot.js_click(elem, delay_after_click=1)

    def get_items_from_pages(self, page_number, driver):
        return self.__load_items_from_page(driver=driver, page_number=page_number)

    def scroll_botton_page(self):
        self.bot.execute_javascript(script='window.scrollTo(0, document.body.scrollHeight);', delay_after=1)


if __name__ == '__main__':
    pass
