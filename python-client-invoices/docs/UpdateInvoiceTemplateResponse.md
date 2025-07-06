# UpdateInvoiceTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.update_invoice_template_response import UpdateInvoiceTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInvoiceTemplateResponse from a JSON string
update_invoice_template_response_instance = UpdateInvoiceTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateInvoiceTemplateResponse.to_json())

# convert the object into a dict
update_invoice_template_response_dict = update_invoice_template_response_instance.to_dict()
# create an instance of UpdateInvoiceTemplateResponse from a dict
update_invoice_template_response_from_dict = UpdateInvoiceTemplateResponse.from_dict(update_invoice_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


