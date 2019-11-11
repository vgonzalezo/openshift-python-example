#15 -10 EL PRINT DE LOS ARCHIVOS QUE SE DESCARGAN NO ESTA CORRECTO
import urllib
from selenium import webdriver
import time
import os
import random
#from pyvirtualdisplay import Display


from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager

def abrir_chrome(path,carpeta_descargas,url):
    #display = Display(visible=0, size=(800, 800))  
    #display.start()
    #driver = webdriver.Chrome("%s/chromedriver" % path)
    driver = webdriver.PhantomJS()
    #driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    driver.get(f"http://{url}")  
    return driver

def borrar_docs(path,carpeta):
    entries = os.scandir("%s/%s" % (path,carpeta))
    for entry in entries:
        entrypath = "%s/%s/%s" % (path,carpeta,entry.name)
        os.unlink(entrypath)    

def crear_txt(path,indice,carpeta):
    entries = os.scandir(f"{path}/{carpeta}/{indice}")
    print(entries)
    with open(f"output/output_{indice}.txt","w+") as f:
        for entry in entries:
            f.write(f"{entry.name}\n")

def main_tsoft_1(path,cant):
    borrar_docs(path,"Descargas/1")
    driver = abrir_chrome(path,"Descargas","toastytech.com/evil/")
    links = driver.find_elements_by_tag_name("a")
    links = [l.get_attribute("href") for l in links]
    for i in range(int(cant)):
        time.sleep(2)
        driver.get(random.choice(links))
        try:
            name = f"{random.randint(1,101)}_{random.randint(101,201)}_{i}.png"
            with open(f"Descargas/1/{name}", 'wb') as file:
                file.write(driver.find_element_by_tag_name('img').screenshot_as_png)
            print(f"Descarga {name}")
        except Exception as e:
            i = -1
            print(e)
    driver.close()
    crear_txt(path,1,"Descargas")

def main_tsoft_2(path,cant):
    borrar_docs(path,"Descargas\\2")
    driver = abrir_chrome(path,"Descargas","toastytech.com/evil/")
    links = driver.find_elements_by_tag_name("a")
    links = [l.get_attribute("href") for l in links]
    for i in range(int(cant)):
        time.sleep(2)
        driver.get(random.choice(links))
        try:
            name = f"{random.randint(3,301)}_{random.randint(401,501)}_{i}.png"
            with open(f"Descargas\\2\\{name}", 'wb') as file:
                file.write(driver.find_element_by_tag_name('img').screenshot_as_png)
            print(f"Descarga {name}")
        except Exception as e:
            i = -1
            print(e)
    driver.close()
    crear_txt(path,2,"Descargas")

if __name__ == "__main__":
    path = os.getcwd()

    crear_txt(path,2,"Descargas")