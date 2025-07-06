# UpdateAProjectResponseProject

Name of the project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Unoque ID of the project | [optional] 
**project_name** | **str** | Name of the project. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**customer_id** | **str** | Unique ID of the customer. | [optional] 
**customer_name** | **str** | Name of the client of the project | [optional] 
**currency_code** | **str** | Code to denote currency | [optional] 
**description** | **str** | Project Description - A short note on the project details | [optional] 
**status** | **str** | Project Status | [optional] 
**billing_type** | **str** | The way you bill your customer. Allowed Values: &lt;code&gt;fixed_cost_for_project&lt;/code&gt;, &lt;code&gt;based_on_project_hours&lt;/code&gt;, &lt;code&gt;based_on_staff_hours&lt;/code&gt; and &lt;code&gt;based_on_task_hours&lt;/code&gt; | [optional] 
**rate** | **float** | Total project cost | [optional] 
**budget_type** | **str** | Project budject type | [optional] 
**total_hours** | **str** | Total hours spent on project | [optional] 
**total_amount** | **float** | Total cost of the project | [optional] 
**billed_hours** | **str** | Total duration/hours of a project that is billed | [optional] 
**billed_amount** | **float** | Total billable amount of the project | [optional] 
**un_billed_hours** | **str** | Hours of the project that cannot be billed | [optional] 
**un_billed_amount** | **float** | Total value of Unbilled expense of the project | [optional] 
**billable_hours** | **str** | Hours charged for, in total project hours | [optional] 
**billable_amount** | **float** | Total billed amount | [optional] 
**non_billable_hours** | **str** | Non-billable project hours | [optional] 
**non_billable_amount** | **float** | Total value of non-billable expense | [optional] 
**created_time** | **str** | Time of project creation | [optional] 
**show_in_dashboard** | **bool** | To check if dashboard view is available for project | [optional] 
**tasks** | [**List[ProjectResponseTasksInner]**](ProjectResponseTasksInner.md) | Tasks comprising a project | [optional] 
**users** | [**List[ProjectResponseUsersInner]**](ProjectResponseUsersInner.md) | Users of a project | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.update_a_project_response_project import UpdateAProjectResponseProject

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAProjectResponseProject from a JSON string
update_a_project_response_project_instance = UpdateAProjectResponseProject.from_json(json)
# print the JSON string representation of the object
print(UpdateAProjectResponseProject.to_json())

# convert the object into a dict
update_a_project_response_project_dict = update_a_project_response_project_instance.to_dict()
# create an instance of UpdateAProjectResponseProject from a dict
update_a_project_response_project_from_dict = UpdateAProjectResponseProject.from_dict(update_a_project_response_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


