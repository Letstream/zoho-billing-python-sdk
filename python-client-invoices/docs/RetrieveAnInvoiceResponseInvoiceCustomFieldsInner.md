# RetrieveAnInvoiceResponseInvoiceCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index of the custom field. It can hold any value from 1 to 10. | [optional] 
**label** | **str** | Label of the Custom Field | [optional] 
**value** | **str** | Value of the Custom Field | [optional] 
**data_type** | **str** | Data type of the custom field. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.retrieve_an_invoice_response_invoice_custom_fields_inner import RetrieveAnInvoiceResponseInvoiceCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAnInvoiceResponseInvoiceCustomFieldsInner from a JSON string
retrieve_an_invoice_response_invoice_custom_fields_inner_instance = RetrieveAnInvoiceResponseInvoiceCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(RetrieveAnInvoiceResponseInvoiceCustomFieldsInner.to_json())

# convert the object into a dict
retrieve_an_invoice_response_invoice_custom_fields_inner_dict = retrieve_an_invoice_response_invoice_custom_fields_inner_instance.to_dict()
# create an instance of RetrieveAnInvoiceResponseInvoiceCustomFieldsInner from a dict
retrieve_an_invoice_response_invoice_custom_fields_inner_from_dict = RetrieveAnInvoiceResponseInvoiceCustomFieldsInner.from_dict(retrieve_an_invoice_response_invoice_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


