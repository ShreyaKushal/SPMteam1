import unittest
import flask_testing
import json
from app import app, db, JobRoles, Skills, JobRoleWithSkills


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


class TestCreateJobRoles(TestApp):
    def test_assigning_skills_to_roles(self):

        jr1 = JobRoles(JobRole_ID='PD12', JobRole_Name='A',JobRole_Status='Active')    
        skill = Skills(Skill_ID='PYT12', Skill_Name="Python", Skill_Desc="Able to code in Python.", Skill_Status="Active")
        db.session.add(jr1)
        db.session.add(skill)
        db.session.commit()
        request_body = {
            "JobRoleWithSkills_ID": 1,
            "JobRole_ID": "PD12",
            "Skill_ID": "PYT12"
        }
     
        response = self.client.post("/addJobRoleWithSkills",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {   
            "JobRoleWithSkills_ID": 1,
            "JobRole_ID": "PD12",
            "Skill_ID": "PYT12"
        })

# class TestCreateSkills(TestApp):
#     def test_create_skill(self):
#         jr1 = Skills(Skill_ID="AB123", Skill_Name="AB123",
#         Skill_Desc="AB123", Skill_Status="Active")    
#         db.session.add(jr1)
#         db.session.commit()

#         request_body = {
#             'Skill_ID': "AB123",
#             'Skill_Name': "AB123",
#             'Skill_Desc': "AB123",
#             'Skill_Status':"Active"
#         }

#         response = self.client.post("/addSkill",
#                                     data=json.dumps(request_body),
#                                     content_type='application/json')
#         self.assertEqual(response.json, {
#             "data": {
#                 'Skill_ID': "AB123",
#                 'Skill_Name': "AB123",
#                 'Skill_Desc': "AB123",
#                 'Skill_Status':"Active"
#             }
#         })




if __name__ == '__main__':
    unittest.main()