import unittest

from app import JobRoles, Skills, Courses, Role, Staff, JobRoleWithSkills, SkillsRequiredCourses, LearningJourney


# class TestCoursesRoute(unittest.TestCase):
#     def test_courses_route_status_code(self):
#         route = "/Courses"
#         rv = self.get(route)
#         assert rv.status_code == 200

class TestJobRoles(unittest.TestCase):
    def test_to_dict(self):
        role = JobRoles(JobRole_ID='SD01', JobRole_Name='Software Developer', JobRole_Status='Active')
        self.assertEqual(role.to_dict(), {
            'JobRole_ID': 'SD01',
            'JobRole_Name': 'Software Developer',
            'JobRole_Status': 'Active'}
        )
        
class TestSkills(unittest.TestCase):
    def test_to_dict(self):
        skill = Skills(Skill_ID='VBA01', Skill_Name='Visual Basic for Applications in Excel', 
        Skill_Desc='Able to automate complicated tasks & debug errors Visual Basic for Applications in Microsoft Excel Able'
        ,Skill_Status='Active')
        self.assertEqual(skill.to_dict(), {
            'Skill_ID': 'VBA01',
            'Skill_Name': 'Visual Basic for Applications in Excel',
            'Skill_Desc': 'Able to automate complicated tasks & debug errors Visual Basic for Applications in Microsoft Excel Able',
            'Skill_Status': 'Active'}
        )
    # def test_skills_route_status_code(self):
    #     route = "/Skills"
    #     rv = self.get(route)
    #     assert rv.status_code == 200


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

class TestJobRoleWithSkills(unittest.TestCase):
    def test_to_dict(self):
        jobrolewithskill = JobRoleWithSkills(JobRole_ID='HE8', Skill_ID='HT9')
        self.assertEqual(jobrolewithskill.to_dict(), {
            'JobRole_ID': 'HE8',
            'Skill_ID': 'HT9'}
        )

class TestSkillsRequiredCourses(unittest.TestCase):
    def test_to_dict(self):
        skillrequiredcourse = SkillsRequiredCourses(Course_ID='COR004', Skill_ID='COR6')
        self.assertEqual(skillrequiredcourse.to_dict(), {
            'Course_ID': 'COR004',
            'Skill_ID': 'COR6'}
        )

class TestLearningJourney(unittest.TestCase):
    def test_to_dict(self):
        learning_journey = LearningJourney(JobRole_ID='HE8',Skill_ID='COR6', Course_ID='COR004', Staff_ID='172002')
        self.assertEqual(learning_journey.to_dict(), {
            'JobRole_ID': 'HE8',
            'Skill_ID': 'COR6',
            'Course_ID': 'COR004',
            'Staff_ID': '172002'}
        )


if __name__ == "__main__":
    unittest.main()
