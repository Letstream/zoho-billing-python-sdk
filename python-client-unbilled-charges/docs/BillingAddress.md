# BillingAddress

Customer's billing address object. It contains <code>street</code>, <code>city</code>, <code>state</code>,<code>zip</code> and <code>country</code>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | **str** | Name of the street. | [optional] 
**city** | **str** | Name of the city. | [optional] 
**state** | **str** | Name of the state. | [optional] 
**zip** | **str** | Zip code of the customer&#39;s address. | [optional] 
**country** | **str** | Name of the country. | [optional] 
**fax** | **str** | Customer&#39;s fax number. | [optional] 

## Example

```python
from ls_zoho_billing_unbilled_charges.models.billing_address import BillingAddress

# TODO update the JSON string below
json = "{}"
# create an instance of BillingAddress from a JSON string
billing_address_instance = BillingAddress.from_json(json)
# print the JSON string representation of the object
print(BillingAddress.to_json())

# convert the object into a dict
billing_address_dict = billing_address_instance.to_dict()
# create an instance of BillingAddress from a dict
billing_address_from_dict = BillingAddress.from_dict(billing_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


