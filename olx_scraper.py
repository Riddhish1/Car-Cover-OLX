from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import random
import pandas as pd
import os

def get_browser_agent():
    agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
    ]
    return random.choice(agents)

def grab_element(browser, selector, timeout=10, attempts=3):
    for try_count in range(attempts):
        try:
            element = WebDriverWait(browser, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            return element
        except (StaleElementReferenceException, TimeoutException):
            if try_count == attempts - 1:
                raise
            time.sleep(1)
    return None

def get_text(element, selector, fallback=""):
    try:
        return element.find_element(By.CSS_SELECTOR, selector).text
    except (NoSuchElementException, StaleElementReferenceException):
        return fallback

def check_car_cover(title, description):
    title = title.lower()
    description = description.lower()
    
    keywords = ['car cover', 'car covers', 'vehicle cover', 'auto cover']
    bad_words = ['parking cover', 'car parking', 'garage', 'house', 'plot', 'apartment']
    
    is_good = any(keyword in title or keyword in description for keyword in keywords)
    is_bad = any(word in title for word in bad_words)
    
    return is_good and not is_bad

def dump_to_csv(items, filename='car_covers.csv'):
    if not items:
        print("Nothing to save")
        return False
        
    try:
        base = os.path.splitext(filename)[0]
        ext = os.path.splitext(filename)[1]
        count = 1
        
        while os.path.exists(filename):
            filename = f"{base}_{count}{ext}"
            count += 1
        
        df = pd.DataFrame(items)
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"Saved {len(items)} items to {filename}")
        return True
    except Exception as e:
        print(f"Failed to save: {str(e)}")
        return False

def scrape_olx(max_pages=5):
    opts = webdriver.ChromeOptions()
    opts.add_argument('--headless')
    opts.add_argument(f'user-agent={get_browser_agent()}')
    opts.add_argument('--disable-gpu')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
    
    browser = webdriver.Chrome(options=opts)
    found_items = []
    
    try:
        start_url = "https://www.olx.in/items/q-car-cover"
        
        for page_num in range(1, max_pages + 1):
            current_url = f"{start_url}?page={page_num}" if page_num > 1 else start_url
            print(f"Checking page {page_num}...")
            
            browser.get(current_url)
            time.sleep(2)
            
            try:
                container = grab_element(browser, '[data-aut-id="itemBox3"]')
                if not container:
                    print(f"Page {page_num} is empty")
                    continue
            except (TimeoutException, StaleElementReferenceException):
                print(f"Page {page_num} timed out")
                continue
            
            items = browser.find_elements(By.CSS_SELECTOR, '[data-aut-id="itemBox3"]')
            
            if not items:
                print(f"No items on page {page_num}")
                break
            
            for item in items:
                try:
                    title = get_text(item, '[data-aut-id="itemTitle"]')
                    details = get_text(item, '[data-aut-id="itemDetails"]')
                    
                    if not check_car_cover(title, details):
                        continue
                    
                    item_data = {
                        'title': title,
                        'price': get_text(item, '[data-aut-id="itemPrice"]'),
                        'location': get_text(item, '[data-aut-id="item-location"]'),
                        'details': details,
                        'image_url': '',
                        'link': ''
                    }
                    
                    try:
                        img = item.find_element(By.CSS_SELECTOR, '[data-aut-id="itemImage"] img')
                        item_data['image_url'] = img.get_attribute('src')
                    except (NoSuchElementException, StaleElementReferenceException):
                        pass
                    
                    try:
                        link = item.find_element(By.CSS_SELECTOR, 'a')
                        item_data['link'] = link.get_attribute('href')
                    except (NoSuchElementException, StaleElementReferenceException):
                        pass
                    
                    if item_data['title'] and item_data['price']:
                        found_items.append(item_data)
                        print(f"Found: {item_data['title']} - {item_data['price']}")
                    
                except Exception as e:
                    print(f"Error with item: {str(e)}")
                    continue
            
            time.sleep(random.uniform(2, 4))
        
        dump_to_csv(found_items)
            
    except Exception as e:
        print(f"Something went wrong: {str(e)}")
        if found_items:
            dump_to_csv(found_items)
        
    finally:
        browser.quit()

if __name__ == "__main__":
    scrape_olx() 