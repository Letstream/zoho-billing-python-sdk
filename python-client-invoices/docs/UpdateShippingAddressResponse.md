# UpdateShippingAddressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.update_shipping_address_response import UpdateShippingAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShippingAddressResponse from a JSON string
update_shipping_address_response_instance = UpdateShippingAddressResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateShippingAddressResponse.to_json())

# convert the object into a dict
update_shipping_address_response_dict = update_shipping_address_response_instance.to_dict()
# create an instance of UpdateShippingAddressResponse from a dict
update_shipping_address_response_from_dict = UpdateShippingAddressResponse.from_dict(update_shipping_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


