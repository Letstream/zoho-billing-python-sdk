# DataSubscriptionAddonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_code** | **str** | Addon code of the addon. | [optional] 
**name** | **object** | Name of the addon. | [optional] 
**description** | **str** | Description of the plan exclusive to this subscription. This will be displayed in place of the plan name in invoices generated for this subscription. | [optional] 
**quantity** | **int** | Required quantity of the chosen addon. | [optional] 
**price** | **float** | A value can be provided here if the per unit addon price has to be overridden for this subscription. | [optional] 
**discount** | **object** | Discount applied for the addon. | [optional] 
**total** | **object** | Total amount for the addon. | [optional] 
**tax_id** | **object** | Unique ID of the tax applied for the addon. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.data_subscription_addons_inner import DataSubscriptionAddonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataSubscriptionAddonsInner from a JSON string
data_subscription_addons_inner_instance = DataSubscriptionAddonsInner.from_json(json)
# print the JSON string representation of the object
print(DataSubscriptionAddonsInner.to_json())

# convert the object into a dict
data_subscription_addons_inner_dict = data_subscription_addons_inner_instance.to_dict()
# create an instance of DataSubscriptionAddonsInner from a dict
data_subscription_addons_inner_from_dict = DataSubscriptionAddonsInner.from_dict(data_subscription_addons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


