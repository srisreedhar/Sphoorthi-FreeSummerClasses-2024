# Passport


passport = input("Enter your Passport number :")

passport_new = passport.upper()
country = passport_new[:2]


if country == 'IN':
    print("Passport belongs to INDIA")
else:
    print("Passport does not belong to India")
