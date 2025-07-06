# DataSubscriptionCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index of the custom field. It can hold any value from 1 to 10. | [optional] 
**label** | **str** | Label of the Custom Field | [optional] 
**value** | **str** | Value of the Custom Field | [optional] 
**data_type** | **str** | Data type of the custom field | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.data_subscription_custom_fields_inner import DataSubscriptionCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataSubscriptionCustomFieldsInner from a JSON string
data_subscription_custom_fields_inner_instance = DataSubscriptionCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(DataSubscriptionCustomFieldsInner.to_json())

# convert the object into a dict
data_subscription_custom_fields_inner_dict = data_subscription_custom_fields_inner_instance.to_dict()
# create an instance of DataSubscriptionCustomFieldsInner from a dict
data_subscription_custom_fields_inner_from_dict = DataSubscriptionCustomFieldsInner.from_dict(data_subscription_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


