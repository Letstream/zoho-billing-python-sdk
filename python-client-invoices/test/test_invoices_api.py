# coding: utf-8

"""
    Invoices

    Invoices describe how much a customer owes for his subscription. Invoices are created for recurring charges, one time charges including any prorated adjustments.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_invoices.api.invoices_api import InvoicesApi


class TestInvoicesApi(unittest.TestCase):
    """InvoicesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InvoicesApi()

    def tearDown(self) -> None:
        pass

    def test_invoice_invoice_id_customfields_put(self) -> None:
        """Test case for invoice_invoice_id_customfields_put

        Update custom field in existing invoices
        """
        pass

    def test_invoices_get(self) -> None:
        """Test case for invoices_get

        List all invoices
        """
        pass

    def test_invoices_invoice_id_address_put(self) -> None:
        """Test case for invoices_invoice_id_address_put

        Update address
        """
        pass

    def test_invoices_invoice_id_attachment_post(self) -> None:
        """Test case for invoices_invoice_id_attachment_post

        Add attachment to an invoice
        """
        pass

    def test_invoices_invoice_id_cancelwriteoff_post(self) -> None:
        """Test case for invoices_invoice_id_cancelwriteoff_post

        Cancel write off
        """
        pass

    def test_invoices_invoice_id_collect_post(self) -> None:
        """Test case for invoices_invoice_id_collect_post

        Collect charge via bank account / credit card
        """
        pass

    def test_invoices_invoice_id_converttoopen_post(self) -> None:
        """Test case for invoices_invoice_id_converttoopen_post

        Convert to open
        """
        pass

    def test_invoices_invoice_id_credits_post(self) -> None:
        """Test case for invoices_invoice_id_credits_post

        Apply Multiple Credits to Invoice
        """
        pass

    def test_invoices_invoice_id_customfields_post(self) -> None:
        """Test case for invoices_invoice_id_customfields_post

        Update Custom Fields
        """
        pass

    def test_invoices_invoice_id_delete(self) -> None:
        """Test case for invoices_invoice_id_delete

        Delete an invoice
        """
        pass

    def test_invoices_invoice_id_email_post(self) -> None:
        """Test case for invoices_invoice_id_email_post

        Email an invoice
        """
        pass

    def test_invoices_invoice_id_get(self) -> None:
        """Test case for invoices_invoice_id_get

        Retrieve an invoice
        """
        pass

    def test_invoices_invoice_id_lineitems_item_id_delete(self) -> None:
        """Test case for invoices_invoice_id_lineitems_item_id_delete

        Delete items from a pending invoice
        """
        pass

    def test_invoices_invoice_id_lineitems_post(self) -> None:
        """Test case for invoices_invoice_id_lineitems_post

        Add items to a pending invoice
        """
        pass

    def test_invoices_invoice_id_put(self) -> None:
        """Test case for invoices_invoice_id_put

        Update an invoice
        """
        pass

    def test_invoices_invoice_id_void_post(self) -> None:
        """Test case for invoices_invoice_id_void_post

        Void an invoice
        """
        pass

    def test_invoices_invoice_id_writeoff_post(self) -> None:
        """Test case for invoices_invoice_id_writeoff_post

        Write off
        """
        pass

    def test_invoices_post(self) -> None:
        """Test case for invoices_post

        Create an invoice
        """
        pass


if __name__ == '__main__':
    unittest.main()
