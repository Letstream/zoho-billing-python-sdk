# coding: utf-8

"""
    Credit-Notes

    Credit notes are created when a refund is to be made to a customer. A credit note object allows you to keep track of all credit note related information.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_credit_notes.api.credit_notes_api import CreditNotesApi


class TestCreditNotesApi(unittest.TestCase):
    """CreditNotesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CreditNotesApi()

    def tearDown(self) -> None:
        pass

    def test_creditnotes_creditnote_id_converttoopen_post(self) -> None:
        """Test case for creditnotes_creditnote_id_converttoopen_post

        Open a voided credit note
        """
        pass

    def test_creditnotes_creditnote_id_delete(self) -> None:
        """Test case for creditnotes_creditnote_id_delete

        Delete a credit note
        """
        pass

    def test_creditnotes_creditnote_id_email_post(self) -> None:
        """Test case for creditnotes_creditnote_id_email_post

        Email a credit note
        """
        pass

    def test_creditnotes_creditnote_id_get(self) -> None:
        """Test case for creditnotes_creditnote_id_get

        Retreive a credit note
        """
        pass

    def test_creditnotes_creditnote_id_invoices_post(self) -> None:
        """Test case for creditnotes_creditnote_id_invoices_post

        Apply Credits to Multiple Invoices
        """
        pass

    def test_creditnotes_creditnote_id_void_post(self) -> None:
        """Test case for creditnotes_creditnote_id_void_post

        Void a credit note
        """
        pass

    def test_creditnotes_post(self) -> None:
        """Test case for creditnotes_post

        Create a credit note
        """
        pass


if __name__ == '__main__':
    unittest.main()
