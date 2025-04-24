import cloudinary
from decouple import config
CLOUD_NAME = config('CLOUD_NAME',default='')
API_KEY = config('API_KEY',default='')
API_SECRET = config('API_SECRET',default='')
def cloudinary_init():
    cloudinary.config(
    cloud_name = CLOUD_NAME, 
    api_key = API_KEY, 
    api_secret = API_SECRET, # Click 'View API Keys' above to copy your API secret
    secure=True
    )