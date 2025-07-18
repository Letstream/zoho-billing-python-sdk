# coding: utf-8

"""
    Settings

    Tax Settings Related APIs.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_settings.models.taxes_response import TaxesResponse

class TestTaxesResponse(unittest.TestCase):
    """TaxesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaxesResponse:
        """Test TaxesResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaxesResponse`
        """
        model = TaxesResponse()
        if include_optional:
            return TaxesResponse(
                is_default_tax = 'true',
                is_editable = 'true',
                tax_authority_id = '903000006345',
                tax_authority_name = 'ATO',
                tax_id = '903000002345',
                tax_name = 'GST',
                tax_percentage = '15',
                tax_type = 'tax_group'
            )
        else:
            return TaxesResponse(
        )
        """

    def testTaxesResponse(self):
        """Test TaxesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
