# coding: utf-8

"""
    Hosted-Pages

    Zoho Billing provides a hosted payment page to integrate with your websites. You can securely integrate with Zoho Billing for collecting your customer's sensitive card information through the hosted page. These Hosted Pages will expire within one hour.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_hosted_pages.models.data_subscription_addons_inner import DataSubscriptionAddonsInner

class TestDataSubscriptionAddonsInner(unittest.TestCase):
    """DataSubscriptionAddonsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataSubscriptionAddonsInner:
        """Test DataSubscriptionAddonsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataSubscriptionAddonsInner`
        """
        model = DataSubscriptionAddonsInner()
        if include_optional:
            return DataSubscriptionAddonsInner(
                addon_code = 'Email-basic',
                name = Monthly Addon,
                description = 'Monthly Basic plan.',
                quantity = 1,
                price = 10,
                discount = None,
                total = None,
                tax_id = None
            )
        else:
            return DataSubscriptionAddonsInner(
        )
        """

    def testDataSubscriptionAddonsInner(self):
        """Test DataSubscriptionAddonsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
