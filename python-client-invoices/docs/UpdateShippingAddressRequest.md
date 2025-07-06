# UpdateShippingAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Shipping address of the customer | [optional] 
**city** | **str** | City of the contact&#39;s shipping address | [optional] 
**state** | **str** | State of the Contact&#39;s shipping address | [optional] 
**zip** | **str** | ZIP code of the contact&#39;s shipping address | [optional] 
**country** | **str** | Contact&#39;s country for the given shipping address | [optional] 
**fax** | **str** | FAX number of the contact | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.update_shipping_address_request import UpdateShippingAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShippingAddressRequest from a JSON string
update_shipping_address_request_instance = UpdateShippingAddressRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateShippingAddressRequest.to_json())

# convert the object into a dict
update_shipping_address_request_dict = update_shipping_address_request_instance.to_dict()
# create an instance of UpdateShippingAddressRequest from a dict
update_shipping_address_request_from_dict = UpdateShippingAddressRequest.from_dict(update_shipping_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


