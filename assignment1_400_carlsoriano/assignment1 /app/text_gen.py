import os
import random
import string

file_path = '/serverdata/random.txt'

# Check if the file exists
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        existing_data = file.read()
        print(f'Existing Data: {existing_data}')

# Generate new random text data
new_data = ''.join(random.choices(string.ascii_letters + string.digits, k=100))

# Write the new data to the file
with open(file_path, 'w') as file:
    file.write(new_data)
    print(f'New Data: {new_data}')  

    