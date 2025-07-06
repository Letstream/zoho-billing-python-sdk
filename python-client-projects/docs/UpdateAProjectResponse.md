# UpdateAProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**project** | [**UpdateAProjectResponseProject**](UpdateAProjectResponseProject.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.update_a_project_response import UpdateAProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAProjectResponse from a JSON string
update_a_project_response_instance = UpdateAProjectResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAProjectResponse.to_json())

# convert the object into a dict
update_a_project_response_dict = update_a_project_response_instance.to_dict()
# create an instance of UpdateAProjectResponse from a dict
update_a_project_response_from_dict = UpdateAProjectResponse.from_dict(update_a_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


