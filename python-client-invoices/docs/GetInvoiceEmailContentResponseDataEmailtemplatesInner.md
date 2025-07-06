# GetInvoiceEmailContentResponseDataEmailtemplatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected** | **bool** | To check if invoice is selected | [optional] 
**name** | **str** | name of te invoice | [optional] 
**email_template_id** | **str** | ID of the email template used | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.get_invoice_email_content_response_data_emailtemplates_inner import GetInvoiceEmailContentResponseDataEmailtemplatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceEmailContentResponseDataEmailtemplatesInner from a JSON string
get_invoice_email_content_response_data_emailtemplates_inner_instance = GetInvoiceEmailContentResponseDataEmailtemplatesInner.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceEmailContentResponseDataEmailtemplatesInner.to_json())

# convert the object into a dict
get_invoice_email_content_response_data_emailtemplates_inner_dict = get_invoice_email_content_response_data_emailtemplates_inner_instance.to_dict()
# create an instance of GetInvoiceEmailContentResponseDataEmailtemplatesInner from a dict
get_invoice_email_content_response_data_emailtemplates_inner_from_dict = GetInvoiceEmailContentResponseDataEmailtemplatesInner.from_dict(get_invoice_email_content_response_data_emailtemplates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


