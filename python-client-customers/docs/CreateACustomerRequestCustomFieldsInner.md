# CreateACustomerRequestCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label of the custom field. | [optional] 
**value** | **str** | Value of the custom field. | [optional] 

## Example

```python
from ls_zoho_billing_customers.models.create_a_customer_request_custom_fields_inner import CreateACustomerRequestCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateACustomerRequestCustomFieldsInner from a JSON string
create_a_customer_request_custom_fields_inner_instance = CreateACustomerRequestCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(CreateACustomerRequestCustomFieldsInner.to_json())

# convert the object into a dict
create_a_customer_request_custom_fields_inner_dict = create_a_customer_request_custom_fields_inner_instance.to_dict()
# create an instance of CreateACustomerRequestCustomFieldsInner from a dict
create_a_customer_request_custom_fields_inner_from_dict = CreateACustomerRequestCustomFieldsInner.from_dict(create_a_customer_request_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


