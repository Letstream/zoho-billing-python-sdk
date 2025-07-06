# UpdateAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_address** | [**RetrieveAnInvoiceResponseInvoiceBillingAddress**](RetrieveAnInvoiceResponseInvoiceBillingAddress.md) |  | [optional] 
**shipping_address** | [**ShippingAddress**](ShippingAddress.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.update_address_request import UpdateAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAddressRequest from a JSON string
update_address_request_instance = UpdateAddressRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAddressRequest.to_json())

# convert the object into a dict
update_address_request_dict = update_address_request_instance.to_dict()
# create an instance of UpdateAddressRequest from a dict
update_address_request_from_dict = UpdateAddressRequest.from_dict(update_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


