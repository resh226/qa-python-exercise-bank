# ----------------------------------------------------------------------------------------------------------------------------
#This is to test a RESTful web service to ensure all major HTTP methods behave correctly:
# ----------------------------------------------------------------------------------------------------------------------------

import pytest
import requests

base_url = "https://jsonplaceholder.typicode.com"

# Test GET method
@pytest.mark.api
def test_get_posts():
    response = requests.get(f"{base_url}/posts/1")
    assert response.status_code == 200
    assert "userId" in response.json()  # checking through assert whether string "userID" is present in response data

# Test POST method (simulate creating a new post)
@pytest.mark.api
def test_post_new_post():
    payload = {
        "title": "QA Automation",
        "body": "pytest + requests",
        "userId": 1
    }
    response = requests.post(f"{base_url}/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "QA Automation"

#Test PUT method (simulate full update)
@pytest.mark.api
def test_put_update_post():
    payload = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated body",
        "userId": 1
    }
    response = requests.put(f"{base_url}/posts/1", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"

#Test PATCH method (simulate partial update)
@pytest.mark.api
def test_patch_post_title():
    payload = {
        "title": "Patched Title"
    }
    response = requests.patch(f"{base_url}/posts/1", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "Patched Title"

# Test DELETE method
@pytest.mark.api
def test_delete_post():
    response = requests.delete(f"{base_url}/posts/1")
    assert response.status_code == 200
