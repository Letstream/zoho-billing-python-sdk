# coding: utf-8

"""
    Items

    A product is the item offered for sale. It can be a commodity. Based on the type of your business, you can offer one or more goods.<br><br><b>Possible error codes: </b><br><table><thead><tr><th>Error Code</th><th>Message</th></tr></thead><tbody><tr><td><span style=\"color:#FF0000;\"> 1000</span></td><td>The item name already exist</td></tr><tr><tr><td><span style=\"color:#FF0000;\"> 2006</span></td><td>Item does not exist</td></tr><td><span style=\"color:#FF0000;\"> 2049</span></td><td>Items which are a part of other transactions cannot be deleted. Instead, mark them as inactive</td></tr><tr><td><span style=\"color:#FF0000;\"> 2076</span></td><td>Product type cannot be changed for Items having transactions</td></tr></tbody></table>

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_items.models.delete_an_item_response import DeleteAnItemResponse

class TestDeleteAnItemResponse(unittest.TestCase):
    """DeleteAnItemResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteAnItemResponse:
        """Test DeleteAnItemResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteAnItemResponse`
        """
        model = DeleteAnItemResponse()
        if include_optional:
            return DeleteAnItemResponse(
                code = 0,
                message = 'The item has been deleted.'
            )
        else:
            return DeleteAnItemResponse(
        )
        """

    def testDeleteAnItemResponse(self):
        """Test DeleteAnItemResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
