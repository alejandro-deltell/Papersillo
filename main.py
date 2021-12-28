from selenium.common.exceptions import NoSuchElementException
import time
from selenium import webdriver


print("\PAPERSILLO v.0.1\n")

chromeOptions = webdriver.ChromeOptions()

win_chromedriver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=win_chromedriver_path, options=chromeOptions)
# driver.set_window_position(-10000, 0)


def wait():
    time.sleep(1)

with open('listado.txt') as list:
    for i in list:
        if i == "\n":
            pass
        else:
            exists = True
            while exists:
                try:
                    driver.get('https://apps.crossref.org/SimpleTextQuery')
                    query = driver.find_element_by_xpath('//*[@id="freetext"]')
                    query.send_keys(i)
                    submit_button = driver.find_element_by_xpath('//*[@id="mainContent2"]/div/form/font/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[12]/td/input')
                    submit_button.click()
                    url = driver.find_element_by_xpath('/html/body/div[3]/div/div/form/font/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[5]/td/table/tbody/tr[1]/td/a').text
                    driver.get('https://sci-hubtw.hkvisa.net/')
                    search_sci_hub = driver.find_element_by_xpath('//*[@id="input"]/form/input[2]')
                    search_sci_hub.send_keys(url)
                    driver.find_element_by_xpath('//*[@id="open"]/p').click()
                    # download_element = driver.find_element_by_xpath('//*[@id="buttons"]/ul/li[2]/a').click()
                    wait()
                    # response = requests.get(download_url, allow_redirects=False)

                    # Download file with bs:

                    download_url = driver.current_url
                    print(download_url)



                    # Rename the pdf files to i:


                    download = driver.find_element_by_xpath('//*[@id="buttons"]/ul/li[2]/a')
                    download.click()

                    print(f"Descargando {i}\n")
                    with open("Encontrados.txt", "a") as found:
                        found.writelines(f"{i}\n")
                    exists = False

                except NoSuchElementException:
                    print(f"{i} no encontrado.")
                    with open("No encontrados.txt", "a") as not_found:
                        not_found.writelines(f"{i}\n")
                    exists = False


    time.sleep(15)
    driver.quit()