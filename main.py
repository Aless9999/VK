import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json



#авторизация
#url = 'https://oauth.vk.com/authorize?client_id=-1&redirect_uri=https%3A%2F%2Fvk.com%2Fshare.php%3Furl%3Dhttps%253A%252F%252Fddbnews.wordpress.com%252F2017%252F10%252F03%252Fwichtige-botschaft-an-die-deutschen%252F&display=widget'
#женщины новой усмани
#url = 'https://vk.com/friends?act=find&c%5Bage_from%5D=20&c%5Bage_to%5D=45&c%5Bcity%5D=8239&c%5Bcountry%5D=1&c%5Bname%5D=1&c%5Bper_page%5D=40&c%5Bphoto%5D=1&c%5Bsection%5D=people&c%5Bsex%5D=1'


def writer_json(data):
    with open('/home/alessandra/Documents/oksana/file1.json', 'a') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def writer_csv(data):
     with open("/home/alessandra/Documents/oksana/id_people1.csv", 'a') as f:
         order = ['name', 'id']
         writer = csv.DictWriter(f, fieldnames = order)
         writer.writerow(data)

def get_data(html):
    data = {}
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all(class_="people_row search_row clear_fix")
    for item in items:
        id = item.find('div', class_="img").find('a').get('href').replace('id', '').strip('/')
        name = item.find('div' , class_="labeled name").find('a').text
        data = {'id':id,
                 'name':name}

        writer_json(data)
        writer_csv(data)







def get_html(url):
    data ={}
    browser = webdriver.Firefox(executable_path = '/home/alessandra/Documents/Selenium/geckodriver')
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36")
    browser.get(url)

    try:
        id_name = browser.find_element_by_name("email")
        id_name.send_keys('89507636551')
        time.sleep(5)
        id_password = browser.find_element_by_name('pass')
        id_password.send_keys('id7931822')
        time.sleep(5)
        id_password.send_keys(Keys.ENTER)
        time.sleep(10)
        browser.get('https://vk.com/friends?act=find&c%5Bage_from%5D=20&c%5Bage_to%5D=45&c%5Bcity%5D=8239&c%5Bcountry%5D=1&c%5Bname%5D=1&c%5Bper_page%5D=40&c%5Bphoto%5D=1&c%5Bsection%5D=people&c%5Bsex%5D=1')
        for i in range(15):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")#перемещение вниз страницы
            time.sleep(1)
        time.sleep(5)
         #крутить вниз до упора)))!
        html = browser.page_source
        get_data(html)









            # Блок рассылки
            # try:
            #     send_url = 'https://vk.com'+item.find('a', class_="friends_field_act").get('href').replace('write', 'id')
            #     browser.get(send_url)
            #     time.sleep(5)
            #     write_send = browser.find_element_by_css_selector('.profile_btn_cut_left')
            #     write_send.send_keys(Keys.ENTER)
            #     time.sleep(10)
            #     new_mail = browser.find_element_by_id('mail_box_editable')
            #     new_mail.send_keys('')
            #     time.sleep(10)
            #     send = browser.find_element_by_id("mail_box_send")
            #     send.send_keys(Keys.ENTER)
            #     # with open('/home/alessandra/Documents/oksana/file1.html', 'w') as f:
            #     #     f.write(browser.page_source)
            #     time.sleep(10)
            #
            #
            # except:
            #     print('uuups!')
            #
        # try:
        #
        #
        # except:
        #     url=''





        browser.close()
        browser.quit()
        #browser.get('')


    except:
        print(ex)

# def get_data():
#
#
#
#         print(url)




def main():
    url = 'https://oauth.vk.com/authorize?client_id=-1&redirect_uri=https%3A%2F%2Fvk.com%2Fshare.php%3Furl%3Dhttps%253A%252F%252Fddbnews.wordpress.com%252F2017%252F10%252F03%252Fwichtige-botschaft-an-die-deutschen%252F&display=widget'
    get_html(url)







if __name__ == '__main__':
    main()
