# TaxesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **str** | Tax ID applied | [optional] 
**tax_amount** | **float** | total expense amount | [optional] 

## Example

```python
from ls_zoho_billing_expenses.models.taxes_inner import TaxesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TaxesInner from a JSON string
taxes_inner_instance = TaxesInner.from_json(json)
# print the JSON string representation of the object
print(TaxesInner.to_json())

# convert the object into a dict
taxes_inner_dict = taxes_inner_instance.to_dict()
# create an instance of TaxesInner from a dict
taxes_inner_from_dict = TaxesInner.from_dict(taxes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


