# UpdateATaskResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**task** | [**ListTasksResponseTasksInner**](ListTasksResponseTasksInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_tasks.models.update_a_task_response import UpdateATaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateATaskResponse from a JSON string
update_a_task_response_instance = UpdateATaskResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateATaskResponse.to_json())

# convert the object into a dict
update_a_task_response_dict = update_a_task_response_instance.to_dict()
# create an instance of UpdateATaskResponse from a dict
update_a_task_response_from_dict = UpdateATaskResponse.from_dict(update_a_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


