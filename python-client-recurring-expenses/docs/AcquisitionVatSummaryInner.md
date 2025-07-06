# AcquisitionVatSummaryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_name** | **str** | Name of the tax | [optional] 
**tax_amount** | **float** | Total value of tax applied | [optional] 

## Example

```python
from ls_zoho_billing_recurring_expenses.models.acquisition_vat_summary_inner import AcquisitionVatSummaryInner

# TODO update the JSON string below
json = "{}"
# create an instance of AcquisitionVatSummaryInner from a JSON string
acquisition_vat_summary_inner_instance = AcquisitionVatSummaryInner.from_json(json)
# print the JSON string representation of the object
print(AcquisitionVatSummaryInner.to_json())

# convert the object into a dict
acquisition_vat_summary_inner_dict = acquisition_vat_summary_inner_instance.to_dict()
# create an instance of AcquisitionVatSummaryInner from a dict
acquisition_vat_summary_inner_from_dict = AcquisitionVatSummaryInner.from_dict(acquisition_vat_summary_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


