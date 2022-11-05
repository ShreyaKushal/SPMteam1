
import json
from app import app
from app import JobRoles
import unittest 
import flask_testing
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy


def test_get_all_ActiveJobRoles():
    response = app.test_client().get('/ActiveJobRoles')
    assert response.status_code == 200

def test_get_all_InactiveJobRoles():
    response = app.test_client().get('/InactiveJobRoles')
    assert response.status_code == 200

def test_get_all_ActiveSkills():
    response = app.test_client().get('/ActiveSkills')
    assert response.status_code == 200

def test_get_all_InactiveSkills():
    response = app.test_client().get('/InactiveSkills')
    assert response.status_code == 200

def test_get_all_Courses():
    response = app.test_client().get('/Courses')
    assert response.status_code == 200

def test_staff_viewJobRoles():
    response = app.test_client().get('/StaffViewJobRoles')
    assert response.status_code == 200

def test_staff_viewJobRolesWithSkills():
    response = app.test_client().get('/StaffViewJobRoles/DA1')
    res = json.loads(response.data.decode('utf-8')).get("data")
    assert res[0]['Skill_ID'] == 'ST1'
    assert res[0]['Skill_Name'] == 'Statistics'
    assert res[0]['Skill_Desc'] == 'Understand the basics of Statistics'
    assert res[1]['Skill_ID'] == 'ME5'
    assert res[1]['Skill_Name'] == 'Microsoft Excel'
    assert res[1]['Skill_Desc'] == 'Able to use Microsoft Excel'
    assert res[2]['Skill_ID'] == 'COR6'
    assert res[2]['Skill_Name'] == 'Staff Core'
    assert res[2]['Skill_Desc'] == 'To better unerstand the company'
    assert type(res) is list
    assert response.status_code == 200

def test_staff_viewCoursesInSkill():
    response = app.test_client().get('/StaffViewCourses/ST1')
    res = json.loads(response.data.decode('utf-8')).get("data")
    # assert type(res[0]) is object
    assert res[0]['Course_ID'] == 'FIN001'
    assert res[0]['Course_Name'] == 'Data Collection and Analysis'
    assert res[0]['Course_Desc'] == 'Data is meaningless unless insights and analysis can be drawn to provide useful information for business decision-making. It is imperative that data quality, integrity and security '
    assert res[0]['Course_Type'] == 'External'
    assert res[0]['Course_Category'] == 'Finance'
    assert type(res) is list
    assert response.status_code == 200

def test_addJobRole():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "JobRole_ID": "TestingPurffposes12345",
        "JobRole_Name": "For Testing Purposes Only",
        "JobRole_Status": "Active"
    }
    url = '/addJobRole'
    response = app.test_client().post(url, data=json.dumps(data), headers=headers)
    assert response.content_type == mimetype
    assert response.status_code == 201

def test_addSkill():

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "Skill_ID": "TestingPurposes12345",
        "Skill_Name": "For Testing Purposes Only",
        "Skill_Desc": "For Testing Purposes Only!!",
        "Skill_Status": "Active"
    }
    url = '/addSkill'

    response = app.test_client().post(url, data=json.dumps(data), headers=headers)
    assert response.content_type == mimetype
    assert response.status_code == 201

def test_addSkillReqCourses():

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "Skill_ID": "ME5",
        "Course_ID": "tch015",

    }
    url = '/addSkillreqCourses'

    response = app.test_client().post(url, data=json.dumps(data), headers=headers)
    assert response.content_type == mimetype
    assert response.status_code == 201

def test_addJobRoleWithSkills():

    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        "JobRole_ID": "DA1",
        "Skill_ID": "HT9",

    }
    url = '/addJobRoleWithSkills'

    response = app.test_client().post(url, data=json.dumps(data), headers=headers)
    assert response.content_type == mimetype
    assert response.status_code == 201



    
