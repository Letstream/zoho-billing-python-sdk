# CreateAProjectRequestUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | ID of the user to be added to the project. | [optional] 
**is_current_user** | **bool** |  | [optional] 
**user_name** | **str** | Name of the user. &lt;code&gt;Maximum length [200]&lt;/code&gt; | [optional] 
**email** | **str** | Email of the user. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**user_role** | **str** | Role to be assigned. Allowed Values: &lt;code&gt;staff&lt;/code&gt;, &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;timesheetstaff&lt;/code&gt; | [optional] 
**status** | **str** | Project Status | [optional] 
**rate** | **str** | Hourly rate for a task. | [optional] 
**budget_hours** | **str** | Task budget hours | [optional] 
**total_hours** | **str** | Total hours spent on project | [optional] 
**billed_hours** | **str** | Total duration/hours of a project that is billed | [optional] 
**un_billed_hours** | **str** | Hours of the project that cannot be billed | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.create_a_project_request_users_inner import CreateAProjectRequestUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAProjectRequestUsersInner from a JSON string
create_a_project_request_users_inner_instance = CreateAProjectRequestUsersInner.from_json(json)
# print the JSON string representation of the object
print(CreateAProjectRequestUsersInner.to_json())

# convert the object into a dict
create_a_project_request_users_inner_dict = create_a_project_request_users_inner_instance.to_dict()
# create an instance of CreateAProjectRequestUsersInner from a dict
create_a_project_request_users_inner_from_dict = CreateAProjectRequestUsersInner.from_dict(create_a_project_request_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


