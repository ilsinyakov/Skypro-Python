from smartphone import Smartphone


catalog = []
catalog.append(Smartphone('iphone', '16', '+79991234567'))
catalog.append(Smartphone('Samsung', 'A50', '+79999994567'))
catalog.append(Smartphone('Huawei', 'P20', '+79001234567'))
catalog.append(Smartphone('Nokia', '3310', '+79999999999'))
catalog.append(Smartphone('Honor', '10', '+79039994567'))

for smartphone in catalog:
    print(f'{smartphone.brand} - {smartphone.model}. {smartphone.number}')
