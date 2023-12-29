from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'position': 'Python Developer',
    'location': 'New York, USA',
    'salary': '$ 50,000'
}, {
    'id': 2,
    'position': 'Java Developer',
    'location': 'Bangalore, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 3,
    'position': 'Network Engineer',
    'location': 'Hyderabad, India',
    'salary': '$ 25,00,000'
}, {
    'id': 4,
    'position': 'Customer Support',
    'location': 'Pune, India',
    'salary': '$ 15,00,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Careers')


@app.route('/jobs')
def job_list():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
