# UpdateAddressResponseInvoiceAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_address** | [**RetrieveAnInvoiceResponseInvoiceBillingAddress**](RetrieveAnInvoiceResponseInvoiceBillingAddress.md) |  | [optional] 
**shipping_address** | [**ShippingAddress**](ShippingAddress.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.update_address_response_invoice_address import UpdateAddressResponseInvoiceAddress

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAddressResponseInvoiceAddress from a JSON string
update_address_response_invoice_address_instance = UpdateAddressResponseInvoiceAddress.from_json(json)
# print the JSON string representation of the object
print(UpdateAddressResponseInvoiceAddress.to_json())

# convert the object into a dict
update_address_response_invoice_address_dict = update_address_response_invoice_address_instance.to_dict()
# create an instance of UpdateAddressResponseInvoiceAddress from a dict
update_address_response_invoice_address_from_dict = UpdateAddressResponseInvoiceAddress.from_dict(update_address_response_invoice_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


