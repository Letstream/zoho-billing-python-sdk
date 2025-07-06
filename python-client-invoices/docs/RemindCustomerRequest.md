# RemindCustomerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_mail_ids** | **List[str]** | The email IDs to which the invoice is to be mailed. | [optional] 
**cc_mail_ids** | **List[str]** | The email IDs that have to be copied when the credit note is to be mailed. | 
**subject** | **str** | The subject of the email. | [optional] 
**body** | **str** | content of the email | [optional] 
**send_from_org_email_id** | **bool** | Boolean to trigger the email from the organization&#39;s email address | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.remind_customer_request import RemindCustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemindCustomerRequest from a JSON string
remind_customer_request_instance = RemindCustomerRequest.from_json(json)
# print the JSON string representation of the object
print(RemindCustomerRequest.to_json())

# convert the object into a dict
remind_customer_request_dict = remind_customer_request_instance.to_dict()
# create an instance of RemindCustomerRequest from a dict
remind_customer_request_from_dict = RemindCustomerRequest.from_dict(remind_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


