# ----------------------------------------------------------------------------------------------------------------------------
# Demonstrate how to apply custom markers like @pytest.mark.smoke and
# run specific categories of tests using the -m option.
# ----------------------------------------------------------------------------------------------------------------------------

import pytest

# Test marked as "smoke" — a basic sanity test
@pytest.mark.smoke
def test_login_smoke():
    username = "admin"
    password = "admin123"
    assert username == "admin"
    assert password == "admin123"

# Test marked as "regression" — part of a deeper test cycle
@pytest.mark.regression
def test_login_with_wrong_password():
    username = "admin"
    password = "wrongpass"
    assert password != "admin123"

# Test marked with both "smoke" and "regression"
@pytest.mark.smoke
@pytest.mark.regression
def test_dashboard_loads():
    page_title = "Dashboard - Admin Panel"
    assert "Dashboard" in page_title
