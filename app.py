from curses import flash
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root' + \
                                        '@localhost:3306/spm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                        'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)
CORS(app, support_credentials=True)

#many-to-many rlationship db table
job_role_with_skills = db.Table('jobrolewithskills',
        db.Column('JobRole_ID', db.String(50), db.ForeignKey('JobRoles.JobRole_ID')),
        db.Column('Skill_ID', db.String(50), db.ForeignKey('Skills.Skill_ID'))
)

class JobRoles(db.Model):
    __tablename__ = 'JobRoles'
    JobRole_ID = db.Column(db.String(50), primary_key=True)
    JobRole_Name = db.Column(db.String(50))
    JobRole_Status = db.Column(db.String(50))


    def __init__(self, JobRole_ID, JobRole_Name, JobRole_Status): #initialise value of job role record, specify properties of a job role when it is created
        self.JobRole_ID = JobRole_ID
        self.JobRole_Name = JobRole_Name
        self.JobRole_Status = JobRole_Status


    def json(self): #returns json representation of the job role
        return {"JobRole_ID": self.JobRole_ID, "JobRole_Name": self.JobRole_Name, "JobRole_Status":self.JobRole_Status}


    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    def __repr__(self):
        return f'<JobRole: "{self.name}">' 
    
#db.create_all()

class Skills(db.Model):
    __tablename__ = 'Skills'
    Skill_ID = db.Column(db.String(50), primary_key=True)
    Skill_Name = db.Column(db.String(50), nullable=False)
    Skill_Desc = db.Column(db.String(255), nullable=False)
    Skill_Status = db.Column(db.String(50), nullable=False)
    jobroles = db.relationship('JobRoles', secondary=job_role_with_skills,
        backref=db.backref('Skills'))

    def __init__(self, Skill_ID, Skill_Name, Skill_Desc, Skill_Status): #initialise value of job role record, specify properties of a job role when it is created
        self.Skill_ID = Skill_ID
        self.Skill_Name = Skill_Name
        self.Skill_Desc = Skill_Desc
        self.Skill_Status = Skill_Status

    def json(self): #returns json representation of the job role
        return {"Skill_ID": self.Skill_ID, "Skill_Name": self.Skill_Name, "Skill_Desc": self.Skill_Desc, "Skill_Status": self.Skill_Status}
    
    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result
    
    def __repr__(self):
        return f'<Skill: "{self.name}">'

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

class SkillsRequiredCourses(db.Model):
    __tablename__ = 'SkillsRequiredCourses'
    Course_ID= db.Column(db.String(50), primary_key=True)
    Skill_ID =  db.Column(db.String(50), primary_key=True)


    def __init__(self, Course_ID, Skill_ID):
        self.Course_ID = Course_ID
        self.Skill_ID = Skill_ID      

    def json(self): 
        return {'Course_ID' : self.Course_ID, 'Skill_ID' : self.Skill_ID}

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

db.create_all()

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

# Add a Job Role
@app.route("/addJobRole", methods=['POST'])
def create_JobRole():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('JobRole_ID', 'JobRole_Name',
                       'JobRole_Status')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    JobRole = JobRoles(
        JobRole_ID=data['JobRole_ID'], JobRole_Name=data['JobRole_Name'],
        JobRole_Status="Active"
    )
    # Commit to DB
    try:
        db.session.add(JobRole)
        db.session.commit()
        return jsonify(JobRole.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

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

@app.route("/StaffViewJobRoles")
def jobroles():
    jobrole_list = JobRoles.query.all()
    return jsonify(
        {
            "data": [jobrole.to_dict()
                    for jobrole in jobrole_list]
        }
    ), 200

@app.route("/StaffViewJobRoles/<string:jobrole_id>")
def view_JobRoleWithSkills(jobrole_id):
    skills_list = Skills.query.filter(Skills.jobroles.any(JobRole_ID=jobrole_id)).all()
    if skills_list:
        return jsonify(
            {
                "data":[skills.to_dict()
                        for skills in skills_list]
            }
        ), 200
    return jsonify(
        {
            "message": "Skills have yet to assign"
        }
    ), 404


@app.route("/addSkill", methods=['POST'])
def create_skill():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('Skill_ID', 'Skill_Name',
                       'Skill_Desc', 'Skill_Status')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate doctor
    # Skill = Skills.query.filter_by(id=data['doctor_id']).first()
    # if not doctor:
    #     return jsonify({
    #         "message": "Doctor not valid."
    #     }), 500

    # (2): Compute charges
    # charge = doctor.calculate_charges(data['length'])

    # # (3): Validate patient
    # patient = Patient.query.filter_by(id=data['patient_id']).first()
    # if not patient:
    #     return jsonify({
    #         "message": "Patient not valid."
    #     }), 500

    # # (4): Subtract charges from patient's e-wallet
    # try:
    #     patient.ewallet_withdraw(charge)
    # except Exception:
    #     return jsonify({
    #         "message": "Patient does not have enough e-wallet funds."
    #     }), 500
    
    # See if skill already exist 


    # (4): Create consultation record
    Skill = Skills(
        Skill_ID=data['Skill_ID'], Skill_Name=data['Skill_Name'],
        Skill_Desc=data['Skill_Desc'], Skill_Status="Active"
    )

    # (5): Commit to DB
    try:
        db.session.add(Skill)
        db.session.commit()
        return jsonify(Skill.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500


@app.route("/addSkillreqCourses", methods=['POST'])
def create_skillreqCourses():
    data = request.get_json()
    if not all(key in data.keys() for
            key in ('Course_ID', 'Skill_ID')):
            return jsonify({
                "message": "Incorrect JSON object provided."
            }), 500
    
    SkillsRequiredCourses = SkillsRequiredCourses(
            Skill_ID=data['Skill_ID'], Course_ID=data['Course_ID']
        )

        # (5): Commit to DB
    try:
        db.session.add(SkillsRequiredCourses)
        db.session.commit()
        return jsonify(SkillsRequiredCourses.to_dict()), 201
    except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500

#@app.route("/JobRoles/<string:jobrole_id>", methods=['DELETE'])
#def delete_jobRole(jobrole_id):
#    jobrole_to_delete=JobRoles.query.get(jobrole_id)
#    try:
#        db.session.delete(jobrole_to_delete)
#        db.session.commit()
#        flash("Job role deleted susccessfully")
#    except:
#        flash("There was no such job role")
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)