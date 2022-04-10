from yandex_homepage import YandexImages
from selenium.webdriver.common.by import By


def test_yandex_images(setup):
    yandex_page = YandexImages(setup)
    yandex_page.go_to_site()
    assert yandex_page.is_present((By.CSS_SELECTOR, '.services-new__icon.services-new__icon_images')), 'no image link'
    yandex_page.go_to_images_page()
    yandex_page.change_window()
    assert yandex_page.get_current_url().startswith("https://yandex.ru/images/"), 'didnt open yandex.ru/images/'
    first_image = yandex_page.get_first_image()
    first_image_text = yandex_page.get_image_text()
    first_image.click()
    link_1 = yandex_page.get_current_url()
    search_text = yandex_page.get_search_text()
    assert first_image_text == search_text, 'image text and search text didnt match'
    first_image_in_category = yandex_page.get_first_image_in_category()
    first_image_in_category.click()
    yandex_page.wait_url_change()
    link_2 = yandex_page.get_current_url()
    assert link_1 != link_2, 'opened same page'
    image = yandex_page.get_image()
    image_source1 = image.get_attribute("src")
    yandex_page.slide_right()
    yandex_page.slide_left()
    image = yandex_page.get_image()
    image_source2 = image.get_attribute("src")
    assert image_source1 == image_source2, 'images didnt match'
