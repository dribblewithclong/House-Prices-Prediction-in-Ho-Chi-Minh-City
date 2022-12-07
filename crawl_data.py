# importing the necessary packages
import pandas as pd
import numpy as np 
import requests
from random import randint
from time import sleep
from bs4 import BeautifulSoup

#Create a dictionary with the key are districts and values are number of page to get data for one time
district_page = {
    'quan-1': 10,
    'quan-2': 10,
    'quan-3': 10,
    'quan-4': 10,
    'quan-5': 10,
    'quan-6': 10,
    'quan-7': 10,
    'quan-8': 10,
    'quan-9': 10,
    'quan-10': 10,
    'quan-11': 10,
    'quan-12': 10,
    'quan-binh-tan': 10,
    'quan-binh-thanh': 10,
    'quan-go-vap': 10,
    'quan-phu-nhuan': 10,
    'quan-tan-binh': 10,
    'quan-tan-phu': 10,
    'quan-thu-duc': 10,
    'huyen-hoc-mon': 10,
    'huyen-binh-chanh': 10,
    'huyen-nha-be': 10
}

def get_id_house(district,total_page=10,scale=0):
    """
    Return id of each house of total page in the selected district

    Parameters:
    district: str
        Districts in HCM City such as "quan-1", "quan-2", "quan-tan-binh"...
    total_page: int
        Number of pages to get data
    scale: int
        Determine the beginning page to get data corresponds to total_page by the following formula:
            begin_page = total_page*scale+1   
    """
    
    id = []
    begin_page = total_page*scale+1
    end_page = begin_page+total_page
    
    for page in range(begin_page,end_page):
        url = 'https://propzy.vn/mua/bat-dong-san/hcm/'+ str(district) + '/p' + str(page)
        id_r = requests.get(url)
        id_coverpage = id_r.content
        id_soup = BeautifulSoup(id_coverpage, 'html5lib')
        id_class = id_soup.find_all('div', class_='item-listing listing-card view-as-list item-compare')
        for i in id_class:
            id.append(int(i['data-id']))
        print('Got id page',page)
    return id 

def get_info_house(district,total_page=10,scale=0):
    """
    Return the house attribute and price of total page in the selected district

    Parameters:
    district: str
        Districts in HCM City such as "quan-1", "quan-2", "quan-tan-binh"...
    total_page: int
        Number of pages to get data
    scale: int
        Determine the beginning page to get data corresponds to total_page by the following formula:
            begin_page = total_page*scale+1
    """
    full_attribute_list = []
    list_id = get_id_house(district,total_page,scale)
    cumsum = 0
    if len(list_id) == 0:
        return list()
    for id in list_id:
        url = 'https://propzy.vn/mua/nha/hcm/' + str(district) + '/id' + str(id)
        attribute_r = requests.get(url)
        attribute_coverpage = attribute_r.content
        attribute_soup = BeautifulSoup(attribute_coverpage)
        attribute = {}
        #Get name_district
        attribute['Địa điểm'] = district
        try:
            #Category type of house
            attribute['Phân Loại'] = attribute_soup.find_all('h1',class_='h3-title')[0].text
            #Get main_attribute
            attribute_class = attribute_soup.find_all('div', class_='tab-content entry-content')[1]
            attribute_list = []
            for a  in attribute_class.strings:
                if a != ' ':
                    attribute_list.append(a.strip())
            key_att = []
            value_att = []
            for index in range(len(attribute_list)):
                if index % 2 != 0:
                    value_att.append(attribute_list[index])
                else: 
                    key_att.append(attribute_list[index])
            for index in range(len(key_att)):
                attribute[key_att[index]] = value_att[index]
            #Get extra_attribute
            extra_class = attribute_soup.find_all('div', class_='tab-content entry-content')[2]
            extra_list = []
            for i in extra_class.strings:
                if i != ' ':
                    extra_list.append(i.strip())
            attribute['Khác'] = '. '.join(extra_list)
            #Get price_house
            price_list = []
            price_tag = attribute_soup.find_all('div',class_='p-price-n')[0].strings
            for i in price_tag:
                if i != ' ':
                    price_list.append(i.strip())
            attribute['Giá'] = price_list[0]
            attribute['Giá/m2'] = price_list[1]
            #Get full attribute and price of district
            full_attribute_list.append(attribute)
            cumsum += 1
            print('Got id',id,'home at',district,'. Total:',cumsum)
        except:
            pass
    
    # if len(full_attribute_list) > 0:
    #     pd.DataFrame(full_attribute_list).to_csv(district+'_p'+str(scale+1)+'.csv',index=False)
    
    return full_attribute_list

def get_info_full_district(district_page,scale=0):
    """
    Return the house attribute and price of total page in multiple selected district
    
    Parameters:
    district_page: dict
        A dictionary containing the key is district and the value is total page to get data
    scale: int
        Determine the beginning page to get data corresponds to total_page by the following formula:
            begin_page = total_page*scale+1
    """
    final = []
    for district in list(district_page.keys()):
        final += get_info_house(district,district_page[district],scale)
        print('Done:',district)
        sleep(randint(2,5))
    df = pd.DataFrame(final)
    df.to_csv(f'data_chunk/part{scale+1}.csv',index=False)
    
    return 'Done' 

get_info_full_district(district_page,scale=0)
get_info_full_district(district_page,scale=1)
get_info_full_district(district_page,scale=2)
get_info_full_district(district_page,scale=3)
get_info_full_district(district_page,scale=4)
get_info_full_district(district_page,scale=5)
get_info_full_district(district_page,scale=6)
get_info_full_district(district_page,scale=7)
get_info_full_district(district_page,scale=8)
get_info_full_district(district_page,scale=9)
get_info_full_district(district_page,scale=10)

#Concatenate to one data frame
full_part = []
for i in range(1,11):
    try:
        full_part.append(pd.read_csv(f'data_chunk/part{i}.csv'))
    except:
        pass
    
pd.concat(full_part).to_csv('data/raw_data.csv',index=False)