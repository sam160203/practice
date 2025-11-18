from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Step 1: Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()
driver.set_page_load_timeout(20)

# Step 2: Open the website
driver.get("https://imcc.mespune.in/")

wait = WebDriverWait(driver, 20)
actions = ActionChains(driver)

# Step 3: Scroll until "Prominent Recruiters" is visible
header = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h2[contains(text(), 'Prominent Recruiters')]")
    )
)
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", header)
time.sleep(2)

# Step 4: Find logos under the section
logos = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//h2[contains(text(), 'Prominent Recruiters')]/following::img")
    )
)

print("Total logos found:", len(logos))

# Step 5: Drag the 3rd logo if exists
if len(logos) >= 3:
    third_logo = logos[2]
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", third_logo)
    time.sleep(1)

    actions.click_and_hold(third_logo).move_by_offset(-100, 0).release().perform()
    print("Dragged 3rd logo by 100px left.")
    time.sleep(2)

else:
    print("Less than 3 logos found")

# Step 6: Close browser
driver.quit()
