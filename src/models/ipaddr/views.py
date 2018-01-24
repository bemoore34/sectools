from flask import Blueprint, request, session, url_for, render_template, redirect
from src.models.ipaddr import ipaddr

__author__ = 'bmoore'


ipaddr_blueprint = Blueprint('ipaddr', __name__)


@ipaddr_blueprint.route('/ip_lookup', methods=['GET', 'POST'])  # default is only GET
def ip_lookup():
    if request.method == 'POST':
        return render_template('ipaddr/lookup.jinja2')
    pass

