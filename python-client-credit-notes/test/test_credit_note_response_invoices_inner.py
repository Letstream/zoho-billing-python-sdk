# coding: utf-8

"""
    Credit-Notes

    Credit notes are created when a refund is to be made to a customer. A credit note object allows you to keep track of all credit note related information.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_credit_notes.models.credit_note_response_invoices_inner import CreditNoteResponseInvoicesInner

class TestCreditNoteResponseInvoicesInner(unittest.TestCase):
    """CreditNoteResponseInvoicesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreditNoteResponseInvoicesInner:
        """Test CreditNoteResponseInvoicesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreditNoteResponseInvoicesInner`
        """
        model = CreditNoteResponseInvoicesInner()
        if include_optional:
            return CreditNoteResponseInvoicesInner(
                invoice_id = '90300000079426',
                invoice_number = 'INV-384',
                amount = 450
            )
        else:
            return CreditNoteResponseInvoicesInner(
        )
        """

    def testCreditNoteResponseInvoicesInner(self):
        """Test CreditNoteResponseInvoicesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
