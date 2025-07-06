# TaxesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default_tax** | **str** | Set to true for default taxes. | [optional] 
**is_editable** | **str** | Set to true for editable taxes. | [optional] 
**tax_authority_id** | **str** | Unique ID of the tax authority. Tax authority depends on the location of the customer. For example, if the customer is located in NY, then the tax authority is NY tax authority. | [optional] 
**tax_authority_name** | **str** | Unique name of the tax authority. Either tax_authority_id or tax_authority_name can be given. | [optional] 
**tax_id** | **str** | Unique ID of the tax or tax group that can be collected from the contact. Tax can be given only if &lt;code&gt;is_taxable&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;. | [optional] 
**tax_name** | **str** | Name of the tax to which subscription is associated. | [optional] 
**tax_percentage** | **str** | Percentage of tax. | [optional] 
**tax_type** | **str** | Specifies whether the tax is Simple tax or Tax Group. | [optional] 

## Example

```python
from ls_zoho_billing_settings.models.taxes_response import TaxesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaxesResponse from a JSON string
taxes_response_instance = TaxesResponse.from_json(json)
# print the JSON string representation of the object
print(TaxesResponse.to_json())

# convert the object into a dict
taxes_response_dict = taxes_response_instance.to_dict()
# create an instance of TaxesResponse from a dict
taxes_response_from_dict = TaxesResponse.from_dict(taxes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


