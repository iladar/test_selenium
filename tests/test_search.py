from yandex_homepage import YandexSearch
from selenium.webdriver.common.by import By


def test_yandex_search(setup):
    yandex_page = YandexSearch(setup)
    yandex_page.go_to_site()
    assert (yandex_page.is_present((By.ID, 'text'))), 'couldnt find search box'
    yandex_page.enter_word('Тензор')
    assert (yandex_page.is_present((By.CSS_SELECTOR, '.mini-suggest__popup-content'))), 'didnt find suggest block'
    yandex_page.start_search()
    assert (yandex_page.is_present((By.ID, 'search-result'))), 'no search results'
    links = yandex_page.find_search_links()
    link_finded = False
    for link in links:
        url = yandex_page.get_link_url(link)
        if url.find('tensor.ru') > 0:
            link_finded=True
    assert link_finded, 'links not finded'


