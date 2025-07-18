# coding: utf-8

"""
    Invoices

    Invoices describe how much a customer owes for his subscription. Invoices are created for recurring charges, one time charges including any prorated adjustments.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_invoices.models.update_billing_address_request import UpdateBillingAddressRequest

class TestUpdateBillingAddressRequest(unittest.TestCase):
    """UpdateBillingAddressRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateBillingAddressRequest:
        """Test UpdateBillingAddressRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateBillingAddressRequest`
        """
        model = UpdateBillingAddressRequest()
        if include_optional:
            return UpdateBillingAddressRequest(
                address = 'B-1104, 11F, 
Horizon International Tower, 
No. 6, ZhiChun Road, HaiDian District',
                city = 'Beijing',
                state = 'Beijing',
                zip = '1000881',
                country = '',
                fax = '+86-10-82637827'
            )
        else:
            return UpdateBillingAddressRequest(
        )
        """

    def testUpdateBillingAddressRequest(self):
        """Test UpdateBillingAddressRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
