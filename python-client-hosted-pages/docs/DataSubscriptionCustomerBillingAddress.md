# DataSubscriptionCustomerBillingAddress

Customer's billing address object. It contains <code>attention</code>, <code>street</code>, <code>city</code>, <code>state</code>, <code>zip</code>, <code>country</code> and <code>fax</code>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | **str** | Street of the customer’s billing address. | [optional] 
**city** | **str** | City of the customer’s billing address. | [optional] 
**state** | **str** | State of the customer’s billing address. | [optional] 
**country** | **str** | Country of the customer’s billing address. | [optional] 
**zip** | **str** | Zip code of the customer’s billing address. | [optional] 
**fax** | **str** | Fax number of the customer&#39;s billing address. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.data_subscription_customer_billing_address import DataSubscriptionCustomerBillingAddress

# TODO update the JSON string below
json = "{}"
# create an instance of DataSubscriptionCustomerBillingAddress from a JSON string
data_subscription_customer_billing_address_instance = DataSubscriptionCustomerBillingAddress.from_json(json)
# print the JSON string representation of the object
print(DataSubscriptionCustomerBillingAddress.to_json())

# convert the object into a dict
data_subscription_customer_billing_address_dict = data_subscription_customer_billing_address_instance.to_dict()
# create an instance of DataSubscriptionCustomerBillingAddress from a dict
data_subscription_customer_billing_address_from_dict = DataSubscriptionCustomerBillingAddress.from_dict(data_subscription_customer_billing_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


