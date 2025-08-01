# coding: utf-8

"""
    Coupons

    Coupons are used to provide discounts and special offers to customers. These coupons can be applied to a subscription at any time.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_coupons.models.coupon_response_addons_inner import CouponResponseAddonsInner

class TestCouponResponseAddonsInner(unittest.TestCase):
    """CouponResponseAddonsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CouponResponseAddonsInner:
        """Test CouponResponseAddonsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CouponResponseAddonsInner`
        """
        model = CouponResponseAddonsInner()
        if include_optional:
            return CouponResponseAddonsInner(
                addon_code = 'Email-basic',
                name = Email Basic
            )
        else:
            return CouponResponseAddonsInner(
        )
        """

    def testCouponResponseAddonsInner(self):
        """Test CouponResponseAddonsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
