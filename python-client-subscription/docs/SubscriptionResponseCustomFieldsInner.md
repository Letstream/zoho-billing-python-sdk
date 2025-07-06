# SubscriptionResponseCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index of the custom field. It can hold any value from 1 to 10. | [optional] 
**label** | **str** | Label of the Custom Field | [optional] 
**value** | **str** | Value of the Custom Field | [optional] 
**data_type** | **str** | Data type of the custom field. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.subscription_response_custom_fields_inner import SubscriptionResponseCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionResponseCustomFieldsInner from a JSON string
subscription_response_custom_fields_inner_instance = SubscriptionResponseCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(SubscriptionResponseCustomFieldsInner.to_json())

# convert the object into a dict
subscription_response_custom_fields_inner_dict = subscription_response_custom_fields_inner_instance.to_dict()
# create an instance of SubscriptionResponseCustomFieldsInner from a dict
subscription_response_custom_fields_inner_from_dict = SubscriptionResponseCustomFieldsInner.from_dict(subscription_response_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


