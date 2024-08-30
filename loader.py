import os

# Load the secret key from the environment (GitHub Actions will provide this)
api_secret = os.getenv('API_SECRET')

if api_secret:
    print(f'Successfully loaded API secret: {api_secret}')
else:
    print('Error: API secret not found!')
