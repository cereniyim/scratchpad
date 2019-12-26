# create Menu class
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

# Give our Menu class a string representation method that will tell you the name of the menu.
    def __repr__(self):
        return "{name} available from {start_time} to {end_time}.".\
            format(name=self.name,
                   start_time=self.start_time,
                   end_time=self.end_time)

# Have calculate_bill return the total price of a purchase
# consisiting of all the items in purchased_items.
    def calculate_bill(self, purchased_items):
        total_price = 0
        for key, value in purchased_items.items():
            # check if the ordered item in the menu
            if key in self.items.keys():
                total_price += self.items[key] * purchased_items[key]
        return total_price


# create Franchise
class Franchise():
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

# Give our Franchises a string representation
    def __repr__(self):
        return "Address of the franchise is {address}".\
            format(address=self.address)

# available_menus() method that takes in a time parameter and
# returns a list of the Menu objects that are available at that time.
    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if (int(time.split(".")[0]) >= int(menu.start_time.split(".")[0])) and (
                    int(time.split(".")[0]) <= int(menu.end_time.split(".")[0])):
                available_menus.append(menu)
        return available_menus


# create Business class
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


# Let’s create our first menu: brunch.
# Brunch is served from 11am to 4pm. The following items are sold
brunch = Menu("Brunch Menu", {'pancakes': 7.50,
                              'waffles': 9.00,
                              'burger': 11.00,
                              'home fries': 4.50,
                              'coffee': 1.50,
                              'espresso': 3.00,
                              'tea': 1.00,
                              'mimosa': 10.50,
                              'orange juice': 3.50
                              }, "11.00", "16.00")
print(brunch)

print(brunch.calculate_bill({'pancakes': 1, 'home fries': 1, 'coffee': 1}))


# Let’s create our second menu item early_bird.
# Early-bird Dinners are served from 3pm to 6pm. The following items are available
early_bird = Menu("Early Bird Menu", {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50,
    'espresso': 3.00,
}, "15.00", "18.00")
print(early_bird)
print(early_bird.calculate_bill({'salumeria plate': 1, 'mushroom ravioli (vegan)': 1}))

# Let’s create our third menu, dinner. Dinner is served from 5pm to 11pm.
dinner = Menu("Dinner Menu", {
    'crostini with eggplant caponata': 13.00,
    'ceaser salad': 16.00,
    'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00,
    'espresso': 3.00,
}, "17.00", "23.00")
print(dinner)

# And let’s create our last menu, kids.
# The kids menu is available from 11am until 9pm
kids = Menu("Kids Menu", {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
}, "11.00", "21.00")
print(kids)

# create franchise objects:
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
print(flagship_store)

# provide list of available menus for 12 Noon
print(flagship_store.available_menus("12.00"))

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

# provide list of available menus for 17.00
print(new_installment.available_menus("17.00"))

# create business object
heart_business = Business("Basta Fazoolin\' with my Heart", [flagship_store, new_installment])

# create arepas menu
arepas_menu = Menu("Take a’ Arepa", {'arepa pabellon': 7.00,
                                     'pernil arepa': 8.50,
                                     'guayanes arepa': 8.00,
                                     'jamon arepa': 7.50
                                     }, "10.00", "20.00")

# create arepas franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# create arepas business
arepas_business = Business("Take a' Arepa", [arepas_place])