from datetime import datetime
import os

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)


@app.route('/')
def index():
   referral_id = request.args.get("referral_id")

   # TODO - 
   # Lookup referral_id in the SQL DATABASE
  
   # If it exists
   print('Request for index page received')
   return render_template('index.html', referral_id = referral_id)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/dobchecker', methods=['POST'])
def dobchecker():
   dob = request.form.get('dob')

   # TODO - 
   #  Check dob entered, with dob from referral_id SQL record

   if dob:
       print('Request for hello page received with name=%s' % dob)
       return render_template('dobchecker.html', name = dob)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))




if __name__ == '__main__':
   app.run()