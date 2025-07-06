# BuyOneTimeAddonForASubscriptionResponseHostedpageCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index of the custom field. It can hold any value from 1 to 10. | [optional] 
**value** | **str** | Value of the Custom Field | [optional] 
**label** | **str** | Label of the Custom Field | [optional] 
**data_type** | **str** | Data type of the custom field | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.buy_one_time_addon_for_a_subscription_response_hostedpage_custom_fields_inner import BuyOneTimeAddonForASubscriptionResponseHostedpageCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BuyOneTimeAddonForASubscriptionResponseHostedpageCustomFieldsInner from a JSON string
buy_one_time_addon_for_a_subscription_response_hostedpage_custom_fields_inner_instance = BuyOneTimeAddonForASubscriptionResponseHostedpageCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(BuyOneTimeAddonForASubscriptionResponseHostedpageCustomFieldsInner.to_json())

# convert the object into a dict
buy_one_time_addon_for_a_subscription_response_hostedpage_custom_fields_inner_dict = buy_one_time_addon_for_a_subscription_response_hostedpage_custom_fields_inner_instance.to_dict()
# create an instance of BuyOneTimeAddonForASubscriptionResponseHostedpageCustomFieldsInner from a dict
buy_one_time_addon_for_a_subscription_response_hostedpage_custom_fields_inner_from_dict = BuyOneTimeAddonForASubscriptionResponseHostedpageCustomFieldsInner.from_dict(buy_one_time_addon_for_a_subscription_response_hostedpage_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


