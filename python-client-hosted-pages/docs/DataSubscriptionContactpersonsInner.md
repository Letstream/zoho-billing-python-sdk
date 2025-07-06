# DataSubscriptionContactpersonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contactperson_id** | **str** | Contact person ID of the customer’s contact person. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.data_subscription_contactpersons_inner import DataSubscriptionContactpersonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataSubscriptionContactpersonsInner from a JSON string
data_subscription_contactpersons_inner_instance = DataSubscriptionContactpersonsInner.from_json(json)
# print the JSON string representation of the object
print(DataSubscriptionContactpersonsInner.to_json())

# convert the object into a dict
data_subscription_contactpersons_inner_dict = data_subscription_contactpersons_inner_instance.to_dict()
# create an instance of DataSubscriptionContactpersonsInner from a dict
data_subscription_contactpersons_inner_from_dict = DataSubscriptionContactpersonsInner.from_dict(data_subscription_contactpersons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


