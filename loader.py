import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Get the secret key from the environment
secret_key = os.getenv('MY_SECRET_KEY')

if secret_key:
    print(f'Successfully loaded secret key: {secret_key}')
else:
    print('Error: Secret key not found!')
