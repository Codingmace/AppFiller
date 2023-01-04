
from http.server import executable
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Edge(executable_path="./msedgedriver.exe")
driver.maximize_window()
#xs3 = driver.find_element()
#driver = webdriver.Firefox(executable_path= "./geckodriver.exe")
# Spidering a query

def spider(query, endPageSize):
	baseUrl = "https://www.dice.com/jobs"
	query = "?q=" + query.replace(" ", "%20")
#	query = "?q=penetration+tester"
	countryCode = "&countryCode=US&radius=30&radiusUnit=mi"
	pageNumber = "&page="
	pageSize = "&pageSize=20"
	pageStart = 1
#	endPageSize = 30
	easyApply = "&filters.easyApply=true"
	remote = "&filters.isRemote=true"
	contractOnly = "&filters.employmentType=CONTRACTS"
	lang = "&language=en"
	directHire = "&filters.employerType=Direct%20Hire"

	import os
	if not os.path.exists('results.csv'):
		open('results.csv','w').write("naming,link\n")
	g = open('results.csv','a')
	fullCount = []
	while pageStart < endPageSize:
		fulls = baseUrl + query + countryCode + pageNumber + str(pageStart) + pageSize + easyApply + remote + directHire + contractOnly + lang
		driver.get(fulls)
		timeout = 10
		try:
			elements_present = EC.presence_of_element_located((By.ID, 'searchDisplay-div'))
			WebDriverWait(driver, timeout).until(elements_present)
			elements = driver.find_elements(By.CLASS_NAME, 'card-title-link')
			for e in elements:
				curTitle = e.text.lower()
				if "senior" not in curTitle and 'lead' not in curTitle and "sr." not in curTitle:
					g.write(e.text + "," + e.get_property('href') + "\n")
					g.flush()
	
		except TimeoutException:
			print("Timed out waiting for page to load")
		pageStart += 1
		time.sleep(5)


def applying():
	# Applying
	driver.get("https://www.dice.com")
	input("Login")

	# Automate applying
	f = open("results.csv",'r')
	import os
	if not os.path.exists('done.csv'):
		open('done.csv','w').write("naming,link,status\n")
	h = open('done.csv','a')
	con = 1
	f.readline() # read header
	lines = f.readlines()
	for line in lines:
		curUrl = line.split(",")[-1].strip()
		driver.get(curUrl)
		timeout = 5
		
		try:
			elements_present = EC.presence_of_element_located((By.XPATH , '//dhi-wc-apply-button'))
			WebDriverWait(driver, timeout).until(elements_present)
		except TimeoutException:
			print("Timed out waiting for page to load")
		
#		time.sleep(20)
		applyButton = driver.find_element(By.XPATH , '//dhi-wc-apply-button')
		time.sleep(2)
		applyButton.click()
		time.sleep(2)
#		time.sleep(20)
		
		try:
			elements_present = EC.presence_of_element_located((By.CLASS_NAME, 'steps'))
			WebDriverWait(driver, timeout).until(elements_present)
		except TimeoutException:
			print("\nTimed out waiting for page to load\n")
		
		steps = driver.find_elements(By.CLASS_NAME, 'steps')
		i = 0
		isDone = False
		while i < 3:
			try:
				time.sleep(1)
				
				try:
					elements_present = EC.presence_of_element_located((By.TAG_NAME, 'button'))
					WebDriverWait(driver, timeout).until(elements_present)
				except TimeoutException:
					print("Timed out waiting for page to load")
				
				buttons = driver.find_elements(By.TAG_NAME,'button')
				for butts in buttons:
					if butts.text.lower() == 'next':
						butts.click()
						print("Next page")
						break
					if butts.text.lower() == 'apply':
						butts.click()
						print("Finished application")
						isDone = True
						break
				time.sleep(5)
			except:
				print("Something broke")
				pass
			i+= 1
		h.write(line.strip() + ",")
		if isDone:
			h.write("Finished\n")
		else:
			h.write("Incomplete\n")
		h.flush()
	if con % 5 == 0:
		time.sleep(30)
	if con % 10 == 0:
		time.sleep(30)
	if con == 20:
		return
	con += 1

applying()
#spider("cyber security", 19)
#spider("penetration tester", 1)
#spider("threat", 3)
#spider("SOC", 5)
#spider("software developer", 35)
#spider("penetration tester")