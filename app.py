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


class JobRoles(db.Model):
    __tablename__ = 'JobRoles'
    JobRole_ID = db.Column(db.String(10), primary_key=True)
    JobRole_Name = db.Column(db.String(50), nullable=False)
    JobRole_Status = db.Column(db.String(10), nullable=False)

    def __init__(self, JobRole_ID, JobRole_Name, JobRole_Status): #initialise value of job role record, specify properties of a job role when it is created
        self.JobRole_ID = JobRole_ID
        self.JobRole_Name = JobRole_Name
        self.JobRole_Status = JobRole_Status

    def json(self): #returns json representation of the job role
        return {"JobRole_ID": self.JobRole_ID, "JobRole_Name": self.JobRole_Name, "JobRole_Status":self.JobRole_Status}
    
    def getName(self):
        return {"JobRole_Name":self.JobRole_Name}
    
    def name(self):
        return self.JobRole_Name

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
    Skill_ID = db.Column(db.String(10), primary_key=True)
    Skill_Name = db.Column(db.String(50), nullable=False)
    Skill_Desc = db.Column(db.String(255), nullable=False)
    Skill_Status = db.Column(db.String(10), nullable=False)

    def __init__(self, Skill_ID, Skill_Name, Skill_Desc, Skill_Status): #initialise value of job role record, specify properties of a job role when it is created
        self.Skill_ID = Skill_ID
        self.Skill_Name = Skill_Name
        self.Skill_Desc = Skill_Desc
        self.Skill_Status = Skill_Status

    def json(self): #returns json representation of the job role
        return {"Skill_ID": self.Skill_ID, "Skill_Name": self.Skill_Name, "Skill_Desc": self.Skill_Desc, "Skill_Status": self.Skill_Status}
    
    def getName(self):
        return {"Skill_Name":self.Skill_Name}
    
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
    Course_ID= db.Column(db.String(20), primary_key=True)
    Course_Name= db.Column(db.String(50), nullable=False)
    Course_Desc= db.Column(db.String(255))
    Course_Status= db.Column(db.String(15))
    Course_Type= db.Column(db.String(10))
    Course_Category= db.Column(db.String(50))

    def __init__(self, Course_ID, Course_Name, Course_Desc, Course_Status, Course_Type, Course_Category):
        self.Course_ID = Course_ID
        self.Course_Name = Course_Name
        self.Course_Desc = Course_Desc
        self.Course_Status = Course_Status
        self.Course_Type = Course_Type
        self.Course_Category = Course_Category

    def json(self): 
        return { 'Course_ID' : self.Course_ID, 'Course_Name' : self.Course_Name, 'Course_Desc' : self.Course_Desc, 'Course_Status' : self.Course_Status, 'Course_Type' : self.Course_Type, 'Course_Category' : self.Course_Category}

    def getName(self):
        return {"Course_Name":self.Course_Name}
    
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
        
class Role(db.Model):
    __tablename__ = 'Role'
    Role_ID = db.Column(db.Integer, primary_key=True)
    Role_Name = db.Column(db.String(20), nullable=False)

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

class Staff(db.Model):
    __tablename__ = 'Staff'
    Staff_ID = db.Column(db.Integer, primary_key=True)
    Staff_Fname = db.Column(db.String(50), nullable=False)
    Staff_Lname = db.Column(db.String(50), nullable=False)
    Dept = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Role_ID = db.Column(db.Integer, db.ForeignKey('Role.Role_ID'))

    def json(self): 
        return {'Staff_ID' : self.Staff_ID, 'Staff_Fname' : self.Staff_Fname, 'Staff_Lname' : self.Staff_Lname, 'Dept' : self.Dept, 'Email' : self.Email, 'Role_ID' : self.Role_ID}

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

class JobRoleWithSkills(db.Model):
    __tablename__ = 'JobRoleWithSkills'
    JobRoleWithSkills_ID = db.Column(db.Integer, primary_key=True)
    JobRole_ID = db.Column(db.String(10), db.ForeignKey('Role.Role_ID'))
    Skill_ID = db.Column(db.String(10), db.ForeignKey('Skills.Skill_ID'))

    def __init__(self, JobRole_ID, Skill_ID):
        self.JobRole_ID = JobRole_ID
        self.Skill_ID = Skill_ID      

    def json(self): 
        return {'JobRoleWithSkills_ID' : self.JobRoleWithSkills_ID, 'JobRole_ID' : self.JobRole_ID, 'Skill_ID' : self.Skill_ID}
    
    def getSkillID(self):
        return self.Skill_ID
    
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

class SkillsRequiredCourses(db.Model):
    __tablename__ = 'SkillsRequiredCourses'
    SkillsRequiredCourses_ID = db.Column(db.Integer, primary_key=True)
    Course_ID = db.Column(db.String(20), db.ForeignKey('Courses.Course_ID'))
    Skill_ID = db.Column(db.String(10), db.ForeignKey('Skills.Skill_ID'))

    def __init__(self, Course_ID, Skill_ID):
        self.Course_ID = Course_ID
        self.Skill_ID = Skill_ID      

    def json(self): 
        return {'SkillsRequiredCourses_ID' : self.SkillsRequiredCourses_ID, 'Course_ID' : self.Course_ID, 'Skill_ID' : self.Skill_ID}
    
    def getCourseID(self):
        return self.Course_ID

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

class LearningJourney(db.Model):
    __tablename__ = 'LearningJourney'
    LearningJourney_ID = db.Column(db.Integer, primary_key=True)
    Staff_ID =  db.Column(db.Integer, db.ForeignKey('Staff.Staff_ID'))
    JobRole_ID = db.Column(db.String(10), db.ForeignKey('JobRoles.JobRole_ID'))
    Skill_ID = db.Column(db.String(10), db.ForeignKey('Skills.Skill_ID'))
    Course_ID = db.Column(db.String(20), db.ForeignKey('Courses.Course_ID'))

    def __init__(self, Staff_ID, JobRole_ID, Skill_ID, Course_ID):
        self.Staff_ID = Staff_ID
        self.JobRole_ID= JobRole_ID
        self.Skill_ID = Skill_ID
        self.Course_ID = Course_ID

    def json(self): 
        return { 'LearningJourney_ID' : self.LearningJourney_ID, 'Staff_ID' : self.Staff_ID, 'JobRole_ID' : self.JobRole_ID, 'Skill_ID' : self.Skill_ID, 'Course_ID' : self.Course_ID}

    def getCourseID(self):
        return self.Course_ID

    def getJobRoleID(self):
        return self.JobRole_ID
    
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

db.create_all()

# Retrieve staff details based on staffID
@app.route("/StaffDetails/<string:staff_id>")
def get_StaffDetails(staff_id):
    staff = Staff.query.filter_by(Staff_ID=staff_id).first()
    if staff:
        return jsonify({
            "data": staff.json()
        }), 200
    else:
        return jsonify({
            "message": "JobRole not found."
        }), 404

# Retrieve all active jobroles
@app.route("/ActiveJobRoles")
def get_all_ActiveJobRoles():
    JobRole = JobRoles.query.filter_by(JobRole_Status = 'Active').all()
    if len(JobRole):
        return jsonify({
            "data": [JobRoles.json() for JobRoles in JobRole]
        }), 200
    else:
        return jsonify({
            "message": "Job Role not found."
        }), 404

# Retrieve top 3 active jobroles
@app.route("/TopThreeActiveJobRoles")
def get_topthree_ActiveJobRoles():
    JobRole = JobRoles.query.filter_by(JobRole_Status = 'Active').limit(3).all()
    if len(JobRole):
        return jsonify({
            "data": [JobRoles.json() for JobRoles in JobRole]
        }), 200
    else:
        return jsonify({
            "message": "Job Role not found."
        }), 404

# Retrieve top 3 active skills
@app.route("/TopThreeActiveSkills")
def get_topthree_ActiveSkills():
    Skill = Skills.query.filter_by(Skill_Status = 'Active').limit(3).all()
    if len(Skill):
        return jsonify({
            "data": [Skills.json() for Skills in Skill]
        }), 200
    else:
        return jsonify({
            "message": "Job Role not found."
        }), 404

# Retrieve all inactive jobroles
@app.route("/InactiveJobRoles")
def get_all_InactiveJobRoles():
    JobRole = JobRoles.query.filter_by(JobRole_Status = 'Inactive').all()
    return jsonify({
        "data": [JobRoles.json() for JobRoles in JobRole]
    }), 200

# Retrieve all active skills
@app.route("/ActiveSkills")
def get_all_ActiveSkills():
    Skill = Skills.query.filter_by(Skill_Status = 'Active').all()
    if len(Skill):
        return jsonify({
            "data": [Skills.json() for Skills in Skill]
        }), 200
    else:
        return jsonify({
            "message": "Skill not found."
        }), 404

# Retrieve all inactive skills
@app.route("/InactiveSkills")
def get_all_InactiveSkills():
    Skill = Skills.query.filter_by(Skill_Status = 'Inactive').all()
    return jsonify({
        "data": [Skills.json() for Skills in Skill]
    }), 200

# Create a Job Role
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
        return jsonify({"data": JobRole.to_dict()}), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

# Retrieve all courses
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

# Retrieve jobrole details based on Jobrole_ID
@app.route("/JobRolesDetails/<string:jobrole_id>")
def get_JobRoleDetails(jobrole_id):
    jobrole = JobRoles.query.filter_by(JobRole_ID=jobrole_id).first()
    if jobrole:
        return jsonify({
            "data": jobrole.json()
        }), 200
    else:
        return jsonify({
            "message": "JobRole not found."
        }), 404

# Retrieve skill details based on skill_ID
@app.route("/SkillDetails/<string:skill_id>")
def get_SkillDetails(skill_id):
    skill = Skills.query.filter_by(Skill_ID=skill_id).first()
    if skill:
        return jsonify({
            "data": skill.json()
        }), 200
    else:
        return jsonify({
            "message": "JobRole not found."
        }), 404

# Retrieve list of skill_ID assign on that Jobrole (JobRole_ID)
@app.route("/SkillsOnJobRole/<string:jobrole_id>")
def get_SkillsOnJobRole(jobrole_id):
    skill_list = JobRoleWithSkills.query.filter_by(JobRole_ID=jobrole_id).all()
    return jsonify(
        {
            "data": [skill.getSkillID() 
                for skill in skill_list]
        }
    ), 200

# Retrieve list of course_ID assign on that skill (Skill_ID)
@app.route("/CoursesOnSkill/<string:skill_id>")
def get_CoursesOnSkill(skill_id):
    course_list = SkillsRequiredCourses.query.filter_by(Skill_ID=skill_id).all()
    return jsonify(
        {
            "data": [course.getCourseID() 
                for course in course_list]
        }
    ), 200

# Update jobrole based on JobRole_ID
@app.route("/JobRolesDetails/<string:JobRole_ID>/<string:new_JobRole_ID>/<string:new_JobRole_Name>", methods=['GET', 'POST'])
def update_jobroleDetails(JobRole_ID, new_JobRole_ID, new_JobRole_Name):

    jobrole = JobRoles.query.filter_by(JobRole_ID = JobRole_ID).first()
    
    setattr(jobrole, 'JobRole_ID', new_JobRole_ID)
    setattr(jobrole, 'JobRole_Name', new_JobRole_Name)

    try:
        db.session.commit()
        jobrole_list = JobRoles.query.all()
        return jsonify(
            {
                "data": [jobrole.to_dict()
                        for jobrole in jobrole_list]
            }
        ), 200
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

# Update skill based on Skill_ID
@app.route("/SkillDetails/<string:Skill_ID>/<string:new_Skill_ID>/<string:new_Skill_Name>/<string:new_Skill_Desc>", methods=['GET', 'POST'])
def update_skillDetails(Skill_ID, new_Skill_ID, new_Skill_Name, new_Skill_Desc):

    skill = Skills.query.filter_by(Skill_ID = Skill_ID).first()
    
    setattr(skill, 'Skill_ID', new_Skill_ID)
    setattr(skill, 'Skill_Name', new_Skill_Name)
    setattr(skill, 'Skill_Desc', new_Skill_Desc)

    try:
        db.session.commit()
        skill_list = Skills.query.all()
        return jsonify(
            {
                "data": [skill.to_dict()
                        for skill in skill_list]
            }
        ), 200
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

# Soft delete jobrole based on JobRole_ID
@app.route("/JobRoles/<string:JobRole_ID>", methods=['GET', 'POST'])
def update_jobrole(JobRole_ID):
    jobrole = JobRoles.query.filter_by(JobRole_ID = JobRole_ID).first()
    
    setattr(jobrole, 'JobRole_Status', "Inactive")
    db.session.commit()

    jobrole_list = JobRoles.query.all()

    return jsonify(
        {
            "data": [jobrole.to_dict()
                    for jobrole in jobrole_list]
        }
    ), 200

# Re-activate jobrole based on JobRole_ID
@app.route("/ReactivateJobRoles/<string:JobRole_ID>", methods=['GET', 'POST'])
def reactivate_jobrole(JobRole_ID):
    jobrole = JobRoles.query.filter_by(JobRole_ID = JobRole_ID).first()
    
    setattr(jobrole, 'JobRole_Status', "Active")
    db.session.commit()

    jobrole_list = JobRoles.query.all()

    return jsonify(
        {
            "data": [jobrole.to_dict()
                    for jobrole in jobrole_list]
        }
    ), 200

# Soft delete skill based on Skill_ID
@app.route("/Skills/<string:Skill_ID>", methods=['GET', 'POST'])
def update_skill(Skill_ID):
    skill = Skills.query.filter_by(Skill_ID = Skill_ID).first()
    
    setattr(skill, 'Skill_Status', "Inactive")
    db.session.commit()

    skill_list = Skills.query.all()

    return jsonify(
        {
            "data": [skill.to_dict()
                    for skill in skill_list]
        }
    ), 200

# Re-activate skill based on Skill_ID
@app.route("/ReactivateSkills/<string:Skill_ID>", methods=['GET', 'POST'])
def reactivate_skill(Skill_ID):
    skill = Skills.query.filter_by(Skill_ID = Skill_ID).first()
    
    setattr(skill, 'Skill_Status', "Active")
    db.session.commit()

    skill_list = Skills.query.all()

    return jsonify(
        {
            "data": [skill.to_dict()
                    for skill in skill_list]
        }
    ), 200

# Retrieve jobrole_Name based on jobrole_ID
@app.route("/StaffViewJobRoles/<string:jobrole_id>")
def get_jobrole(jobrole_id):
    jobrole = JobRoles.query.filter_by(JobRole_ID=jobrole_id).first()
    return jsonify(
        {
            "data": [jobrole.getName()]
        }
    ), 200

# Retrieve jobrole_Name based on jobrole_ID
@app.route("/StaffGetJobRolesName/<string:jobrole_id>")
def get_jobroleName(jobrole_id):
    jobrole = JobRoles.query.filter_by(JobRole_ID=jobrole_id).first()
    return jsonify(
        {
            "data": jobrole.name()
        }
    ), 200

# Retrieve skill_Name based on skill_ID
@app.route("/StaffGetSkillName/<string:skill_id>")
def get_skillName(skill_id):
    skill = Skills.query.filter_by(Skill_ID=skill_id).first()
    return jsonify(
        {
            "data": [skill.getName()]
        }
    ), 200

# Retrieve course_Name based on course_ID
@app.route("/StaffGetCourseName/<string:course_id>")
def get_courseName(course_id):
    course = Courses.query.filter_by(Course_ID=course_id).first()
    return jsonify(
        {
            "data": [course.getName()]
        }
    ), 200

# Retrieve required skills based on jobrole_ID
@app.route("/StaffViewJobRolesWithSkills/<string:jobrole_id>")
def view_JobRoleWithSkills(jobrole_id):
    skills_list = Skills.query.join(JobRoleWithSkills, JobRoleWithSkills.Skill_ID==Skills.Skill_ID).join(JobRoles, JobRoles.JobRole_ID==JobRoleWithSkills.JobRole_ID).filter(JobRoles.JobRole_ID==jobrole_id).all()
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

# Retrieve required courses based on skill_ID
@app.route("/StaffViewCourses/<string:skill_id>")
def view_CoursesInSkill(skill_id):
    course_list = Courses.query.join(SkillsRequiredCourses, SkillsRequiredCourses.Course_ID==Courses.Course_ID).join(Skills, Skills.Skill_ID==SkillsRequiredCourses.Skill_ID).filter(Skills.Skill_ID==skill_id).all()
    return jsonify(
        {
            "data":[course.to_dict()
                    for course in course_list]
            }
    ), 200

# Create Staff Learning Journey
@app.route("/StaffLearningJourney", methods=['POST'])
def create_learningJourney():
    data = request.get_json()
    if not all(key in data.keys() for key in ('JobRole_ID', 'Skill_ID', 'Course_ID', 'Staff_ID')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate jobrole
    jobrole = JobRoles.query.filter_by(JobRole_ID=data['JobRole_ID']).first()
    if not jobrole:
        return jsonify({
            "message": "Job role not valid."
        }), 500
    
    # (2): Validate skill
    skill = Skills.query.filter_by(Skill_ID=data['Skill_ID']).first()
    if not skill:
        return jsonify({
            "message": "Skill not valid."
        }), 500

    # (3): Validate course
    course = Courses.query.filter_by(Course_ID=data['Course_ID']).first()
    if not course:
        return jsonify({
            "message": "Course not valid."
        }), 500
    
    # (4): Validate staff
    staff = Staff.query.filter_by(Staff_ID=data['Staff_ID']).first()
    if not staff:
        return jsonify({
            "message": "Staff not valid."
        }), 500
    
    # (5): Create learning journey record
    learningJourney = LearningJourney(
        JobRole_ID=data['JobRole_ID'],
        Skill_ID=data['Skill_ID'],
        Course_ID=data['Course_ID'],
        Staff_ID=data['Staff_ID']
    )
    
    # (6): Commit to DB
    try:
        db.session.add(learningJourney)
        db.session.commit()
        return jsonify(learningJourney.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

# Retrieve Learning journey Based on staffid and jobroleid
@app.route("/StaffLearningJourney/<int:staff_id>/<string:jobrole_id>")
def get_StaffLearningJourneysBasedOnJobRole(staff_id, jobrole_id):
    learningjourney_list = LearningJourney.query.filter_by(Staff_ID=staff_id).filter_by(JobRole_ID=jobrole_id).all()
    if learningjourney_list:
        return jsonify({
            "data": [LearningJourney.json() for LearningJourney in learningjourney_list]
        }), 200

# Retrieve the list of jobroleid added by staff (staffid) to the learning journey
@app.route("/StaffLearningJourney/<int:staff_id>")
def get_StaffLearningJourneys(staff_id):
    jobrole_list = LearningJourney.query.filter_by(Staff_ID=staff_id).all()
    return jsonify({
        "data": [jobrole.getJobRoleID() 
                for jobrole in jobrole_list]
    }), 200
        
# Delete course in Staff Learning Journey
@app.route("/StaffLearningJourney/<string:staff_id>/<string:jobrole_id>/<string:course_id>", methods=['DELETE'])
def delete_coursesFromStaffLearningJourney(staff_id, jobrole_id, course_id):
    learningJourney = LearningJourney.query.filter_by(Staff_ID=staff_id).filter_by(JobRole_ID=jobrole_id).filter_by(Course_ID=course_id).first()
    if learningJourney:
        db.session.delete(learningJourney)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Staff_ID": staff_id,
                    "JobRole_ID": jobrole_id,
                    "Course_ID": course_id
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "Staff_ID": staff_id,
                "JobRole_ID": jobrole_id,
                "Course_ID": course_id
            },
            "message": "Course not found in Learning Journey."
        }
    ), 404

# Delete the entire Staff Learning Journey
@app.route("/StaffDeleteLearningJourney/<string:staff_id>/<string:jobrole_id>", methods=['DELETE'])
def delete_entireStaffLearningJourneyBasedOnJobRole(staff_id, jobrole_id):
    learningJourney = LearningJourney.query.filter_by(Staff_ID=staff_id).filter_by(JobRole_ID=jobrole_id).all()
    if learningJourney:
        for course in learningJourney:
            db.session.delete(course)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Staff_ID": staff_id,
                    "JobRole_ID": jobrole_id
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "Staff_ID": staff_id,
                "JobRole_ID": jobrole_id
            },
            "message": "Learning Journey not found."
        }
    ), 404

# Retrieve the list of course the staff has added to his/her learning journey based on JobRole_ID
@app.route("/StaffLearningJourneyButton/<string:staff_id>/<string:jobrole_id>")
def view_StaffAddedCourses(staff_id, jobrole_id):
    course_list = LearningJourney.query.filter_by(Staff_ID=staff_id).filter_by(JobRole_ID=jobrole_id).all()
    return jsonify(
        {
            "data":[course.getCourseID()
                    for course in course_list]
            }
        )

# Assign jobrole with required skill
@app.route("/addJobRoleWithSkills", methods=['POST'])
def create_JobRoleWithSkills():
    data = request.get_json()
    if not all(key in data.keys() for
            key in ('JobRole_ID', 'Skill_ID')):
            return jsonify({
                "message": "Incorrect JSON object provided."
            }), 500
    
    # (1): Validate jobrole
    jobrole = JobRoles.query.filter_by(JobRole_ID=data['JobRole_ID']).first()
    if not jobrole:
        return jsonify({
            "message": "Job role not valid."
        }), 500
    
    # (2): Validate skill
    skill = Skills.query.filter_by(Skill_ID=data['Skill_ID']).first()
    if not skill:
        return jsonify({
            "message": "Skill not valid."
        }), 500

    # (3): Create job role with skill record
    jobRoleWithSkill = JobRoleWithSkills(
        JobRole_ID=data['JobRole_ID'],
        Skill_ID=data['Skill_ID']
    )

    # (4): Commit to DB
    try:
        db.session.add(jobRoleWithSkill)
        db.session.commit()
        return jsonify(jobRoleWithSkill.to_dict()), 201
    except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500

# Delete jobrole with required skills
@app.route("/deleteJobRoleWithSkills/<string:jobrole_id>", methods=['DELETE'])
def delete_JobRoleWithSkills(jobrole_id):
    jobRoleWithSkills = JobRoleWithSkills.query.filter_by(JobRole_ID = jobrole_id).all()
    if jobRoleWithSkills:
        for skill in jobRoleWithSkills:
            db.session.delete(skill)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "JobRole_ID": jobrole_id
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "JobRole_ID": jobrole_id
            },
            "message": "JobRole not found."
        }
    ), 404

# Delete skill with required courses
@app.route("/deleteSkillsRequiredCourses/<string:skill_id>", methods=['DELETE'])
def delete_SkillsRequiredCourses(skill_id):
    skillsRequiredCourses = SkillsRequiredCourses.query.filter_by(Skill_ID = skill_id).all()
    if skillsRequiredCourses:
        for course in skillsRequiredCourses:
            db.session.delete(course)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Skill_ID": skill_id
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "Skill_ID": skill_id
            },
            "message": "Skill not found."
        }
    ), 404

# Create Skill
@app.route("/addSkill", methods=['POST'])
def create_skill():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('Skill_ID', 'Skill_Name',
                       'Skill_Desc', 'Skill_Status')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

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

# Assign skill with required course
@app.route("/addSkillreqCourses", methods=['POST'])
def create_skillreqCourses():
    data = request.get_json()
    if not all(key in data.keys() for
            key in ('Course_ID', 'Skill_ID')):
            return jsonify({
                "message": "Incorrect JSON object provided."
            }), 500
    
    # (1): Validate skill
    skill = Skills.query.filter_by(Skill_ID=data['Skill_ID']).first()
    if not skill:
        return jsonify({
            "message": "Skill not valid."
        }), 500
    
    # (2): Validate course
    course = Courses.query.filter_by(Course_ID=data['Course_ID']).first()
    if not course:
        return jsonify({
            "message": "Course not valid."
        }), 500

    # (3): Create skill with course record
    skillsRequiredCourses = SkillsRequiredCourses(
            Course_ID=data['Course_ID'], Skill_ID=data['Skill_ID']
        )

    # (4): Commit to DB
    try:
        db.session.add(skillsRequiredCourses)
        db.session.commit()
        return jsonify(skillsRequiredCourses.to_dict()), 201
    except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)