from selenium import webdriver
import pandas as pd
import time
class fetch_ZZ500:

    def __init__(self,
                url="http://data.eastmoney.com/other/index/zz500.html",
                btn_last_page = "#PageCont > a:nth-child(8)",
                btn_nxt_page="#PageCont > a:nth-child(9)"):

        self.url = url
        self.path_btn = btn_nxt_page
        self.path_btn_last = btn_last_page
        self.driver = webdriver.Firefox()
        self.result = pd.DataFrame()

        self.__fetch_loop()

    def __fetch_loop(self):
        # Initialize Robot
        self.driver.get(self.url)
        
        # Get number count
        pagenum = int(self.driver.find_element_by_css_selector(self.path_btn_last).text)

        for i in range(pagenum):
            time.sleep(0.5)
            self.result = pd.concat([self.result, self.__fetch_data()])
            # Turn Page
            fp_next = self.driver.find_element_by_css_selector(self.path_btn)
            fp_next.click()

    def __fetch_data(self):
        # Get Table
        colname = self.driver.find_element_by_css_selector("#dt_1 > thead:nth-child(1)").text.replace("\n","").split(" ")
        list_temp = self.driver.find_element_by_tag_name("tbody").text.split('\n')
        tbody = [i.split(" ") for i in list_temp]
        # Pretty Table
        df = pd.DataFrame(tbody)
        df = df.drop(columns=[5,6,7])
        df.columns=colname
        
        return df

    def to_csv(self):
        self.result.to_excel("中证500.xlsx")
        self.driver.close()

if __name__ == "__main__":
    a = fetch_ZZ500()
    a.to_csv()