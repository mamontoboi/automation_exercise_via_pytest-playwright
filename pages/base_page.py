from playwright.sync_api import Page, expect
import logging

logger = logging.getLogger(__name__)

class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def check_header_text(self, expected_text):
        logger.info(f"Checking that header contains {expected_text}")
        expect(self.page.locator("h2.title")).to_contain_text(expected_text)
