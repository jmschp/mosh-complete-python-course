# 08 Browser Automation

# https://selenium-python.readthedocs.io/

# In this example we are goint to test function on a website, with browser automation.
# Writing a script that will test the log-in function in git hub.

from selenium import webdriver

browser = webdriver.Chrome() # Here we create a browser object

browser.get("https://github.com") # We use the broweser object to navigate to https://github.com

signin_link = browser.find_element_by_link_text("Sign in") # Finding the "Sign in" botton by ist text
signin_link.click()

username_box = browser.find_element_by_id("login_field") # Finding the username filed by the id.
username_box.send_keys("jmschp") # We use the ".send_keys()" method to type the user name in the username field.

password_box = browser.find_element_by_id("password") # Finding the username filed by the id.
password_box.send_keys("17OtteR93") # We use the ".send_keys()" method to type the user name in the username field.
password_box.submit()

# To make sure this log in function worked properly we want to make an assertion

# assert "jmschp" in browser.page_source # The ".page_source" attribute return qthe html content of the webpage. And we are aaserting if the "jmschp" is in that html.


# we can be more spcific with the asserting. like this
profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")

assert "jmschp" in link_label # The ".page_source" attribute return qthe html content of the webpage.

browser.quit()