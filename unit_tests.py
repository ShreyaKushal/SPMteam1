import unittest

from app import JobRoles, Skills


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

if __name__ == "__main__":
    unittest.main()
