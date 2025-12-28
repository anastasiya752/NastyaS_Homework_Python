from address import Address
from mailing import Mailing


to_address = Address("658920", "Ростов", "Ленина", "58", "13")
from_address = Address("632984", "Екатеринбург", "Красный проспект", "5", "67")
cost = 1025
track = ("DT54513")

mailing = Mailing(to_address, from_address, cost, track)

print(mailing)
