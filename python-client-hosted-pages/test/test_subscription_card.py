# coding: utf-8

"""
    Hosted-Pages

    Zoho Billing provides a hosted payment page to integrate with your websites. You can securely integrate with Zoho Billing for collecting your customer's sensitive card information through the hosted page. These Hosted Pages will expire within one hour.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_hosted_pages.models.subscription_card import SubscriptionCard

class TestSubscriptionCard(unittest.TestCase):
    """SubscriptionCard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubscriptionCard:
        """Test SubscriptionCard
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubscriptionCard`
        """
        model = SubscriptionCard()
        if include_optional:
            return SubscriptionCard(
                card_id = 90300000079226,
                last_four_digits = 2145,
                payment_gateway = 'payflow_pro',
                expiry_month = 9,
                expiry_year = 2030
            )
        else:
            return SubscriptionCard(
        )
        """

    def testSubscriptionCard(self):
        """Test SubscriptionCard"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
