# coding: utf-8

"""
    Hosted-Pages

    Zoho Billing provides a hosted payment page to integrate with your websites. You can securely integrate with Zoho Billing for collecting your customer's sensitive card information through the hosted page. These Hosted Pages will expire within one hour.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_hosted_pages.models.shipping_address import ShippingAddress

class TestShippingAddress(unittest.TestCase):
    """ShippingAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ShippingAddress:
        """Test ShippingAddress
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ShippingAddress`
        """
        model = ShippingAddress()
        if include_optional:
            return ShippingAddress(
                attention = 'Benjamin George',
                street = 'Harrington Bay Street',
                city = 'Salt Lake City',
                state = 'CA',
                country = 'U.S.A',
                zip = '92612',
                fax = '4527389'
            )
        else:
            return ShippingAddress(
        )
        """

    def testShippingAddress(self):
        """Test ShippingAddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
