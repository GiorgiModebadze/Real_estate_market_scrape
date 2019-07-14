# 4

from helper_funcs import getHTML


def get_items(item_list):
    sales_info = list()

    for item in item_list:

        appartment_info = dict()

        item_link = f'https://www.myhome.ge/en/pr/{item}'
        print(item_link)
        page_soup = getHTML(item_link)

        appartment_info['id'] = item
        appartment_info['link'] = item_link

        # address
        try:
            appartment_info['address'] = page_soup.find("span", {"class": "address"}).text.strip()
        except:
            pass
        # lat
        try:
            appartment_info['lat'] = page_soup.find("div", {"id": "map"})['data-lat']
        except:
            pass
        # long 
        try:
            appartment_info['long'] = page_soup.find("div", {"id": "map"})['data-lng']
        except:
            pass
        # Price - GEL
        try:
            appartment_info['price_gel'] = page_soup.find("div", {"class": "price"}).find('span', {'class': 'd-block'})[
                'data-price-gel']
        except:
            pass
        # Price - USD
        appartment_info['price_usd'] = page_soup.find("div", {"class": "price"}).find('span', {'class': 'd-block'})[
            'data-price-usd']
        # Building Type
        appartment_info['b_type'] = page_soup.find("div", {"class": "main-features"}).find("span",
                                                                                           {"class": "pr-1"}).text
        # area 
        appartment_info['area'] = page_soup.find("div", {"class": "_asd"}).find("div", {"class": "space"}).text.replace(
            'Area: ', '').replace(' m² ', '')
        # description
        try:
            appartment_info['d_original'] = page_soup.find("div", {"class": "description"}).find('p', {
                "class": "original"}).text.strip()
            appartment_info['d_translated'] = page_soup.find("div", {"class": "description"}).find('p', {
                "class": "translated"}).text.strip()
        except:
            pass

        # amenities:
        try:
            amenities = list()
            for item in page_soup.findAll("ul", {"class": "amenities-ul"}):
                for li in item:
                    if 'no-element' not in li.find('i')['class']:
                        amenities.append(li.text.strip().replace('\t', '').replace('\n', ' '))
            appartment_info['amenities'] = amenities
        except:
            pass
        # similars:
        try:
            similars = list()
            for div in page_soup.find("div", {"class": "similar-prs"}):
                try:
                    similars.append(div['data-product-id'])
                except:
                    pass

            appartment_info['similar_items'] = similars
        except:
            pass

        sales_info.append(appartment_info)

    return sales_info
