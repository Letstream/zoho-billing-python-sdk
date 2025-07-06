# CreateASubscriptionRequestCustomerDefaultTemplates

Default templates associated with the customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_template_id** | **str** | Unique Id used to denote the invoice template. | [optional] 
**creditnote_template_id** | **str** | Unique Id used to denote the credit note template. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.create_a_subscription_request_customer_default_templates import CreateASubscriptionRequestCustomerDefaultTemplates

# TODO update the JSON string below
json = "{}"
# create an instance of CreateASubscriptionRequestCustomerDefaultTemplates from a JSON string
create_a_subscription_request_customer_default_templates_instance = CreateASubscriptionRequestCustomerDefaultTemplates.from_json(json)
# print the JSON string representation of the object
print(CreateASubscriptionRequestCustomerDefaultTemplates.to_json())

# convert the object into a dict
create_a_subscription_request_customer_default_templates_dict = create_a_subscription_request_customer_default_templates_instance.to_dict()
# create an instance of CreateASubscriptionRequestCustomerDefaultTemplates from a dict
create_a_subscription_request_customer_default_templates_from_dict = CreateASubscriptionRequestCustomerDefaultTemplates.from_dict(create_a_subscription_request_customer_default_templates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


