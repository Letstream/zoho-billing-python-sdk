# CreateAProjectRequestTasksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_name** | **str** | Name of the task. &lt;code&gt;Maximum length [100]&lt;/code&gt; | 
**description** | **str** | Task description. &lt;code&gt;Maximum length [500]&lt;/code&gt; | [optional] 
**rate** | **str** | Hourly rate of a task. | [optional] 
**budget_hours** | **str** | Task budgeting. | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.create_a_project_request_tasks_inner import CreateAProjectRequestTasksInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAProjectRequestTasksInner from a JSON string
create_a_project_request_tasks_inner_instance = CreateAProjectRequestTasksInner.from_json(json)
# print the JSON string representation of the object
print(CreateAProjectRequestTasksInner.to_json())

# convert the object into a dict
create_a_project_request_tasks_inner_dict = create_a_project_request_tasks_inner_instance.to_dict()
# create an instance of CreateAProjectRequestTasksInner from a dict
create_a_project_request_tasks_inner_from_dict = CreateAProjectRequestTasksInner.from_dict(create_a_project_request_tasks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


