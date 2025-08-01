# coding: utf-8

"""
    Refunds

    A refund object enables you to manage your refunds. Refunds can be made by direct payment to the respective customer or through credits.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_refunds.models.refund_a_credit_note_request import RefundACreditNoteRequest

class TestRefundACreditNoteRequest(unittest.TestCase):
    """RefundACreditNoteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RefundACreditNoteRequest:
        """Test RefundACreditNoteRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RefundACreditNoteRequest`
        """
        model = RefundACreditNoteRequest()
        if include_optional:
            return RefundACreditNoteRequest(
                amount = 20,
                description = 'Refund for discount Offer'
            )
        else:
            return RefundACreditNoteRequest(
                amount = 20,
        )
        """

    def testRefundACreditNoteRequest(self):
        """Test RefundACreditNoteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
