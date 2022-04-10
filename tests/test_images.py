from yandex_homepage import YandexImages
from selenium.webdriver.common.by import By


def test_yandex_images(setup):
    yandex_page = YandexImages(setup)
    yandex_page.go_to_site()
    assert yandex_page.is_present((By.CSS_SELECTOR, '.services-new__icon.services-new__icon_images')), 'no element'
    yandex_page.go_to_images_page()
    yandex_page.change_window()
    assert yandex_page.get_current_url().startswith("https://yandex.ru/images/"), 'didnt open yandex.ru/images/'
    first_image = yandex_page.find_element((By.CSS_SELECTOR, '.PopularRequestList-Item_pos_0'))
    first_image_text = yandex_page.find_element((By.CSS_SELECTOR, '.PopularRequestList-Item_pos_0 .PopularRequestList-SearchText')).text
    first_image.click()
    search_text = yandex_page.find_element((By.CSS_SELECTOR, '.input__control.mini-suggest__input')).get_attribute("value")
    assert first_image_text == search_text, 'image text and search text didnt match'
    first_image_in_category = yandex_page.find_element((By.CSS_SELECTOR, '.serp-item__link'))
    first_image_in_category.click()
    image = yandex_page.find_element((By.XPATH, '/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[3]/div/img'))
    image_source1 = image.get_attribute("src")
    right_button = yandex_page.find_element((By.CSS_SELECTOR, '.MediaViewer-ButtonNext'))
    right_button.click()
    left_button = yandex_page.find_element((By.CSS_SELECTOR, '.MediaViewer-ButtonPrev'))
    left_button.click()
    image = yandex_page.find_element((By.XPATH, '/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[3]/div/img'))
    image_source2 = image.get_attribute("src")
    print(image_source1)
    print(image_source2)
    assert image_source1 == image_source2, 'images didnt match'
