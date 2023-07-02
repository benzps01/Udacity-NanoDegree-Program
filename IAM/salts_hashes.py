import bcrypt

password = b'studyhard'

salt = bcrypt.gensalt(14)

hashed = bcrypt.hashpw(password,salt)
print("This is the salt: ",salt)
print("This is the hashed password: ", hashed)

check = bcrypt.checkpw(password, hashed)
print(check)

# @TODO: Which password correctly matches the following salted digest?

# hashed = b'$2b$14$EFOxm3q8UWH8ZzK1h.WTZeRcPyr8/X0vRfuL3/e9z7AKIMnocurBG'
# passwords : 'securepassword', 'udacity', 'learningisfun'

hashed = b'$2b$14$EFOxm3q8UWH8ZzK1h.WTZeRcPyr8/X0vRfuL3/e9z7AKIMnocurBG'

password_list = [b'securepassword', b'udacity', b'learningisfun']

for i in password_list:
    is_password_correct = bcrypt.checkpw(i,hashed)
    if is_password_correct:
        print(i)
