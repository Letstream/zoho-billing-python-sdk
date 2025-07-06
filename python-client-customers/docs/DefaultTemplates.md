# DefaultTemplates

Default templates associated with the customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_template_id** | **str** | Unique Id used to denote the invoice template. | [optional] 
**creditnote_template_id** | **str** | Unique Id used to denote the credit note template. | [optional] 

## Example

```python
from ls_zoho_billing_customers.models.default_templates import DefaultTemplates

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultTemplates from a JSON string
default_templates_instance = DefaultTemplates.from_json(json)
# print the JSON string representation of the object
print(DefaultTemplates.to_json())

# convert the object into a dict
default_templates_dict = default_templates_instance.to_dict()
# create an instance of DefaultTemplates from a dict
default_templates_from_dict = DefaultTemplates.from_dict(default_templates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


