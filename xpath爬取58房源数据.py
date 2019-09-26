import requests
from lxml import html
etree = html.etree

url = 'https://bj.58.com/ershoufang/?sort=huansuanyue_asc&sort_hack=1'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3'
                 '729.169 Safari/537.36'

}
response = requests.get(url=url,headers=headers)
page_text = response.text

#数据解析
tree = etree.HTML(page_text)
house_list = tree.xpath('//ul[@class="house-list-wrap"]/li/div[@class="list-info"]/h2/a/text()')
f = open('58.txt', 'w', encoding='utf-8')
for house in house_list:
    f.write(house)
