from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    try:
        return render_template('maths_play.html')
    except Exception as e:
        return f"Error: {str(e)}<br>Current directory: {os.getcwd()}"

@app.route('/arithmetic_operations')
def arithmetic_operations():
    return render_template('arithmetic_operations.html')

@app.route('/powers_roots')
def power_roots():
    return render_template('powers_roots.html')

@app.route('/number_theory')
def number_theory():
    return render_template('number_theory.html')

@app.route('/mensuration')
def mensuration():
    return render_template('mensuration.html')

if __name__ == '__main__':
    app.debug = True
    app.run()