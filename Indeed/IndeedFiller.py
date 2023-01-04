# selenium 4
from multiprocessing.connection import wait
from pickletools import uint8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import string
import random
import time

def generatePassword():
	pwd_length = 12
	letters = string.ascii_letters
	q_list = [random.choice(letters) for i in range(pwd_length)]
	digits = string.digits
	special = '!@#$%^&*()<>{}:'
	digitPlace = random.randint(0,pwd_length -1)
	specialPlace = random.randint(0, pwd_length - 1)
	while digitPlace == specialPlace:
		digitPlace = random.randint(0, pwd_length -1)
	q_list[digitPlace] = random.choice(digits)
	q_list[specialPlace] = random.choice(special)
	pwd = ''
	for q in q_list:
		pwd += q
	print(pwd)
	return pwd

def parseResultPage(src):
	initInd1 = src.index("<td id=\"resultsCol\">")
	src = src[initInd1::]
	initInd2 = src.index('mosaic-zone')
	newSrc = src[initInd2::]
	fullList = []
	while 'href' in newSrc:
		hInd = newSrc.index('href')
		newSrc = newSrc[hInd::]
		hEnd = newSrc.index('>')
		hLink = newSrc[5:hEnd]
#		pageAdInd = 100
		companyInd = 100
#		try:
#			pageAdInd = newSrc.index('pagead')
#		except:
#			pass
		try:
			companyInd = newSrc.index('company')
		except:
			pass
		if companyInd < 10:
#		if pageAdInd < 10 or companyInd < 10:
			if " " in hLink:
				hLink = hLink.split(" ")[0]
			fullList.append(hLink)
#			fullList.append(newSrc[5:hEnd])
#		print(newSrc[0:hEnd])
		newSrc = newSrc[hEnd::]
	return fullList

def setup():
	options = webdriver.EdgeOptions()
	options.add_argument("--ignore-certificate-error")
	options.add_argument("--ignore-ssl-errors")
	options.add_argument('--ignore-certificate-errors-spki-list')
	options.add_argument('log-level=3')
	return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

def getLinks(query, limit):
	url6 = "https://indeed.com/"
	joboption = "/jobs?q=" + query
	salary = "%2485%2C000" 
	remote = "&sc=0kf%3Aattr%28DSQF7%29%3B"
	dateSort = "&sort=date"
	twoWeeks = "&fromage=14"
#	extra_stuff = "&sc=0kf%3Aattr%28DSQF7%29%3B&sort=date"
#	extra_stuff = salary + remote + dateSort + twoWeeks
	extra_stuff = remote + dateSort + twoWeeks
	startCount = 0
	fullList = []
	while startCount < limit:
		if startCount == 0:
			driver.get(url6 + joboption + extra_stuff)
		else:
			driver.get(url6 + joboption + extra_stuff + "&start=" + str(startCount))
		time.sleep(1)
		src = driver.page_source
		newLinks = parseResultPage(src)
		for s in newLinks:
			fullList.append(s.strip("\""))
		startCount += 10
	return fullList

def spider(query):
	query = query.replace(' ', '+')
	fullList = getLinks(query, 600)
	g = open('urlLinks.txt','a')
	for q in fullList:
		g.write(q + "\n")
		g.flush()
	g.close()

# V.rdeC8jvCAm52F

def apply(driver , url):
	driver.get(url)
	time.sleep(3)
	try:
		butts = driver.find_element(By.ID, 'indeedApplyButton').click()
	except:
		print("Page is not valid")
		return "NOPE"
#	input("Waiting on input")
	# Needs input if text == ""
	steps = 0
	while steps < 7:
		nexts = driver.find_elements(By.TAG_NAME, 'button')
		for n in nexts:
			if n.accessible_name == 'Continue':
				n.click()
				break
			if n.accessible_name == 'Submit your application':
				n.click()
				steps = 8
				return "FINISHED"
		time.sleep(2)
		steps += 1
	return "MISSING DATA"

driver = setup()
driver.maximize_window()
baseurl = "https://indeed.com/" 
driver.get(baseurl)
loggedIn = input("Login to account then press y")
while loggedIn != 'y':
	loggedIn = input("Press y when you have logged into your account")

pathway = input("Would you like to spider or apply?")
if "spider" in pathway:
	print("We are spidering. Need more input though")
#	print("What phrase are you wanting to spider?")
	phrase = input("What phrase are you wanting to spider? ")
	spider(phrase)
elif "apply" in pathway:
	g = open('urlLinks.txt', 'r')
	h = open('results.csv', 'a')
	h.write("url,status\n")
	lines = g.readlines()
	con = 1
	for line in lines:
		res = apply(driver, ('https://indeed.com' + line.strip()))
		h.write("\"indeed.com" + line.strip() + "\"," + res + '\n')
		h.flush()
		print(res)
		if res != "FINISHED":
#			break
			pass
		if con % 5 == 0:
			time.sleep(60)
		else:
			time.sleep(5)
		con += 1
print("At the end")