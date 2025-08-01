# coding: utf-8

"""
    Plans

    A plan object contains the billing and pricing information of a plan. Your organization may consist of plans that differ either by features or by the plan’s billing frequency. You can have a $10 basic plan, $20 professional plan, $24 monthly or a $240 yearly plan.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_plans.models.retrieve_a_plan_response_plan import RetrieveAPlanResponsePlan

class TestRetrieveAPlanResponsePlan(unittest.TestCase):
    """RetrieveAPlanResponsePlan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RetrieveAPlanResponsePlan:
        """Test RetrieveAPlanResponsePlan
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RetrieveAPlanResponsePlan`
        """
        model = RetrieveAPlanResponsePlan()
        if include_optional:
            return RetrieveAPlanResponsePlan(
                plan_code = 'basic-monthly',
                name = 'Basic',
                description = 'Basic monthly plan.',
                store_markup_description = 'Mailbox Storage-100GB | User & Docs Storage-500GB | User',
                status = 'active',
                product_id = '903000000045027',
                account_id = '903000987009900',
                account_name = 'Sales',
                trial_period = 0,
                setup_fee = 0,
                setup_fee_account_id = '903000987009903',
                setup_fee_account_name = 'General Income',
                tags = [
                    ls_zoho_billing_plans.models.plan_response_tags_inner.plan_response_tags_inner(
                        tag_option_id = 460000000054280, 
                        is_tag_mandatory = 'false', 
                        tag_name = 'Colors', 
                        tag_id = 460000000054182, 
                        tag_option_name = 'Black', )
                    ],
                custom_fields = [
                    ls_zoho_billing_plans.models.plan_response_custom_fields_inner.plan_response_custom_fields_inner(
                        customfield_id = '2000000029001', 
                        is_active = 'true', 
                        show_in_all_pdf = 'true', 
                        value_formatted = 'Normal', 
                        data_type = 'string', 
                        index = 1, 
                        label = 'cfitem', 
                        show_on_pdf = 'false', 
                        placeholder = 'cf_cfitem', 
                        value = 'Normal', )
                    ],
                recurring_price = 400,
                unit = 'kg',
                interval = 1,
                interval_unit = 'months',
                billing_cycles = -1,
                url = 'https://billing.zoho.com/subscribe/3b884751f87f05e584c3952b6388e7f96a2bba0f6b0532177e00f0ba8db832fc/basic-monthly',
                tax_id = 'no tax will be associated',
                product_type = 'goods',
                hsn_or_sac = '74191010',
                sat_item_key_code = '71121206',
                unitkey_code = 'E48',
                item_tax_preferences = [
                    ls_zoho_billing_plans.models.item_tax_preferences_inner.item_tax_preferences_inner(
                        tax_specification = 'intra', 
                        tax_name = 'GST', 
                        tax_percentage = 10, 
                        tax_id = 'no tax will be associated', )
                    ],
                created_time = '2016-06-05T17:40:49-0700',
                updated_time = '2016-06-05T24:40:49-0700'
            )
        else:
            return RetrieveAPlanResponsePlan(
        )
        """

    def testRetrieveAPlanResponsePlan(self):
        """Test RetrieveAPlanResponsePlan"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
