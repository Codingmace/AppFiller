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
		pageAdInd = 100
		companyInd = 100
		try:
			pageAdInd = newSrc.index('pagead')
		except:
			pass
		try:
			companyInd = newSrc.index('company')
		except:
			pass
		if pageAdInd < 10 or companyInd < 10:
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
	startCount = 0
	fullList = []
	while startCount < limit:
		if startCount == 0:
			driver.get(url6 + joboption)
		else:
			driver.get(url6 + joboption + "&start=" + str(startCount))
		time.sleep(1)
		src = driver.page_source
		newLinks = parseResultPage(src)
		for s in newLinks:
			fullList.append(s.strip("\""))
		startCount += 10
	return fullList
# V.rdeC8jvCAm52F

def apply(driver):
	try:
		butts = driver.find_element(By.ID, 'indeedApplyButton').click()
	except:
		print("Page is not valid")
		return "NOPE"
	input("Waiting on input")
	# Needs input if text == ""
	steps = 0
	while steps < 7:
		elements = driver.find_elements(By.TAG_NAME, 'input')
		# Get the button that says continue
		nexts = driver.find_elements(By.TAG_NAME, 'button')
		for n in nexts:
			if n.accessible_name == 'Continue':
				n.click()
				break
			if n.accessible_name == 'Submit your application':
				n.click()
				print("Finished application")
				steps = 8
				return "FINISHED"
#				break
		time.sleep(1)
		steps += 1
#		print("Got elements")
	return "MISSING DATA"

driver = setup()
driver.maximize_window()
#driver.execute_script("window.open('https://google.com');")
#url = "https://recruiting2.ultipro.com/STE1004/JobBoard/fbeef081-b55b-0ae3-a2ac-7b4fb3db6826/Account/Register?redirectUrl=%2FSTE1004%2FJobBoard%2Ffbeef081-b55b-0ae3-a2ac-7b4fb3db6826%2FOpportunityApply%3FopportunityId%3D7e61ab94-83f2-4275-98af-af2ad6a30c13&cancelUrl=https%3A%2F%2Frecruiting2.ultipro.com%2FSTE1004%2FJobBoard%2Ffbeef081-b55b-0ae3-a2ac-7b4fb3db6826%2FOpportunityDetail%3FopportunityId%3D7e61ab94-83f2-4275-98af-af2ad6a30c13%26utm_source%3DLINKEDIN%26utm_medium%3Dreferrer"
#url2 = "https://recruiting2.ultipro.com/STE1004/JobBoard/fbeef081-b55b-0ae3-a2ac-7b4fb3db6826/OpportunityApply?opportunityId=7e61ab94-83f2-4275-98af-af2ad6a30c13"
#url3 = "https://www.landis.com/careers?gh_jid=5086595003&gh_src=1c10720f3us#grnhse_app"
#url4 = "https://www.credera.com/careers/jobs/4133816?gh_jid=4133816&gh_src=9d4f0c621us"
#url5 = "https://www.indeed.com/jobs?q=security%20architect&l=Plano%2C%20TX&from=searchOnHP&vjk=c59d431687d977e7"
#url6 = "https://indeed.com/" 
#driver.get(url6)
#input("waiting for login")
url7 = "https://indeed.com/company/HealthComp/jobs/Devop-Engineer-fb9329314daf04f3?fccid=1cd5b3f61a77d3c3&amp;vjs=3"

driver.get(url7)
apply(driver)
'''
try:
	butts = driver.find_element(By.ID, 'indeedApplyButton').click()
#	print(len(butts))
except:
	print("Page is not valid")
'''
'''
fullList = getLinks('devops+engineer', 50)
#fullList = []
g = open('urlLinks.txt','w')
for q in fullList:
	g.write(q + "\n")
	g.flush()
g.close()
#driver.get(url6 + joboption)
'''

#driver.get(url6 + joboption + "&start=" + str(startCount))
'''
f = open('info.csv')
lines = f.readlines()
inputs = []
answers = []
for line in lines:
	split = line.split(',')
	inputs.append(split[0].lower())
	answers.append(split[1].strip())
'''

'''
time.sleep(1)
src = driver.page_source
fullList = []
newLinks = parseResultPage(src)
for s in newLinks:
	fullList.append(s.strip("\""))
#fullList.append(newLinks)
print(len(fullList))
#print(fullList[0])
#input("made it here")
'''
'''
for r in range(0, len(fullList)):
	driver.get(url6 + fullList[r][1::])
	try:
		butts = driver.find_element(By.ID, 'indeedApplyButton').click()
	except:
		print("Page is not valid")
'''

#tiles = driver.find_elements(By.CLASS_NAME, 'jobsearch-ResultList css-0')
#fr = driver.find_elements(By.TAG_NAME, 'iframe')
#driver.switch_to.frame(fr[0])
#driver.switch_to.frame(0)
#driver.switch_to.frame(driver.find_elements(By.TAG_NAME, 'iframe')[0])
'''
elements = driver.find_elements(By.TAG_NAME, 'input')
if 'Register' in src:
	print("this is a registry page")
	password = generatePassword()
	time.sleep(1)
	for e in elements:
		curField = e.accessible_name.lower()
#		print('cur Field',curField)
		matches = False
		for a in range(0, len(inputs)):
			if inputs[a] in curField:
				matches = True
				e.send_keys(answers[a])
		if e.accessible_name == '':
			if not matches and e.aria_role != 'none':
				print("We Couldn't find input for " + curField) # Later can do best match

#			print(e.get_attribute())
#			print('Something is wrong')
#		print(e.accessible_name)
#print(src.find('input'))
#print("done with that thing")
elif "Sign in" in src or "Login" in src:
	print("This is signing in") # To do
	print("Read from the password file and match it up")
#	ele = driver.find_elements(By.TAG_NAME, 'form')
#	print(len(ele))
else:
	time.sleep(1)
#	print(driver.page_source)
	elements = driver.find_elements(By.TAG_NAME, 'input')
	selects = driver.find_elements(By.TAG_NAME, 'select')
	time.sleep(2)
	for e in elements:
		curField = e.accessible_name.lower()
#		print('cur Field',curField)
		matches = False
		for a in range(0, len(inputs)):
			if inputs[a] in curField:
				matches = True
				e.send_keys(answers[a])
		if e.accessible_name == '':
			if not matches and e.aria_role != 'none':
				print("We Couldn't find input for " + curField) # Later can do best match
	for s in selects: # Combobox
		if s.text != '':
			curField = s.accessible_name.lower()
			matches = False
			for a in range(0, len(inputs)):
				if inputs[a] in curField:
					matches = True
					options = s.text.split('\n')
					bestOption = 0
					for b in range(0, len(options)):
						if answers[a].lower() in options[b].lower():
							bestOption = b
					s.send_keys(options[b])

					'''
print("At the end")
# aria_role = checkbox , none, textbox, radio, combobox
#for e in elements:
#	if 'First Name' in e.accessible_name:
#		e.send_keys('Name')
#    print(e)
#user = driver.find_element(By.XPATH, "//*[@id='first_name']")
#print(user)
#user.send_keys('Jake')
#while True:
#	wait

