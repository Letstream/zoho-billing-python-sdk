# coding: utf-8

"""
    Invoices

    Invoices describe how much a customer owes for his subscription. Invoices are created for recurring charges, one time charges including any prorated adjustments.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_invoices.models.get_invoice_email_content_response_data_from_emails_inner import GetInvoiceEmailContentResponseDataFromEmailsInner

class TestGetInvoiceEmailContentResponseDataFromEmailsInner(unittest.TestCase):
    """GetInvoiceEmailContentResponseDataFromEmailsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetInvoiceEmailContentResponseDataFromEmailsInner:
        """Test GetInvoiceEmailContentResponseDataFromEmailsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetInvoiceEmailContentResponseDataFromEmailsInner`
        """
        model = GetInvoiceEmailContentResponseDataFromEmailsInner()
        if include_optional:
            return GetInvoiceEmailContentResponseDataFromEmailsInner(
                user_name = 'David Sujin',
                selected = True,
                email = 'benjamin.george@bowmanfurniture.com',
                organization_contact_id = '2000000002266',
                is_org_email_id = True
            )
        else:
            return GetInvoiceEmailContentResponseDataFromEmailsInner(
        )
        """

    def testGetInvoiceEmailContentResponseDataFromEmailsInner(self):
        """Test GetInvoiceEmailContentResponseDataFromEmailsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
