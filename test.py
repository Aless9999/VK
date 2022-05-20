from bs4 import BeautifulSoup




with open('/home/alessandra/Documents/oksana/file.html') as f:
    html = f.read()




soup = BeautifulSoup(html, 'lxml')
items = soup.find_all(class_="people_row search_row clear_fix")
for item in items:
    try:
        send_url = 'https://vk.com'+item.find('a', class_="friends_field_act").get('href').replace('write', 'id')

        print(send_url)

    except:
        print('')
