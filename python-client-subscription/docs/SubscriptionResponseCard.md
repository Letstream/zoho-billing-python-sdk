# SubscriptionResponseCard

Customer's card object. This contains <code>payment_gateway</code>, <code>last_four_digits</code>, <code>expiry_month</code> and <code>expiry_year</code>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **object** | Customer&#39;s card ID. | [optional] 
**last_four_digits** | **int** | Last four digits of the customer&#39;s card. | [optional] 
**payment_gateway** | **str** | Payment gateway through which payment needs to be made. Supported payment gateway values &lt;code&gt;test_gateway&lt;/code&gt;, &lt;code&gt;payflow_pro&lt;/code&gt;, &lt;code&gt;stripe&lt;/code&gt;, &lt;code&gt;2checkout&lt;/code&gt;, &lt;code&gt;authorize_net&lt;/code&gt;, &lt;code&gt;payments_pro&lt;/code&gt;, &lt;code&gt;forte&lt;/code&gt;, &lt;code&gt;worldpay&lt;/code&gt;, &lt;code&gt;wepay&lt;/code&gt;. | [optional] 
**expiry_month** | **int** | Expiry month of the customer&#39;s card. | [optional] 
**expiry_year** | **int** | Expiry year of the customer&#39;s card. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.subscription_response_card import SubscriptionResponseCard

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionResponseCard from a JSON string
subscription_response_card_instance = SubscriptionResponseCard.from_json(json)
# print the JSON string representation of the object
print(SubscriptionResponseCard.to_json())

# convert the object into a dict
subscription_response_card_dict = subscription_response_card_instance.to_dict()
# create an instance of SubscriptionResponseCard from a dict
subscription_response_card_from_dict = SubscriptionResponseCard.from_dict(subscription_response_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


