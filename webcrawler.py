from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def search_for_compound(scraper, compound_name):
    driver, url = scraper
    driver.get(url)
    search = driver.find_element(By.CSS_SELECTOR, '[id^="search"]')
    search.send_keys(compound_name)
    search.send_keys(Keys.RETURN)


def name_match(title, compound):
    match = True
    compound_words = compound.lower().split(' ')
    for word in range(min(len(compound_words), 2)):
        if compound_words[word] not in title.text.lower():
            match = False
    return match


def retrieve_value(page_text, compound_property):
    value = float('NaN')
    if compound_property in page_text:
        split_string = page_text.split(f'{compound_property} ')
        further_split_string = split_string[1].split(' ')
        value = further_split_string[0]
    return float(value)


def set_up_blank_dictionary():
    blank_dictionary = {'retrieval_failure': False,
                        'Molecular Weight': float('NaN'),
                        'Hydrogen Bond Donor Count': float('NaN'),
                        'Hydrogen Bond Acceptor Count': float('NaN'),
                        'Rotatable Bond Count': float('NaN'),
                        'Topological Polar Surface Area': float('NaN'),
                        'Heavy Atom Count': float('NaN')
                        }
    return blank_dictionary


def navigate_to_compound_page(compound_name, scraper_details):
    driver = scraper_details[0]
    search_for_compound(scraper_details, compound_name)
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, '[class=" capitalized"]')))
    link = driver.find_element(By.CSS_SELECTOR, '[class=" capitalized"]')
    link.click()
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, '[class="m-zero p-zero"]')))
    title = driver.find_element(By.CSS_SELECTOR, '[class="m-zero p-zero"]')
    return title


def find_missing_values(compound_details):
    properties = set_up_blank_dictionary()
    scraper = webdriver.Chrome('./chromedriver.exe'), 'https://pubchem.ncbi.nlm.nih.gov/'
    try:
        properties = fetch_data(compound_details, scraper, properties)
    except Exception:
        properties['retrieval_failure'] = True
    finally:
        scraper[0].close()
    return properties


def fetch_data(compound_details, scraper, properties):
    title = navigate_to_compound_page(compound_details[0], scraper)
    driver = scraper[0]
    web_formula = find_formula_on_page(driver)
    if compound_match(compound_details, title, web_formula):
        table = driver.find_element(By.CSS_SELECTOR, '[id="Computed-Properties"]')
        for key in properties:
            properties[key] = retrieve_value(table.text, key)
        properties['retrieval_failure'] = False
        properties['Molecular Formula'] = web_formula
        return properties
    else:
        properties['retrieval_failure'] = True
        return properties


def find_formula_on_page(driver):
    web_formula = ''
    forbidden_sub_strings = ['.', '(', ' ', '=', 'PubChem', 'Wikipedia']
    web_formula_section = driver.find_element(By.CSS_SELECTOR, '[id="Molecular-Formula"]')
    web_formula_strings = web_formula_section.text.split('\n')
    for string in web_formula_strings:
        if any(sub_string in string for sub_string in forbidden_sub_strings):
            pass
        else:
            web_formula = string
    return web_formula


def compound_match(compound_details, title, web_formula):
    compound_name = compound_details[0]
    formula = compound_details[1]
    if isinstance(formula, str) and formula in web_formula:
        return True
    else:
        return name_match(title, compound_name)
