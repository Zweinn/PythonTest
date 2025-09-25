todos = ["Brot", "Hafer",]

for _ in range(1000):
    newitem = input("Hinzufügen: ") 
    todos.append(newitem)
    print("Einkaufsliste:")

    for todo in todos:
        print(f" - {todo}")

print("Ende")