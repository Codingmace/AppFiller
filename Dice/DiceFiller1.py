
from http.server import executable
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


baseUrl = "https://www.dice.com/jobs"
query = "?q=devops"
countryCode = "&countryCode=US&radius=30&radiusUnit=mi"
pageNumber = "&page="
pageSize = "&pageSize=20"
pageStart = 1
endPageSize = 90
easyApply = "&filters.easyApply=true"
remote = "&filters.isRemote=true"
lang = "&language=en"

fulls = baseUrl + query + countryCode + pageNumber + str(pageStart) + pageSize + easyApply + remote + lang
#firefoxPath = "C:\Program Files\Mozilla Firefox\firefox.exe"
#driver = webdriver.Edge()
#import os
#print(os.listdir("./"))
driver = webdriver.Edge(executable_path="./msedgedriver.exe")
#driver = webdriver.Firefox(executable_path="./geckodriver.exe")
#driver = webdriver.Firefox(executable_path=firefoxPath)

driver.get(fulls)
timeout = 20
try:
#	elements_present = EC.presence_of_all_elements_located((By.CLASS_NAME, 'card-title-link'))
	elements_present = EC.presence_of_element_located((By.ID, 'searchDisplay-div'))
	WebDriverWait(driver, timeout).until(elements_present)
	elements = driver.find_elements(By.CLASS_NAME, 'card-title-link')
	curEl = elements[0]
#	print(curEl.get_attribute())
	print(curEl.get_property('href'))
	'''
	src = driver.page_source

	initInd = src.index('searchDisplay-div')
	newSrc = src[initInd::]
	while 'href="https://www.dice.com' in newSrc:
		ind = newSrc.index('href="https://www.dice.com')
		newSrc = newSrc[ind + len('href="')::]
		endInd = newSrc.index('"')
		if endInd < 200:	
			print(newSrc[0:endInd])
		newSrc = newSrc[endInd::]

	'''
	lists = driver.find_element(By.ID, 'searchDisplay-div')
	print("Loaded the driver.")
	print(lists.page_source)
	
except TimeoutException:
	print("Timed out waiting for page to load")