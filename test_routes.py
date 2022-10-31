import pytest
import json
from app import app

def test_get_all_ActiveJobRoles():
    response = app.test_client().get('/ActiveJobRoles')
    assert response.status_code == 200

def test_get_all_InactiveJobRoles():
    response = app.test_client().get('/InactiveJobRoles')
    assert response.status_code == 200

def test_get_all_Courses():
    response = app.test_client().get('/Courses')
    assert response.status_code == 200


# def test_get_all_LearningJourneys():
#     response = app.test_client().get('/LearningJourneys')
#     assert response.status_code == 200