from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re

driver = webdriver.Chrome()

driver.get("https://www.whoscored.com/Regions/108/Tournaments/5/Seasons/1957/Stages/3277/RefereeStatistics/Italy-Serie-A-2009-2010")

# review_button = driver.find_element_by_xpath('//*[@id="referee-tournaments-table-body"]/tr')
# review_button.click()


csv_file = open('SA09P.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

yup = driver.find_element_by_xpath('//*[@id="referee-stats-options"]/li[2]/a')
yup.click()

reviews = driver.find_elements_by_xpath('//tbody[@id="referee-tournaments-table-body"]/tr')
# reviews = driver.find_elements_by_xpath(('//a[@class="tournament-link"]'))[i].get_attribute('href')

print(reviews)
review_dict = {}

for review in reviews:

	R = review.find_element_by_xpath('./td[2]/a').text
	print(R)
	# Referee = review.find_element_by_xpath('.//td[2]').text
	# Apps = review.find_element_by_xpath('.//td[3]').text
	# Home_Win = review.find_element_by_xpath('.//td[4]').text
	# Away_Win = review.find_element_by_xpath('.//td[5]').text
	# Draw = review.find_element_by_xpath('.//td[6]').text

	# review_dict['R'] = R
	# review_dict['Referee'] = Referee
	# review_dict['Appearances'] = Apps
	# review_dict['Home Win %'] = Home_Win
	# review_dict['Away Win %'] = Away_Win
	# review_dict['Draw %'] = Draw

	# R = review.find_element_by_xpath('.//td[1]').text
	# Referee = review.find_element_by_xpath('.//td[2]').text
	# Apps = review.find_element_by_xpath('.//td[3]').text
	# Fouls_pg = review.find_element_by_xpath('.//td[4]').text
	# Fouls_Tackles = review.find_element_by_xpath('.//td[5]').text
	# Pen_PG = review.find_element_by_xpath('.//td[6]').text
	# Yel_PG = review.find_element_by_xpath('.//td[7]/span').text
	# Yellow = review.find_element_by_xpath('.//td[8]/span').text
	# Red_PG = review.find_element_by_xpath('.//td[9]/span').text
	# Red = review.find_element_by_xpath('.//td[10]/span').text

	# review_dict['R'] = R
	# review_dict['Referee'] = Referee
	# review_dict['Appearances'] = Apps
	# review_dict['Fouls_per_Game'] = Fouls_pg
	# review_dict['Fouls_per_Tackle'] = Fouls_Tackles
	# review_dict['Penalty_per_game'] = Pen_PG
	# # review_dict['Yellows_per_game'] = Yel_PG
	# # review_dict['Total_Yellow_Cards'] = Yellow
	# # review_dict['Reds_per_game'] = Red_PG
	# # review_dict['Total_Red_Cards'] = Red

	# writer.writerow(review_dict.values())


# page_2 = driver.find_element_by_xpath('//*[@id="next"]')
# page_2.click()

# ratings = driver.find_elements_by_xpath('//*[@id="referee-tournaments-table-body"]/tr')


# for review in reviews:

# 	reviews_dict = {}

# 	R = ratings.find_element_by_xpath('.//td[1]').text
# 	Referee = ratings.find_element_by_xpath('.//td[2]').text
# 	Apps = ratings.find_element_by_xpath('.//td[3]').text
# 	Home_Win = ratings.find_element_by_xpath('.//td[4]').text
# 	Away_Win = rating.find_element_by_xpath('.//td[5]').text
# 	Draw = ratings.find_element_by_xpath('.//td[6]').text

# 	reviews_dict['R'] = R
# 	reviews_dict['Referee'] = Referee
# 	reviews_dict['Appearances'] = Apps
# 	reviews_dict['Home Win %'] = Home_Win
# 	reviews_dict['Away Win %'] = Away_Win
# 	reviews_dict['Draw %'] = Draw
# reviews = driver.find_elements_by_xpath('//*[@id="referee-tournaments-table-body"]/tr')

# for review in reviews:

	

# 	R = review.find_element_by_xpath('.//td[1]').text 
# 	Referee = review.find_element_by_xpath('.//td[2]').text
# 	Apps = review.find_element_by_xpath('.//td[3]').text
# 	Fouls_pg = review.find_element_by_xpath('.//td[4]').text
# 	Fouls_Tackles = review.find_element_by_xpath('.//td[5]').text
# 	Pen_PG = review.find_element_by_xpath('.//td[6]').text
# 	# Yel_PG = review.find_element_by_xpath('.//td[7]/span').text
# 	# Yellow = review.find_element_by_xpath('.//td[8]/span').text
# 	# Red_PG = review.find_element_by_xpath('.//td[9]/span').text
# 	# Red = review.find_element_by_xpath('.//td[10]/span').text	

# 	review_dict['R'] = R
# 	review_dict['Referee'] = Referee
# 	review_dict['Appearances'] = Apps
# 	review_dict['Fouls_per_Game'] = Fouls_pg
# 	review_dict['Fouls_per_Tackle'] = Fouls_Tackles
# 	review_dict['Penalty_per_game'] = Pen_PG
# 	# review_dict['Yellows_per_game'] = Yel_PG
# 	# review_dict['Total_Yellow_Cards'] = Yellow
# 	# review_dict['Reds_per_game'] = Red_PG
# 	# review_dict['Total_Red_Cards'] = Red

# 	writer.writerow(review_dict.values())

# csv_file.close()
driver.close()




