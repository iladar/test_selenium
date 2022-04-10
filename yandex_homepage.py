from selenium.webdriver.common.keys import Keys
from BaseApp import BasePage
from selenium.webdriver.common.by import By


class YandexSearch(BasePage):

    def enter_word(self, word):
        search_field = self.find_element((By.ID, 'text'))
        search_field.click()
        search_field.send_keys(word)

    def start_search(self):
        search_field = self.find_element((By.ID, 'text'))
        search_field.send_keys(Keys.RETURN)

    def find_search_links(self):
        links = self.find_elements((By.CSS_SELECTOR, '#search-result li .OrganicTitle a'))[:5]
        return links


class YandexImages(BasePage):

    def go_to_images_page(self):
        images_icon = self.find_element((By.CSS_SELECTOR, '.services-new__icon.services-new__icon_images'))
        images_icon.click()

    def change_window(self):
        self.go_to_chosen_window(1)

    def get_first_image(self):
        return self.find_element((By.CSS_SELECTOR, '.PopularRequestList-Item_pos_0'))

    def get_image_text(self):
        return self.find_element((By.CSS_SELECTOR, '.PopularRequestList-Item_pos_0 .PopularRequestList-SearchText')).text

    def get_search_text(self):
        return self.find_element((By.CSS_SELECTOR, '.input__control.mini-suggest__input')).get_attribute("value")

    def get_first_image_in_category(self):
        return self.find_element((By.CSS_SELECTOR, '.serp-item__link'))

    def get_image(self):
        return self.find_element((By.CSS_SELECTOR, 'img.MMImage-Origin'))

    def slide_right(self):
        right_button = self.find_element((By.CSS_SELECTOR, '.MediaViewer-ButtonNext'))
        right_button.click()

    def slide_left(self):
        left_button = self.find_element((By.CSS_SELECTOR, '.MediaViewer-ButtonPrev'))
        left_button.click()








