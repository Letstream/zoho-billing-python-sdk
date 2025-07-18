# coding: utf-8

"""
    Invoices

    Invoices describe how much a customer owes for his subscription. Invoices are created for recurring charges, one time charges including any prorated adjustments.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_invoices.models.get_an_invoice_attachment_response import GetAnInvoiceAttachmentResponse

class TestGetAnInvoiceAttachmentResponse(unittest.TestCase):
    """GetAnInvoiceAttachmentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAnInvoiceAttachmentResponse:
        """Test GetAnInvoiceAttachmentResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAnInvoiceAttachmentResponse`
        """
        model = GetAnInvoiceAttachmentResponse()
        if include_optional:
            return GetAnInvoiceAttachmentResponse(
                code = 0,
                message = 'success'
            )
        else:
            return GetAnInvoiceAttachmentResponse(
        )
        """

    def testGetAnInvoiceAttachmentResponse(self):
        """Test GetAnInvoiceAttachmentResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
