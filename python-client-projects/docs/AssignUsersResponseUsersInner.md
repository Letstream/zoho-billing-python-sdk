# AssignUsersResponseUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | ID of the user to be added to the project. | [optional] 
**is_current_user** | **bool** |  | [optional] 
**user_name** | **str** | Name of the user. &lt;code&gt;Maximum length [200]&lt;/code&gt; | [optional] 
**email** | **str** | Email of the user. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**user_role** | **str** | Role to be assigned. Allowed Values: &lt;code&gt;staff&lt;/code&gt;, &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;timesheetstaff&lt;/code&gt; | [optional] 
**status** | **str** | Project Status | [optional] 
**rate** | **float** | Total project cost | [optional] 
**budget_hours** | **str** | Planned hours for completion of project | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.assign_users_response_users_inner import AssignUsersResponseUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of AssignUsersResponseUsersInner from a JSON string
assign_users_response_users_inner_instance = AssignUsersResponseUsersInner.from_json(json)
# print the JSON string representation of the object
print(AssignUsersResponseUsersInner.to_json())

# convert the object into a dict
assign_users_response_users_inner_dict = assign_users_response_users_inner_instance.to_dict()
# create an instance of AssignUsersResponseUsersInner from a dict
assign_users_response_users_inner_from_dict = AssignUsersResponseUsersInner.from_dict(assign_users_response_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


