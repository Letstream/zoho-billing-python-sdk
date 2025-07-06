# UpdateUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | Name of the user. &lt;code&gt;Maximum length [200]&lt;/code&gt; | [optional] 
**user_role** | **str** | Role to be assigned. Allowed Values: &lt;code&gt;staff&lt;/code&gt;, &lt;code&gt;admin&lt;/code&gt; and &lt;code&gt;timesheetstaff&lt;/code&gt; | [optional] 
**rate** | **float** | Total project cost | [optional] 
**budget_hours** | **str** | Planned hours for completion of project | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.update_user_request import UpdateUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserRequest from a JSON string
update_user_request_instance = UpdateUserRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserRequest.to_json())

# convert the object into a dict
update_user_request_dict = update_user_request_instance.to_dict()
# create an instance of UpdateUserRequest from a dict
update_user_request_from_dict = UpdateUserRequest.from_dict(update_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


