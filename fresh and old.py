fresh_loaves = int(input("Enter the number of fresh loaves purchased: "))
day_old_loaves = int(input("Enter the number of day-old loaves purchased: "))
fresh_price = fresh_loaves * 185
discounted_price = day_old_loaves * (185 * 0.4)  # 60% discount, so 100% - 60% = 40%
total_price = fresh_price + discounted_price
print(f"Regular price: Rs.{fresh_price:.2f}")
print(f"Amount of new loaves: Rs.{fresh_price:.2f}")
print(f"Amount of day-old loaves: Rs.{discounted_price:.2f}")
print(f"Total amount: Rs.{total_price:.2f}")