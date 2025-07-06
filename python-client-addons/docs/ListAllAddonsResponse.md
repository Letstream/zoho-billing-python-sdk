# ListAllAddonsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**addons** | [**List[ListAllAddonsResponseAddonsInner]**](ListAllAddonsResponseAddonsInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_addons.models.list_all_addons_response import ListAllAddonsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllAddonsResponse from a JSON string
list_all_addons_response_instance = ListAllAddonsResponse.from_json(json)
# print the JSON string representation of the object
print(ListAllAddonsResponse.to_json())

# convert the object into a dict
list_all_addons_response_dict = list_all_addons_response_instance.to_dict()
# create an instance of ListAllAddonsResponse from a dict
list_all_addons_response_from_dict = ListAllAddonsResponse.from_dict(list_all_addons_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


