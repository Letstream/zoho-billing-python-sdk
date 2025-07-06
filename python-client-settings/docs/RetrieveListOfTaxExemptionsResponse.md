# RetrieveListOfTaxExemptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**tax_exemptions** | [**List[RetrieveListOfTaxExemptionsResponseTaxExemptionsInner]**](RetrieveListOfTaxExemptionsResponseTaxExemptionsInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_settings.models.retrieve_list_of_tax_exemptions_response import RetrieveListOfTaxExemptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveListOfTaxExemptionsResponse from a JSON string
retrieve_list_of_tax_exemptions_response_instance = RetrieveListOfTaxExemptionsResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveListOfTaxExemptionsResponse.to_json())

# convert the object into a dict
retrieve_list_of_tax_exemptions_response_dict = retrieve_list_of_tax_exemptions_response_instance.to_dict()
# create an instance of RetrieveListOfTaxExemptionsResponse from a dict
retrieve_list_of_tax_exemptions_response_from_dict = RetrieveListOfTaxExemptionsResponse.from_dict(retrieve_list_of_tax_exemptions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


