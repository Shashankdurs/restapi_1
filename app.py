from flask import Flask,jsonify

todo=Flask('__name__')

students = [
        {
            'id': 1,
            'student-name':'std1',
            'age':'20',
            'email':'std1@gmail.com'
        },
        {
            'id': 2,
            'student-name': 'std2',
            'age': '20',
            'email': 'std2@gmail.com'
        },
        {
            'id': 3,
            'student-name': 'std3',
            'age': '20',
            'email': 'std3@gmail.com'
        }
    ]
@todo.route('/student-list')
def student_list():
    return jsonify(students)


@todo.route('/student/get/<int:id>',methods=['GET'])
def student_id(id):
    student=next((student for student in students if student['id']==id),None)

    if student is None:
        return jsonify({'message':'Student not found'}),404

    return jsonify(student)



if __name__=='__main__':
    todo.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )