## wap that collects the name , birth year, phone number, 3 subject marks
# from the user.
# calculate the total of 3 subject marks, age of the person and
# display everything

# Data part

name = input("Enter your name here : ")
birth_year = input("Enter your year of birth here : ")
phone_number = input("Enter your contact here : ")
maths = input("Enter your math marks : ")
science = input("Enter your science marks : ")
social = input("Enter your social marks here : ")
current_year = 2024

# processing/Logic Part

birth_yr_new = int(birth_year)
maths_new = int(maths)
science_new = int(science)
social_new = int(social)

total_marks = maths_new + science_new + social_new
age = current_year - birth_yr_new


# Display the results

print("""
Hi,
You've entered below details,
Name : """,name, "\n your contact number is :",phone_number, "\n your total marks:",total_marks)






