# GetInvoiceEmailContentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**data** | [**GetInvoiceEmailContentResponseData**](GetInvoiceEmailContentResponseData.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.get_invoice_email_content_response import GetInvoiceEmailContentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoiceEmailContentResponse from a JSON string
get_invoice_email_content_response_instance = GetInvoiceEmailContentResponse.from_json(json)
# print the JSON string representation of the object
print(GetInvoiceEmailContentResponse.to_json())

# convert the object into a dict
get_invoice_email_content_response_dict = get_invoice_email_content_response_instance.to_dict()
# create an instance of GetInvoiceEmailContentResponse from a dict
get_invoice_email_content_response_from_dict = GetInvoiceEmailContentResponse.from_dict(get_invoice_email_content_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


