# Hashing with the hashlib LIBRARY

## Example walkthrough:

*Learning hashing using the hashlib library*

import hashlib

password = "Daniel@123"

*Turning the password in bytes - required by hashlib*

password_bytes = password.encode()

*Creating the hash object*

hash_object = hashlib.sha256(password_bytes)

*Getting the hexadecimal representation of the hash - this is the hash*

final_hash = hash_object.hexdigest()

*Printing the hash*

print(f"The hash of the password is: {final_hash}")
