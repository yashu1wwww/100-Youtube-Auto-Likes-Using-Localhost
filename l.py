from selenium import webdriver
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

time.sleep(2)
driver.get("https://www.youtube.com/watch?v=jNQXAC9IVRw") #replace with your required url

time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(2)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[1]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(2)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#2 account click 
#click on nextt 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(2)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#3 account click 
#click on nextt 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#4th account click 
#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next 
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#5th account click 
#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click()
time.sleep(3)


#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)


#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#6th account click
#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)


#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#7th account click
#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#8th account click
#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(2)

#9th account click
#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')

time.sleep(2)
#10th account click
#click on nextt
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[4]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[5]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[6]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[7]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[8]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[9]/tp-yt-paper-icon-item').click()

time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)

#click on id
driver.find_element_by_id("avatar-btn").click()
time.sleep(3)

#switch
driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()')
time.sleep(2)

#click on next
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[10]/tp-yt-paper-icon-item').click()
time.sleep(3)

#like
driver.execute_script('document.querySelector("#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button").click()')
time.sleep(3)
#end > 10th acc - each acc contain 10 brand accs
