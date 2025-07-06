# RetrieveListOfTaxAuthoritiesResponseTaxAuthoritiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Appropriate description for teh tax exemption. | [optional] 
**tax_authority_id** | **str** | Unique ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority. | [optional] 
**tax_authority_name** | **str** | Unique name of the tax authority. Either tax_authority_id or tax_authority_name can be given. | [optional] 

## Example

```python
from ls_zoho_billing_settings.models.retrieve_list_of_tax_authorities_response_tax_authorities_inner import RetrieveListOfTaxAuthoritiesResponseTaxAuthoritiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveListOfTaxAuthoritiesResponseTaxAuthoritiesInner from a JSON string
retrieve_list_of_tax_authorities_response_tax_authorities_inner_instance = RetrieveListOfTaxAuthoritiesResponseTaxAuthoritiesInner.from_json(json)
# print the JSON string representation of the object
print(RetrieveListOfTaxAuthoritiesResponseTaxAuthoritiesInner.to_json())

# convert the object into a dict
retrieve_list_of_tax_authorities_response_tax_authorities_inner_dict = retrieve_list_of_tax_authorities_response_tax_authorities_inner_instance.to_dict()
# create an instance of RetrieveListOfTaxAuthoritiesResponseTaxAuthoritiesInner from a dict
retrieve_list_of_tax_authorities_response_tax_authorities_inner_from_dict = RetrieveListOfTaxAuthoritiesResponseTaxAuthoritiesInner.from_dict(retrieve_list_of_tax_authorities_response_tax_authorities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


