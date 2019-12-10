import requests
import json

data = dict()

TOKEN = '1046403625:AAG2y-Tk5OvYsVqW8PMIBC8G9EgZgDojcxQ'

def parse(INN):
    req = requests.get(f"https://api.crftr.net/v1/org/?inn={INN}&apikey={TOKEN}")
    file = json.loads(req.text)
    if file['total'] ==1:
        data['Название организации'] = file['items'][0]['fullName']
        data['Регион'] = file['items'][0]['regionName'] + ' ' + file['items'][0]['regionCode']
        data['Тип'] = file['items'][0]['opfType']
        data['Статус'] = file['items'][0]['egrulStatus']
        data['ОГРН'] = file['items'][0]['ogrn']
        data['ИНН'] = file['items'][0]['inn']
        data['КПП'] = file['items'][0]['kpp']
        data['Гранты'] = file['items'][0]['incomeDetail']['grants']['totalSum']
        data['Субсидии'] = file['items'][0]['incomeDetail']['fedSubsidies']['totalSum']
        data['Контракты'] = int(
            file['items'][0]['incomeDetail']['contracts44']['totalSum'] + file['items'][0]['incomeDetail']['contracts94'][
                'totalSum'] + file['items'][0]['incomeDetail']['contracts223']['totalSum'])
        data['Ссылка'] = 'https://openngo.ru/organization/' + file['items'][0]['ogrn']
    else:
        data['fail'] = 0
