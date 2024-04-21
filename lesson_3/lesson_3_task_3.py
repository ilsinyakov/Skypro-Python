from address import Address
from mailing import Mailing

mailing = Mailing(Address(111222, 'New York', 'Walt street', 1, 300),
                  Address(222111, 'Moscow', 'Red Square', 2, 1),
                  123.45,
                  '38276847563948374691'
                  )

print(f'Отправление {mailing.track} из {mailing.from_address.zip_code}, \
{mailing.from_address.city}, \
{mailing.from_address.street}, \
{mailing.from_address.house} - \
{mailing.from_address.flat}.')
