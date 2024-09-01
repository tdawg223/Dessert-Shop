from dessert import Candy, Cookie, IceCream, Sundae, Order
import receipt
from payable import PayType
from enum import Enum
from typing import Dict

class DessertShop(Order):
  def __init__(self):
    self.customer_db: Dict[str, Customer] = {} # Is a whole system that allows us to add dessert items to our order via user input

  def user_prompt_candy(self): # Asks for user input for candy specific items.
    self.user_candy = input("Please enter the type of candy: ") # We enter the type of candy, which corresponds to the name of candy
    self.user_weight = float(input("Enter the candy weight amount: "))# we enter the weight, which corresponds to candy_weight
    self.user_price = float(input("Enter the price per pound: ")) # we enter the price per pound, which corresponds to price_per_pound
    print()
    if self.user_weight < 0: # Input validation. We ensure that negative numbers are not being used and only positive numbers
      raise ValueError("Please only enter positive values")
    elif self.user_price < 0:
      raise ValueError("Please only enter positive values")

    candy_item = Candy(self.user_candy,self.user_weight,self.user_price) # We create an object that stores the input values of Candy as a sort of item
    #self.add_dessert_item(candy_item) # This borrows the attribute from Order and just basically adds candy_item to the order by appending it.
    return candy_item



  def user_prompt_cookie(self): # This code block asks for a user cookie
    self.user_cookie = input("Enter the type of cookie: ")
    self.user_amount = float(input("Enter the quantity purchased: "))
    self.user_price = float(input("Enter the price per dozen: "))
    print()
    if self.user_amount < 0:
      raise ValueError("Please only enter positive values")
    elif self.user_price < 0:
      raise ValueError("Please only enter positive values")

    cookie_item = Cookie(self.user_cookie,self.user_amount,self.user_price)
    #self.add_dessert_item(cookie_item)
    return cookie_item

  def user_prompt_icecream(self): # This code block asks for user input in regards to ice cream
    self.user_icecream = input("Please enter the type of ice cream: ")
    self.user_scoops = float(input("Enter the number of scoops: "))
    self.user_price = float(input("Enter the price per scoop: "))
    print()
    if self.user_scoops < 0:
      raise ValueError("Please only enter positive values")
    elif self.user_price < 0:
      raise ValueError("Please only enter positive values")

    icecream_item = IceCream(self.user_icecream,self.user_scoops,self.user_price)
    #self.add_dessert_item(icecream_item)
    return icecream_item

  def user_prompt_sundae(self): # Asks for input in regards to creating a sundae
    self.user_icecream = input("Please enter the type of ice cream: ")
    self.user_scoops = int(input("Enter the number of scoops: "))
    self.scoop_price = float(input("Enter the price per scoop: "))
    self.user_topping = input("Enter the topping: ")
    self.topping_price = float(input("Enter the price for the topping: "))
    print()
    if self.user_scoops < 0:
      raise ValueError("Please only enter positive values")
    elif self.scoop_price < 0:
      raise ValueError("Please only enter positive values")
    elif self.topping_price < 0:
      raise ValueError("Please only enter positive values")

    sundae_item = Sundae(self.user_icecream,self.user_scoops,self.scoop_price,self.user_topping,self.topping_price)
    #self.add_dessert_item(sundae_item)
    return sundae_item

  def prompt_pay(self,order_instance):
    print()
    print("1: Cash\n2: Card\n3: Phone\n")
    order_instance.get_user_pay = int(input("Please enter a payment method: "))
    #order_instance.get_user_pay = order_instance.get_user_pay

    #pay_order = Order()
    if order_instance.get_user_pay == 1:
      order_instance.payment_method = PayType.CASH
    elif order_instance.get_user_pay == 2:
      order_instance.payment_method = PayType.CARD
    #elif order_instance.payment_method == 3:
      #order_instance.payment_method = PayType.PHONE
    elif order_instance.get_user_pay == 3:
      order_instance.payment_method = PayType.PHONE

  def best_customer(self):
        best_customer = None
        best_total_cost = 0

        for customer_name, customer in self.customer_db.items():
            total_cost = 0

            # Calculate the total cost for all orders of the current customer
            for order in customer.order_history:
                total_cost += order.order_cost()

            if total_cost > best_total_cost:
                best_total_cost = total_cost
                best_customer = customer

        if best_customer:
            return f"The Dessert Shop's most valued customer is: {best_customer.customer_name}!"
        else:
            return "No customer data available."



class Customer:
  id = 1000
  def __init__(self, customer_name):
    self.customer_name = customer_name
    self.order_history = [] # Will be a list of orders the customer bought
    self.customer_id = Customer.id
    Customer.id += 1

  def add2history(self, order:Order) -> "Customer":
    self.order_history.append(order)
    return self


def main(): # We start our main function that allows us to create objects and start using our classes.
  #START OF COPIED CODE. This code assists with user input by providing console prompts.
  shop = DessertShop()
  while True:
    print()
    new_user_order = input("Would you like to start a new order? Y for Yes, N for No: ").lower()
    if new_user_order == "y":
      order = Order()
      #shop = DessertShop()
    # elif new_user_order == "n":
    #   break
    # else:
    #   raise ValueError("Incorrect value. Please enter either y or n")
    else:
      break



    # order.add_dessert_item(Candy('Candy Corn', 1.5, 0.25))
    # order.add_dessert_item(Candy('Gummy Bears', 1.5, 0.25))
    # order.add(Cookie('Chocolate Chip', 6, 3.99))
    # order.add(IceCream('Pistachio', 2, 0.79))
    # order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    # order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    # candy1 = Candy('Candy Corn', 1.5, 0.25)
    # candy2 = Candy('Candy Corn', 1.5, 0.25)
    # candy1.combine(candy2)
    # cookie1 = Cookie("Chip", 12, 1.99)
    # cookie2 = Cookie("Chip", 12, 1.99)
    # cookie1.combine(cookie2)
    #icecream1 = IceCream("Chocolate", 2, 0.59)
    #icecream2 = IceCream("Chocolate", 2, 0.59)
    # sundae1 = Sundae("Vanilla", 2, 0.59, "sprinkles", 0.15)
    # sundae2 = Sundae("Vanilla", 2, 0.59, "sprinkles", 0.15)
    # sundae1.combine(sundae2)
    # order.add_dessert_item(sundae1)
    #icecream1.combine(icecream2)
    #order.add_dessert_item(icecream1)
    #order.add_dessert_item(icecream2)
    # order.add_dessert_item(cookie1)
    # order.add_dessert_item(candy1)
    # boolean done = false
    done: bool = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
              '1: Candy',
              '2: Cookie',            
              '3: Ice Cream',
              '4: Sundae',
              '5: Admin Module',
              '\nWhat would you like to add to the order?(1-5, Enter for done): '
        ])

    while not done:
      choice = input(prompt)
      match choice:
        case '':
          done = True
        case '1':            
          item = shop.user_prompt_candy()
          #combined = False
          order.add_dessert_item(item)
          # for existing_item in order.order:
          #   if existing_item.can_combine(item):
          #     existing_item.combine(item)
          #     combined = True
          #     #break
          # if not combined:
          #   order.add_dessert_item(item)
            #print(order)
          #print(f'{item.name} has been added to your order.')
          #print(item)
          print()
          print(order)
        case '2':            
          item = shop.user_prompt_cookie()
          order.add_dessert_item(item)
          # combined = False
          # for existing_item in order.order:
          #   if existing_item.can_combine(item):
          #     existing_item.combine(item)
          #     combined = True
          #     #break
          # if not combined:
          #   order.add_dessert_item(item)

          print(order)
        case '3':            
          item = shop.user_prompt_icecream()
          order.add_dessert_item(item)
          # combined = False
          # for existing_item in order.order:
          #   if existing_item.can_combine(item):
          #     existing_item.combine(item)
          #     combined = True
          #     #break
          # if not combined:
          #   order.add_dessert_item(item)
          print(order)
        case '4':            
          item = shop.user_prompt_sundae()
          order.add_dessert_item(item)
          # combined = False
          # for existing_item in order.order:
          #   if existing_item.can_combine(item):
          #     existing_item.combine(item)
          #     combined = True
          #     #break
          # if not combined:
          #   order.add_dessert_item(item)
          print(order)
        #case '5':
          #payment_type = shop.prompt_pay(order)
          #order.add_dessert_item(payment_type)
          #print(order)
        case '5':
          print()
          user_input = int(input("1: Shop Customer List\n2: Customer Order History\n3: Best Customer\n4: Exit Admin Module\nWhat would you like to do? (1-4): "))
          print()
          if user_input == 1:
            for customer_name, customer in shop.customer_db.items():
              customer_id = customer.customer_id
              order_history_length = len(customer.order_history)
              print(f"Customer Name: {customer_name}         Customer ID: {customer_id}")
          elif user_input == 2:
            user_lookup = input("Enter the name of the customer: ").lower()
            for customer_name, customer in shop.customer_db.items():
              if customer_name.lower() == user_lookup:
                customer_id = customer.customer_id
                print(f"Customer Name: {customer_name}         Customer ID: {customer_id}")
                print("---------------------------------------------------")
              #print("Order #", len(customer.order_history))
                order_count = 0
                for order in customer.order_history:
              # order_gen = [order for order in customer.order_history]
                  order_count +=1
                  print("Order #:", order_count)
                  print(order)
          elif user_input == 3:
            print(shop.best_customer())
            print("-----------------------------------------------------")
          elif user_input == 4:
            continue


        case _:            
          print('Invalid response:  Please enter a choice from the menu (1-4) or Enter')

    customer_dict_name = input("Please Enter Your Name: ")
    if customer_dict_name not in shop.customer_db:
      customer = Customer(customer_dict_name)
      shop.customer_db[customer_dict_name] = customer
    customer.add2history(order) 

    shop.prompt_pay(order)
    sorted_order = order.order_sort_by_price()  # Sort the order
    order.order = sorted_order 
    print(order)


    #start_new_order = input("Would you like to start a new order, y for yes, n for no then hit enter").lower()


    print()



    data = [] # Is a list where the receipt attributes get appended
    top_receipt = ["Name", "Packaging","Quantity","Unit Price","Cost","Tax"]  # Name, item cost and tax show up on the top of the receipt
    data.append(top_receipt) # We add top_receipt to data
    item_costs = [] # Represents the cost of our items
    tax_amounts = [] # Represents the tax amounts of our items
    for item in order: # Iterates through the order list to add these items to the receipt
      receipt_items = str(item).split("\n")
      for line in receipt_items:
        line_item = line.split(", ")

        #  name = item.name_pass() # gets the name of the item and puts it on the receipt
        #  item_cost = item.calculate_cost() # Gets the item cost and puts it on the receipt
        #  tax_amount = item.calculate_cost() * item.tax_percent / 100 # Gets the item tax amount and puts it onto the receipt

        #  receipt_list = [name, f"${item_cost:.2f}", f"${tax_amount:.2f}"] # correctly formats the receipt by adding the name, item cost and tax amount using an f string.
        data.append(line_item) # We append this to the list. The receipt has to be a list of lists, hence why we are doing it this way. 

        #  item_costs.append(item_cost) # We append item_costs to its own list so that it can be summed properly for final calculations
        #  tax_amounts.append(tax_amount)# We do the same as above to tax_amounts
        #  item_sum = sum(item_costs)# Now that the above are appending to the lists, we can sum everything within the list together
        #  total_tax = sum(tax_amounts)# Same as above
    #data.append(["-" * 56]) # Creates the line that separates items with the totals
    subtotal_text = ("Order Subtotals",'','','', f"${order.order_cost():.2f}", f"${order.order_tax():.2f}") # We get the sub total before tax, formatted using fstrings
    data.append(subtotal_text)
    total_text = ("Order Total",'','','',f"{order.order_cost()+ order.order_tax():.2f}")
    data.append(total_text)
    length_order = len(order)
    length_text = ("Total items in the order",'', f"{length_order}")
    data.append(length_text)
    #pay_order = Order()
    receipt_payment = ("Paid With",'',f"{order.payment_method.value}")
    data.append(receipt_payment)

    customer_receipt_name = ("Customer Name:",f'{customer_dict_name}')
    data.append(customer_receipt_name)
    current_customer = shop.customer_db.get(customer_dict_name)
    total_orders = len(current_customer.order_history) if current_customer else 1
    customer_receipt_id = ("Customer ID:",f'{current_customer.customer_id}')
    data.append(customer_receipt_id) 
    customer_total_orders = ("Total Orders:",f'{total_orders}')
    data.append(customer_total_orders)
    receipt.make_receipt(data,"receipt.pdf")
    print(*data,sep = "\n")


  # def hard_coded():
  #   headers = ["0","1","2","3","4","5"]
  #   data = []
  #   data.append(headers)
  #   letter_list = "A,B,C,D,E,F".split(",")
  #   data.append(letter_list)
  #   cards = ["Queen","10","Ace","King","7","6"]
  #   data.append(cards)

    receipt.make_receipt(data,"receipt1.pdf")


if __name__ == "__main__":
    main()
      #hard_coded()     