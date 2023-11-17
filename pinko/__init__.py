import config
from random import sample
import json
from flask_security import current_user
from taozi.models import Post, Event, Issue, Meta
from konbini.forms import AddToCartForm
from taozi.compile import compile_markdown
from konbini.core import get_product, get_products
from flask import Blueprint, make_response, render_template, abort, redirect, request, url_for

routes = Blueprint('pinko', __name__)

@routes.route('/intro')
def intro():
    return render_template('intro.html')

@routes.route('/')
def index():

    banner = {'name': Meta.get_by_slug('banner-title'),
    'description': Meta.get_by_slug('banner-description'),
    'image': Meta.get_by_slug('banner-image-url'),
    'path': Meta.get_by_slug('banner-url')}

    posts = Post.query.filter(Post.published).limit(2)

    products = [p for p in get_products() if p.id != "prod_" + config.SUBSCRIPTION_PLAN_ID]
    products = products[0:4]

    popup = 'none' if ('popup' in request.cookies) else ''
    resp = make_response(render_template('index.html',
        products=products,
        banner=banner,
        posts=posts,
        popup=popup))
    if 'popup' not in request.cookies: resp.set_cookie('popup', '')

    return resp

@routes.route('/<issue>/<slug>')
def post(issue, slug):
    post = Post.query.filter(Post.slug==slug, Post.issue.has(slug=issue)).first_or_404()
    if not post.published and not current_user.is_authenticated:
        abort(404)
    return render_template('post.html', post=post)

@routes.route('/in-print/<slug>')
def issue(slug):
    issue = Issue.query.filter(Issue.slug==slug).first_or_404()
    if not issue.published and not current_user.is_authenticated:
        abort(404)
    product_id = issue['product_id']
    product = get_product(product_id) if product_id else ''

    form = AddToCartForm(name=product.name, sku=product.default_price.id, product=product.id)

    issue.description = compile_markdown(issue['description'])
    return render_template('issue.html', issue=issue, product=product, form=form)

@routes.route('/magazine')
def archive():
    data = request.args
    page = int(data.get('page', 1))

    print_only = json.dumps({'print_only': False})
    posts = Post.query.filter(Post.published, Post.meta==print_only, Post.event==None).paginate(page, per_page=6)
    return render_template('writing.html', posts=posts.items, paginator=posts)

@routes.route('/in-print')
def issues():
    issues = Issue.query.filter(Issue.published, Issue.name != 'Web').all()
    manifesto = get_product(config.MANIFESTO_PRODUCT_ID)
    zines = [p for p in get_products() if p.metadata.get('zine') == 'true']
    return render_template('issues.html', issues=issues, manifesto=manifesto, zines=zines)

@routes.route('/events')
def events():
    events = [e.post for e in Event.query.order_by(Event.start.desc(), Event.end.desc()).all() if e.post.published]
    events.reverse()
    return render_template('events.html', events=events)

@routes.route('/search')
def search():
    query = request.args.get('query')
    posts = Post.search(query) if query else []
    return render_template('search.html', query=query, posts=posts)

@routes.route('/about')
def about():
    issns = Meta.get_by_slug('issns')
    about = Meta.get_by_slug('about')
    collective = Meta.get_by_slug('collective')
    return render_template('about.html', issns=issns, about=about, collective=collective)

@routes.route('/legal')
def legal():
    return render_template('legal.html')

@routes.route('/donate')
def donate():
    donate = Meta.get_by_slug('donate')
    return render_template('donate.html', donate=donate)

@routes.route('/shop/product/<id>')
def product(id):
    p = get_product(id)
    also = get_products()
    if p in also:
        also.remove(p)
    form = AddToCartForm(name=p.name, sku=p.default_price.id, product=p.id) if p.default_price else ''
    return render_template('shop/product.html', product=p, form=form, also=sample(also,2))
