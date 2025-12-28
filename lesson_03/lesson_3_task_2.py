from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy J5", "+79135896425"),
    Smartphone("Sony", "Z5", "+79995846971"),
    Smartphone("iPhone", "12 Pro Max", "+19235894125"),
    Smartphone("HuaWei", "P9", "+79832359869"),
    Smartphone("Xiaomi", "Mi2A", "+79995556987")
]


for smartphone in catalog:
    print(f"{smartphone.mark} - {smartphone.model}. {smartphone.number}")
