import math
import stripe
import json
import easypost
from flask import current_app
from ..util import send_email
def get_shipping_rate(products, addr, **config):
    """Estimate a shipping rate for a product.
    This does not actually purchase shipping, this is just to figure out
    how much to charge for it."""
    metadata_fields, urls, i = ['digital_url'], {}, 0
    for p, q in products:
        missing_fields = [k for k in metadata_fields if k not in p.metadata]
        if missing_fields:
            new_order_recipients = current_app.config['NEW_ORDER_RECIPIENTS']
            send_email(new_order_recipients, "Missing product metadata", "admin_msg", message="Product {} is missing metadata fields in Stripe: {}".format(p.name, ", ".join(missing_fields)))
        urls['digital_url'+str(i)] = p.metadata['digital_url']
        urls['digital_name'+str(i)] = p.name
        i = i+1
    # Convert to cents
    return 0, urls
def buy_shipment(**kwargs):
    urls, i = {}, 0
    while kwargs.get('digital_url' + str(i)):
        urls[kwargs.get('digital_name' + str(i))] = kwargs.get('digital_url' + str(i))
        i = i+1
    return urls
def shipment_exists(shipment_id):
    return False, None
