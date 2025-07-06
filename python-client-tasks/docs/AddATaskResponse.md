# AddATaskResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**task** | [**TaskResponse**](TaskResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_tasks.models.add_a_task_response import AddATaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddATaskResponse from a JSON string
add_a_task_response_instance = AddATaskResponse.from_json(json)
# print the JSON string representation of the object
print(AddATaskResponse.to_json())

# convert the object into a dict
add_a_task_response_dict = add_a_task_response_instance.to_dict()
# create an instance of AddATaskResponse from a dict
add_a_task_response_from_dict = AddATaskResponse.from_dict(add_a_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


