#Imports
import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

#State list
states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware', 'Florida','Georgia','Guam','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Marshall Islands','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Northern Mariana Islands','Ohio','Oklahoma','Oregon','Palau','Pennsylvania','Puerto Rico','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virgin Island','Virginia','Washington','West Virginia','Wisconsin','Wyoming']

#Initiate driver
chromedriver = 'C:/Users/Henry/Desktop/chromedriver'
driver = webdriver.Chrome(chromedriver)

#Loop through all states
for i in states:
    url = ('https://www.google.com/search?source=hp&ei=sqo_XJjIO--xggfBhavIDA&q=marijuana+doctor+' + i + '&btnK=Google+Search&oq=marijuana+doctor+' + i + '&gs_l=psy-ab.3...2922.7594..7738...3.0..0.107.1890.26j3......0....1..gws-wiz.....0..0j0i131j0i22i30.48UsNHAZfaM')
    driver.get(url)
    #Checks to see if there are ads
    try:
        ads = driver.find_elements_by_class_name('ads-ad')
    except NoSuchElementException as exception:
        print('There are no ads')
    #Variable holding description of Ad
    textAds = []
    #Extract Ad text from element
    for a in ads:
        textAds.append(a.text)
    #Variable holding how many ads were found
    howManyAds = len(ads)
    #If ads were found
    if howManyAds > 0:
        print("There were " + str(howManyAds) + " ads found when googling Marijuana Doctor " + i)
        print("These were the ads found :")
        for i in textAds:
            print(i)
        #opens google report ad
        driver.get('https://support.google.com/google-ads/troubleshooter/4578507#ts=6006595')
        #fills out form
        inputs = driver.find_elements_by_tag_name('input')
        inputs[7].send_keys('djhugoi2@hotmail.com')
        illegalDrugs = driver.find_elements_by_class_name('list-item')
        illegalDrugs[2].click()
        inputs[20].send_keys('google.com')
        textArea = driver.find_element_by_tag_name('textarea')
        textArea.send_keys('Ad violates dangerous products or services policy.')
        #Input to continue to the next state
        input("Press Enter to continue...")
    #Else if there are no ads still output to user
    elif howManyAds == 0:
        print("No Ads were found for Marijuana Doctor " + i)
#Close driver
driver.quit()