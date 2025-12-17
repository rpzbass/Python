import subprocess
import time
import requests 
from bs4 import BeautifulSoup


url =  "http://192.168.30.7/4sensor.htm"



while(True):
    time.sleep(120)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    temperatura = soup.select_one("table tr:nth-of-type(1) td:nth-of-type(2)").text.strip()
    temperatura_fix = temperatura.replace("º", "").replace("C", "")
    print(temperatura_fix)

    if (temperatura_fix >= "25.0"):
        print(f'Temperatura muito alta')
        subprocess.run(['msg', '*', 'ALERTA TEMPERATURA DATACENTER AUMENTANDO 25ºC !!!!!'])
        
        

        