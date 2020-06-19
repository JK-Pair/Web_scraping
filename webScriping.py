from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path='chromedriver') #, options=chrome_options
# driver.get('https://www.lazada.co.th/products/fantech-x9-thor-optical-macro-key-rgb-gaming-mouse-dpi-200-4800-mmorpg-bns-fps-moba-9-i154468083-s182005735.html?spm=a2o4m.seller.list.3.5a107b1boI0R7v&mp=1')

driver.get("https://www.lazada.co.th/products/sterile-size-s-i367630136-s718474026.html?spm=a2o4m.home.just4u.16.2e6e719cfFlR4U&scm=1007.17519.162103.0&pvid=2c3353da-d8cb-4633-a6db-827688b3a4e5&clickTrackInfo=tcExpIds%3A245%3Btcsceneid%3AHPJFY%3Bbuyernid%3A1fc1acee-a4f6-4f85-f91c-1fab511447c1%3Btcbid%3A5%3Btcboost%3A0%3Bpvid%3A2c3353da-d8cb-4633-a6db-827688b3a4e5%3Bchannel_id%3A0000%3Bmt%3Ai2i%3Bitem_id%3A367630136%3Bself_ab_id%3A162103%3Bself_app_id%3A7519%3Blayer_buckets%3A955.3629%3B")

timeout = 30
try:
    category_product = driver.find_element(By.XPATH,'//*[@id="J_breadcrumb_list"]/ul')
    product_title = category_product.find_elements(By.CLASS_NAME,"breadcrumb_item")[-2].text
    print("title: ", product_title)

    category_price = driver.find_element(By.ID,'module_product_price_1').text
    product_price = category_price.strip('฿').splitlines()[0]
    print(product_price)

    try:
        
        category_image_path = driver.find_element(By.XPATH,'//*[@id="module_item_gallery_1"]/div/div[@class="next-slick next-slick-outer next-slick-horizontal"]/div/div/div/div[@class="next-slick-slide next-slick-active item-gallery__thumbnail"]/div/img')

# next-slick-slide next-slick-active item-gallery__thumbnail item-gallery__thumbnail_state_active

    except:
        category_image_path = driver.find_element(By.XPATH,'//*[@id="module_item_gallery_1"]/div/div/div/img')

    image_path = category_image_path.get_attribute("src")
    print(image_path)

    # data = {'product_title': product_title, 'product_price': product_price, 'product_link' : image_path}

    driver.quit()
except TimeoutException:
    driver.quit()