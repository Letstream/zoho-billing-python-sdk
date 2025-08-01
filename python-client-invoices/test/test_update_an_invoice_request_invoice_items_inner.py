# coding: utf-8

"""
    Invoices

    Invoices describe how much a customer owes for his subscription. Invoices are created for recurring charges, one time charges including any prorated adjustments.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_invoices.models.update_an_invoice_request_invoice_items_inner import UpdateAnInvoiceRequestInvoiceItemsInner

class TestUpdateAnInvoiceRequestInvoiceItemsInner(unittest.TestCase):
    """UpdateAnInvoiceRequestInvoiceItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateAnInvoiceRequestInvoiceItemsInner:
        """Test UpdateAnInvoiceRequestInvoiceItemsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateAnInvoiceRequestInvoiceItemsInner`
        """
        model = UpdateAnInvoiceRequestInvoiceItemsInner()
        if include_optional:
            return UpdateAnInvoiceRequestInvoiceItemsInner(
                product_id = '7000000079434',
                project_id = '90300000087378',
                time_entry_ids = [],
                expense_id = ' ',
                name = 'Basic',
                product_type = 'goods',
                hsn_or_sac = '74191010',
                sat_item_key_code = '71121206',
                unitkey_code = 'E48',
                description = 'Payment has been made for the invoice INV-384',
                item_order = 1,
                price = '50',
                quantity = 1,
                unit = ' ',
                discount = 0,
                tax_id = '903002205046032',
                tds_tax_id = '982000000557012',
                tax_exemption_id = '903002205042099',
                avatax_use_code = '',
                avatax_exempt_no = '',
                tax_name = 'VAT',
                tax_type = 'tax',
                tax_percentage = 12.5,
                item_total = 400
            )
        else:
            return UpdateAnInvoiceRequestInvoiceItemsInner(
                product_id = '7000000079434',
        )
        """

    def testUpdateAnInvoiceRequestInvoiceItemsInner(self):
        """Test UpdateAnInvoiceRequestInvoiceItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
