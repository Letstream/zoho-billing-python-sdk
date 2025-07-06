# ListProjectsResponseProjectsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Unoque ID of the project | [optional] 
**project_name** | **str** | Name of the project. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**customer_id** | **str** | Unique ID of the customer. | [optional] 
**customer_name** | **str** | Name of the client of the project | [optional] 
**description** | **str** | Project Description - A short note on the project details | [optional] 
**status** | **str** | Project Status | [optional] 
**billing_type** | **str** | The way you bill your customer. Allowed Values: &lt;code&gt;fixed_cost_for_project&lt;/code&gt;, &lt;code&gt;based_on_project_hours&lt;/code&gt;, &lt;code&gt;based_on_staff_hours&lt;/code&gt; and &lt;code&gt;based_on_task_hours&lt;/code&gt; | [optional] 
**rate** | **float** | Total project cost | [optional] 
**created_time** | **str** | Time of project creation | [optional] 
**has_attachment** | **bool** | attached bills, receipts etc. | [optional] 
**total_hours** | **str** | Total hours spent on project | [optional] 
**billable_hours** | **str** | Hours charged for, in total project hours | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.list_projects_response_projects_inner import ListProjectsResponseProjectsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListProjectsResponseProjectsInner from a JSON string
list_projects_response_projects_inner_instance = ListProjectsResponseProjectsInner.from_json(json)
# print the JSON string representation of the object
print(ListProjectsResponseProjectsInner.to_json())

# convert the object into a dict
list_projects_response_projects_inner_dict = list_projects_response_projects_inner_instance.to_dict()
# create an instance of ListProjectsResponseProjectsInner from a dict
list_projects_response_projects_inner_from_dict = ListProjectsResponseProjectsInner.from_dict(list_projects_response_projects_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


