# ShippingAddress

Customer’s shipping address object. It contains <code>attention</code>,<code>street</code>, <code>city</code>, <code>state</code>,<code>zip</code>,<code>country</code>, <code>state_code</code> and <code>fax</code>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attention** | **str** | Attention of the customer’s shipping address. | [optional] 
**street** | **str** | Name of the street of the customer’s shipping address. | [optional] 
**city** | **str** | Name of the city of the customer’s shipping address. | [optional] 
**state** | **str** | Name of the state of the customer’s shipping address. | [optional] 
**zip** | **str** | Zip code of the customer’s shipping address. | [optional] 
**country** | **str** | Country name of the customer’s shipping address. | [optional] 
**state_code** | **str** | State Code of the customer&#39;s shipping address. Find their region&#39;s code &lt;a href&#x3D;\&quot;#state-codes\&quot;&gt;here&lt;/a&gt; | [optional] 
**fax** | **str** | Fax number of the customer’s shipping address. | [optional] 

## Example

```python
from ls_zoho_billing_customers.models.shipping_address import ShippingAddress

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


