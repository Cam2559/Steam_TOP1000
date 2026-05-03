from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

driver = webdriver.Chrome()
driver.get("https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam")

wait = WebDriverWait(driver, 20)


wait.until(EC.presence_of_element_located((By.ID, "main_stats")))

stats = driver.find_element(By.ID, "main_stats")


targets = [
    ("OS Version", "#osversion_stats_row", "#osversion_details"),
    ("System RAM", "#cat0_stats_row", "#cat0_details"),
    ("Physical CPUs", "#cat2_stats_row", "#cat2_details"),
    ("Video Card Description", "#cat3_stats_row", "#cat3_details"),
]

results = {}

for name, row_selector, detail_selector in targets:
    
    row = stats.find_element(By.CSS_SELECTOR, row_selector)
    driver.execute_script("arguments[0].click();", row)

    
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR, detail_selector).text.strip() != "")

   
    title = row.find_element(By.CSS_SELECTOR, ".stats_col_left").text.strip()

    
    details = stats.find_element(By.CSS_SELECTOR, detail_selector).text.strip()

    results[name] = {
        "title": title,
        "details": details
    }

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

stats_info = []

for category, content in results.items():
    text = content["details"]

    blocks = text.split("\n\n")

    for b in blocks:
        parts = b.strip().split("\n")

        if len(parts) >= 2:
            name = parts[0].strip()
            percent = re.search(r"[\d.]+%", parts[1])

            if percent:
                stats_info.append([category, name, percent.group()])

df = pd.DataFrame(stats_info, columns=["Items", "Name", "Percent"])

df.to_csv("D:\Steam_top1000\Data\hw_survey.csv")

driver.quit()






