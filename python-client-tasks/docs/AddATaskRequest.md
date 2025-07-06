# AddATaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_name** | **str** | The name of the task. &lt;code&gt;Maximum length [100]&lt;/code&gt; | 
**description** | **str** | The description of the project. | [optional] 
**rate** | **int** | Hourly rate for a task. | [optional] 
**budget_hours** | **int** | Task budget hours. | [optional] 

## Example

```python
from ls_zoho_billing_tasks.models.add_a_task_request import AddATaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddATaskRequest from a JSON string
add_a_task_request_instance = AddATaskRequest.from_json(json)
# print the JSON string representation of the object
print(AddATaskRequest.to_json())

# convert the object into a dict
add_a_task_request_dict = add_a_task_request_instance.to_dict()
# create an instance of AddATaskRequest from a dict
add_a_task_request_from_dict = AddATaskRequest.from_dict(add_a_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


