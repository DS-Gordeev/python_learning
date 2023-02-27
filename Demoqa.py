from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime as dt


options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# Можно использовать не опцию, а встроенный в Selenium метод maximize_window(), нужно убрать options=options
# driver.maximize_window()

driver.get('https://dzen.ru')

# Удаленный запуск
#def remote_start():
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--remote-debugging-port=9222')
#chrome_options.add_argument("--disable-dev-shm-usage")
#chrome_options.add_argument('--user-data-dir=/home/dsgordeev/for_driver')

#chrome_options.set_capability("browserName", "chrome")
#chrome_options.set_capability("browserVersion", "106")
#chrome_options.set_capability("platformName", "LINUX")
#river = webdriver.Remote(command_executor='http://158.160.15.157:4444/wd/hub', options=chrome_options)
#driver.get('https://ya.ru')
#print('Тест выполнен!!!')
#print('Браузер закрыт!!!')
#quit()

# Text Box
def text_box():
    text_box_url = 'https://demoqa.com/text-box'
    user_data = {'user_name': 'Marazmator',
            'user_email': 'test@mail.ru',
            'current_adress': 'Moscow',
            'permanent_adress': 'Sherbakovskaya street, 32/7, app. 10'}
    time.sleep(2)

    # Переходим в раздел Elements
    driver.find_element(By.CSS_SELECTOR, 'div.card.mt-4.top-card').click() # Переходим в раздел Elements

    # Выбираем подраздел Text Box
    driver.find_element(By.XPATH, '//li[@id="item-0"]/span[contains(., "Text Box")]').click()

    # Проверяем, что мы в разделе Text Box
    assert driver.current_url == text_box_url, 'Current URL id wrong'

    driver.find_element(By.ID, 'userName').send_keys(user_data['user_name'])
    driver.find_element(By.ID, 'userEmail').send_keys(user_data['user_email'])
    driver.find_element(By.ID, 'currentAddress').send_keys(user_data['current_adress'])
    driver.find_element(By.ID, 'permanentAddress').send_keys(user_data['permanent_adress'])
    driver.find_element(By.CSS_SELECTOR, 'button#submit').click()

    assert user_data['user_name'] in driver.find_element(By.CSS_SELECTOR, 'div#output p#name').text, 'Wrong username output'
    assert user_data['user_email'] in driver.find_element(By.CSS_SELECTOR, 'div#output p#email').text, 'Wrong email output'
    assert user_data['current_adress'] in driver.find_element(By.CSS_SELECTOR, 'div#output p#currentAddress').text, 'Wrong currentAddress output'
    assert user_data['permanent_adress'] in driver.find_element(By.CSS_SELECTOR, 'div#output p#permanentAddress').text, 'Wrong permanentAddress output'
    driver.quit()

# Обновляем страницу, gеремещение вперед-назад в истории браузера
def refresh_and_back_forward():
    driver.refresh()
    driver.back()
    driver.forward()

# Нажатиея на клавишу BACKSPACE для очистки поля ввода
def keys_module():
    driver.find_element(By.ID, 'userName').send_keys(Keys.BACKSPACE * 10)

# Очистка поля методом clear()
def clear_input():
    driver.find_element(By.ID, 'userName').clear()

# Прокрутка окна браузера вниз на указанное кол-во пикселей
def scroll_down_javascript():
    driver.execute_script("window.scrollTo(0, 500)")

# Прокрутка окна браузера до определенного элемента ActionChains
def scroll_to_elem():
    action = ActionChains(driver)
    elem = driver.find_element(By.CSS_SELECTOR, 'div.element-group:nth-child(5) span.group-header div.header-wrapper')
    action.scroll_to_element(elem).perform()
    driver.quit()

# Делаем скриншот экрана
def do_screenshot():
    date_format = dt.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    driver.save_screenshot(f'./screenshots/text_box_screenshot {date_format}.png')

# Check Box (проверка, что чекбокс активен)
def check_box():
    driver.find_element(By.XPATH, '//li[@id="item-1"]/span[contains(., "Check Box")]').click()
    driver.find_element(By.CSS_SELECTOR, 'button[title="Expand all"]').click()
    driver.find_element(By.CSS_SELECTOR, 'button[title="Collapse all"]').click()
    driver.find_element(By.CSS_SELECTOR, 'ol li button:first-child').click()

    # Проверка, что checkbox нажат или нет (обращение именно к input)
    status_checkbox = driver.find_element(By.CSS_SELECTOR, 'input#tree-node-desktop').is_selected()
    print(status_checkbox) # не нажат - False
    driver.find_element(By.CSS_SELECTOR, 'input#tree-node-desktop + span.rct-checkbox').click()
    status_checkbox = driver.find_element(By.CSS_SELECTOR, 'input#tree-node-desktop').is_selected()
    print(status_checkbox) # нажат - True
    driver.quit()

# Radio Button (проверка, что радиобаттон активен)
def radio_button():
    driver.find_element(By.XPATH, '//li[@id="item-2"]/span[contains(., "Radio Button")]').click()

    # Проверка, что radio button нажата или нет (обращение именно к input)
    status_radio = driver.find_element(By.CSS_SELECTOR, 'input#yesRadio').is_selected()
    print(status_radio) # не нажат - False
    driver.find_element(By.CSS_SELECTOR, 'label[for="yesRadio"]').click()
    status_radio = driver.find_element(By.CSS_SELECTOR, 'input#yesRadio').is_selected()
    print(status_radio) # не нажат - False
    driver.quit()

# Buttons (двойной клик, клик правой кнопкой мыши)
def buttons():
    driver.find_element(By.XPATH, '//li[@id="item-4"]/span[contains(., "Buttons")]').click()

    action = ActionChains(driver)
    double_click_button = driver.find_element(By.ID, 'doubleClickBtn')
    right_click_button = driver.find_element(By.ID, 'rightClickBtn')
    time.sleep(0.5)
    action.double_click(double_click_button).scroll_from_origin.context_click(right_click_button).perform()
    driver.quit()

# Slider (перетаскивание бегунка)
def slider():
    driver.execute_script("window.scrollTo(0, 1000)")
    driver.find_element(By.CSS_SELECTOR, 'div.accordion div.element-group:nth-child(4) span div').click() # Переходим в раздел Widgets
    time.sleep(1)
    driver.find_element(By.XPATH, '//li[@id="item-3"]/span[contains(., "Slider")]').click()

    element = driver.find_element(By.CSS_SELECTOR, 'div#sliderContainer input')
    action = ActionChains(driver)
    action.click_and_hold(element).move_by_offset(500, 0).release().perform()
    driver.quit()

# Implicit waiting (Неявное ожидание)
def waiting_implicitly_wait():
    driver.implicitly_wait(20) # Неявное ожидание 20 секунд
    driver.get('https://demoqa.com/dynamic-properties')
    driver.find_element(By.ID, 'visibleAfter')
    driver.quit()

def waiting():
    driver.implicitly_wait(20) # Явное ожидание до момента появления элемента в DOM
    driver.get('https://demoqa.com/dynamic-properties')
    WebDriverWait(driver, timeout=20).until(lambda x: x.find_element(By.ID, "visibleAfter").is_displayed()) # Явное ожидание с указанием лямбда-функции
    WebDriverWait(driver, 10).until(EC.staleness_of(message))  # Явное ожидание когда объект исчезнет из DOM (c использованием класса expected_conditions)
    driver.find_element(By.ID, 'visibleAfter').click()
    driver.quit()

# Сохраняем текст всей страницы
def current_page_source():
    page = driver.page_source
    print(page)
    driver.quit()

# Работа с вкладками в браузере (открытие новых, переключение между, закрытие, получения списка всех открытых вкладок)
def work_with_browser_handles():
    original_window = driver.current_window_handle # сохраняем "id" текущей вкладки браузера (потом можем на нее переключаться)
    driver.switch_to.new_window('tab') # открываем новую вкладку в браузере и сразу переключаемся на нее
    driver.get('http://ya.ru')
    driver.close()
    driver.switch_to.window(original_window)
    driver.switch_to.new_window('tab')
    driver.get('http://rambler.ru')
    driver.close()
    driver.switch_to.window(original_window)
    all_handles = driver.window_handles  # возвращает List всех открытых вкладок, для доступа используем, например, all_handles[0]
    print(all_handles)
    driver.quit()

# Загрузка файла для формы input с type="file"
def upload_file():
    driver.get('https://demoqa.com/upload-download')
    file_to_upload = 'C:\\AutoTests_home\\autotests_python\\Screenshot_1.jpg'
    driver.find_element(By.ID, 'uploadFile').send_keys(file_to_upload)
    success_text = driver.find_element(By.ID, 'uploadedFilePath').text
    assert success_text == 'C:\\fakepath\\Screenshot_1.jpg', 'Файл не был загружен'
    driver.quit()

# Проверяем цвет текста кнопки
def work_with_color():
    driver.get('https://demoqa.com/dynamic-properties')
    WebDriverWait(driver, timeout=20).until(EC.visibility_of_element_located((By.ID, 'visibleAfter')))
    object = driver.find_element(By.ID, 'colorChange')
    color_button = Color.from_string(object.value_of_css_property('color')).hex # получаем цвет объекта и конвертируем в HEX
    print(color_button)
    assert color_button == '#dc3545', 'Неправильный цвет кнопки'
    driver.quit()

# Изменяем значение атрибута у элемента в DOM
def change_attribute():
    # Устанавливаем новое значение
    object = driver.find_element(By.ID, 'ID')
    driver.execute_script("arguments[0].setAttribute('attribute_name','new_attribute_value');", object)
    # Проверяем, что значение изменилось
    object_attribute = object.get_attribute("attribute_name")
    print(object_attribute)


elems = driver.find_elements(By.CSS_SELECTOR, 'div[class="card-news__tabPane-3_ card-news__active-2u"] li[class="news-story__story-2M"]')
print(len(elems))
for i in elems:
    print(i.find_element(By.XPATH, './a').get_attribute('href'))
