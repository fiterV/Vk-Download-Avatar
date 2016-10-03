import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import urllib
from time import *

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='Link to VK account')
args = parser.parse_args()
if (None in [args.url]):
	print('Provide the full information(read help)')
	exit(0)

driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
driver.get(args.url)
avatar = driver.find_element_by_class_name('page_avatar_img')
avatar.click()
sleep(0.5)
name = driver.title

img = driver.find_element_by_tag_name('img')
url = img.get_attribute('src')
if (not os.path.exists('photos/')):
	os.mkdir('photos')
urllib.urlretrieve(url, 'photos/'+name)
driver.close()