# ProjectResponseTasksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | ID of the task(s) performed in a project | [optional] 
**task_name** | **str** | Name of the task performed in a project | [optional] 
**description** | **str** | Project Description - A short note on the project details | [optional] 
**rate** | **float** | Total project cost | [optional] 
**budget_hours** | **str** | Planned hours for completion of project | [optional] 
**total_hours** | **str** | Total hours spent on project | [optional] 
**billed_hours** | **str** | Total duration/hours of a project that is billed | [optional] 
**un_billed_hours** | **str** | Hours of the project that cannot be billed | [optional] 
**non_billable_hours** | **str** | Non-billable project hours | [optional] 
**status** | **str** | Project Status | [optional] 
**is_billable** | **bool** | Boolean to check if a task or expense is billable in a project | [optional] 
**task_custom_fields** | **str** | Additional fields to describe task | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.project_response_tasks_inner import ProjectResponseTasksInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResponseTasksInner from a JSON string
project_response_tasks_inner_instance = ProjectResponseTasksInner.from_json(json)
# print the JSON string representation of the object
print(ProjectResponseTasksInner.to_json())

# convert the object into a dict
project_response_tasks_inner_dict = project_response_tasks_inner_instance.to_dict()
# create an instance of ProjectResponseTasksInner from a dict
project_response_tasks_inner_from_dict = ProjectResponseTasksInner.from_dict(project_response_tasks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


