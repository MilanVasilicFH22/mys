import os

# Load the MY_SECRET from the environment (GitHub Actions will provide this)
my_secret = os.getenv('MY_SECRET')

if my_secret:
    print(f'Successfully loaded MY_SECRET: {my_secret}')
else:
    print('Error: MY_SECRET not found!')
