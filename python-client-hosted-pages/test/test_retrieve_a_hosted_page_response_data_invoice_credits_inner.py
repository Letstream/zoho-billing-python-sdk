# coding: utf-8

"""
    Hosted-Pages

    Zoho Billing provides a hosted payment page to integrate with your websites. You can securely integrate with Zoho Billing for collecting your customer's sensitive card information through the hosted page. These Hosted Pages will expire within one hour.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_hosted_pages.models.retrieve_a_hosted_page_response_data_invoice_credits_inner import RetrieveAHostedPageResponseDataInvoiceCreditsInner

class TestRetrieveAHostedPageResponseDataInvoiceCreditsInner(unittest.TestCase):
    """RetrieveAHostedPageResponseDataInvoiceCreditsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RetrieveAHostedPageResponseDataInvoiceCreditsInner:
        """Test RetrieveAHostedPageResponseDataInvoiceCreditsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RetrieveAHostedPageResponseDataInvoiceCreditsInner`
        """
        model = RetrieveAHostedPageResponseDataInvoiceCreditsInner()
        if include_optional:
            return RetrieveAHostedPageResponseDataInvoiceCreditsInner(
                creditnote_id = '9030000079876',
                creditnotes_number = 'CN-26',
                credited_date = '2016-06-15',
                credited_amount = '15'
            )
        else:
            return RetrieveAHostedPageResponseDataInvoiceCreditsInner(
        )
        """

    def testRetrieveAHostedPageResponseDataInvoiceCreditsInner(self):
        """Test RetrieveAHostedPageResponseDataInvoiceCreditsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
