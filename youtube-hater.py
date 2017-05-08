from splinter import *
from time import sleep

with Browser("chrome") as browser:
        browser.visit("https://accounts.google.com/ServiceLogin")
        browser.fill("identifier", "example")
        browser.find_by_id("identifierNext").click()
        sleep(3)
        browser.fill("password", "example")
        browser.find_by_id("passwordNext").click()
        
        sleep(1)
	
        browser.visit("https://youtube.com")
        browser.find_by_css(".yt-ui-ellipsis").first.click()
        sleep(5)
        while True:
		
                try:
                        browser.find_by_css(".like-button-renderer-like-button-unclicked").first.click()
                        browser.find_by_css(".content-link").first.click()
                        sleep(5)
                except:
                        browser.find_by_css(".content-link").first.click()
                        sleep(3)
