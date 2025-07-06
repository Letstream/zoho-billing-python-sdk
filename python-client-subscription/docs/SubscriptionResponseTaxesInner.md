# SubscriptionResponseTaxesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **str** | Unique ID of the tax or tax group that can be collected from the contact. Tax can be given only if &lt;code&gt;is_taxable&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;. | [optional] 
**tax_name** | **str** | Name of the tax to which subscription is associated. | [optional] 
**tax_amount** | **str** | Tax amount applied to the subscription. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.subscription_response_taxes_inner import SubscriptionResponseTaxesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionResponseTaxesInner from a JSON string
subscription_response_taxes_inner_instance = SubscriptionResponseTaxesInner.from_json(json)
# print the JSON string representation of the object
print(SubscriptionResponseTaxesInner.to_json())

# convert the object into a dict
subscription_response_taxes_inner_dict = subscription_response_taxes_inner_instance.to_dict()
# create an instance of SubscriptionResponseTaxesInner from a dict
subscription_response_taxes_inner_from_dict = SubscriptionResponseTaxesInner.from_dict(subscription_response_taxes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


