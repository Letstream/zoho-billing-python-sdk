# UpdateReferenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_id** | **object** | A string of your choice is required to easily identify and keep track of your subscriptions. | 

## Example

```python
from ls_zoho_billing_subscription.models.update_reference_request import UpdateReferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateReferenceRequest from a JSON string
update_reference_request_instance = UpdateReferenceRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateReferenceRequest.to_json())

# convert the object into a dict
update_reference_request_dict = update_reference_request_instance.to_dict()
# create an instance of UpdateReferenceRequest from a dict
update_reference_request_from_dict = UpdateReferenceRequest.from_dict(update_reference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


