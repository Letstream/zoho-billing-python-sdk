# coding: utf-8

"""
    Payments

    A payment object describes details regarding a particular customer payment. There can be multiple payments for a single invoice. Multiple invoices can be paid in a single payment as well.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_payments.models.autotransaction import Autotransaction

class TestAutotransaction(unittest.TestCase):
    """Autotransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Autotransaction:
        """Test Autotransaction
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Autotransaction`
        """
        model = Autotransaction()
        if include_optional:
            return Autotransaction(
                autotransaction_id = '90300000079465',
                payment_gateway = 'payflow_pro',
                gateway_transaction_id = 'B10E6E0F31BD',
                gateway_error_message = 'Gateway error message for a failed transaction.',
                card_id = '90300000079226',
                last_four_digits = 1111,
                expiry_month = 9,
                expiry_year = 2030
            )
        else:
            return Autotransaction(
        )
        """

    def testAutotransaction(self):
        """Test Autotransaction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
