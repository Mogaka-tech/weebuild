""" server/app.py """

from flask import Flask, jsonify


@app.route('/courses', methods=['GET'])
def all_courses():
    return jsonify({
        'status': 'success',
        'courses': COURSES
    })

COURSES = [
    {
        'title': 'Effective JavaScript: 68 Specific Ways to Harness the Power of JavaS                   cript ',
        'author': 'David Herman',
        'paperback': True
    },
    {
        'title': 'JavaScript: The Good Parts',
        'author': 'Douglas Crockford',
        'paperback': False
    },
    {
        'title': 'Eloquent JavaScript: A Modern Introduction to Programming',
        'author': 'Marijn Haverbeke',
        'paperback': True
    }
]
