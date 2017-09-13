from base import *
 
DEBUG = True
 
INSTALLED_APPS.append('debug_toolbar')
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware')
 
# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_gxhY77b3TWmXhbv9r7sJhHg7')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_zuqEExSaYKO7YtDb6wfwR9z7')
 
# Paypal environment variables
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'http://3649e6b1.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'diagnostix-sell@me.com'