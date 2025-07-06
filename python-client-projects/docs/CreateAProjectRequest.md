# CreateAProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_name** | **str** | Name of the project. &lt;code&gt;Maximum length [100]&lt;/code&gt; | 
**customer_id** | **str** | ID of the customer. | 
**description** | **str** | Project description. &lt;code&gt;Maximu length [500]&lt;/code&gt; | [optional] 
**billing_type** | **str** | The way you bill your customer. Allowed Values: &lt;code&gt;fixed_cost_for_project&lt;/code&gt;, &lt;code&gt;based_on_project_hours&lt;/code&gt;, &lt;code&gt;based_on_staff_hours&lt;/code&gt; and &lt;code&gt;based_on_task_hours&lt;/code&gt; | 
**rate** | **str** | Rate of the Project. &lt;br&gt;Mandatory for projects whose billing_type is either &lt;code&gt;fixed_cost_for_project&lt;/code&gt; or &lt;code&gt;based_on_project_hours&lt;/code&gt; | [optional] 
**budget_type** | **str** | The way you budget. Allowed Values: &lt;code&gt;total_project_cost&lt;/code&gt;, &lt;code&gt;total_project_hours&lt;/code&gt;, &lt;code&gt;hours_per_task&lt;/code&gt; and &lt;code&gt;hours_per_staff&lt;/code&gt; | [optional] 
**budget_hours** | **str** | Task budget hours | [optional] 
**budget_amount** | **str** | Give value, if you are estimating total project cost. | [optional] 
**tasks** | [**List[CreateAProjectRequestTasksInner]**](CreateAProjectRequestTasksInner.md) | Tasks comprising a project | [optional] 
**users** | [**List[CreateAProjectRequestUsersInner]**](CreateAProjectRequestUsersInner.md) | Users of a project | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.create_a_project_request import CreateAProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAProjectRequest from a JSON string
create_a_project_request_instance = CreateAProjectRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAProjectRequest.to_json())

# convert the object into a dict
create_a_project_request_dict = create_a_project_request_instance.to_dict()
# create an instance of CreateAProjectRequest from a dict
create_a_project_request_from_dict = CreateAProjectRequest.from_dict(create_a_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


