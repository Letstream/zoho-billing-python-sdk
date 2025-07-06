# MarkAsActiveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_plans.models.mark_as_active_response import MarkAsActiveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarkAsActiveResponse from a JSON string
mark_as_active_response_instance = MarkAsActiveResponse.from_json(json)
# print the JSON string representation of the object
print(MarkAsActiveResponse.to_json())

# convert the object into a dict
mark_as_active_response_dict = mark_as_active_response_instance.to_dict()
# create an instance of MarkAsActiveResponse from a dict
mark_as_active_response_from_dict = MarkAsActiveResponse.from_dict(mark_as_active_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


