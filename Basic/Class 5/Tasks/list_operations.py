def stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return {"sum": total, "average": average, "maximum": maximum, "minimum": minimum}


user_list = []
for _ in range(5):
    user_input = int(input("Provide a number: "))
    user_list.append(user_input)

item = stats(user_list)

print(f"list = {user_list}\n"
      f"SUM: {item['sum']}\n"
      f"AVG: {item['average']}\n"
      f"MAX: {item['maximum']}\n"
      f"MIN: {item['minimum']}")
