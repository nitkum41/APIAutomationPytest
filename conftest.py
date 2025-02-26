import pytest
from pathlib import Path
from datetime import datetime
import os,json

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("reports",today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True,exist_ok=True)
    pytest_html = report_dir / f"Report_{today.strftime('%Y-%m-%d-%H-%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True

def setup_teardown():
    print("\n setting up resources")
    yield
    print("\n Tearing down resources")

def pytest_html_report_title(report):
    report.title="Pytest API Automation"

@pytest.fixture
def load_user_data():
    json_file_path = os.path.join(os.path.dirname(__file__),"data","test_data.json")
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    return data
