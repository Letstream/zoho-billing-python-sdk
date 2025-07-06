# InviteUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | Name of the user. &lt;code&gt;Maximum length [200]&lt;/code&gt; | 
**email** | **str** | Email of the user. &lt;code&gt;Maximum length [100]&lt;/code&gt; | 
**user_role** | **str** | Role to be assigned. Allowed Values: &lt;code&gt;staff&lt;/code&gt;, &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;timesheetstaff&lt;/code&gt; | [optional] 
**rate** | **str** | Hourly rate for a task. | [optional] 
**budget_hours** | **str** | Planned hours for completion of project | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.invite_user_request import InviteUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InviteUserRequest from a JSON string
invite_user_request_instance = InviteUserRequest.from_json(json)
# print the JSON string representation of the object
print(InviteUserRequest.to_json())

# convert the object into a dict
invite_user_request_dict = invite_user_request_instance.to_dict()
# create an instance of InviteUserRequest from a dict
invite_user_request_from_dict = InviteUserRequest.from_dict(invite_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


