# Data part
# store all the input values collected in details
details={}


name = input("Enter your name here : ")
details['name']=name
birth_year = input("Enter your year of birth here : ")
details['birth_year']=birth_year 
phone_number = input("Enter your contact here : ")
details['phone_number']=phone_number
maths = input("Enter your math marks : ")
details['maths']=maths
science = input("Enter your science marks : ")
details['science']=science
social = input("Enter your social marks here : ")
details['social']=social
current_year = 2024

# processing/Logic Part

details['birth_yr_new'] = int(birth_year)

details['maths_new'] = int(maths)
details['science_new'] = int(science)
details['social_new'] = int(social)

total_marks = details['maths_new'] + details['science_new'] + details['social_new']
age = current_year - details['birth_yr_new']

details['total_marks']=total_marks
details['age']=age


# Display the results
print(details)
