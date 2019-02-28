"""
Google ads does not allow ads for subrances that alter metal state for the purpose of recreation
or otherwise induce "highs"

This script is meant to find ads that are Marijuana related and to report them to Google AdWords
"""

#Imports
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os

#State list
states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware', 'Florida','Georgia','Guam','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Marshall Islands','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Palau','Pennsylvania','Puerto Rico','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virgin Island','Virginia','Washington','West Virginia','Wisconsin','Wyoming']

#Keywords to append to state search query
#Add keywords to his variable
keywords = ['Marijuana Card', 'Marijuana Clinic', 'Marijuana Doctor', 'MMJ Card', 'MMJ Doctor', 'Cannabis Doctor', 'Medical Marijuana', 'Medical Cannabis']

#Get desktop location that is where chromedriver is installed
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
chromedriver = desktop + '/chromedriver'

#Initiate Driver
driver = webdriver.Chrome(chromedriver)

#Loop through states and keywords and append to google query
for x in states:
    for i in keywords:
        #Split keywords so we can add a '+' in bewteen 
        p = i.split(' ')
        #Driver get the URL 
        driver.get('https://www.google.com/search?q=' + p[0].lower() + '+' + p[1].lower() + '+' + x.lower() +'&rlz=1C1CHBF_enUS815US815&oq=cannabis+doctor+alabama&aqs=chrome..69i57.6359j0j1&sourceid=chrome&ie=UTF-8')
        #Element is always visiable wether there are ads or not
        #If there are no ads the length of ads will be 0
        ads = ads = driver.find_elements_by_class_name('ads-ad')
        #Holds text extracted from web elements
        textAds = []
        #If statement for no ads
        if len(ads) == 0:
            print('No ads found: ' + i + ' ' + x)
            time.sleep(2)
        else:
            pass
        #If statement if 1 add was found
        if len(ads) == 1:
            #Let user know how many ads were found and what search it came from
            print('One ad was found: ' + i + ' ' + x)
            print(' ')
            #Split ad by new line character
            for ad in ads:
                a = ad.text.split('\n')
            #Loop through the split ads
            for b in a:
                #If statement to find website from ads extracted text
                if 'Adwww.' in b:
                    websiteText = print('Website: ' + b)    
            #Output for user to see if they would like to report the ad 
            print('Ad Name: ' + a[0])
            websiteText
            #User input if ad should be reported
            report = input('Would you like to report Y/N >>>>>>>>>>> ').upper()
            #If statement to check if user wants to report ad
            if report == 'Y':
                #User input to see what email should be used to report ad
                email = input('What email would you like to use >>>>>>> ')
                #Initiate a new driver
                reportDriver = webdriver.Chrome(chromedriver)
                #Navigate to google ad words report page
                reportDriver.get('https://support.google.com/google-ads/troubleshooter/4578507#ts=6006595')
                #Fill out section of form that program can fill out
                reportDriver.find_element_by_name('Contact_Email').send_keys(email)
                reportDriver.find_element_by_css_selector('#vio_other_aw_policy > div:nth-child(2) > div:nth-child(3) > label > label > div.material-radio__circle').click()
                reportDriver.find_element_by_name('url_viewed').send_keys('www.google.com')
                reportDriver.find_element_by_tag_name('textarea').send_keys('Ad violates dangerous products or services policy.')
                print(' ')
                #Input to wait for user to fill out form
                input('Press enter to continue >>>')
                #Close driver
                reportDriver.quit()
                print(' ')
        #If statement for 2 ads
        if len(ads) == 2:
            #Output to user to let them know how many ads were found and what search it came from
            print('Two ads were found: ' + i + ' ' + x)
            print(' ')
            #loop through ads to split by new line character 
            #and extract text from the web elements and append to splitads
            splitAds = []
            for ad in ads:
                splitAds.append(ad.text.split('\n'))
            #Loop through list of splitAds and append to ad website and name variables
            adWebsites = []
            adNames = []
            for splitAd in splitAds:
                for y in splitAd:
                    #Loop through the elements within the list to find the website
                    if 'Adwww' in y:
                        adWebsites.append(y)
                #Name will always be the first element
                adNames.append(splitAd[0])
            #Output for user so they can decided to report or not
            print('First Ad')
            print('Ad Name:    ' + adNames[0])
            print('Ad Website: ' + adWebsites[0])
            #Recieve user input if they would like to report ad
            report = input('Would you like to report Y/N >>>>>>>>>>> ').upper()
            ##If statement if they choose to report ad
            #Else program will continue
            if report == 'Y':
                #User input to see what email should be used to report ad
                email = input('What email would you like to use >>>>>>> ')
                #Initiate a new driver
                reportDriver = webdriver.Chrome(chromedriver)
                #Navigate to google ad words report page
                reportDriver.get('https://support.google.com/google-ads/troubleshooter/4578507#ts=6006595')
                #Fill out section of form that program can fill out
                reportDriver.find_element_by_name('Contact_Email').send_keys(email)
                reportDriver.find_element_by_css_selector('#vio_other_aw_policy > div:nth-child(2) > div:nth-child(3) > label > label > div.material-radio__circle').click()
                reportDriver.find_element_by_name('url_viewed').send_keys('www.google.com')
                reportDriver.find_element_by_tag_name('textarea').send_keys('Ad violates dangerous products or services policy.')
                print(' ')
                #Input to wait for user to fill out form
                input('Press enter to continue >>>')
                #Close driver
                reportDriver.quit()
                print(' ')
            #Output for user so they can decided to report or not
            print('Second Ad')
            print('Ad Name:    ' + adNames[1])
            print('Ad Website: ' + adWebsites[1])
            #User input if ad should be reported
            report = input('Would you like to report Y/N >>>>>>>>>>> ').upper()
            #If statement to check if user wants to report ad
            if report == 'Y':
                #User input to see what email should be used to report ad
                email = input('What email would you like to use >>>>>>> ')
                #Initiate a new driver
                reportDriver = webdriver.Chrome(chromedriver)
                #Navigate to google ad words report page
                reportDriver.get('https://support.google.com/google-ads/troubleshooter/4578507#ts=6006595')
                #Fill out section of form that program can fill out
                reportDriver.find_element_by_name('Contact_Email').send_keys(email)
                reportDriver.find_element_by_css_selector('#vio_other_aw_policy > div:nth-child(2) > div:nth-child(3) > label > label > div.material-radio__circle').click()
                reportDriver.find_element_by_name('url_viewed').send_keys('www.google.com')
                reportDriver.find_element_by_tag_name('textarea').send_keys('Ad violates dangerous products or services policy.')
                print(' ')
                #Input to wait for user to fill out form
                input('Press enter to continue >>>')
                #Close driver
                reportDriver.quit()
                print(' ')
        #If statement for 3 ads
        if len(ads) == 3:
            #Output to user to let them know how many ads were found and what search it came from
            print('Three ads were found: ' + i + ' ' + x)
            #loop through ads to split by new line character 
            #and extract text from the web elements and append to splitads            
            splitAds = []
            for ad in ads:
                splitAds.append(ad.text.split('\n'))
            #Loop through list of splitAds and append to ad website and name variables        
            adWebsites = []
            adNames = []
            for splitAd in splitAds:
                for y in splitAd:
                    #Loop through the elements within the list to find the website
                    if 'Adwww' in y:
                        adWebsites.append(y)
                #Name will always be the first element
                adNames.append(splitAd[0])
            #Output for user so they can decided to report or not
            print('First Ad')
            print('Ad Name:    ' + adNames[0])
            print('Ad Website: ' + adWebsites[0])
            #Recieve user input if they would like to report ad
            report = input('Would you like to report Y/N >>>>>>>>>>> ').upper()
            ##If statement if they choose to report ad
            #Else program will continue
            if report == 'Y':
                #User input to see what email should be used to report ad
                email = input('What email would you like to use >>>>>>> ')
                #Initiate a new driver
                reportDriver = webdriver.Chrome(chromedriver)
                #Navigate to google ad words report page
                reportDriver.get('https://support.google.com/google-ads/troubleshooter/4578507#ts=6006595')
                #Fill out section of form that program can fill out
                reportDriver.find_element_by_name('Contact_Email').send_keys(email)
                reportDriver.find_element_by_css_selector('#vio_other_aw_policy > div:nth-child(2) > div:nth-child(3) > label > label > div.material-radio__circle').click()
                reportDriver.find_element_by_name('url_viewed').send_keys('www.google.com')
                reportDriver.find_element_by_tag_name('textarea').send_keys('Ad violates dangerous products or services policy.')
                print(' ')
                #Input to wait for user to fill out form
                input('Press enter to continue >>>')
                #Close driver
                reportDriver.quit()
                print(' ')
            #Output for user so they can decided to report or not    
            print('Second Ad')
            print('Ad Name:    ' + adNames[1])
            print('Ad Website: ' + adWebsites[1])
            #User input if ad should be reported
            report = input('Would you like to report Y/N >>>>>>>>>>> ').upper()
            #If statement to check if user wants to report ad
            if report == 'Y':
                #User input to see what email should be used to report ad
                email = input('What email would you like to use >>>>>>> ')
                #Initiate a new driver
                reportDriver = webdriver.Chrome(chromedriver)
                #Navigate to google ad words report page
                reportDriver.get('https://support.google.com/google-ads/troubleshooter/4578507#ts=6006595')
                #Fill out section of form that program can fill out
                reportDriver.find_element_by_name('Contact_Email').send_keys(email)
                reportDriver.find_element_by_css_selector('#vio_other_aw_policy > div:nth-child(2) > div:nth-child(3) > label > label > div.material-radio__circle').click()
                reportDriver.find_element_by_name('url_viewed').send_keys('www.google.com')
                reportDriver.find_element_by_tag_name('textarea').send_keys('Ad violates dangerous products or services policy.')
                print(' ')
                #Input to wait for user to fill out form
                input('Press enter to continue >>>')
                #Close driver
                reportDriver.quit()
                print(' ')
            #Output for user so they can decided to report or not
            print('Third Ad')
            print('Ad Name:    ' + adNames[2])
            print('Ad Website: ' + adWebsites[2])
            #User input if ad should be reported
            report = input('Would you like to report Y/N >>>>>>>>>>> ').upper()
            #If statement to check if user wants to report ad
            if report == 'Y':
                #User input to see what email should be used to report ad
                email = input('What email would you like to use >>>>>>> ')
                #Initiate a new driver
                reportDriver = webdriver.Chrome(chromedriver)
                #Navigate to google ad words report page
                reportDriver.get('https://support.google.com/google-ads/troubleshooter/4578507#ts=6006595')
                #Fill out section of form that program can fill out
                reportDriver.find_element_by_name('Contact_Email').send_keys(email)
                reportDriver.find_element_by_css_selector('#vio_other_aw_policy > div:nth-child(2) > div:nth-child(3) > label > label > div.material-radio__circle').click()
                reportDriver.find_element_by_name('url_viewed').send_keys('www.google.com')
                reportDriver.find_element_by_tag_name('textarea').send_keys('Ad violates dangerous products or services policy.')
                print(' ')
                #Input to wait for user to fill out form
                input('Press enter to continue >>>')
                #Close driver
                reportDriver.quit()
                print(' ') 

        #If statement for 4 ads                                           
        if len(ads) == 4:
            #Output to user to let them know how many ads were found and what search it came from
            print('Four ads were found: ' + i + ' ' + x)
            #loop through ads to split by new line character 
            #and extract text from the web elements and append to splitads             
            splitAds = []
            for ad in ads:
                splitAds.append(ad.text.split('\n'))
            #Loop through list of splitAds and append to ad website and name variables        
            adWebsites = []
            adNames = []
            for splitAd in splitAds:
                for y in splitAd:
                    #Loop through the elements within the list to find the website
                    if 'Adwww' in y:
                        adWebsites.append(y)
                #Name will always be the first element
                adNames.append(splitAd[0])
            #Output for user so they can decided to report or not
            print('First Ad')
            print('Ad Name:    ' + adNames[0])
            print('Ad Website: ' + adWebsites[0])
            #Recieve user input if they would like to report ad
            report = input('Would you like to report Y/N >>>>>>>>>>> ').upper()
            ##If statement if they choose to report ad
            #Else program will continue            
            if report == 'Y':
                #User input to see what email should be used to report ad
                email = input('What email would you like to use >>>>>>> ')
                #Initiate a new driver
                reportDriver = webdriver.Chrome(chromedriver)
                #Navigate to google ad words report page
                reportDriver.get('https://support.google.com/google-ads/troubleshooter/4578507#ts=6006595')
                #Fill out section of form that program can fill out
                reportDriver.find_element_by_name('Contact_Email').send_keys(email)
                reportDriver.find_element_by_css_selector('#vio_other_aw_policy > div:nth-child(2) > div:nth-child(3) > label > label > div.material-radio__circle').click()
                reportDriver.find_element_by_name('url_viewed').send_keys('www.google.com')
                reportDriver.find_element_by_tag_name('textarea').send_keys('Ad violates dangerous products or services policy.')
                print(' ')
                #Input to wait for user to fill out form
                input('Press enter to continue >>>')
                #Close driver
                reportDriver.quit()
                print(' ')
            #Output for user so they can decided to report or not  
            print('Second Ad')
            print('Ad Name:    ' + adNames[1])
            print('Ad Website: ' + adWebsites[1])
            #User input if ad should be reported
            report = input('Would you like to report Y/N >>>>>>>>>>> ').upper()
            #If statement to check if user wants to report ad
            if report == 'Y':
                #User input to see what email should be used to report ad
                email = input('What email would you like to use >>>>>>> ')
                #Initiate a new driver
                reportDriver = webdriver.Chrome(chromedriver)
                #Navigate to google ad words report page
                reportDriver.get('https://support.google.com/google-ads/troubleshooter/4578507#ts=6006595')
                #Fill out section of form that program can fill out
                reportDriver.find_element_by_name('Contact_Email').send_keys(email)
                reportDriver.find_element_by_css_selector('#vio_other_aw_policy > div:nth-child(2) > div:nth-child(3) > label > label > div.material-radio__circle').click()
                reportDriver.find_element_by_name('url_viewed').send_keys('www.google.com')
                reportDriver.find_element_by_tag_name('textarea').send_keys('Ad violates dangerous products or services policy.')
                print(' ')
                #Input to wait for user to fill out form
                input('Press enter to continue >>>')
                #Close driver
                reportDriver.quit()
                print(' ')
            #Output for user so they can decided to report or not
            print('Third Ad')
            print('Ad Name:    ' + adNames[2])
            print('Ad Website: ' + adWebsites[2])
            #User input if ad should be reported
            report = input('Would you like to report Y/N >>>>>>>>>>> ').upper()
            #If statement to check if user wants to report ad
            if report == 'Y':
                #User input to see what email should be used to report ad
                email = input('What email would you like to use >>>>>>> ')
                #Initiate a new driver
                reportDriver = webdriver.Chrome(chromedriver)
                #Navigate to google ad words report page
                reportDriver.get('https://support.google.com/google-ads/troubleshooter/4578507#ts=6006595')
                #Fill out section of form that program can fill out
                reportDriver.find_element_by_name('Contact_Email').send_keys(email)
                reportDriver.find_element_by_css_selector('#vio_other_aw_policy > div:nth-child(2) > div:nth-child(3) > label > label > div.material-radio__circle').click()
                reportDriver.find_element_by_name('url_viewed').send_keys('www.google.com')
                reportDriver.find_element_by_tag_name('textarea').send_keys('Ad violates dangerous products or services policy.')
                print(' ')
                #Input to wait for user to fill out form
                input('Press enter to continue >>>')
                #Close driver
                reportDriver.quit()
                print(' ')  
            #Output for user so they can decided to report or not
            print('Fourth Ad')
            print('Ad Name:    ' + adNames[3])
            print('Ad Website: ' + adWebsites[3])
            #User input if ad should be reported
            report = input('Would you like to report Y/N >>>>>>>>>>> ').upper()
            #If statement to check if user wants to report ad
            if report == 'Y':
                #User input to see what email should be used to report ad
                email = input('What email would you like to use >>>>>>> ')
                #Initiate a new driver
                reportDriver = webdriver.Chrome(chromedriver)
                #Navigate to google ad words report page
                reportDriver.get('https://support.google.com/google-ads/troubleshooter/4578507#ts=6006595')
                #Fill out section of form that program can fill out
                reportDriver.find_element_by_name('Contact_Email').send_keys(email)
                reportDriver.find_element_by_css_selector('#vio_other_aw_policy > div:nth-child(2) > div:nth-child(3) > label > label > div.material-radio__circle').click()
                reportDriver.find_element_by_name('url_viewed').send_keys('www.google.com')
                reportDriver.find_element_by_tag_name('textarea').send_keys('Ad violates dangerous products or services policy.')
                print(' ')
                #Input to wait for user to fill out form
                input('Press enter to continue >>>')
                #Close driver
                reportDriver.quit()
                print(' ')                            
        #If statement to let user know there are more than 4 ads time to update code
        if len(ads) > 4:
            print('There are ' + str(len(ads)) + ' ads in this search.')
            print('Update code to handle ' + str(len(ads)) + ' ads.')