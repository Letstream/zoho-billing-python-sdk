# coding: utf-8

"""
    Subscriptions

    A subscription enables you to charge customers at specified intervals for a plan of their choice.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_subscription.models.buy_one_time_addon_response_invoice_credits_inner import BuyOneTimeAddonResponseInvoiceCreditsInner

class TestBuyOneTimeAddonResponseInvoiceCreditsInner(unittest.TestCase):
    """BuyOneTimeAddonResponseInvoiceCreditsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BuyOneTimeAddonResponseInvoiceCreditsInner:
        """Test BuyOneTimeAddonResponseInvoiceCreditsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BuyOneTimeAddonResponseInvoiceCreditsInner`
        """
        model = BuyOneTimeAddonResponseInvoiceCreditsInner()
        if include_optional:
            return BuyOneTimeAddonResponseInvoiceCreditsInner(
                creditnote_id = '9030000079876',
                creditnotes_number = 'CN-26',
                credited_date = '2016-06-15',
                credited_amount = '15'
            )
        else:
            return BuyOneTimeAddonResponseInvoiceCreditsInner(
        )
        """

    def testBuyOneTimeAddonResponseInvoiceCreditsInner(self):
        """Test BuyOneTimeAddonResponseInvoiceCreditsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
