# DeleteAnAddonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.delete_an_addon_response import DeleteAnAddonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAnAddonResponse from a JSON string
delete_an_addon_response_instance = DeleteAnAddonResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteAnAddonResponse.to_json())

# convert the object into a dict
delete_an_addon_response_dict = delete_an_addon_response_instance.to_dict()
# create an instance of DeleteAnAddonResponse from a dict
delete_an_addon_response_from_dict = DeleteAnAddonResponse.from_dict(delete_an_addon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


