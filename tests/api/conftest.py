import pytest
from pathlib import Path
from pytest import Item

REPORTS_DIR = Path("reports")
TRACES_DIR = REPORTS_DIR / "traces"

TRACES_DIR.mkdir(parents=True, exist_ok=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call):
    """There are three phases in pytest: setup, call (test body) and teardown. 
    The hook runs for each of them, setting attributes to each object
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
