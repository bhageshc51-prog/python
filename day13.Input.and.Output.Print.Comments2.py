print("karnataka")  # output

boy_name = input("Boy Name: ")
boy_age = int(input("Boy Age: "))

girl_name = input("Girl Name: ")
girl_age = int(input("Girl Age: "))

age_diff = int(boy_age) - int(girl_age)

print(boy_name + " loves " + girl_name + ". Age Difference is " + str(age_diff))

print(f"{boy_name} loves {girl_name}. Age Difference is {age_diff}")