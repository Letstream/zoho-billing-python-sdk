# coding: utf-8

"""
    Invoices

    Invoices describe how much a customer owes for his subscription. Invoices are created for recurring charges, one time charges including any prorated adjustments.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_invoices.models.retrieve_an_invoice_response_invoice_payments_inner import RetrieveAnInvoiceResponseInvoicePaymentsInner

class TestRetrieveAnInvoiceResponseInvoicePaymentsInner(unittest.TestCase):
    """RetrieveAnInvoiceResponseInvoicePaymentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RetrieveAnInvoiceResponseInvoicePaymentsInner:
        """Test RetrieveAnInvoiceResponseInvoicePaymentsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RetrieveAnInvoiceResponseInvoicePaymentsInner`
        """
        model = RetrieveAnInvoiceResponseInvoicePaymentsInner()
        if include_optional:
            return RetrieveAnInvoiceResponseInvoicePaymentsInner(
                payment_id = '90300000079467',
                payment_mode = 'autotransaction',
                invoice_payment_id = '90300000079469',
                amount_refunded = 50,
                gateway_transaction_id = 'B10E6E0F31BD',
                description = 'Payment has been made for the invoice INV-384',
                var_date = '2016-06-05',
                reference_number = 'INV-384',
                amount = 370,
                bank_charges = 10,
                exchange_rate = 1,
                autotransaction = ls_zoho_billing_invoices.models.retrieve_an_invoice_response_invoice_payments_inner_autotransaction.retrieve_an_invoice_response_invoice_payments_inner_autotransaction(
                    autotransaction_id = '9030000079465', 
                    payment_gateway = 'payflow_pro', 
                    gateway_transaction_id = 'B10E6E0F31BD', 
                    gateway_error_message = 'Gateway error message for a failed transaction.', 
                    account_id = '9030000000000361', )
            )
        else:
            return RetrieveAnInvoiceResponseInvoicePaymentsInner(
        )
        """

    def testRetrieveAnInvoiceResponseInvoicePaymentsInner(self):
        """Test RetrieveAnInvoiceResponseInvoicePaymentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
