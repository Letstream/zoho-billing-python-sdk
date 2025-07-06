# SubscriptionResponseContactpersonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contactperson_id** | **str** | Contact person ID of the customer’s contact person. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.subscription_response_contactpersons_inner import SubscriptionResponseContactpersonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionResponseContactpersonsInner from a JSON string
subscription_response_contactpersons_inner_instance = SubscriptionResponseContactpersonsInner.from_json(json)
# print the JSON string representation of the object
print(SubscriptionResponseContactpersonsInner.to_json())

# convert the object into a dict
subscription_response_contactpersons_inner_dict = subscription_response_contactpersons_inner_instance.to_dict()
# create an instance of SubscriptionResponseContactpersonsInner from a dict
subscription_response_contactpersons_inner_from_dict = SubscriptionResponseContactpersonsInner.from_dict(subscription_response_contactpersons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


