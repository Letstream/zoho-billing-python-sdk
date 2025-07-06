# UpdateAnAddonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**addon** | [**UpdateAnAddonResponseAddon**](UpdateAnAddonResponseAddon.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_an_addon_response import UpdateAnAddonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnAddonResponse from a JSON string
update_an_addon_response_instance = UpdateAnAddonResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAnAddonResponse.to_json())

# convert the object into a dict
update_an_addon_response_dict = update_an_addon_response_instance.to_dict()
# create an instance of UpdateAnAddonResponse from a dict
update_an_addon_response_from_dict = UpdateAnAddonResponse.from_dict(update_an_addon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


