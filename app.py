from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root' + \
                                        '@localhost:3306/spm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class JobRoles(db.Model):
    __tablename__ = 'JobRoles'
    JobRole_ID = db.Column(db.String(50), primary_key=True)
    JobRole_Name = db.Column(db.String(50))


    def __init__(self, JobRole_ID, JobRole_Name): #initialise value of job role record, specify properties of a job role when it is created
        self.JobRole_ID = JobRole_ID
        self.JobRole_Name = JobRole_Name
  
 
    def json(self): #returns json representation of the job role
        return {"JobRole_ID": self.JobRole_ID, "JobRole_Name": self.JobRole_Name}
#db.create_all()

class Skills(db.Model):
    __tablename__ = 'Skills'
    Course_ID = db.Column(db.String(50), primary_key=True)
    Course_Name = db.Column(db.String(50), nullable=False)
    Course_Desc = db.Column(db.String(255), nullable=False)

    def __init__(self, Course_ID, Course_Name, Course_Desc): #initialise value of job role record, specify properties of a job role when it is created
        self.Course_ID = Course_ID
        self.Course_Name = Course_Name
        self.Course_Desc = Course_Desc
 
    def json(self): #returns json representation of the job role
        return {"Course_ID": self.Course_ID, "Course_Name": self.Course_Name, "Course_Desc": self.Course_Desc}
        
class Courses(db.Model):
    __tablename__ = 'Courses'
    Course_ID = db.Column(db.String(50), primary_key=True)
    Course_Name = db.Column(db.String(50), nullable=False)
    Course_Desc = db.Column(db.String(255), nullable=False)
    Course_Status = db.Column(db.String(15), nullable=False)
    Course_Type = db.Column(db.String(10), nullable=False)
    Course_Category = db.Column(db.String(50), nullable=False)

    def __init__(self, Course_ID, Course_Name, Course_Desc, Course_Status, Course_Type, Course_Category): #initialise value of job role record, specify properties of a job role when it is created
        self.Course_ID = Course_ID
        self.Course_Name = Course_Name
        self.Course_Desc = Course_Desc
        self.Course_Status = Course_Status
        self.Course_Type = Course_Type
        self.Course_Category = Course_Category
 
    def json(self): #returns json representation of the job role
        return {"Course_ID": self.Course_ID, "Course_Name": self.Course_Name, "Course_Desc": self.Course_Desc, 
        "Course_Status":self.Course_Status, "Course_Type":self.Course_Type, "Course_Category": self.Course_Category}



@app.route("/JobRoles")
def get_all_JobRoles():
    JobRole = JobRoles.query.all()
    if len(JobRole):
        return jsonify({
            "data": [JobRoles.json() for JobRoles in JobRole]
        }), 200
    else:
        return jsonify({
            "message": "Job Role not found."
        }), 404


@app.route("/Skills")
def get_all_Skills():
    Skill = Skills.query.all()
    if len(Skill):
        return jsonify({
            "data": [Skills.json() for Skills in Skill]
        }), 200
    else:
        return jsonify({
            "message": "Skill not found."
        }), 404

@app.route("/Courses")
def get_all_Courses():
    Course = Courses.query.all()
    if len(Course):
        return jsonify({
            "data": [Courses.json() for Courses in Course]
        }), 200
    else:
        return jsonify({
            "message": "Course not found."
        }), 404

# def JobRole_by_id(JobRole_ID):
#     JobRole = JobRoles.query.filter_by(JobRole_ID=JobRole_ID).all()
#     if JobRole:
#         return jsonify({
#             "data": [JobRoles.json() for JobRoles in JobRole]
#         }), 200
#     else:
#         return jsonify({
#             "message": "Job Role not found."
#         }), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)