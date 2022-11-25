from selenium.common import exceptions
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BotController:
    def __init__(self, your_driver):
        self.driver = your_driver

    def find_element_xpath(self, xpath_exp, focus_on=None, delay_after=0, delay_before=0):
        try:
            time.sleep(delay_before)
            result = self.driver.find_element(By.XPATH, xpath_exp)
            if focus_on:
                self.driver.execute_script('arguments[0].scrollIntoView();', result)
            time.sleep(delay_after)
            return result
        except exceptions.StaleElementReferenceException as elem_error:
            print(elem_error)
            return ''
        except exceptions.NoSuchElementException as elem_error:
            print(elem_error)
            return ''

    def get_page(self, url, delay_after=0, delay_before=0):
        try:
            time.sleep(delay_before)
            self.driver.get(url)
            self.driver.maximize_window()
            time.sleep(delay_after)
        except exceptions.TimeoutException as elem_error:
            raise BrokenPipeError("Timeout error")
        except exceptions.SessionNotCreatedException as elem_error:
            pass
            # raise BrokenPipeError("Problems with version of chromedriver")

    def find_elements_xpath(self, xpath_exp, elem_name='element', focus_on=None, delay_before=0, delay_afeter=0):
        time.sleep(delay_before)
        results = self.driver.find_elements(By.XPATH, xpath_exp)
        if focus_on:
            self.driver.execute_script('arguments[0].scrollIntoView();', results)
        time.sleep(delay_afeter)
        return results

    def send_info_xpath_element(self, xpath_exp, info):
        try:
            self.find_element_xpath(xpath_exp=xpath_exp).send_keys(info)
        except exceptions.NoSuchElementException:
            raise BrokenPipeError("there is no such element")
        except exceptions.ElementNotInteractableException:
            raise BrokenPipeError("there is no element")
        except exceptions.ElementClickInterceptedException:
            raise BrokenPipeError("click intercepted")

    def execute_javascript(self, script, element=None, script_name="default", delay_before=0, delay_after=0):
        try:
            if not element:
                time.sleep(delay_before)
                self.driver.execute_script(script)
                time.sleep(delay_after)
                return True
            else:
                time.sleep(delay_before)
                self.driver.execute_script(script, element)
                time.sleep(delay_after)
                return True
        except exceptions.JavascriptException as jserr:
            print(jserr)
            raise BrokenPipeError("error in page while executing JS")

    def js_click(self, element, elem_name="default", delay_before_click=0, delay_after_click=0, focus_on=None):
        try:
            time.sleep(delay_before_click)
            if focus_on:
                self.driver.execute_script("'arguments[0].scrollIntoView();'", element)
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(delay_after_click)
            return True
        except exceptions.JavascriptException as jserr:
            print(jserr)
            return False
        except Exception as err:
            print(err)
            return False

    def js_get_string_from_xpath(self, locator_xpath, script_name="default"):
        try:
            result_text = self.driver.execute_script(
                f"var xpath = function(xpathToExecute){{"
                f"var result = '';"
                f"var nodesSnapshot = document.evaluate(xpathToExecute, document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null );"
                f"for ( var i=0 ; i < nodesSnapshot.snapshotLength; i++ ){{"
                f"result+=nodesSnapshot.snapshotItem(i).data+' ';"
                f"}} return result; }};"
                f"return xpath('{locator_xpath}');"
            )
            return result_text
        except exceptions.JavascriptException as jserr:
            print(jserr)
            return False
        except Exception as err:
            print(err)
            return False

    def econdition_click(self, locator_xpath, elem_name="default", timeout=6, just_wait=None):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, locator_xpath)))
        if just_wait:
            return True
        element.click()
        return True

    def close_alert(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present(),
                                                'Timed out waiting for PA creation ' +
                                                'confirmation popup to appear.')

            alert = self.driver.switch_to.alert
            alert.dismiss()
        except exceptions.TimeoutException:
            pass

    @staticmethod
    def get_text_from_element(input_element):
        result_list = []
        if isinstance(input_element, list):
            for elem in input_element:
                if elem:
                    if isinstance(elem, list):
                        anidate_list = []
                        for el in elem:
                            anidate_list.append(el.text)
                        result_list.append(anidate_list)
                    else:
                        text_element = elem.text
                        result_list.append(text_element)
                else:
                    result_list.append(elem)
            return result_list
        if input_element != '':
            return input_element.text
        else:
            return input_element

    @staticmethod
    def force_backspace(elem, times=15):
        """ this method force errase info for a textfield, this is usefull when in a textbox field
        we got DEFAULT TEXT written instead an EMPTY FIELD with or without placeholder"""
        for click in range(times):
            elem.send_keys(Keys.BACK_SPACE)
        return elem
