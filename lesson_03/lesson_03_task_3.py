from address import Address
from mailing import Mailing

# 1. Создаем адрес получателя (to_address)
to_addr = Address("191000", "Санкт-Петербург", "Невский проспект", "10", "25")

# 2. Создаем адрес отправителя (from_address)
from_addr = Address("101000", "Москва", "Тверская улица", "5", "12")

# 3. Создаем экземпляр класса Mailing
shipment = Mailing(
    to_address=to_addr, from_address=from_addr, cost=450, track="RA123456789RU"
)

# 4. Распечатываем информацию, получая все данные строго из объекта shipment
# Замените ваш print на этот вариант с переносами строк:
print(
    f"Отправление {shipment.track} из "
    f"{shipment.from_address.index}, {shipment.from_address.city}, "
    f"{shipment.from_address.street}, {shipment.from_address.house} - "
    f"{shipment.from_address.apartment} в {shipment.to_address.index}, "
    f"{shipment.to_address.city}, {shipment.to_address.street}, "
    f"{shipment.to_address.house} - {shipment.to_address.apartment}. "
    f"Стоимость {shipment.cost} рублей."
)
