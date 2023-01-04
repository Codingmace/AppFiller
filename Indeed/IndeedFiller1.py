# selenium 4
from multiprocessing.connection import wait
from selenium import webdriver
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
	spx = newSrc.split("<li>")
	print(len(spx))
	#g = open('urlPages.txt', 'w')
	print(len(spx[0]))
	print(len(spx[1]))
	fullList = []
	validCount = 0
	while 'href' in newSrc:
		hInd = newSrc.index('href')
		newSrc = newSrc[hInd::]
		hEnd = newSrc.index('>')
		if 'pagead' in newSrc[5:hEnd].lower() or 'company' in newSrc[5:hEnd].lower():
			validCount += 1
		if " " not in newSrc[5:hEnd]:
			fullList.append(newSrc[5:hEnd])
		print(newSrc[0:hEnd])
		newSrc = newSrc[hEnd::]

options = webdriver.EdgeOptions()
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('log-level=3')
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
driver.maximize_window()
#url = "https://recruiting2.ultipro.com/STE1004/JobBoard/fbeef081-b55b-0ae3-a2ac-7b4fb3db6826/Account/Register?redirectUrl=%2FSTE1004%2FJobBoard%2Ffbeef081-b55b-0ae3-a2ac-7b4fb3db6826%2FOpportunityApply%3FopportunityId%3D7e61ab94-83f2-4275-98af-af2ad6a30c13&cancelUrl=https%3A%2F%2Frecruiting2.ultipro.com%2FSTE1004%2FJobBoard%2Ffbeef081-b55b-0ae3-a2ac-7b4fb3db6826%2FOpportunityDetail%3FopportunityId%3D7e61ab94-83f2-4275-98af-af2ad6a30c13%26utm_source%3DLINKEDIN%26utm_medium%3Dreferrer"
#url2 = "https://recruiting2.ultipro.com/STE1004/JobBoard/fbeef081-b55b-0ae3-a2ac-7b4fb3db6826/OpportunityApply?opportunityId=7e61ab94-83f2-4275-98af-af2ad6a30c13"
url3 = "https://www.landis.com/careers?gh_jid=5086595003&gh_src=1c10720f3us#grnhse_app"
url4 = "https://www.credera.com/careers/jobs/4133816?gh_jid=4133816&gh_src=9d4f0c621us"
url5 = "https://www.indeed.com/jobs?q=security%20architect&l=Plano%2C%20TX&from=searchOnHP&vjk=c59d431687d977e7"
url6 = "https://indeed.com/" 
#driver.get(url6)
#input("waiting for login")
joboption = "/jobs?q=Cloud+engineer"
startCount = 10
#driver.get('https://careers.klaviyo.com/en/search-jobs/job/security-architect-staff-security-lead-platform-engineering-remote-eligible-5299552003/?gh_jid=5299552003&gh_src=0453f0b73us&s=LinkedIn&source=LinkedIn')
driver.get(url6 + joboption)
#input("Waiting for the input")
driver.get(url6 + joboption + "&start=" + str(startCount))
f = open('info.csv')
lines = f.readlines()
print(generatePassword())
inputs = []
answers = []
for line in lines:
	split = line.split(',')
	inputs.append(split[0].lower())
	answers.append(split[1].strip())
#print(inputs)
#print(answers)
#print(driver.find_element('first_name'))
#user = driver.find_element(By.ID, 'first_name')
time.sleep(3)
src = driver.page_source
#print(driver.__doc__)
#print(type(src))
#ele = driver.find_elements(By.TAG_NAME, 'form')
#print(len(driver.find_elements(By.TAG_NAME,'iframe')))
tiles = driver.find_elements(By.ID, 'resultsCol')
#tiles = driver.find_elements(By.ID, "mosaic-provider-jobcards")
initInd1 = src.index("<td id=\"resultsCol\">")
src = src[initInd1::]
initInd2 = src.index('mosaic-zone')
newSrc = src[initInd2::]
spx = newSrc.split("<li>")
print(len(spx))
#g = open('urlPages.txt', 'w')
print(len(spx[0]))
print(len(spx[1]))
fullList = []
validCount = 0
while 'href' in newSrc:
	hInd = newSrc.index('href')
	newSrc = newSrc[hInd::]
	hEnd = newSrc.index('>')
	if 'pagead' in newSrc[5:hEnd].lower() or 'company' in newSrc[5:hEnd].lower():
		validCount += 1
	if " " not in newSrc[5:hEnd]:
		fullList.append(newSrc[5:hEnd])
	print(newSrc[0:hEnd])
	newSrc = newSrc[hEnd::]
#	input("waiting for next")
print(tiles[0])
selements = driver.find_elements(By.TAG_NAME, 'href')
elements = tiles[0].find_elements(By.TAG_NAME, 'li')
#tiles = driver.find_elements(By.CLASS_NAME, 'jobsearch-ResultList css-0')
print(tiles[0].text)
#fr = driver.find_elements(By.TAG_NAME, 'iframe')
#driver.switch_to.frame(fr[0])
#driver.switch_to.frame(0)
#driver.switch_to.frame(driver.find_elements(By.TAG_NAME, 'iframe')[0])
#print(len(ele))
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

print("At the end")
# aria_role = checkbox , none, textbox, radio, combobox
#for e in elements:
#	if 'First Name' in e.accessible_name:
#		e.send_keys('Name')
#    print(e)
#user = driver.find_element(By.XPATH, "//*[@id='first_name']")
#print(user)
#user.send_keys('Jake')
while True:
	wait
#driver.get('https://www.google.com/')
#driver.maximize_window()