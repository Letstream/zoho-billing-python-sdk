# CloneAProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_name** | **str** | Name of the project. &lt;code&gt;Maximum length [100]&lt;/code&gt; | 
**description** | **str** | Project description. &lt;code&gt;Maximum length [500]&lt;/code&gt; | [optional] 

## Example

```python
from ls_zoho_billing_projects.models.clone_a_project_request import CloneAProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloneAProjectRequest from a JSON string
clone_a_project_request_instance = CloneAProjectRequest.from_json(json)
# print the JSON string representation of the object
print(CloneAProjectRequest.to_json())

# convert the object into a dict
clone_a_project_request_dict = clone_a_project_request_instance.to_dict()
# create an instance of CloneAProjectRequest from a dict
clone_a_project_request_from_dict = CloneAProjectRequest.from_dict(clone_a_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


