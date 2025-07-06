# RetrieveListOfTaxesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**taxes** | [**List[TaxesResponse]**](TaxesResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_settings.models.retrieve_list_of_taxes_response import RetrieveListOfTaxesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveListOfTaxesResponse from a JSON string
retrieve_list_of_taxes_response_instance = RetrieveListOfTaxesResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveListOfTaxesResponse.to_json())

# convert the object into a dict
retrieve_list_of_taxes_response_dict = retrieve_list_of_taxes_response_instance.to_dict()
# create an instance of RetrieveListOfTaxesResponse from a dict
retrieve_list_of_taxes_response_from_dict = RetrieveListOfTaxesResponse.from_dict(retrieve_list_of_taxes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


