# coding: utf-8

"""
    Subscriptions

    A subscription enables you to charge customers at specified intervals for a plan of their choice.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_subscription.models.subscription_response_plan import SubscriptionResponsePlan

class TestSubscriptionResponsePlan(unittest.TestCase):
    """SubscriptionResponsePlan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubscriptionResponsePlan:
        """Test SubscriptionResponsePlan
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubscriptionResponsePlan`
        """
        model = SubscriptionResponsePlan()
        if include_optional:
            return SubscriptionResponsePlan(
                plan_code = 'basic-monthly',
                name = 'GatorHost-Basic',
                quantity = 1,
                price = 50,
                tags = [
                    ls_zoho_billing_subscription.models.tags_inner.tags_inner(
                        tag_id = 56, 
                        tag_option_id = 56, )
                    ],
                item_custom_fields = [
                    ls_zoho_billing_subscription.models.item_custom_fields_inner.item_custom_fields_inner(
                        label = '', 
                        value = '', )
                    ],
                discount = 20,
                total = 50,
                setup_fee = 20,
                plan_description = 'Monthly Basic plan',
                tax_id = '903000002345',
                trial_days = 0
            )
        else:
            return SubscriptionResponsePlan(
        )
        """

    def testSubscriptionResponsePlan(self):
        """Test SubscriptionResponsePlan"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
