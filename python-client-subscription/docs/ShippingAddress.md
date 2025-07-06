# ShippingAddress

Customer's shipping address object. It contains <code>attention</code>, <code>street</code>, <code>city</code>, <code>state</code>,<code>zip</code>, <code>country</code> and <code>fax</code>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attention** | **str** | Attention of the customer’s shipping address. | [optional] 
**street** | **str** | Street of the customer’s shipping address. | [optional] 
**city** | **str** | City of the customer’s shipping address. | [optional] 
**state** | **str** | State of the customer’s shipping address. | [optional] 
**zip** | **str** | Zip code of the customer’s shipping address. | [optional] 
**country** | **str** | Country of the customer’s shipping address. | [optional] 
**fax** | **str** | Fax number of the customer’s shipping address. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.shipping_address import ShippingAddress

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


