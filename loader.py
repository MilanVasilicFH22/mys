import os

# Ensure this matches the secret name exactly as used in GitHub
api_secret = os.getenv('API_SECRET')

if api_secret:
    print(f'Successfully loaded API secret: {api_secret}')
else:
    print('Error: API secret not found!')
