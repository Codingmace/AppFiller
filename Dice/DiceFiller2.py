
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
def spider():
	baseUrl = "https://www.dice.com/jobs"
	query = "?q=devops"
	countryCode = "&countryCode=US&radius=30&radiusUnit=mi"
	pageNumber = "&page="
	pageSize = "&pageSize=20"
	pageStart = 1
	endPageSize = 80
	easyApply = "&filters.easyApply=true"
	remote = "&filters.isRemote=true"
	lang = "&language=en"


	import os
	if not os.path.exists('results.csv'):
		open('results.csv','w').write("naming,link\n")
	g = open('results.csv','a')
	fullCount = []
	while pageStart < endPageSize:
		fulls = baseUrl + query + countryCode + pageNumber + str(pageStart) + pageSize + easyApply + remote + lang
		driver.get(fulls)
		timeout = 20
		try:
		#	elements_present = EC.presence_of_all_elements_located((By.CLASS_NAME, 'card-title-link'))
			elements_present = EC.presence_of_element_located((By.ID, 'searchDisplay-div'))
			WebDriverWait(driver, timeout).until(elements_present)
			elements = driver.find_elements(By.CLASS_NAME, 'card-title-link')
	#		curEl = elements[0]
			for e in elements:
				if "senior" not in e.text.lower() and 'lead' not in e.text.lower():
					g.write(e.text + "," + e.get_property('href') + "\n")
					g.flush()
	#		print(curEl.get_property('href'))
	#		lists = driver.find_element(By.ID, 'searchDisplay-div')
	#		print("Loaded the driver.")
	#		print(lists.page_source)
	
		except TimeoutException:
			print("Timed out waiting for page to load")
		pageStart += 1
		time.sleep(5)

# Applying
driver.get("https://www.dice.com")
input("Login")
testUrl = "https://www.dice.com/jobs/detail/1f2028b260075b96793dbf7ceb42b4e0?searchlink=search%2F%3Fq%3Ddevops%26countryCode%3DUS%26radius%3D30%26radiusUnit%3Dmi%26page%3D3%26pageSize%3D20%26filters.easyApply%3Dtrue%26filters.isRemote%3Dtrue%26language%3Den%26eid%3DS2Q_%2Cbw_1&searchId=07720242-c95a-4706-bc21-42434eaa7373"
testUrl2 = "https://www.dice.com/jobs/detail/20afb00ce41dbd43811ceac411fde418?searchlink=search%2F%3Fq%3Ddevops%26countryCode%3DUS%26radius%3D30%26radiusUnit%3Dmi%26page%3D3%26pageSize%3D20%26filters.easyApply%3Dtrue%26filters.isRemote%3Dtrue%26language%3Den%26eid%3DS2Q_%2Cbw_1&searchId=07720242-c95a-4706-bc21-42434eaa7373"
testUrl3 = "https://www.dice.com/jobs/detail/f25dee6a8c337947c18f5f084c9a47e3?searchlink=search%2F%3Fq%3Ddevops%26countryCode%3DUS%26radius%3D30%26radiusUnit%3Dmi%26page%3D3%26pageSize%3D20%26filters.easyApply%3Dtrue%26filters.isRemote%3Dtrue%26language%3Den%26eid%3DS2Q_%2Cbw_1&searchId=07720242-c95a-4706-bc21-42434eaa7373"
driver.get(testUrl3)
#input("Got this point")
#applyButton = driver.find_element(By.CLASS_NAME, 'button-primary')

#xs8 = driver.find_elements(By.TAG_NAME, 'button')
#xs9 = driver.find_element(By.XPATH, '//button[1]')
time.sleep(3)

xs10 = driver.find_element(By.XPATH , '//dhi-wc-apply-button')
#xs10.submit()
#print(xs10.location)
time.sleep(1)
xs10.click()
time.sleep(5)
#for xs13 in driver.find_elements(By.TAG_NAME, 'button'):
#	print(xs13.text)
#print(len(driver.find_elements(By.TAG_NAME, 'button')))
#xs12 = driver.find_element(By.CLASS_NAME, 'button-primary')
#xs10.click()
#xs11 = driver.find_element(By.XPATH ,"//button[@class='button-primary']")
#js_command = '$0'
# send the command to the selenium webbrowser
#send_js_command = ActionChains(driver)
#send_js_command.send_keys(js_command, Keys.ENTER).perform()
#xs7 = driver.execute_script('return $0')
#print(send_js_command)
def expand_shadow_element(element):
  shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root

#xs6 = expand_shadow_element(driver)
#xs5 = driver.find_elements(By.CSS_SELECTOR,)
#xs4 = driver.find_element_by_name('Apply Now') 
#driver.get('https://www.tiendasjumbo.co/buscar?q=mani')
#item = driver.execute_script("return document.querySelector('impulse-search').shadowRoot.querySelector('')")
#print(item.text)

def getShadowRoot(host):
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", host)
    return shadow_root


#root1 = driver.find_element(By.ID, 'lowerApplyBtn')
#xs = getShadowRoot(root1)
#xs2 = root1.find_element(By.CSS_SELECTOR, '#shadow_host')
#xs1 = root1.find_element(By.ID, 'ja-apply-button')
#shadow_host = driver.find_element(By.CSS_SELECTOR, 'shadow_host')
#children = driver.execute_script('return arguments[0].shadowRoot.children', shadow_host)

#shadow_content = next(child for child in children if child.get_attribute('id') == 'shadow_content')

#shadow_host = driver.find_element(By.CSS_SELECTOR, 'shadow-root')
#shadow_host = driver.find_element_by_css_selector('#shadow_host')
#shadow_roit = driver.execute_script()
#shadow_root = driver.execute_script('return arguments[0].shadowRoot', driver)
#shadow_content = shadow_root.find_element_by_css_selector('#shadow_content')
#sx = driver.find_element(By.CSS_SELECTOR, 'lowerApplyBtn')
#outer = expand_shadow_element(driver.find_element(By.CSS_SELECTOR,"div#lowerApplyBtn"))
#inner = outer.find_element(By.XPATH ,'//div[@id="ja-apply-button"]')
#inner.click()

#applyButton = driver.find_elements(By.TAG_NAME, 'button')
#for q in applyButton:
#	print(q.text)
#applyButton = driver.find_element(By.ID, 'ja-apply-button')
#applyButton.click()
#time.sleep(5)

steps = driver.find_elements(By.CLASS_NAME, 'steps')
i = 0

while i < 3:
	try:
		buttons = driver.find_elements(By.TAG_NAME,'button')
		for butts in buttons:
			if butts.text.lower() == 'next':
				butts.click()
				print("Next page")
				break
			if butts.text.lower() == 'apply':
				butts.click()
				print("Finished application")
				break
		time.sleep(5)
	except:
		print("Something broke")
		pass