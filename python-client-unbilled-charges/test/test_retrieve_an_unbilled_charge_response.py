# coding: utf-8

"""
    Unbilled-Charges

    These are charges to be converted into an invoice at a later point of time, either by manual intervention or during renewal.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_unbilled_charges.models.retrieve_an_unbilled_charge_response import RetrieveAnUnbilledChargeResponse

class TestRetrieveAnUnbilledChargeResponse(unittest.TestCase):
    """RetrieveAnUnbilledChargeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RetrieveAnUnbilledChargeResponse:
        """Test RetrieveAnUnbilledChargeResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RetrieveAnUnbilledChargeResponse`
        """
        model = RetrieveAnUnbilledChargeResponse()
        if include_optional:
            return RetrieveAnUnbilledChargeResponse(
                code = 0,
                message = 'success',
                unbilled_charge = ls_zoho_billing_unbilled_charges.models.unbilled_charge_response.unbilled_charge-response(
                    unbilled_charge_id = '90300000079200', 
                    number = 'UNBILL-000004', 
                    status = 'open', 
                    unbilled_charge_date = '2016-06-05', 
                    customer_id = 903000000000099, 
                    customer_name = 'Bowman Furniture', 
                    email = 'benjamin.george@bowmanfurniture.com', 
                    unbilled_charge_items = [
                        ls_zoho_billing_unbilled_charges.models.unbilled_charge_items_inner.unbilled_charge_items_inner(
                            unbilled_charge_item_id = '90300000079201', 
                            product_id = '7000000079434', 
                            name = 'Basic', 
                            description = Usage charges for last month, 
                            code = 'basic-monthly', 
                            price = '50', 
                            quantity = 1, 
                            discount_amount = 80, 
                            item_total = 400, 
                            tax_id = 90300000079226, 
                            product_type = 'goods', 
                            hsn_or_sac = '74191010', 
                            tax_exemption_id = 90300000079226, 
                            tax_exemption_code = 'NGO', )
                        ], 
                    coupons = [
                        ls_zoho_billing_unbilled_charges.models.coupons_inner.coupons_inner(
                            coupon_code = 'THANKSGIVING20', 
                            coupon_name = 'Flat 10', )
                        ], 
                    total = 370, 
                    currency_code = 'USD', 
                    currency_symbol = '$', 
                    created_time = '2016-06-05T02:15:15-0700', 
                    updated_time = '2016-06-05T02:15:15-0700', 
                    billing_address = ls_zoho_billing_unbilled_charges.models.billing_address.billing_address(
                        street = 'Harrington Bay Street', 
                        city = 'Salt Lake City', 
                        state = 'CA', 
                        zip = '92612', 
                        country = 'U.S.A', 
                        fax = '4527389', ), 
                    shipping_address = ls_zoho_billing_unbilled_charges.models.shipping_address.shipping_address(
                        street = 'Harrington Bay Street', 
                        city = 'Salt Lake City', 
                        state = 'CA', 
                        zip = '92612', 
                        country = 'U.S.A', 
                        fax = '4527389', ), )
            )
        else:
            return RetrieveAnUnbilledChargeResponse(
        )
        """

    def testRetrieveAnUnbilledChargeResponse(self):
        """Test RetrieveAnUnbilledChargeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
