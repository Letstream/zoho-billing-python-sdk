# UpdateCardForASubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | Unique ID generated for a subscription. | 
**redirect_url** | **str** | It specifies the url to which the customer will be redirected after successful transaction. | [optional] 
**payment_gateways** | [**List[PaymentGatewaysInner]**](PaymentGatewaysInner.md) | List of payment gateways configured for the customer. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.update_card_for_a_subscription_request import UpdateCardForASubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCardForASubscriptionRequest from a JSON string
update_card_for_a_subscription_request_instance = UpdateCardForASubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCardForASubscriptionRequest.to_json())

# convert the object into a dict
update_card_for_a_subscription_request_dict = update_card_for_a_subscription_request_instance.to_dict()
# create an instance of UpdateCardForASubscriptionRequest from a dict
update_card_for_a_subscription_request_from_dict = UpdateCardForASubscriptionRequest.from_dict(update_card_for_a_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


