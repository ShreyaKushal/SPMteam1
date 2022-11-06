import unittest
import flask_testing
import json
from app import app, db, JobRoles, Skills, Courses, Staff


class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True
    app.config.update({
    'SQLALCHEMY_POOL_SIZE': None,
    'SQLALCHEMY_POOL_TIMEOUT': None
})

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

       
    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestAssignSkillsToRoles(TestApp):
    def test_assign_skills_to_roles(self):
        jr = JobRoles(JobRole_ID='PD12', JobRole_Name='Python Developer',JobRole_Status='Active')    
        skill = Skills(Skill_ID='PYT12', Skill_Name="Python", Skill_Desc="Able to code in Python.", Skill_Status="Active")
        db.session.add(jr)
        db.session.add(skill)
        db.session.commit()

        request_body = {
            "JobRoleWithSkills_ID": 1,
            "JobRole_ID": jr.JobRole_ID,
            "Skill_ID": skill.Skill_ID
        }
     
        response = self.client.post("/addJobRoleWithSkills",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {   
            "JobRoleWithSkills_ID": 1,
            "JobRole_ID": "PD12",
            "Skill_ID": "PYT12"
        })
    
    def test_assign_skills_invalid_skill(self):
        jr1 = JobRoles(JobRole_ID='SD07', JobRole_Name='Software Developer',JobRole_Status='Active')  
        db.session.add(jr1)
        db.session.commit()

        request_body = {
            "JobRoleWithSkills_ID": 1,
            "JobRole_ID": jr1.JobRole_ID,
            "Skill_ID": jr1.JobRole_ID
        }
             
        response = self.client.post("/addJobRoleWithSkills",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {
            'message': 'Skill not valid.'
        })
    
    def test_assign_skills_invalid_roles(self):
        skill1 = Skills(Skill_ID='PYT12', Skill_Name="Python", Skill_Desc="Able to code in Python.", Skill_Status="Active")
        db.session.add(skill1)
        db.session.commit()

        request_body = {
            "JobRoleWithSkills_ID": 1,
            "JobRole_ID": skill1.Skill_ID,
            "Skill_ID": skill1.Skill_ID
        }
            
        response = self.client.post("/addJobRoleWithSkills",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {
            'message': 'Job role not valid.'
        })

class TestAssignSkillsToCourses(TestApp):
    def test_assign_skills_to_courses(self):
        course = Courses(Course_ID='LTB02', Course_Name='Leadership and Team Building', 
        Course_Desc='Learn how to enhance the relationships between employees and help them collaborate in the most effective way possible',
        Course_Status='Active', Course_Type='Internal', Course_Category='Management')
        skill = Skills(Skill_ID='LE12', Skill_Name="Leadership", Skill_Desc="Strong sense of leadership", Skill_Status="Active")
        db.session.add(course)
        db.session.add(skill)
        db.session.commit()

        request_body = {
            "SkillsRequiredCourses_ID": 1,
            "Course_ID": course.Course_ID,
            "Skill_ID": skill.Skill_ID,
        }

        response = self.client.post("/addSkillreqCourses",
                            data=json.dumps(request_body),
                            content_type='application/json')

        self.assertEqual(response.json, {   
            "SkillsRequiredCourses_ID": 1,
            "Course_ID": "LTB02",
            "Skill_ID": "LE12",
        })

    def test_assign_skills_invalid_skill(self):
        course1 = Courses(Course_ID='FIN01', Course_Name='Corporate Finance', 
        Course_Desc='Covers fundamental issues of corporate finance, including corporate governance, capital budgeting, and capital structure.',
        Course_Status='Active', Course_Type='External', Course_Category='Finance')
        db.session.add(course1)
        db.session.commit()

        request_body = {
            "SkillsRequiredCourses_ID": 1,
            "Course_ID": course1.Course_ID,
            "Skill_ID": course1.Course_ID,
        }

        response = self.client.post("/addSkillreqCourses",
                            data=json.dumps(request_body),
                            content_type='application/json')

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {
            'message': 'Skill not valid.'
        })

    def test_assign_skills_invalid_course(self):
        skill1 = Skills(Skill_ID='LE01', Skill_Name="Leadership", Skill_Desc="Strong sense of leadership", Skill_Status="Active")
        db.session.add(skill1)
        db.session.commit()

        request_body = {
            "SkillsRequiredCourses_ID": 1,
            "Course_ID": skill1.Skill_ID,
            "Skill_ID": skill1.Skill_ID,
        }

        response = self.client.post("/addSkillreqCourses",
                            data=json.dumps(request_body),
                            content_type='application/json')

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {
            'message': 'Course not valid.'
        })

class TestCreateLearningJourney(TestApp):
    def test_create_learningjourney(self):
        jr = JobRoles(JobRole_ID='PD12', JobRole_Name='Python Developer',JobRole_Status='Active')    
        skill = Skills(Skill_ID='PYT12', Skill_Name="Python", Skill_Desc="Able to code in Python.", Skill_Status="Active")
        course = Courses(Course_ID='PY001', Course_Name='Introduction to Python', 
        Course_Desc='Learn the basics of Python Programming',
        Course_Status='Active', Course_Type='External', Course_Category='Technical')
        staff = Staff(Staff_ID= 172001, Staff_Fname='Leo', Staff_Lname='Lee', Dept='Sales', Email='leolee@allinone.com.sg', Role_ID=2)
        db.session.add(jr)
        db.session.add(skill)
        db.session.add(course)
        db.session.add(staff)
        db.session.commit()

        request_body = {
            'LearningJourney_ID': 1,
            'JobRole_ID': jr.JobRole_ID,
            'Skill_ID': skill.Skill_ID,
            'Course_ID': course.Course_ID,
            'Staff_ID': staff.Staff_ID
        }

        response = self.client.post("/StaffLearningJourney",
                        data=json.dumps(request_body),
                        content_type='application/json')

        self.assertEqual(response.json, {   
            'LearningJourney_ID': 1,
            'JobRole_ID': 'PD12',
            'Skill_ID': 'PYT12',
            'Course_ID': 'PY001',
            'Staff_ID': 172001
            })

    def test_create_learningjourney_invalid_role(self):
        skill1 = Skills(Skill_ID='PYT12', Skill_Name="Python", Skill_Desc="Able to code in Python.", Skill_Status="Active")
        course1 = Courses(Course_ID='PY001', Course_Name='Introduction to Python', 
        Course_Desc='Learn the basics of Python Programming',
        Course_Status='Active', Course_Type='External', Course_Category='Technical')
        staff1 = Staff(Staff_ID= 172001, Staff_Fname='Leo', Staff_Lname='Lee', Dept='Sales', Email='leolee@allinone.com.sg', Role_ID=2)
      
        db.session.add(skill1)
        db.session.add(course1)
        db.session.add(staff1)
        db.session.commit()

        request_body = {
            'LearningJourney_ID': 1,
            'JobRole_ID': skill1.Skill_ID,
            'Skill_ID': skill1.Skill_ID,
            'Course_ID': course1.Course_ID,
            'Staff_ID': staff1.Staff_ID
        }

        response = self.client.post("/StaffLearningJourney",
                        data=json.dumps(request_body),
                        content_type='application/json')

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {
            'message': 'Job role not valid.'
        })

    def test_create_learningjourney_invalid_skill(self):
        jr2 = JobRoles(JobRole_ID='PD12', JobRole_Name='Python Developer',JobRole_Status='Active')   
        course2 = Courses(Course_ID='PY001', Course_Name='Introduction to Python', 
        Course_Desc='Learn the basics of Python Programming',
        Course_Status='Active', Course_Type='External', Course_Category='Technical')
        staff2 = Staff(Staff_ID= 172001, Staff_Fname='Leo', Staff_Lname='Lee', Dept='Sales', Email='leolee@allinone.com.sg', Role_ID=2)
      
        db.session.add(jr2)
        db.session.add(course2)
        db.session.add(staff2)
        db.session.commit()

        request_body = {
            'LearningJourney_ID': 1,
            'JobRole_ID': jr2.JobRole_ID,
            'Skill_ID': jr2.JobRole_ID,
            'Course_ID': course2.Course_ID,
            'Staff_ID': staff2.Staff_ID
        }

        response = self.client.post("/StaffLearningJourney",
                        data=json.dumps(request_body),
                        content_type='application/json')

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {
            'message': 'Skill not valid.'
        })

    def test_create_learningjourney_invalid_course(self):
        jr3 = JobRoles(JobRole_ID='PD12', JobRole_Name='Python Developer',JobRole_Status='Active')    
        skill3 = Skills(Skill_ID='PYT12', Skill_Name="Python", Skill_Desc="Able to code in Python.", Skill_Status="Active")
        staff3 = Staff(Staff_ID= 172001, Staff_Fname='Leo', Staff_Lname='Lee', Dept='Sales', Email='leolee@allinone.com.sg', Role_ID=2)
        db.session.add(jr3)
        db.session.add(skill3)
        db.session.add(staff3)
        db.session.commit()

        request_body = {
            'LearningJourney_ID': 1,
            'JobRole_ID': jr3.JobRole_ID,
            'Skill_ID': skill3.Skill_ID,
            'Course_ID': skill3.Skill_ID,
            'Staff_ID': staff3.Staff_ID
        }

        response = self.client.post("/StaffLearningJourney",
                        data=json.dumps(request_body),
                        content_type='application/json')

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {
            'message': 'Course not valid.'
        })

    def test_create_learningjourney_invalid_staff(self):
        jr4 = JobRoles(JobRole_ID='PD12', JobRole_Name='Python Developer',JobRole_Status='Active')    
        skill4 = Skills(Skill_ID='PYT12', Skill_Name="Python", Skill_Desc="Able to code in Python.", Skill_Status="Active")
        course4 = Courses(Course_ID='PY001', Course_Name='Introduction to Python', 
        Course_Desc='Learn the basics of Python Programming',
        Course_Status='Active', Course_Type='External', Course_Category='Technical')
        db.session.add(jr4)
        db.session.add(skill4)
        db.session.add(course4)

        db.session.commit()

        request_body = {
            'LearningJourney_ID': 1,
            'JobRole_ID': jr4.JobRole_ID,
            'Skill_ID': skill4.Skill_ID,
            'Course_ID': course4.Course_ID,
            'Staff_ID': course4.Course_ID,
        }

        response = self.client.post("/StaffLearningJourney",
                        data=json.dumps(request_body),
                        content_type='application/json')

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {
            'message': 'Staff not valid.'
        })



if __name__ == '__main__':
    unittest.main()