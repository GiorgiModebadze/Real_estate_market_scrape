from datetime import datetime
import pandas as pd
from helper_funcs import getHTML
from get_items import get_items
import json
import csv

from matplotlib import style
import matplotlib.pyplot as plt
style.use('seaborn-paper')


# 1
main_link = 'https://www.myhome.ge/en/s/Apartment-for-sale?PrTypeID=1&AdTypeID=1'

page_soup = getHTML(main_link)
last_page = page_soup.find('li',{'class':'space-item-last'})

num_pages = int(last_page.text)

# 2

page = list()
time = list()

for i in range(1,3):

    item_list = list()

    start = datetime.now()
    
    url = f'https://www.myhome.ge/en/s/Apartment-for-sale?PrTypeID=1&AdTypeID=1&Page={i}&mapOp=1'
    
    page_soup = getHTML(url)

    containers = page_soup.findAll("span",{"class":"d-block"})
    
    for item in containers:
        if 'ID ' in item.text:
            item_list.append(item.text.replace('ID ',''))
    
    page.append(i)
    sp_time = (datetime.now() - start).total_seconds()
    time.append(sp_time)

    items = get_items(item_list)

    # 5
    with open(f'data/file_{i}.json', 'w', encoding='utf-8') as outfile:
        json.dump(items, outfile, ensure_ascii=False, indent=2)


# 3 
df = pd.DataFrame({
    'page' : page,
    'time' : time,
})

df['total_time'] = df.time.cumsum()
ax = df.time.plot()
df.total_time.plot(ax=ax)
plt.show()
