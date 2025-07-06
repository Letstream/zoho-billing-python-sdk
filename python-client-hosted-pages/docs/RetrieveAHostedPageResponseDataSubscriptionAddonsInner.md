# RetrieveAHostedPageResponseDataSubscriptionAddonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_code** | **str** | Addon code of the addon. | [optional] 
**name** | **object** | Name of the addon. | [optional] 
**description** | **str** | Description of the plan exclusive to this subscription. This will be displayed in place of the plan name in invoices generated for this subscription. | [optional] 
**quantity** | **int** | Required quantity of the chosen addon. | [optional] 
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] 
**item_custom_fields** | [**List[ItemCustomFieldsInner]**](ItemCustomFieldsInner.md) | Custom fields for a item. | [optional] 
**price** | **float** | A value can be provided here if the per unit addon price has to be overridden for this subscription. | [optional] 
**discount** | **object** | Discount applied for the addon. | [optional] 
**total** | **object** | Total amount for the addon. | [optional] 
**tax_id** | **object** | Unique ID of the tax applied for the addon. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.retrieve_a_hosted_page_response_data_subscription_addons_inner import RetrieveAHostedPageResponseDataSubscriptionAddonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAHostedPageResponseDataSubscriptionAddonsInner from a JSON string
retrieve_a_hosted_page_response_data_subscription_addons_inner_instance = RetrieveAHostedPageResponseDataSubscriptionAddonsInner.from_json(json)
# print the JSON string representation of the object
print(RetrieveAHostedPageResponseDataSubscriptionAddonsInner.to_json())

# convert the object into a dict
retrieve_a_hosted_page_response_data_subscription_addons_inner_dict = retrieve_a_hosted_page_response_data_subscription_addons_inner_instance.to_dict()
# create an instance of RetrieveAHostedPageResponseDataSubscriptionAddonsInner from a dict
retrieve_a_hosted_page_response_data_subscription_addons_inner_from_dict = RetrieveAHostedPageResponseDataSubscriptionAddonsInner.from_dict(retrieve_a_hosted_page_response_data_subscription_addons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


