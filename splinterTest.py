from splinter import Browser

browser = Browser('firefox')
browser.visit('http://google.com')
browser.find_by_name('q').fill('splinter - python acceptance testing for web applications')
browser.find_by_name('btnK').click()

if browser.is_text_present('splinter.readthedocs.io'):
    print("Yes, the official website was found!")
else:
    print("No, it wasn't found... We need to improve our SEO techniques")

browser.quit()
