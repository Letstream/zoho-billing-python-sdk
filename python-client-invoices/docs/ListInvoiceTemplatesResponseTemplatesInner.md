# ListInvoiceTemplatesResponseTemplatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_name** | **str** | Name of the invoice template used | [optional] 
**template_id** | **str** | ID of the pdf template associated with the invoice. | [optional] 
**template_type** | **str** | The type of template type | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.list_invoice_templates_response_templates_inner import ListInvoiceTemplatesResponseTemplatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListInvoiceTemplatesResponseTemplatesInner from a JSON string
list_invoice_templates_response_templates_inner_instance = ListInvoiceTemplatesResponseTemplatesInner.from_json(json)
# print the JSON string representation of the object
print(ListInvoiceTemplatesResponseTemplatesInner.to_json())

# convert the object into a dict
list_invoice_templates_response_templates_inner_dict = list_invoice_templates_response_templates_inner_instance.to_dict()
# create an instance of ListInvoiceTemplatesResponseTemplatesInner from a dict
list_invoice_templates_response_templates_inner_from_dict = ListInvoiceTemplatesResponseTemplatesInner.from_dict(list_invoice_templates_response_templates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


