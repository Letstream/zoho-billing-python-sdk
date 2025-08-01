# coding: utf-8

"""
    Payments

    A payment object describes details regarding a particular customer payment. There can be multiple payments for a single invoice. Multiple invoices can be paid in a single payment as well.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_payments.models.payment_response_invoices_inner import PaymentResponseInvoicesInner

class TestPaymentResponseInvoicesInner(unittest.TestCase):
    """PaymentResponseInvoicesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentResponseInvoicesInner:
        """Test PaymentResponseInvoicesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentResponseInvoicesInner`
        """
        model = PaymentResponseInvoicesInner()
        if include_optional:
            return PaymentResponseInvoicesInner(
                invoice_id = '90300000079426',
                invoice_number = 'INV-384',
                var_date = 2016-06-05,
                invoice_amount = 450,
                amount_applied = 450,
                balance_amount = 0
            )
        else:
            return PaymentResponseInvoicesInner(
        )
        """

    def testPaymentResponseInvoicesInner(self):
        """Test PaymentResponseInvoicesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
