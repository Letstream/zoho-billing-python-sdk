# coding: utf-8

"""
    Events

    Events can be used to let you know when something happens in your organization. Every happening in your organization will be recorded as a new Event. For example, when a new payment is received, we will create a <code>payment_thankyou</code> event; when a subscription is created, we will create a <code>subscription_created</code> event.<br/> <br/>You can retrieve these events individually or as a <a href=\"https://www.zoho.com/billing/api/v1/events/#list-of-events\">list</a> using our API. If you want to update the data on your server when an event occurs, you can use webhooks to send these event objects directly to an endpoint on your application’s server. Learn more about <a href=\"https://www.zoho.com/billing/help/settings/automation.html\">webhooks</a>.<br/><br/>

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ls_zoho_billing_events.models.list_of_events_response_events_inner import ListOfEventsResponseEventsInner

class TestListOfEventsResponseEventsInner(unittest.TestCase):
    """ListOfEventsResponseEventsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListOfEventsResponseEventsInner:
        """Test ListOfEventsResponseEventsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListOfEventsResponseEventsInner`
        """
        model = ListOfEventsResponseEventsInner()
        if include_optional:
            return ListOfEventsResponseEventsInner(
                event_id = '90300000005337',
                event_type = 'subscription_activation',
                event_time = '2016-06-05T18:28:20-0700'
            )
        else:
            return ListOfEventsResponseEventsInner(
        )
        """

    def testListOfEventsResponseEventsInner(self):
        """Test ListOfEventsResponseEventsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
