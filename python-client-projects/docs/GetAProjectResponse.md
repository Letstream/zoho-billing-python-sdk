# GetAProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**project** | [**GetAProjectResponseProject**](GetAProjectResponseProject.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.get_a_project_response import GetAProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAProjectResponse from a JSON string
get_a_project_response_instance = GetAProjectResponse.from_json(json)
# print the JSON string representation of the object
print(GetAProjectResponse.to_json())

# convert the object into a dict
get_a_project_response_dict = get_a_project_response_instance.to_dict()
# create an instance of GetAProjectResponse from a dict
get_a_project_response_from_dict = GetAProjectResponse.from_dict(get_a_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


