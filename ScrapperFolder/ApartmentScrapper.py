import IPmask as Mask
from IPmask import requests
from IPmask import BeautifulSoup
import csv
"""
Reminder make sure you include timer to avoid any type of pretermined attack (DDOS)
"""
# ~ == check
# * == error
Apartmentcom_url = "https://www.apartments.com/"
area=["princess anne","md"]
Apartmentcom_url_format=(Apartmentcom_url+area[0]+" "+area[1]).replace(' ','-') #https://www.apartments.com/princess-anne-md

#try:
#    page=requests.get(Apartmentcom_url_format, proxies
# ^ not finished yet
#print(Apartmentcom_url_format) ~


