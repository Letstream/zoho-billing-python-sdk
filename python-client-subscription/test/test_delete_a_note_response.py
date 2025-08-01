# coding: utf-8

"""
    Subscriptions

    A subscription enables you to charge customers at specified intervals for a plan of their choice.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_subscription.models.delete_a_note_response import DeleteANoteResponse

class TestDeleteANoteResponse(unittest.TestCase):
    """DeleteANoteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteANoteResponse:
        """Test DeleteANoteResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteANoteResponse`
        """
        model = DeleteANoteResponse()
        if include_optional:
            return DeleteANoteResponse(
                code = 0,
                message = 'The note has been deleted.'
            )
        else:
            return DeleteANoteResponse(
        )
        """

    def testDeleteANoteResponse(self):
        """Test DeleteANoteResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
