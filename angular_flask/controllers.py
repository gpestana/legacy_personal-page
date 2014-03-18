import os

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort
from flask import jsonify

from angular_flask import app

# routing for basic pages (pass routing onto the Angular app)
@app.route('/')
@app.route('/about')
@app.route('/blog')
@app.route('/message')
def basic_pages(**kwargs):
	return make_response(open('angular_flask/templates/index.html').read())


@app.route('/_api/message')
def api_message():
	data = {'msg': 'OLA MUNDO'}
	return jsonify(data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



