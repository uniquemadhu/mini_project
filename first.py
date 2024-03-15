from flask import Flask, render_template, request
import pandas as pd
import os
app = Flask(__name__)

# Load the dataset containing paths to real and fake logos
real_logos_df = pd.read_csv('logo_dataset/real_logo.csv')
fake_logos_df = pd.read_csv('logo_dataset/fake_logo.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display_logos', methods=['POST'])
def display_logos():
    brand_name = request.form['brand_name']
    
    real_logo_path = 'real_logo/' + brand_name + '/000001.jpg'
    fake_logo_path = 'fake_logo/' + brand_name + '/000003.jpg' 
    
    return render_template('logos.html', real_logo_path=real_logo_path, fake_logo_path=fake_logo_path)


if __name__ == '__main__':
    app.run(debug=True)
