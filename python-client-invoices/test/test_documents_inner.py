# coding: utf-8

"""
    Invoices

    Invoices describe how much a customer owes for his subscription. Invoices are created for recurring charges, one time charges including any prorated adjustments.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_invoices.models.documents_inner import DocumentsInner

class TestDocumentsInner(unittest.TestCase):
    """DocumentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocumentsInner:
        """Test DocumentsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocumentsInner`
        """
        model = DocumentsInner()
        if include_optional:
            return DocumentsInner(
                file_name = Rental Agreement.pdf,
                file_type = pdf,
                file_size = 5447,
                file_size_formatted = 5.3 KB,
                document_id = 903000005689,
                attachment_order = 1
            )
        else:
            return DocumentsInner(
        )
        """

    def testDocumentsInner(self):
        """Test DocumentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
