# CreateAnAddonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**addon** | [**AddonResponse**](AddonResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_an_addon_response import CreateAnAddonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnAddonResponse from a JSON string
create_an_addon_response_instance = CreateAnAddonResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAnAddonResponse.to_json())

# convert the object into a dict
create_an_addon_response_dict = create_an_addon_response_instance.to_dict()
# create an instance of CreateAnAddonResponse from a dict
create_an_addon_response_from_dict = CreateAnAddonResponse.from_dict(create_an_addon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


