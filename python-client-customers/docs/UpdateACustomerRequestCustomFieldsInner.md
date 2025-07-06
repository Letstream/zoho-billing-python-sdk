# UpdateACustomerRequestCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index of the custom field. It can hold any value from 1 to 10. | [optional] 
**value** | **str** | Value of the custom field. | [optional] 
**label** | **str** | Label of the custom field. | [optional] 
**data_type** | **str** | Data type of the custom field. | [optional] 

## Example

```python
from ls_zoho_billing_customers.models.update_a_customer_request_custom_fields_inner import UpdateACustomerRequestCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateACustomerRequestCustomFieldsInner from a JSON string
update_a_customer_request_custom_fields_inner_instance = UpdateACustomerRequestCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateACustomerRequestCustomFieldsInner.to_json())

# convert the object into a dict
update_a_customer_request_custom_fields_inner_dict = update_a_customer_request_custom_fields_inner_instance.to_dict()
# create an instance of UpdateACustomerRequestCustomFieldsInner from a dict
update_a_customer_request_custom_fields_inner_from_dict = UpdateACustomerRequestCustomFieldsInner.from_dict(update_a_customer_request_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


