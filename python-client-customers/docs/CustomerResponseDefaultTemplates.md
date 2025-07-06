# CustomerResponseDefaultTemplates

Default templates associated with the customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_template_id** | **str** | Unique Id used to denote the invoice template. | [optional] 
**creditnote_template_id** | **str** | Unique Id used to denote the credit note template. | [optional] 

## Example

```python
from ls_zoho_billing_customers.models.customer_response_default_templates import CustomerResponseDefaultTemplates

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerResponseDefaultTemplates from a JSON string
customer_response_default_templates_instance = CustomerResponseDefaultTemplates.from_json(json)
# print the JSON string representation of the object
print(CustomerResponseDefaultTemplates.to_json())

# convert the object into a dict
customer_response_default_templates_dict = customer_response_default_templates_instance.to_dict()
# create an instance of CustomerResponseDefaultTemplates from a dict
customer_response_default_templates_from_dict = CustomerResponseDefaultTemplates.from_dict(customer_response_default_templates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


