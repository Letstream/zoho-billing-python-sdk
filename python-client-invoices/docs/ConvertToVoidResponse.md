# ConvertToVoidResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.convert_to_void_response import ConvertToVoidResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertToVoidResponse from a JSON string
convert_to_void_response_instance = ConvertToVoidResponse.from_json(json)
# print the JSON string representation of the object
print(ConvertToVoidResponse.to_json())

# convert the object into a dict
convert_to_void_response_dict = convert_to_void_response_instance.to_dict()
# create an instance of ConvertToVoidResponse from a dict
convert_to_void_response_from_dict = ConvertToVoidResponse.from_dict(convert_to_void_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


