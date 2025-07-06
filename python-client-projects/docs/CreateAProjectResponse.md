# CreateAProjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**project** | [**ProjectResponse**](ProjectResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.create_a_project_response import CreateAProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAProjectResponse from a JSON string
create_a_project_response_instance = CreateAProjectResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAProjectResponse.to_json())

# convert the object into a dict
create_a_project_response_dict = create_a_project_response_instance.to_dict()
# create an instance of CreateAProjectResponse from a dict
create_a_project_response_from_dict = CreateAProjectResponse.from_dict(create_a_project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


