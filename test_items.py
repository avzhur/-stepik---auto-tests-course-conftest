import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_visible(browser):
    browser.get(link)
    time.sleep(30)
    try:
        button = browser.find_element_by_css_selector("button.btn-add-to-basket")
        b = True
    except:
        b = False
    assert b, 'Кнопки нет!'