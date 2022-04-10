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
    i = 1
    links = yandex_page.find_search_links()
    for link in links:
        url = yandex_page.get_link_url(link)
        assert url.find('tensor.ru') > 0, f'link to another site in {i} position - {url}'
        i = i + 1

