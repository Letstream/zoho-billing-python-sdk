# coding: utf-8

"""
    Products

    A product refers to the service you offer your customers. There can be multiple products created if you offer more than one service. Each product can have different plans and addons associated with it.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_products.models.create_a_product_request import CreateAProductRequest

class TestCreateAProductRequest(unittest.TestCase):
    """CreateAProductRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateAProductRequest:
        """Test CreateAProductRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateAProductRequest`
        """
        model = CreateAProductRequest()
        if include_optional:
            return CreateAProductRequest(
                name = 'PiperHost',
                description = 'Dedicated server for web hosting',
                email_ids = 'piper@zillum.com',
                redirect_url = 'http://www.zillum.com/products/piperhost'
            )
        else:
            return CreateAProductRequest(
                name = 'PiperHost',
        )
        """

    def testCreateAProductRequest(self):
        """Test CreateAProductRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
