# PostponeRenewalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**renewal_at** | **str** | Enter the future date to which the subscription renewal has to be postponed. | 

## Example

```python
from ls_zoho_billing_subscription.models.postpone_renewal_request import PostponeRenewalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostponeRenewalRequest from a JSON string
postpone_renewal_request_instance = PostponeRenewalRequest.from_json(json)
# print the JSON string representation of the object
print(PostponeRenewalRequest.to_json())

# convert the object into a dict
postpone_renewal_request_dict = postpone_renewal_request_instance.to_dict()
# create an instance of PostponeRenewalRequest from a dict
postpone_renewal_request_from_dict = PostponeRenewalRequest.from_dict(postpone_renewal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


