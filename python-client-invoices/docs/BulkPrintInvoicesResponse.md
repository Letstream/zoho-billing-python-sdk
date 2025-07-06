# BulkPrintInvoicesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.bulk_print_invoices_response import BulkPrintInvoicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPrintInvoicesResponse from a JSON string
bulk_print_invoices_response_instance = BulkPrintInvoicesResponse.from_json(json)
# print the JSON string representation of the object
print(BulkPrintInvoicesResponse.to_json())

# convert the object into a dict
bulk_print_invoices_response_dict = bulk_print_invoices_response_instance.to_dict()
# create an instance of BulkPrintInvoicesResponse from a dict
bulk_print_invoices_response_from_dict = BulkPrintInvoicesResponse.from_dict(bulk_print_invoices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


