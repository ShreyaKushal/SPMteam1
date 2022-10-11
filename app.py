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
    JobRole_Status = db.Column(db.String(50))


    def __init__(self, JobRole_ID, JobRole_Name, JobeRole_Status): #initialise value of job role record, specify properties of a job role when it is created
        self.JobRole_ID = JobRole_ID
        self.JobRole_Name = JobRole_Name
        self.JobRole_Status = JobeRole_Status
  
 
    def json(self): #returns json representation of the job role
        return {"JobRole_ID": self.JobRole_ID, "JobRole_Name": self.JobRole_Name, "JobRole_Status":self.JobRole_Status}
#db.create_all()

class Skills(db.Model):
    __tablename__ = 'Skills'
    Skill_ID = db.Column(db.String(50), primary_key=True)
    Skill_Name = db.Column(db.String(50), nullable=False)
    Skill_Desc = db.Column(db.String(255), nullable=False)
    Skill_Status = db.Column(db.String(50), nullable=False)

    def __init__(self, Skill_ID, Skill_Name, Skill_Desc, Skill_Status): #initialise value of job role record, specify properties of a job role when it is created
        self.Skill_ID = Skill_ID
        self.Skill_Name = Skill_Name
        self.Skill_Desc = Skill_Desc
        self.Skill_Status = Skill_Status
 
    def json(self): #returns json representation of the job role
        return {"Skill_ID": self.Skill_ID, "Skill_Name": self.Skill_Name, "Skill_Desc": self.Skill_Desc, "Skill_Status": self.Skill_Status}

class Courses(db.Model):
    __tablename__ = 'Courses'
    Course_ID= db.Column(db.String(50), primary_key=True)
    Course_Name= db.Column(db.String(50), nullable=False)
    Course_Desc= db.Column(db.String(50), nullable=False)
    Course_Status= db.Column(db.String(50), nullable=False)
    Course_Type= db.Column(db.String(50), nullable=False)
    Course_Category= db.Column(db.String(50), nullable=False)

    def __init__(self, Course_ID, Course_Name, Course_Desc, Course_Status, Course_Type, Course_Category):
        self.Course_ID = Course_ID
        self.Course_Name = Course_Name
        self.Course_Desc = Course_Desc
        self.Course_Status = Course_Status
        self.Course_Type = Course_Type
        self.Course_Category = Course_Category

    def json(self): 
        return { 'Course_ID' : self.Course_ID, 'Course_Name' : self.Course_Name, 'Course_Desc' : self.Course_Desc, 'Course_Status' : self.Course_Status, 'Course_Type' : self.Course_Type, 'Course_Category' : self.Course_Category}



class LearningJourney(db.Model):
    __tablename__ = 'LearningJourney'
    LearningJourney_ID= db.Column(db.String(50), primary_key=True)
    Staff_ID =  db.Column(db.String(50), nullable=False)
    JobRole_ID= db.Column(db.String(50), nullable=False)
    Skill_ID= db.Column(db.String(50), nullable=False)
    Course_ID= db.Column(db.String(50), nullable=False)

    def __init__(self, LearningJourney_ID, Staff_ID, JobRole_ID, Skill_ID, Course_ID):
        self.LearningJourney_ID = LearningJourney_ID
        self.Staff_ID = Staff_ID
        self.JobRole_ID= JobRole_ID
        self.Skill_ID = Skill_ID
        self.Course_ID = Course_ID
        

    def json(self): 
        return { 'LearningJourney_ID' : self.LearningJourney_ID, 'Staff_ID' : self.Staff_ID, 'JobRole_ID' : self.JobRole_ID, 'Skill_ID' : self.Skill_ID, 'Course_ID' : self.Course_ID}

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

@app.route("/LearningJourneys")
def get_all_LearningJourneys():
    LearningJourneys = LearningJourney.query.all()
    if len(LearningJourneys):
        return jsonify({
            "data": [LearningJourney.json() for LearningJourney in LearningJourneys]
        }), 200
    else:
        return jsonify({
            "message": "Learning Journey not found."
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


 # @app.route('/allcourses/<string:user_id>')
# def get_all_courses(user_id):
  #  relevant_course = 



@app.route("/JobRoles/<string:jobrole_id>", methods=['PUT'])
def update_jobrole(JobRole_ID):
    try:
        jobrole = JobRoles.query.filter_by(JobRole_ID=JobRole_ID).first()
        if not jobrole:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "JobRole_ID": JobRole_ID
                    },
                    "message": "Job role not found."
                }
            ), 404

        # update status
        data = request.get_json()
        if data['JobRole_Status']:
            JobRoles.JobRole_Status = data['JobRole_Status']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": JobRoles.json()
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "JobRole_ID": JobRole_ID
                },
                "message": "An error occurred while updating the job role. " + str(e)
            }
        ), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)