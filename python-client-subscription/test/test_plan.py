# coding: utf-8

"""
    Subscriptions

    A subscription enables you to charge customers at specified intervals for a plan of their choice.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_subscription.models.plan import Plan

class TestPlan(unittest.TestCase):
    """Plan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Plan:
        """Test Plan
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Plan`
        """
        model = Plan()
        if include_optional:
            return Plan(
                plan_code = 'basic-monthly',
                name = 'GatorHost-Basic',
                quantity = 1,
                price = 50,
                discount = 20,
                total = 50,
                setup_fee = 20,
                plan_description = 'Monthly Basic plan',
                tax_id = '903000002345',
                trial_days = 0
            )
        else:
            return Plan(
        )
        """

    def testPlan(self):
        """Test Plan"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
