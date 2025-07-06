# RetrieveListOfTaxAuthoritiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**tax_authorities** | [**List[RetrieveListOfTaxAuthoritiesResponseTaxAuthoritiesInner]**](RetrieveListOfTaxAuthoritiesResponseTaxAuthoritiesInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_settings.models.retrieve_list_of_tax_authorities_response import RetrieveListOfTaxAuthoritiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveListOfTaxAuthoritiesResponse from a JSON string
retrieve_list_of_tax_authorities_response_instance = RetrieveListOfTaxAuthoritiesResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveListOfTaxAuthoritiesResponse.to_json())

# convert the object into a dict
retrieve_list_of_tax_authorities_response_dict = retrieve_list_of_tax_authorities_response_instance.to_dict()
# create an instance of RetrieveListOfTaxAuthoritiesResponse from a dict
retrieve_list_of_tax_authorities_response_from_dict = RetrieveListOfTaxAuthoritiesResponse.from_dict(retrieve_list_of_tax_authorities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


