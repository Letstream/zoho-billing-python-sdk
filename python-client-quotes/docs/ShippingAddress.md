# ShippingAddress

The shipping address of the customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Billing address for the quote | [optional] 
**city** | **str** | City of the customer’s billing address. | [optional] 
**state** | **str** | State of the customer’s billing address. | [optional] 
**zip** | **str** | Zip code of the customer’s billing address. | [optional] 
**country** | **str** | Country of the customer’s billing address. | [optional] 
**fax** | **str** | Customer&#39;s fax number. | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.shipping_address import ShippingAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingAddress from a JSON string
shipping_address_instance = ShippingAddress.from_json(json)
# print the JSON string representation of the object
print(ShippingAddress.to_json())

# convert the object into a dict
shipping_address_dict = shipping_address_instance.to_dict()
# create an instance of ShippingAddress from a dict
shipping_address_from_dict = ShippingAddress.from_dict(shipping_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


