import os

# Load the secret key from the environment (GitHub Actions will provide this)
secret_key = os.getenv('MY_SECRET_KEY')

if secret_key:
    print(f'Successfully loaded secret key: {secret_key}')
else:
    print('Error: Secret key not found!')
