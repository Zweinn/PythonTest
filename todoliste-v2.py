todos = ["Brot", "Hafer",]


for _ in range(1000):
    print("Was willst du tun?")
    print("(1) To-dos anzeigen")
    print("(2) To-dos hinzufügen")

    option = input("Bitte auswählen: ")

    if int(option) == 1:
        print("Einkaufsliste:")       
        for todo in todos:
            print(f" - {todo}")

    if int(option) == 2:
        newitem = input("Hinzufügen: ") 
        todos.append(newitem)
print("")
print("")
print("Ende")