from enum import Enum
from typing import Any, Optional, Union

import allure


class AllureParentSuite(str, Enum):
    API = "API Tests"
    UI = "UI Tests"


class AllureSuiteName(str, Enum):
    AUTHENTICATION = "Test Authentication"
    USER_MANAGEMENT = "Test User Management"
    PRODUCTS = "Test Products"
    CONTACT_US = "Test Contact Us"
    TEST_CASES = "Test Cases"
    SUBSCRIPTION = "Test Subscription"
    LOGIN = "Test Login"
    BRANDS = "Test Brands"
    RETRY_HANDLING = "Test Retry Handling"


def _resolve_value(value: Union[str, Enum, None]) -> Optional[str]:
    if value is None:
        return None
    return value.value if isinstance(value, Enum) else value


def report_case(
    parent_suite: Union[str, Enum, None] = None,
    suite: Union[str, Enum, None] = None,
    sub_suite: Union[str, Enum, None] = None,
    severity: Any = None,
    title: Optional[str] = None,
):
    def decorator(func):
        parent_value = _resolve_value(parent_suite)
        suite_value = _resolve_value(suite)
        sub_suite_value = _resolve_value(sub_suite)

        if parent_value is not None:
            func = allure.parent_suite(parent_value)(func)
        if suite_value is not None:
            func = allure.suite(suite_value)(func)
        if sub_suite_value is not None:
            func = allure.sub_suite(sub_suite_value)(func)
        if severity is not None:
            func = allure.severity(severity)(func)
        if title is not None:
            func = allure.title(title)(func)
        return func

    return decorator
