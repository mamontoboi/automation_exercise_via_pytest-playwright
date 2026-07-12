import logging
import re
from pathlib import Path

import allure
import pytest
from pytest import Item

REPORTS_DIR = Path("reports")
TRACES_DIR = REPORTS_DIR / "traces"
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"

TRACES_DIR.mkdir(parents=True, exist_ok=True)
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)


def _sanitize_test_name(nodeid: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", nodeid).strip("_")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call):
    """Capture failure artifacts and attach them to the current test case."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    if rep.when != "call" or not rep.failed:
        return

    page = item.funcargs.get("page")
    if page is None:
        return

    test_name = _sanitize_test_name(item.nodeid)
    screenshot_path = SCREENSHOTS_DIR / f"{test_name}.png"

    try:
        page.screenshot(path=screenshot_path, full_page=True)
        allure.attach.file(
            screenshot_path,
            name=f"{test_name}_failure.png",
            attachment_type=allure.attachment_type.PNG,
        )
    except Exception as exc:  # pragma: no cover - defensive branch
        logging.warning("Unable to capture screenshot for %s: %s", item.nodeid, exc)

    try:
        allure.attach(
            page.content(),
            name=f"{test_name}_page.html",
            attachment_type=allure.attachment_type.HTML,
        )
    except Exception as exc:  # pragma: no cover - defensive branch
        logging.warning("Unable to attach page HTML for %s: %s", item.nodeid, exc)

    try:
        allure.attach(
            page.url,
            name="Page URL",
            attachment_type=allure.attachment_type.TEXT,
        )
    except Exception as exc:  # pragma: no cover - defensive branch
        logging.warning("Unable to attach page URL for %s: %s", item.nodeid, exc)
