# SubscriptionResponseAddonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_code** | **str** | Addon code of the addon. | [optional] 
**name** | **object** | Name of the addon. | [optional] 
**addon_description** | **str** | Description of the addon exclusive to this subscription. This will be displayed in place of the addon name in invoices generated for this subscription. | [optional] 
**quantity** | **int** | Required quantity of the chosen addon. | [optional] 
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] 
**item_custom_fields** | [**List[ItemCustomFieldsInner]**](ItemCustomFieldsInner.md) | Custom fields for a item. | [optional] 
**price** | **float** | A value can be provided here if the per unit addon price has to be overridden for this subscription. | [optional] 
**discount** | **object** | Discount applied for the addon. | [optional] 
**total** | **object** | Total amount for the addon. | [optional] 
**tax_id** | **object** | Unique ID of the tax applied for the addon. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.subscription_response_addons_inner import SubscriptionResponseAddonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionResponseAddonsInner from a JSON string
subscription_response_addons_inner_instance = SubscriptionResponseAddonsInner.from_json(json)
# print the JSON string representation of the object
print(SubscriptionResponseAddonsInner.to_json())

# convert the object into a dict
subscription_response_addons_inner_dict = subscription_response_addons_inner_instance.to_dict()
# create an instance of SubscriptionResponseAddonsInner from a dict
subscription_response_addons_inner_from_dict = SubscriptionResponseAddonsInner.from_dict(subscription_response_addons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


