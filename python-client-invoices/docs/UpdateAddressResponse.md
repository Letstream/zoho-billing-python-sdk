# UpdateAddressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**invoice_address** | [**UpdateAddressResponseInvoiceAddress**](UpdateAddressResponseInvoiceAddress.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.update_address_response import UpdateAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAddressResponse from a JSON string
update_address_response_instance = UpdateAddressResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAddressResponse.to_json())

# convert the object into a dict
update_address_response_dict = update_address_response_instance.to_dict()
# create an instance of UpdateAddressResponse from a dict
update_address_response_from_dict = UpdateAddressResponse.from_dict(update_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


