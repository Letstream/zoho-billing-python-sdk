# UpdateASubscriptionResponseSubscriptionCustomer

Customer object of the customer for whom you want to create a subscription. Each object contains <code>display_name</code>, <code>company_name</code>, <code>first_name</code>, <code>last_name</code>, <code>email</code>, <code>fax</code>, <code>currency_code</code> and <code>billing_address</code>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | This will be name which will be displayed in the interface and invoices. | [optional] 
**salutation** | **str** | Salutation of the customer. | [optional] 
**first_name** | **str** | First name of the customer. | [optional] 
**last_name** | **str** | Last name of the customer. | [optional] 
**email** | **str** | Email address of the customer. | [optional] 
**company_name** | **str** | Registered name of the company the customer represents. | [optional] 
**billing_address** | [**BillingAddress**](BillingAddress.md) |  | [optional] 
**shipping_address** | [**ShippingAddress**](ShippingAddress.md) |  | [optional] 
**payment_terms** | **int** | Payment Due details for the invoices. | [optional] 
**payment_terms_label** | **str** | Label for the paymet due details. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.update_a_subscription_response_subscription_customer import UpdateASubscriptionResponseSubscriptionCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateASubscriptionResponseSubscriptionCustomer from a JSON string
update_a_subscription_response_subscription_customer_instance = UpdateASubscriptionResponseSubscriptionCustomer.from_json(json)
# print the JSON string representation of the object
print(UpdateASubscriptionResponseSubscriptionCustomer.to_json())

# convert the object into a dict
update_a_subscription_response_subscription_customer_dict = update_a_subscription_response_subscription_customer_instance.to_dict()
# create an instance of UpdateASubscriptionResponseSubscriptionCustomer from a dict
update_a_subscription_response_subscription_customer_from_dict = UpdateASubscriptionResponseSubscriptionCustomer.from_dict(update_a_subscription_response_subscription_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


