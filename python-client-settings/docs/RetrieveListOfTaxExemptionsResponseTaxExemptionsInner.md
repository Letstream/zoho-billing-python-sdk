# RetrieveListOfTaxExemptionsResponseTaxExemptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Appropriate description for teh tax exemption. | [optional] 
**tax_exemption_id** | **str** | Unique ID of the tax exemption. | [optional] 
**tax_exemption_code** | **str** | Unique code of the tax exemption. | [optional] 
**type** | **str** | Tax exemption can be of customer or item type. | [optional] 

## Example

```python
from ls_zoho_billing_settings.models.retrieve_list_of_tax_exemptions_response_tax_exemptions_inner import RetrieveListOfTaxExemptionsResponseTaxExemptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveListOfTaxExemptionsResponseTaxExemptionsInner from a JSON string
retrieve_list_of_tax_exemptions_response_tax_exemptions_inner_instance = RetrieveListOfTaxExemptionsResponseTaxExemptionsInner.from_json(json)
# print the JSON string representation of the object
print(RetrieveListOfTaxExemptionsResponseTaxExemptionsInner.to_json())

# convert the object into a dict
retrieve_list_of_tax_exemptions_response_tax_exemptions_inner_dict = retrieve_list_of_tax_exemptions_response_tax_exemptions_inner_instance.to_dict()
# create an instance of RetrieveListOfTaxExemptionsResponseTaxExemptionsInner from a dict
retrieve_list_of_tax_exemptions_response_tax_exemptions_inner_from_dict = RetrieveListOfTaxExemptionsResponseTaxExemptionsInner.from_dict(retrieve_list_of_tax_exemptions_response_tax_exemptions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


