def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    return price - (price * (discount_percent/100))
  else:
   return price

#prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: ")) 
    #calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)   
    
    #print results
    if discount_percentage >= 20:
       print(f"The final price after discount is  :${final_price:.2f}")    
    else:
       print(f"No discount applied. The original price is: ${original_price:.2f}")    
except ValueError:
   print("Invalid input. Please enter a numeric value for the price and discount.")                