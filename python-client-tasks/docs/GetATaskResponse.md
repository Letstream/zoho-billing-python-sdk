# GetATaskResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**task** | [**GetATaskResponseTask**](GetATaskResponseTask.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_tasks.models.get_a_task_response import GetATaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetATaskResponse from a JSON string
get_a_task_response_instance = GetATaskResponse.from_json(json)
# print the JSON string representation of the object
print(GetATaskResponse.to_json())

# convert the object into a dict
get_a_task_response_dict = get_a_task_response_instance.to_dict()
# create an instance of GetATaskResponse from a dict
get_a_task_response_from_dict = GetATaskResponse.from_dict(get_a_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


