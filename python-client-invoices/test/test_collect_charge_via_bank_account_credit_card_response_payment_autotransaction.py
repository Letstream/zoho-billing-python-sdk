# coding: utf-8

"""
    Invoices

    Invoices describe how much a customer owes for his subscription. Invoices are created for recurring charges, one time charges including any prorated adjustments.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_invoices.models.collect_charge_via_bank_account_credit_card_response_payment_autotransaction import CollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction

class TestCollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction(unittest.TestCase):
    """CollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction:
        """Test CollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction`
        """
        model = CollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction()
        if include_optional:
            return CollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction(
                autotransaction_id = '9030000079465',
                payment_gateway = 'payflow_pro',
                gateway_transaction_id = 'B10E6E0F31BD',
                gateway_error_message = 'Gateway error message for a failed transaction.',
                account_id = '9030000000000361'
            )
        else:
            return CollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction(
        )
        """

    def testCollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction(self):
        """Test CollectChargeViaBankAccountCreditCardResponsePaymentAutotransaction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
