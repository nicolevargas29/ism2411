
#Self - Assesment questions 
#1) The first bug that I spotted immediately was the colon for the second for loop. Off the top of my head I know that loops need colons. I saw it after reading the code. For me personally I think this shows that I'm getting better at understanding syntax errors without running the code or even asking for assistance. 
#2) The (apply_discount(price,tier)) basically calculates the price of a product though is in correlation to the tier of membership the customer is apart of. Using the orignal price, and the tiers (selected from, gold, silver, bronze, or none). This then returns the new price after the applied discount of the tier. 
#3) I used the AI to help me with exercise 6, as I had a small mistake. I accidentally had x=999 in a #, messing with the code. This helped me become more aware of the code and understand the smaller parts. Lastly I used AI for exercise 5 when we had to paste in the error message. On my end I was having a situation with the index. Thats when I changed the <= to <. This helped me better understand syntax, and the range of code, and how to keep it within. 



#exercise1 
#define calculate tax functions 

def calculate_tax(price, rate):
 return price *rate 

tax1 = calculate_tax(100,0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}")

# exercise 2 
def apply_discount(price, tier): 
 if tier == "gold": 
  return price *0.85
 elif tier == "silver": 
  return price *0.90 
 elif tier == "bronze": 
  return price * 0.95
 else:
  return price


price = 200 
tiers = {"gold", "silver", "bronze", "none"}

for tier in tiers: 
 print(f"{tier}: ${apply_discount(price, tier):.2f}")

 #exercise 3

discounted = apply_discount(200,"gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax 
print(f" After gold discount: ${discounted:.2f}")
print(f" After Tax: ${after_tax:.2f}") 

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price,tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

#exercise 4 
order = [(200, "gold"), (150,"silver"), (80, "bronze"), (500, "none")]

for price, tiwe in order: 
 total = final_price(price, tier, 0.07)
 print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

 
#exercise 5
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale # The original version was just total = sale. We want each sale to be added to the total. We replace the = sign to +=
print(f"Total: ${total}")

count = 0
for sale in sales: # First one that I scouted. Any For loop must follow up with a colon(:).
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): # Originally we has <=. In order for it to stay in range we had to replace it with <
    print(sales[i])
    i += 1
 
 

#exercise 6 

x = 100 #apple #global 
def double_it():
    x = 999 # ;pca; anpther apple (not the same apple as above)
    return x * 2

print(x) # the first one prints the variable x itself (100) the global variable. 
print(double_it()) # We are now channeling the separate x inside the code. Since were doubling it we print (999*2) 
print(x) # we print the global variable 100 because it has not chnaged 

# Scope has to do with the idea of functions that are not visible outside it.
#  These are variables that can be used within the code. 
# Seen through the exercise 6 we can see that the function is different and separate from the x outside(global)



