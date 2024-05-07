# candidate Interview
# wap to collect the name,age,education,area,college name, phonenumber
# of the people who attend the interview and print


name = input("Enter your name here : ")
education = input("Enter your degree here : ")
college_name = input("Enter your college name here : ")
phone_number = input("Enter your Phone number here : ")
current_year = 2024
birth_year = input("Enter the year you're born : ")
# converting the value from str to int
birth_year = int(birth_year)
age = current_year - birth_year

print("""
Hi,
Below are the details you have entered:
name :""",name )
