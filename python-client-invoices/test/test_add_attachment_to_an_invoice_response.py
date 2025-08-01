# coding: utf-8

"""
    Invoices

    Invoices describe how much a customer owes for his subscription. Invoices are created for recurring charges, one time charges including any prorated adjustments.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_invoices.models.add_attachment_to_an_invoice_response import AddAttachmentToAnInvoiceResponse

class TestAddAttachmentToAnInvoiceResponse(unittest.TestCase):
    """AddAttachmentToAnInvoiceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddAttachmentToAnInvoiceResponse:
        """Test AddAttachmentToAnInvoiceResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddAttachmentToAnInvoiceResponse`
        """
        model = AddAttachmentToAnInvoiceResponse()
        if include_optional:
            return AddAttachmentToAnInvoiceResponse(
                code = 0,
                message = 'Your file has been successfully attached to the invoice.'
            )
        else:
            return AddAttachmentToAnInvoiceResponse(
        )
        """

    def testAddAttachmentToAnInvoiceResponse(self):
        """Test AddAttachmentToAnInvoiceResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
