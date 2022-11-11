# Practice make and check salted, hashed password using bcrypt

# import bcrypt
import bcrypt

# initialize new pasword, make it byte array
password = b'I\'m a new password'

# get random string, salted the random string to 12 salt rounds.
# 12 salt rounds mean we iterate to jumble up the random string to 12 rounds.
salted_random_string = bcrypt.gensalt(12)
hashed = bcrypt.hashpw(password, salted_random_string)

# Check byte array password to salted, hashed digest. Is it match or not.
isMatch = bcrypt.checkpw(password, hashed)

# print salted random string, print salted, hashed digest, print the check result
print(salted_random_string)
print(hashed)
print(isMatch)
