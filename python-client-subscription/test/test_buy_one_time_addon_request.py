# coding: utf-8

"""
    Subscriptions

    A subscription enables you to charge customers at specified intervals for a plan of their choice.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_subscription.models.buy_one_time_addon_request import BuyOneTimeAddonRequest

class TestBuyOneTimeAddonRequest(unittest.TestCase):
    """BuyOneTimeAddonRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BuyOneTimeAddonRequest:
        """Test BuyOneTimeAddonRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BuyOneTimeAddonRequest`
        """
        model = BuyOneTimeAddonRequest()
        if include_optional:
            return BuyOneTimeAddonRequest(
                addons = [
                    ls_zoho_billing_subscription.models.buy_one_time_addon_request_addons_inner.buy_one_time_addon_request_addons_inner(
                        addon_code = 'Email-basic', 
                        quantity = 1, 
                        tags = [
                            ls_zoho_billing_subscription.models.tags_inner.tags_inner(
                                tag_id = 56, 
                                tag_option_id = 56, )
                            ], 
                        item_custom_fields = [
                            ls_zoho_billing_subscription.models.item_custom_fields_inner.item_custom_fields_inner(
                                label = '', 
                                value = '', )
                            ], 
                        price = 10, 
                        tax_id = null, 
                        tax_exemption_id = null, 
                        tax_exemption_code = null, 
                        product_type = 'goods', )
                    ],
                exchange_rate = 2,
                coupon_code = None,
                add_to_unbilled_charges = True
            )
        else:
            return BuyOneTimeAddonRequest(
                addons = [
                    ls_zoho_billing_subscription.models.buy_one_time_addon_request_addons_inner.buy_one_time_addon_request_addons_inner(
                        addon_code = 'Email-basic', 
                        quantity = 1, 
                        tags = [
                            ls_zoho_billing_subscription.models.tags_inner.tags_inner(
                                tag_id = 56, 
                                tag_option_id = 56, )
                            ], 
                        item_custom_fields = [
                            ls_zoho_billing_subscription.models.item_custom_fields_inner.item_custom_fields_inner(
                                label = '', 
                                value = '', )
                            ], 
                        price = 10, 
                        tax_id = null, 
                        tax_exemption_id = null, 
                        tax_exemption_code = null, 
                        product_type = 'goods', )
                    ],
        )
        """

    def testBuyOneTimeAddonRequest(self):
        """Test BuyOneTimeAddonRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
