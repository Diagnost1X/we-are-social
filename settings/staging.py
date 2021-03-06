import dj_database_url
from base import *

DEBUG = False
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
 
# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_gxhY77b3TWmXhbv9r7sJhHg7')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_zuqEExSaYKO7YtDb6wfwR9z7')
 
# Paypal environment variables
SITE_URL = 'we-are-social-diagnostix.herokuapp.com'
PAYPAL_NOTIFY_URL = 'we-are-social-diagnostix.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'diagnostix-sell@me.com'

DATABASES = {
    'default':dj_database_url.config('CLEARDB_DATABASE_URL')
}
