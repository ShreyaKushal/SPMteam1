import unittest

from app import JobRoles, Skills, Courses, Role, Staff, JobRoleWithSkills, SkillsRequiredCourses, LearningJourney

class TestJobRoles(unittest.TestCase):

    def test_to_dict(self):
        role = JobRoles(JobRole_ID='SD01', JobRole_Name='Software Developer', JobRole_Status='Active')
        self.assertEqual(role.to_dict(), {
            'JobRole_ID': 'SD01',
            'JobRole_Name': 'Software Developer',
            'JobRole_Status': 'Active'}
        )
    
    def test_getName(self):
        role1 = JobRoles(JobRole_ID='SSD01', JobRole_Name='Senior Software Developer', JobRole_Status='Active')
        name = role1.getName()
        self.assertEqual(name, {'JobRole_Name': 'Senior Software Developer'})

    def test_json(self):
        role2 = JobRoles(JobRole_ID='SD03', JobRole_Name='Junior Software Developer', JobRole_Status='Active')
        json = role2.json()
        self.assertEqual(json, {
            'JobRole_ID': 'SD03',
            'JobRole_Name': 'Junior Software Developer',
            'JobRole_Status': 'Active'})

        
class TestSkills(unittest.TestCase):
    def test_to_dict(self):
        skill = Skills(Skill_ID='VBA01', Skill_Name='Visual Basic for Applications in Excel', 
        Skill_Desc='Able to automate complicated tasks & debug errors Visual Basic for Applications in Microsoft Excel'
        ,Skill_Status='Active')
        self.assertEqual(skill.to_dict(), {
            'Skill_ID': 'VBA01',
            'Skill_Name': 'Visual Basic for Applications in Excel',
            'Skill_Desc': 'Able to automate complicated tasks & debug errors Visual Basic for Applications in Microsoft Excel',
            'Skill_Status': 'Active'}
        )

    def test_getName(self):
        skill1 = Skills(Skill_ID='MPW01', Skill_Name='People Management', 
        Skill_Desc='Able to manage people at work', Skill_Status='Active')
        name = skill1.getName()
        self.assertEqual(name, {'Skill_Name': 'People Management'})

    def test_json(self):
        skill2 = Skills(Skill_ID='SQL12', Skill_Name='SQL', 
        Skill_Desc='Able to handle database using mySQL', Skill_Status='Active')
        json = skill2.json()
        self.assertEqual(json, {
            'Skill_ID': 'SQL12',
            'Skill_Name': 'SQL',
            'Skill_Desc': 'Able to handle database using mySQL',
            'Skill_Status': 'Active'}
        )

class TestCourses(unittest.TestCase):
    def test_to_dict(self):
        course = Courses(Course_ID='LTB01', Course_Name='Leadership and Team Building', 
        Course_Desc='Learn how to enhance the relationships between employees and help them collaborate in the most effective way possible',
        Course_Status='Active', Course_Type='External', Course_Category='Management')
        self.assertEqual(course.to_dict(), {
            'Course_ID': 'LTB01',
            'Course_Name': 'Leadership and Team Building',
            'Course_Desc': 'Learn how to enhance the relationships between employees and help them collaborate in the most effective way possible',
            'Course_Status': 'Active',
            'Course_Type':'External',
            'Course_Category': 'Management'
            }
        )

    def test_getName(self):
        course1 = Courses(Course_ID='FIN01', Course_Name='Corporate Finance', 
        Course_Desc='Covers fundamental issues of corporate finance, including corporate governance, capital budgeting, and capital structure.',
        Course_Status='Active', Course_Type='External', Course_Category='Finance')
        name = course1.getName()
        self.assertEqual(name, {'Course_Name': 'Corporate Finance'})

    def test_json(self):
        course2 = Courses(Course_ID='ESD01', Course_Name='Enterprise Solution Development', 
        Course_Desc='Learn how to software application designed to meet the multifaceted needs of an organisation.',
        Course_Status='Active', Course_Type='Internal', Course_Category='Technical')
        json = course2.json()
        self.assertEqual(json, {
            'Course_ID': 'ESD01',
            'Course_Name': 'Enterprise Solution Development',
            'Course_Desc': 'Learn how to software application designed to meet the multifaceted needs of an organisation.',
            'Course_Status': 'Active',
            'Course_Type':'Internal',
            'Course_Category': 'Technical'
            }
        )
class TestRole(unittest.TestCase):
    def test_to_dict(self):
        role = Role(Role_ID=5, Role_Name='HR')
        self.assertEqual(role.to_dict(), {
            'Role_ID': 5,
            'Role_Name': 'HR'}
        )

class TestStaff(unittest.TestCase):
    def test_to_dict(self):
        staff = Staff(Staff_ID= 172001, Staff_Fname='Leo', Staff_Lname='Lee', Dept='Sales', Email='leolee@allinone.com.sg', Role_ID=2)
        self.assertEqual(staff.to_dict(), {
            'Staff_ID': 172001,
            'Staff_Fname': 'Leo',
            'Staff_Lname': 'Lee',
            'Dept':'Sales',
            'Email': 'leolee@allinone.com.sg',
            'Role_ID': 2}
        )

    def test_json(self):
        staff1 = Staff(Staff_ID= 172005, Staff_Fname='Sam', Staff_Lname='Tan', Dept='Sales', Email='samtan@allinone.com.sg', Role_ID=2)
        json = staff1.json()
        self.assertEqual(json, {
            'Staff_ID': 172005,
            'Staff_Fname': 'Sam',
            'Staff_Lname': 'Tan',
            'Dept':'Sales',
            'Email': 'samtan@allinone.com.sg',
            'Role_ID': 2
        })

class TestJobRoleWithSkills(unittest.TestCase):
    def test_to_dict(self):
        jobrolewithskill = JobRoleWithSkills(JobRole_ID='HE8', Skill_ID='HT9')
        self.assertEqual(jobrolewithskill.to_dict(), {
            'JobRoleWithSkills_ID': None,
            'JobRole_ID': 'HE8',
            'Skill_ID': 'HT9'}
        )
    
    def test_getSkillID(self):
        jobrolewithskill1 = JobRoleWithSkills(JobRole_ID='SD13', Skill_ID='RU02')
        skill_ID = jobrolewithskill1.getSkillID()
        self.assertEqual(skill_ID, 'RU02')

    def test_json(self):
        jobrolewithskill2 = JobRoleWithSkills(JobRole_ID='SD43', Skill_ID='JVS12')
        json = jobrolewithskill2.json()
        self.assertEqual(json, {
            'JobRoleWithSkills_ID': None,
            'JobRole_ID': 'SD43',
            'Skill_ID': 'JVS12'
        })

class TestSkillsRequiredCourses(unittest.TestCase):
    def test_to_dict(self):
        skillrequiredcourse = SkillsRequiredCourses(Course_ID='COR004', Skill_ID='COR6')
        self.assertEqual(skillrequiredcourse.to_dict(), {
            'SkillsRequiredCourses_ID': None,
            'Course_ID': 'COR004',
            'Skill_ID': 'COR6'}
        )
    
    def test_getCourseID(self):
        skillrequiredcourse1 = SkillsRequiredCourses(Course_ID='MPW003', Skill_ID='COR8')
        course_ID = skillrequiredcourse1.getCourseID()
        self.assertEqual(course_ID, "MPW003")

    def test_json(self):
        skillrequiredcourse2 = SkillsRequiredCourses(Course_ID='ESM001', Skill_ID='JR01')
        json = skillrequiredcourse2.json()
        self.assertEqual(json, {
            'SkillsRequiredCourses_ID': None,
            'Course_ID': 'ESM001',
            'Skill_ID': 'JR01'          
        })

class TestLearningJourney(unittest.TestCase):
    def test_to_dict(self):
        learning_journey = LearningJourney(JobRole_ID='HE8',Skill_ID='COR6', Course_ID='COR004', Staff_ID='172002')
        self.assertEqual(learning_journey.to_dict(), {
            'LearningJourney_ID': None,
            'JobRole_ID': 'HE8',
            'Skill_ID': 'COR6',
            'Course_ID': 'COR004',
            'Staff_ID': '172002'}
        )
    
    def test_getCourseID(self):
        learning_journey1 = LearningJourney(JobRole_ID='HE15',Skill_ID='COR9', Course_ID='COR009', Staff_ID='172003')
        course_ID1 = learning_journey1.getCourseID()
        self.assertEqual(course_ID1, "COR009")

    def test_getCourseID(self):
        learning_journey2 = LearningJourney(JobRole_ID='HE02',Skill_ID='COR6', Course_ID='COR010', Staff_ID='172004')
        course_ID2 = learning_journey2.getJobRoleID()
        self.assertEqual(course_ID2, "HE02")

    def test_json(self):
        learning_journey3 = LearningJourney(JobRole_ID='SF12',Skill_ID='JR02', Course_ID='ESM010', Staff_ID='172005')
        course_ID3 = learning_journey3.json()
        self.assertEqual(course_ID3, {
            'LearningJourney_ID': None,
            'JobRole_ID': 'SF12',
            'Skill_ID': 'JR02',
            'Course_ID': 'ESM010',
            'Staff_ID': '172005'
        })


if __name__ == "__main__":
    unittest.main()
