#This is a script that will execute all tests uploaded with their given steps

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import unittest


class Runner(unittest.TestCase):
  
  def setUp(self):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    #.driver = webdriver.Chrome()
    #self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test1(self):
    self.driver.get("https://mybase.psg.co.za/index.php?c=index/vlogin&z=c_eq_index/xhome")
    self.driver.set_window_size(968, 672)
    self.driver.find_element(By.ID, "mybase_login_idnr").click()
    self.driver.find_element(By.ID, "mybase_login_idnr").send_keys("40690471")
    element = self.driver.find_element(By.ID, "mybase_login_idnr")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "mybase_login_idnr").click()
    self.driver.find_element(By.ID, "loginbtn_next").click()
    self.driver.find_element(By.ID, "passwordInput").click()
    self.driver.find_element(By.ID, "passwordInput").send_keys("P@ssword1")
    self.driver.find_element(By.ID, "submitButton").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dib:nth-child(2)").click()
  
if __name__=='__main__':
  unittest.main()