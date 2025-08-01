# coding: utf-8

"""
    Invoices

    Invoices describe how much a customer owes for his subscription. Invoices are created for recurring charges, one time charges including any prorated adjustments.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_invoices.models.add_items_to_a_pending_invoice_response_invoice_invoice_items_inner import AddItemsToAPendingInvoiceResponseInvoiceInvoiceItemsInner

class TestAddItemsToAPendingInvoiceResponseInvoiceInvoiceItemsInner(unittest.TestCase):
    """AddItemsToAPendingInvoiceResponseInvoiceInvoiceItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddItemsToAPendingInvoiceResponseInvoiceInvoiceItemsInner:
        """Test AddItemsToAPendingInvoiceResponseInvoiceInvoiceItemsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddItemsToAPendingInvoiceResponseInvoiceInvoiceItemsInner`
        """
        model = AddItemsToAPendingInvoiceResponseInvoiceInvoiceItemsInner()
        if include_optional:
            return AddItemsToAPendingInvoiceResponseInvoiceInvoiceItemsInner(
                item_id = '7000000079434',
                name = 'Basic',
                description = Charges for this duration (from 16-April-2016 to 8-June-2016),
                tags = [
                    ls_zoho_billing_invoices.models.tags_inner.tags_inner(
                        tag_id = 56, 
                        tag_option_id = 56, )
                    ],
                item_custom_fields = [
                    ls_zoho_billing_invoices.models.item_custom_fields_inner.item_custom_fields_inner(
                        label = '', 
                        value = '', )
                    ],
                code = 'basic-monthly',
                price = '50',
                quantity = 1,
                discount_amount = 80,
                item_total = 400,
                tax_id = '903002205046032',
                product_type = 'goods',
                hsn_or_sac = '74191010',
                tax_exemption_id = '903002205042099',
                tax_exemption_code = 'NGO'
            )
        else:
            return AddItemsToAPendingInvoiceResponseInvoiceInvoiceItemsInner(
        )
        """

    def testAddItemsToAPendingInvoiceResponseInvoiceInvoiceItemsInner(self):
        """Test AddItemsToAPendingInvoiceResponseInvoiceInvoiceItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
