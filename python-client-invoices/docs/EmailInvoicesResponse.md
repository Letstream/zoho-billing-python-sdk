# EmailInvoicesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.email_invoices_response import EmailInvoicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailInvoicesResponse from a JSON string
email_invoices_response_instance = EmailInvoicesResponse.from_json(json)
# print the JSON string representation of the object
print(EmailInvoicesResponse.to_json())

# convert the object into a dict
email_invoices_response_dict = email_invoices_response_instance.to_dict()
# create an instance of EmailInvoicesResponse from a dict
email_invoices_response_from_dict = EmailInvoicesResponse.from_dict(email_invoices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


