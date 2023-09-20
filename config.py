SECRET_KEY = 'something-secret'

STRIPE_PUBLIC_KEY = 'pk_test_51NX9IZGdgSOLzVnBdiBTJHLJICPgpHCXDCO1JsLfdTLsVN8A9JvmxfO5hCdsowNjC5pzEyccTtfVD5m6u49WxNTT00JldoNDSq'
STRIPE_SECRET_KEY = 'sk_test_51NX9IZGdgSOLzVnBshkRVVJzkLrJHZ6hStsWNXSssLl1JG9lIb7kcVstYg2q5ycfTEPy8QZfFoNWfiCPrOV2io41007XQSiaqK'
EASYPOST_API_KEY = 'EZ...'
SENTRY_DSN = 'https://examplePublicKey@o0.ingest.sentry.io/0'
MANIFESTO_PRODUCT_ID = 'OJnp6Uoo0ympfY'
SUBSCRIPTION_PRODUCT_ID = 'OJnq1E4JnuI49S'

SQLALCHEMY_DATABASE_URI = 'sqlite:////home/arseny/pinko/pinko/pinko.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = 'another-secret'
SECURITY_CHANGEABLE = True
SECURITY_RECOVERABLE = True
SECURITY_EMAIL_SENDER = 'foo@foo.co'

MAIL_SERVER = 'smtp.mailgun.org'
MAIL_USERNAME = 'postmaster@foo.mailgun.org'
MAIL_PASSWORD = 'your-password'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_DEBUG = True
MAIL_DEFAULT_SENDER = 'foo@foo.co'

# Don't forget to create this folder
UPLOAD_FOLDER = '/home/arseny/pinko/pinko/uploads/'
MAX_CONTENT_LENGTH = 10 * 1024 * 1024 # 8MB

# Optional
ISSUE_META = {
    'color': str,
    'description': str,
    'cover_url': str,
    'store_url': str,
    'background_color': str,
    'product_id': str
}

# Optional
AUTHOR_META = {
}

# Optional
POST_META = {
    'print_only': bool
}
