from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_items = Menu()
machine = MoneyMachine()
coffee = CoffeeMaker()

machine_state = "on"

while machine_state == "on":
    response = input(f"What would you like? {menu_items.get_items()}: ").lower()

    if response == "off":
        machine_state = "off"
    elif response == "report":
        coffee.report()
        machine.report()
    else:
        coffee_type = menu_items.find_drink(response)
        if coffee.is_resource_sufficient(coffee_type):
            if machine.make_payment(coffee_type.cost):
                coffee.make_coffee(coffee_type)

if machine_state == "off":
    print("Machine shutting down.")
