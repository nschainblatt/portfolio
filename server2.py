from flask import Flask, render_template, send_from_directory, request, redirect
import os
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(email_data):
    with open('database.txt', mode='a') as database:
        print(email_data)
        email = email_data['email']
        subject = email_data['subject']
        message = email_data['message']
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(email_data):
    with open('database.csv', mode='a', newline='') as database2:
        print(email_data)
        email = email_data['email']
        subject = email_data['subject']
        message = email_data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        print('something went wrong. try')
