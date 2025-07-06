# InviteUserResponseUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | ID of the user to be added to the project. | [optional] 
**user_name** | **str** | Name of the user. &lt;code&gt;Maximum length [200]&lt;/code&gt; | [optional] 
**email** | **str** | Email of the user. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**user_role** | **str** | Role to be assigned. Allowed Values: &lt;code&gt;staff&lt;/code&gt;, &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;timesheetstaff&lt;/code&gt; | [optional] 
**is_current_user** | **bool** |  | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.invite_user_response_users_inner import InviteUserResponseUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of InviteUserResponseUsersInner from a JSON string
invite_user_response_users_inner_instance = InviteUserResponseUsersInner.from_json(json)
# print the JSON string representation of the object
print(InviteUserResponseUsersInner.to_json())

# convert the object into a dict
invite_user_response_users_inner_dict = invite_user_response_users_inner_instance.to_dict()
# create an instance of InviteUserResponseUsersInner from a dict
invite_user_response_users_inner_from_dict = InviteUserResponseUsersInner.from_dict(invite_user_response_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


