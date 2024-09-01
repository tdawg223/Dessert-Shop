from abc import ABC, abstractmethod
import receipt
from packaging import Packaging
from payable import Payable
from payable import PayType
from typing import Protocol
from enum import Enum
from combine import Combinable

'''This Class is a general class that allows us to define the names of 
dessert items in child classes, as well as calculate tax percent. It is abstract,
so the calculate_cost method is able to be implented uniquely in each child class'''

class DessertItem(Packaging):

  def __init__(self,name,tax_percent=7.25):
    self.name = name 
    self.tax_percent = tax_percent
    self.packaging = None

  def __str__(self):
    return f'{self.name}, {self.tax_percent}% tax'


  def name_pass(self): # A method that allows us to return the name of our dessert. 
    return self.name

  @abstractmethod # This method is an abstract method. It allows us to perform unique calculations in each child class based on quantity, weight, etc. 
  def calculate_cost(self):
        pass

  def __eq__(self,other):
    self_total_cost = self.calculate_cost() + self.calculate_cost() * (self.tax_percent / 100)
    other_total_cost = other.calculate_cost() + other.calculate_cost() * (other.tax_percent / 100)
    return self_total_cost == other_total_cost


  def __neq__(self,other):
    self_total_cost = self.calculate_cost() + self.calculate_cost() * (self.tax_percent / 100)
    other_total_cost = other.calculate_cost() + other.calculate_cost() * (other.tax_percent / 100)
    return self_total_cost != other_total_cost

  def __lt__(self,other):
    self_total_cost = self.calculate_cost() + self.calculate_cost() * (self.tax_percent / 100)
    other_total_cost = other.calculate_cost() + other.calculate_cost() * (other.tax_percent / 100)
    return self_total_cost < other_total_cost

  def __gt__(self,other):
    self_total_cost = self.calculate_cost() + self.calculate_cost() * (self.tax_percent / 100)
    other_total_cost = other.calculate_cost() + other.calculate_cost() * (other.tax_percent / 100)
    return self_total_cost > other_total_cost

  def __ge__(self, other):
    self_total_cost = self.calculate_cost() + self.calculate_cost() * (self.tax_percent / 100)
    other_total_cost = other.calculate_cost() + other.calculate_cost() * (other.tax_percent / 100)
    return self_total_cost >= other_total_cost

  def __le__(self, other):
    self_total_cost = self.calculate_cost() + self.calculate_cost() * (self.tax_percent / 100)
    other_total_cost = other.calculate_cost() + other.calculate_cost() * (other.tax_percent / 100)
    return self_total_cost <= other_total_cost
#Is our candy class. This inherits from DessertItem, and represents the candy we choose to use in our order.
class Candy(DessertItem): 
  def __init__(self,name,candy_weight,price_per_pound): # instantiates the attributes of the name, weight, and price per pound of candy.
    super().__init__(name)# We access the name attribute using super() from DessertItem so that it can be implemented correctly in Candy. We do this in all classes except for Sundae. 
    self.candy_weight = float(candy_weight)
    self.price_per_pound = float(price_per_pound)
    self.packaging = "Bag"

  def calculate_cost(self): #Is a concrete class that overrides the abstract method in DessertItem with uniqe implentation
    return self.price_per_pound * self.candy_weight

  def __str__(self):
    #return f'{self.name} "({self.packaging})", \n{self.candy_weight:.2f} lbs, ${self.price_per_pound:.2f}/lb, ${self.price_per_pound * self.candy_weight:.2f}, ${self.price_per_pound * self.candy_weight * (self.tax_percent / 100):.2f}'
    return f'{self.name}, ({self.packaging}), {self.candy_weight} lbs, ${self.price_per_pound:.2f}/lb:, ${self.price_per_pound * (self.candy_weight):.2f}, ${self.price_per_pound * (self.candy_weight) *(self.tax_percent/100):.2f}' 

  def can_combine(self, other:"Combinable") -> bool:
    if isinstance(other, Candy) and (other.price_per_pound == self.price_per_pound) and (self.name == other.name):
      return True
    else:
      return False


  def combine(self, other:"Combinable") -> "Combinable":
    if self.can_combine(other):
      self.candy_weight += other.candy_weight
      del other
      return self
    else:
      raise ValueError("These items are not compatible")


class Cookie(DessertItem): # Defines a cookie class inheriting from DessertItem to make a cookie order
  def __init__(self,name,cookie_quantity,price_per_dozen):
    super().__init__(name)
    self.cookie_quantity = int(cookie_quantity)
    self.price_per_dozen = float(price_per_dozen)
    self.packaging = "Box"

  def calculate_cost(self): # a different implementation of our calculate_cost method. This one divides the quanitity by 12, then multiplies.
    dozens = self.cookie_quantity / 12  
    return dozens * self.price_per_dozen

  def __str__(self):
    return f'{self.name}, ({self.packaging}), {self.cookie_quantity} cookies, ${self.price_per_dozen:.2f}/dozen, ${self.cookie_quantity/12 * (self.price_per_dozen):.2f}, ${self.cookie_quantity/12 * (self.price_per_dozen) *(self.tax_percent/100):.2f}'

  def can_combine(self, other:"Combinable") -> bool:
    if isinstance(other, Cookie) and (other.price_per_dozen == self.price_per_dozen) and (self.name == other.name):
      return True
    else:
      return False


  def combine(self, other:"Combinable") -> "Combinable":
    if self.can_combine(other):
      self.cookie_quantity += other.cookie_quantity
      del other
      return self
    else:
      raise ValueError("These items are not compatible") 



class IceCream(DessertItem):# Defines an ice cream class for adding ice cream to the order
  def __init__(self,name,scoop_count,price_per_scoop):
    super().__init__(name) 
    self.scoop_count = int(scoop_count)
    self.price_per_scoop = float(price_per_scoop)
    self.packaging = "Bowl"

  def calculate_cost(self):
    return self.scoop_count * self.price_per_scoop

  def __str__(self):
    r = f'{self.name}, {self.packaging}, {self.scoop_count} scoops, ${self.price_per_scoop:.2f} scoop, ${self.price_per_scoop * (self.scoop_count):.2f}, ${self.scoop_count * (self.price_per_scoop) *(self.tax_percent/100):.2f}'
    #print(r)
    return r


  def can_combine(self, other:"Combinable") -> bool:
    if isinstance(other, IceCream) and (other.price_per_scoop == self.price_per_scoop) and (self.name == other.name):
      return True
    else:
      return False


  def combine(self, other:"Combinable") -> "Combinable":
    if self.can_combine(other):
      self.scoop_count += other.scoop_count
      del other
      return self
    else:
      raise ValueError("These items are not compatible") 


class Sundae(IceCream): # Sundae inherits from IceCream. This allows us to instantiate scoop_count and price_per_scoop and use them the same way they were used in IceCream
  def __init__(self,name,scoop_count,price_per_scoop,topping_name,topping_price):
    super().__init__(name,scoop_count,price_per_scoop)
    self.topping_name = topping_name # We add an additional attribute for toppings
    self.topping_price = topping_price # We add an additional attribute for the price of the topping
    self.packaging = "Boat"

  def calculate_cost(self): # Essentially the same calculation from Ice cream, but we just add the topping price to that.
    ice_cream_cost = self.scoop_count * self.price_per_scoop
    return ice_cream_cost + self.topping_price

  def __str__(self):
    topping_str = f'{self.topping_name}, , , , ${self.topping_price:.2f}, '
    ice_cream = f'{self.name}, {self.packaging}, {self.scoop_count} scoops, ${self.price_per_scoop:.2f} scoop, ${self.price_per_scoop * (self.scoop_count):.2f}, ${self.scoop_count * (self.price_per_scoop) *(self.tax_percent/100):.2f}'
    r = ice_cream + "\n" + topping_str
    #print(r) 
    return r 

  def can_combine(self, other:"Combinable") -> bool:
    if isinstance(other, Sundae) and (other.price_per_scoop == self.price_per_scoop) and (self.name == other.name) and (self.topping_name == other.topping_name) and (self.topping_price == other.topping_price) :
      return True
    else:
      return False


  def combine(self, other:"Combinable") -> "Combinable":
    if self.can_combine(other):
      self.scoop_count += other.scoop_count
      self. topping_price += other.topping_price
      del other
      return self
    else:
      raise ValueError("These items are not compatible") 


class Order: # This class is responsible for storing our dessert items from our other classes. 

   def __init__(self):# Initiates a list or storage container for our dessert items. 
      self.order = []
      self.payment_method = PayType.CASH

   def add_dessert_item(self,dessert_item): # We append a dessert item to the self.order list. The attribute item allows us to pass in a dessert item later on.
      #print(isinstance(dessert_item, Combinable))
      if isinstance(dessert_item, Combinable):
        for existing_item in self.order:
          if existing_item.can_combine(dessert_item):
            existing_item.combine(dessert_item)
            return  # Exit the method once combined

        # If no combination is found, add the item as a new entry
      self.order.append(dessert_item)



   def __len__(self): # A special method that allows us to return the length of our order, or the total items in the order. 
      return len(self.order)

   def __iter__(self): # A special method that allows us to iterate through our order and use for loops, etc. 
      return iter(self.order)

   def order_cost(self): # Returns the total cost of items in the list before tax. 
    total_cost = sum(item.calculate_cost() for item in self.order) # sums up all of the costs of each item after the calculate_cost method is performed on each item. An item in the order constitutes the name, cost, amount, etc. The item.calculate_cost tells python to use that method on our item. We then sum the other items we might add after calulcate_cost is performed. 
    return total_cost


   def order_tax(self): # Is a method that correctly calculates the tax of each item before being added to the total cost.
    total_tax = sum(item.calculate_cost() * (item.tax_percent / 100) for item in self.order) # Correctly calculates tax before tax is added to the final total. tax_percent has a default amount of 7.25 in DessertItem, so we divide that by 100 to get the correct decimal amount. 
    return total_tax

   def order_sort_by_price(self):
    return sorted(self.order, key=lambda item: item.calculate_cost() + item.calculate_cost() * (item.tax_percent / 100))




   def __str__(self):
    subtotal = self.order_cost()
    total = self.order_cost() + self.order_tax()
    lines1 = f"----------------------------------------------Receipt-------------------------------------"
    #item_strings = [str(item) for item in self.order]
    header =  f"Name, Quantity, UnitPrice, Cost, Tax"
    item_strings = [str(item) for item in self.order]
    lines2 = f"------------------------------------------------------------------------------------------"
    lines3 = f"------------------------------------------------------------------------------------------"
    order_quant = f"Total items in the order {len(self.order)}"
    subtotal_str = f"Order Subtotal                                   ${subtotal:.2f}              ${self.order_tax():.2f}"
    total_str = f"Order Total                                                         ${total:.2f}"       
    payment_line = f"Paid with {self.payment_method.value}"        

    output_strings = [lines1]
    output_strings.extend(item_strings)
    output_strings.append(lines2)
    output_strings.append(order_quant)
    output_strings.append(subtotal_str)
    output_strings.append(total_str)
    output_strings.append(lines3)
    output_strings.append(payment_line)
    return '\n'.join(output_strings)

    #order_instance = Order()