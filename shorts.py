from selenium import webdriver #10 gmails each gmail - 10 brand accounts
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:9222")

driver = webdriver.Chrome(options=option)
time.sleep(5)
driver.get("https://www.youtube.com/shorts/USc22MHu9cU") #replace with your required youtube shorts url
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#2 account click 
#click on nextt 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(4)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#3 account click 
#click on nextt 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#4th account click 
#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#5th account click 
#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click()
time.sleep(3)


#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)


#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#6th account click
#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)


#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#7th account click
#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#8th account click
#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()

time.sleep(4)

#9th account click
#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()

time.sleep(4)
#10th account click
#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()

time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.find_element_by_xpath("//yt-formatted-string[text()='Switch account']").click()
time.sleep(4)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.find_element_by_class_name("yt-spec-button-shape-with-label").click()
time.sleep(3)
#end > 10th acc - each acc contain 10 brand accs

