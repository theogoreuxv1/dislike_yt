from splinter import *
from time import sleep

with Browser() as browser:
	browser.visit("https://accounts.google.com/ServiceLogin")
	browser.fill("Email", "coucouhelicopter")
	browser.find_by_id("next").click()
	browser.fill("Passwd", "jaimelecacao")
	browser.find_by_id("signIn").click()
	
	sleep(1)
		
	
	browser.visit("https://youtube.com")
	browser.find_by_css(".yt-ui-ellipsis").first.click()
	
	sleep(5)
	
	while True:
		
		
		browser.find_by_css(".like-button-renderer-dislike-button-unclicked").first.click()
		browser.find_by_css(".content-link").first.click()
		sleep(5)
