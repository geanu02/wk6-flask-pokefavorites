from flask import render_template

from . import bp

@bp.route('/')
def home():
    return render_template(
        'index.jinja',
        title="PokeFavorites: Welcome!",
    )

@bp.route('/about')
def about():
    return render_template(
        'about.jinja',
        title="PokeFavorites: About Page"
    )