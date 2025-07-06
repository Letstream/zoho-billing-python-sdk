# RetrieveAnAddonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**addon** | [**RetrieveAnAddonResponseAddon**](RetrieveAnAddonResponseAddon.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_addons.models.retrieve_an_addon_response import RetrieveAnAddonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAnAddonResponse from a JSON string
retrieve_an_addon_response_instance = RetrieveAnAddonResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveAnAddonResponse.to_json())

# convert the object into a dict
retrieve_an_addon_response_dict = retrieve_an_addon_response_instance.to_dict()
# create an instance of RetrieveAnAddonResponse from a dict
retrieve_an_addon_response_from_dict = RetrieveAnAddonResponse.from_dict(retrieve_an_addon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


