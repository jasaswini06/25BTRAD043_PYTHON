def generate_bill():
	items = []
	total = 0

	while True:
		name = input("Enter item name : ")
		if name.lower() == "done":
			break

		quantity = int(input("Enter quantity: "))
		price = float(input("Enter price per item: "))
		amount = quantity * price
		items.append((name, quantity, price, amount))
		total += amount

	print("\n========== BILL ==========")
	for name, quantity, price, amount in items:
		print(f"{name}: {quantity} x {price:.2f} = {amount:.2f}")
	print("--------------------------")
	print(f"Total: {total:.2f}")
	print("==========================")


generate_bill()
