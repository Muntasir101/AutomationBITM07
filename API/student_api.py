import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

students = [
    {
        'id': 0,
        'name': 'John',
        'dept': 'CSE'
    },
    {
        'id': 1,
        'name': 'Smith',
        'dept': 'EEE'
    },
    {
        'id': 2,
        'name': 'Kevin',
        'dept': 'SWE'
    },
    {
        'id': 3,
        'name': 'Superman',
        'dept': 'CSE'
    }
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello world</h1> <p> This text from API </p>"


@app.route('/api/students/all', methods=['GET'])
def api_student_all():
    return jsonify(students)


@app.route('/api/students', methods=['GET'])
def api_student_id():
    # Search if an ID was provided as of the URL
    # IF ID is provided , assign it to a variable
    # If ID is not provided, display an error message

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id provided.Please specify an id"

    # creates an empty list of students
    results = []

    for student in students:
        if student['id'] == id:
            results.append(student)

    return jsonify(results)


app.run()
