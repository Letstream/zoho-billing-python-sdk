# GetAUserResponseUsers

Users of a project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | ID of the user to be added to the project. | [optional] 
**is_current_user** | **bool** |  | [optional] 
**user_name** | **str** | Name of the user. &lt;code&gt;Maximum length [200]&lt;/code&gt; | [optional] 
**email** | **str** | Email of the user. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**user_role** | **str** | Role to be assigned. Allowed Values: &lt;code&gt;staff&lt;/code&gt;, &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;timesheetstaff&lt;/code&gt; | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.get_a_user_response_users import GetAUserResponseUsers

# TODO update the JSON string below
json = "{}"
# create an instance of GetAUserResponseUsers from a JSON string
get_a_user_response_users_instance = GetAUserResponseUsers.from_json(json)
# print the JSON string representation of the object
print(GetAUserResponseUsers.to_json())

# convert the object into a dict
get_a_user_response_users_dict = get_a_user_response_users_instance.to_dict()
# create an instance of GetAUserResponseUsers from a dict
get_a_user_response_users_from_dict = GetAUserResponseUsers.from_dict(get_a_user_response_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


