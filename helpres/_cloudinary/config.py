import cloudinary
from config import settings
CLOUD_NAME = settings.CLOUD_NAME
API_KEY = settings.API_KEY
API_SECRET = settings.API_SECRET
def cloudinary_init():
    cloudinary.config(
    cloud_name = CLOUD_NAME, 
    api_key = API_KEY, 
    api_secret = API_SECRET, # Click 'View API Keys' above to copy your API secret
    secure=True
    )