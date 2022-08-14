from order import Order

food={
  'burgers': { 'price': 7.99, 'tax': 0.13 },
  'pizza': { 'price': 16.99, 'tax': 0.05 },
  'salad': { 'price': 4.99, 'tax': 0 }, 
  'fingers': { 'price': 9.99, 'tax': 0.13 }
}
viewed = []
bill = []
password = "stats"
s = ', '
menu = s.join(food.keys())
grand_total = 0

while True:

new_order = Order()
  food_input = input('Select: ' + menu + ', done, cancel: ').lower()
  
  if food.get(food_input):
    quantity_input = input('How many would you like?: ')
    quantity = int(quantity_input)
    
#     food_selection = food.get(food_input)
#     price = food_selection.get('price')
#     tax = food_selection.get('tax')
#     tax += 1
  
#     taxed = price * tax * quantity
#     rounded = round(taxed, 2)

#     viewed.append (food_input)
#     food_selection.update ({'quantity': quantity_input})
#     food_selection.update ({'total': rounded})
#     viewed.append (food_selection)

#     grand_total += rounded 
#     grand_total = round(grand_total, 2)

#     bill.append ({'quantity': quantity_input, 'food': food_input, 'total': rounded})
    
#     print(rounded)
#   elif food_input == password:
#     print(viewed)
#   elif food_input == "done": 
#     for line_item in bill:
#       print(f"{line_item.get('quantity')} x {line_item.get('food')} - ${line_item.get('total')}")
#     print(f"Grand Total: ${grand_total}")

# # print(f'2 x burgers - $14.50')

#     break
#   elif food_input == "cancel":
#     bill = []

