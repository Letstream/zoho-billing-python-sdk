# MarkAsInactiveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_addons.models.mark_as_inactive_response import MarkAsInactiveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarkAsInactiveResponse from a JSON string
mark_as_inactive_response_instance = MarkAsInactiveResponse.from_json(json)
# print the JSON string representation of the object
print(MarkAsInactiveResponse.to_json())

# convert the object into a dict
mark_as_inactive_response_dict = mark_as_inactive_response_instance.to_dict()
# create an instance of MarkAsInactiveResponse from a dict
mark_as_inactive_response_from_dict = MarkAsInactiveResponse.from_dict(mark_as_inactive_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


