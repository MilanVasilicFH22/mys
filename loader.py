import os

# Attempt to load MY_SECRET
my_secret = os.getenv('MY_SECRET')

if my_secret:
    print(f'Successfully loaded MY_SECRET: {my_secret}')
    print(f'Successfully loaded MY_SECRET with length: {len(my_secret)} characters')

else:
    print('Error: MY_SECRET not found!')
