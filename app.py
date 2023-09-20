import config
import sentry_sdk
from pinko import routes
from pinko.taozi_local.taozi import create_app
from pinko.konbini.flask_konbini import Konbini
from sentry_sdk.integrations.flask import FlaskIntegration

app = create_app(config, name='pinko', blueprints=[routes])
Konbini(app)

if not app.debug:
    sentry_sdk.init(
        dsn=config.SENTRY_DSN,
        integrations=[FlaskIntegration()]
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
