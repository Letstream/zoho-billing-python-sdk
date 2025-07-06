# ListInvoiceTemplatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**templates** | [**List[ListInvoiceTemplatesResponseTemplatesInner]**](ListInvoiceTemplatesResponseTemplatesInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.list_invoice_templates_response import ListInvoiceTemplatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListInvoiceTemplatesResponse from a JSON string
list_invoice_templates_response_instance = ListInvoiceTemplatesResponse.from_json(json)
# print the JSON string representation of the object
print(ListInvoiceTemplatesResponse.to_json())

# convert the object into a dict
list_invoice_templates_response_dict = list_invoice_templates_response_instance.to_dict()
# create an instance of ListInvoiceTemplatesResponse from a dict
list_invoice_templates_response_from_dict = ListInvoiceTemplatesResponse.from_dict(list_invoice_templates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


