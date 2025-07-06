# DataSubscriptionTaxesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **str** | Unique ID of the tax or tax group that can be collected from the contact. Tax can be given only if &lt;code&gt;is_taxable&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;. | [optional] 
**tax_name** | **str** | Name of the tax to which subscription is associated. | [optional] 
**tax_amount** | **str** | Tax amount applied to the subscription. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.data_subscription_taxes_inner import DataSubscriptionTaxesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataSubscriptionTaxesInner from a JSON string
data_subscription_taxes_inner_instance = DataSubscriptionTaxesInner.from_json(json)
# print the JSON string representation of the object
print(DataSubscriptionTaxesInner.to_json())

# convert the object into a dict
data_subscription_taxes_inner_dict = data_subscription_taxes_inner_instance.to_dict()
# create an instance of DataSubscriptionTaxesInner from a dict
data_subscription_taxes_inner_from_dict = DataSubscriptionTaxesInner.from_dict(data_subscription_taxes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


