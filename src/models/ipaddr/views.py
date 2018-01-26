from flask import Blueprint, request, session, url_for, render_template, redirect
from src.common.utils import Utils
from src.models.ipaddr.ipaddr import IPAddr

__author__ = 'bmoore'


ipaddr_blueprint = Blueprint('ipaddr', __name__)


@ipaddr_blueprint.route('/ip_lookup', methods=['GET', 'POST'])  # default is only GET
def ip_lookup():
    if request.method == 'POST':
        ipaddr_str = request.form['ipaddr']
        if Utils.check_ip4_address(ipaddr_str):
            ipaddr = IPAddr(value=ipaddr_str, ipv4=True)
            return render_template('ipaddr/lookup.jinja2', ipaddr=ipaddr)
    return render_template('home.jinja2')

