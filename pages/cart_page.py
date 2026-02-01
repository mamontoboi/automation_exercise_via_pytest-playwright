import logging
from pages.base_page import BasePage
from mixins.subscription_mixin import SubscriptionMixin
from playwright.sync_api import expect

logger = logging.getLogger(__name__)

class CartPage(BasePage, SubscriptionMixin):

    def check_card_is_empty(self):
        logger.info("Checking the card is empty")
        expect(self.page.get_by_text("Cart is empty!")).to_be_visible()