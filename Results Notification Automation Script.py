import requests
import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# Load the known options from a file (if it exists)
try:
    with open('known_options.json', 'r') as file:
        known_options = json.load(file)
except FileNotFoundError:
    # Define the initial known options
    known_options = {
        'اعدادي لائحة جديدة': ['-'],
        'الاولى لائحة جديدة': ['الهندسة الميكانيكية'],
        'الاولى لائحة جديدة': ['الهندسة الحيوية الطبية'],
        'الثانية': ['الهندسة الحيوية الطبية'],
        'الثالثة': [],
        'الرابعة': [],
    }

# Set up the Selenium webdriver (make sure to install the appropriate browser driver)
driver = webdriver.Chrome()  # Replace with the path to your browser driver (e.g., chromedriver)

# Load the webpage
url = 'PRIVATE'
driver.get(url)

# Discord webhook URL
discord_webhook_url = 'PRIVATE'

# Find the level combo box
level_select_element = driver.find_element(By.NAME, 'x_gro')
level_select = Select(level_select_element)

# Flag to track if there are any new options
new_options_found = False

# Iterate over each option in the level combo box, excluding the first option
for level_option in level_select.options[1:]:
    # Select the current option in the level combo box
    level_select.select_by_value(level_option.get_attribute('value'))

    # Wait for the department combo box to populate with options
    driver.implicitly_wait(3)  # Adjust the wait time if needed

    # Find the department combo box
    department_select_element = driver.find_element(By.NAME, 'x_dep')
    department_select = Select(department_select_element)

    # Get the departments for the selected level
    departments = []
    if len(department_select.options) > 1:
        for department_option in department_select.options[1:]:
            department_name = department_option.text
            departments.append(department_name)

    # Check if the departments for the current level are different from the known options
    if level_option.text in known_options and departments != known_options[level_option.text]:
        # Exclude the already known options from the departments list
        new_departments = [dept for dept in departments if dept not in known_options[level_option.text]]

        if new_departments:
            # Prepare the message to send via Discord webhook
            message = f"New departments for {level_option.text}:\n"
            for department in new_departments:
                message += f"- {department}\n"

            # Send the message to Discord channel via webhook
            payload = {'content': message}
            headers = {'Content-Type': 'application/json'}
            response = requests.post(discord_webhook_url, data=json.dumps(payload), headers=headers)
            if response.status_code == 204:
                print("Notification sent to Discord channel!")

            # Update the known options with the current departments
            known_options[level_option.text] = departments
            new_options_found = True

# Save the updated known options to the file if new options were found
if new_options_found:
    with open('known_options.json', 'w') as file:
        json.dump(known_options, file)

# Close the browser
driver.quit()
