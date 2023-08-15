import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.time = 200

    def findById(self, id, all=False):
        try:
            element = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.ID, id))
            )
            return element
        except Exception as e:
            print("Houve um erro em findById")
            print(e)

    def findByClass(self, className, all=False):
        try:
            if all:
                elements = WebDriverWait(self.driver, self.time).until(
                    EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, className))
                )
                return elements

            element = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.CLASS_NAME, className))
            )
            return element
        except Exception as e:
            print("Houve um erro em findByClass")
            print(e)

    def findAndWrite(self, value, id, pressEnter=False, pressTab=False):
        try:
            element = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.ID, id))
            )
            time.sleep(2)
            try:
                element.clear()
            except ElementNotInteractableException:
                pass
            time.sleep(2)
            element.send_keys(value)

            if pressEnter:
                time.sleep(2)
                element.send_keys(Keys.ENTER)
            if pressTab:
                time.sleep(2)
                element.send_keys(Keys.TAB)

        except Exception as e:
            print("Houve um erro em findAndWrite")
            print(e)

    def findAndClick(self, id):
        try:
            element = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.ID, id))
            )
            time.sleep(5)
            element.click()

        except Exception as e:
            element = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.ID, id))
            )
            time.sleep(5)
            element.click()

    def closeAll(self):
        try:
            elements = self.finAllByCssSelector(
                "a.x-tab-strip-close", all=True)
            for element in elements:
                try:
                    element.click()
                except Exception as e:
                    pass
                time.sleep(2)
        except Exception as e:
            pass

    def findAndClickByClass(self, id):
        try:
            element = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.CLASS_NAME, id))
            )
            element.click()
        except Exception as e:
            print("Houve um erro em findAndClickByClass")
            print(e)

    def switchToCotext(self, id):
        try:
            element = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.ID, id))
            )
            self.driver.switch_to.frame(element)
        except Exception as e:
            print("Houve um erro em switchToCotext")
            print(e)

    def ReturnToMainContext(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print("Houve um erro em ReturnToMainContext")
            print(e)

    def findAndDoubleClick(self, id):
        try:
            element = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.ID, id))
            )
            self.actions.double_click(element).perform()
        except Exception as e:
            print("Houve um erro em findAndDoubleClick")
            print(e)

    def findAndClickArray(self, ids, isDuble=False):
        for id in ids:
            element = WebDriverWait(self.driver, self.time).until(
                EC.visibility_of_element_located((By.ID, id))
            )
            WebDriverWait(self.driver, self.time).until(
                EC.element_to_be_clickable(element)
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            
            if isDuble:
                self.actions.double_click(element).perform()
            else:
                element.click()

            time.sleep(2)        

    def inputFormMultiple(self, data):
        try:
            for obj in data:
                self.findAndWrite(obj['value'], obj['id'])
        except Exception as e:
            print("Houve um erro em inputFormMultiple")
            print(e)

    def findByXpathAndClick(self, xpath, isDuble=False, element="div"):
        try:
            path = f"//{element}[contains(text(), {xpath})]"
            element = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
            if isDuble:
                self.actions.double_click(element).perform()
            else:
                element.click()
        except Exception as e:
            print("Houve um erro em findByXpathAndClick")
            print(e)

    def WriteCNPJ(self, value, id):
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.ID, id))
        )
        self.driver.execute_script(
            "arguments[0].value = arguments[1];", element, value)

    def pressEnter(self, id):
        time.sleep(3)
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.ID, id))
        )
        element.send_keys(Keys.ENTER)

    def attribute_value_is_false(self, locator, attribute):
        element = self.driver.find_element(*locator)
        return element.get_attribute(attribute) == 'false'

    def awaitLoad(self, timeout=60):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(lambda driver: self.attribute_value_is_false(
                (By.ID, 'DynamicGrid_refresh'), 'aria-disabled'))
        except Exception as e:
            print("Houve um erro em awaitLoad")
            print(e)

    def awaitSave(self, selector, class_name=False):

        for seg in range(0, 60):
            try:
                if class_name:
                    elemento = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, selector)))
                else:
                    elemento = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.ID, selector)))
            except TimeoutException:
                break

            time.sleep(1)

    def insert_value_integration(self, value):
        time.sleep(5)

        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input.x-form-field.x-form-text[style='width: 268px;']"))

        )
        time.sleep(5)

        element.send_keys(value)

    def button_value_integration(self):
        elements = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "button.x-btn-text[style='position: relative; width: 69px;']"))

        )
        for element in elements:
            if (element.text == "Ok"):
                time.sleep(5)
                element.click()
                break

    def findAndClickByCss(self, css):
        time.sleep(5)
        element = WebDriverWait(self.driver, self.time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css))

        )
        element.click()

    def find_element_by_css(self, css):
        try:
            element = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css))
            )
            return element
        except Exception as e:
            print(f"Erro ao encontrar o elemento com CSS '{css}': {str(e)}")
            return None
        
    def finAllByCssSelector(self, cssSelector, all=False):
        try:
            if all:
                elements = WebDriverWait(self.driver, self.time).until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, cssSelector))
                )

                return elements
            element = WebDriverWait(self.driver, self.time).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, cssSelector))
            )
            return element
        except Exception as e:
            pass

    def teste(self):
        # Verifica se o elemento está presente na página
        element_present = EC.presence_of_element_located((By.ID, "rowNum-0"))
        WebDriverWait(self.driver, 20).until(element_present)

        # Verifica se o elemento está clicável
        element_clickable = EC.element_to_be_clickable((By.ID, "rowNum-0"))
        WebDriverWait(self.driver, 20).until(element_clickable)
        # Clica no elemento
        element = self.findById("rowNum-0")
        print(element)
        element.click()

        self.driver.refresh()

    def reaload(self):
        self.driver.refresh()

    def buttonDireito(self):

        elment = self.finAllByCssSelector(
            "td.x-grid3-col.x-grid3-cell.x-grid3-td-SETOR")
        self.actions.context_click(elment).perform()
