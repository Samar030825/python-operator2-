print("===Smart School Dat Planner===")
print("Answer me 3 questions and i will plan your day !/n")

day = input("What day is it? (Monday to Sunday) ").strip().capitalize()
weather = input("What weather is it? ( Sunny / Rainy / cloudy)").strip().lower()
homework = input("Is your homework done? ( yes / no)").strip().lower()

print()
print(F"=== Your plan for {day} ===")
print("-" * 35)

if day in ("Saturday" , "Sunday"):
    print("day type - Weekend ! Enjoy your free time")
elif day == "Monday":
    print("day type - first day of the week.pack your weekly planner")
elif day in "friday":
    print("day type - last day of week . Return books from the library ")
elif day == ("Tuesday" , "Wednesday" , "Thursday"):
    print("day type - regular school day . stay fucused!")
else:
    print("day type - day not recognised . Check the spelling")

if weather == "Sunny" and homework == "Yes":
    print("After school - Headd toward the park , weather is good and homework is done")

if weather == "Rainy" or weather == "Cloudy":
    print("Weather tip - Pack your umbrela . It may get wet outside")

if not homework == ("Yes") :
    print("Homework not done yet - do it before going out")

if weather == ("Rainy") and not homework == ("Yes"):
    print("Best plan - Stay in home and complete your homwork than watch your favourite show")
elif weather == (("Sunny") and not homework == ("Yes") and not day in("Saturday", "Sunday")  ) :
    print("Best plan - all set for school day you oare fully prepared")
elif day in ("Saturday", "Sunday") and weather == "Sunny" :
    print("Best plan - pefect weekend weather - head toward the park ")
else:
    print("Best plan : Take it one step at a time- you have got this")

print()
print("Plan complete! Have a wonderful day")  