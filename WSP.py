from bs4 import BeautifulSoup
import requests


def find_job():
    html_text = requests.get('https://www.computrabajo.com.ar/trabajo-de-python?q=python').text

    print('Escriba una zona de trabajo por ejemplo Capital:')
    zone = input('>').title()
    print(f'Buscando en {zone}')

    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('article', class_='box_border hover dFlex vm_fx mbB cp bClick mB_neg_m mb0_m')

    for job in jobs:
        job_outstanding = job.find('span', class_="tag dest mr10 mb10")
        date = job.find('p', class_="fs13 fc_aux")
        if 'horas' or 'dias' in date:
            position = job.find('h1', class_="fs18 fwB").text.replace(' ', '')
            location = job.find('p', class_="fs16 fc_base mt5 mb10").text.replace(' ', '')
            more_info = job.div.h1.a['href']
            if zone in location:
                print(f"Puesto: {position.strip()}")
                print(f"Lugar de trabajo:{location.strip()}")
                print(f'Mas info: {more_info}')
                print('')


if __name__ == '__main__':
    while True:
        find_job()
