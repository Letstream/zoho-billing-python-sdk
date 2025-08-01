# coding: utf-8

"""
    Coupons

    Coupons are used to provide discounts and special offers to customers. These coupons can be applied to a subscription at any time.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_coupons.models.retrieve_a_coupon_response import RetrieveACouponResponse

class TestRetrieveACouponResponse(unittest.TestCase):
    """RetrieveACouponResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RetrieveACouponResponse:
        """Test RetrieveACouponResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RetrieveACouponResponse`
        """
        model = RetrieveACouponResponse()
        if include_optional:
            return RetrieveACouponResponse(
                code = 0,
                message = 'success',
                coupon = ls_zoho_billing_coupons.models.retrieve_a_coupon_response_coupon.retrieve_a_coupon_response_coupon(
                    coupon_code = 'THANKSGIVING20', 
                    name = 'Thanksgiving 20 percent offer', 
                    description = 'Twenty percent offer for thanks giving.', 
                    type = 'duration', 
                    duration = 2, 
                    status = 'active', 
                    discount_by = 'percentage', 
                    discount_value = 20, 
                    product_id = '903000000045027', 
                    max_redemption = 50, 
                    redemption_count = 10, 
                    expiry_at = '2016-08-28', 
                    apply_to_plans = 'select', 
                    plans = [
                        ls_zoho_billing_coupons.models.coupon_response_plans_inner.coupon_response_plans_inner(
                            plan_code = 'basic-monthly', )
                        ], 
                    apply_to_addons = 'select', 
                    addons = [
                        ls_zoho_billing_coupons.models.coupon_response_addons_inner.coupon_response_addons_inner(
                            addon_code = 'Email-basic', )
                        ], 
                    created_time = '2016-06-05T18:02:26-0700', 
                    updated_time = '2016-06-05T18:02:26-0700', )
            )
        else:
            return RetrieveACouponResponse(
        )
        """

    def testRetrieveACouponResponse(self):
        """Test RetrieveACouponResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
