# ListAllSubscriptionsResponseSubscriptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer ID of the customer for whom a subscription needs to be created. | [optional] 
**customer_name** | **str** | Name of the customer. | [optional] 
**email** | **str** | Email address of the customer. | [optional] 
**plan_name** | **str** | Name of the plan. | [optional] 
**subscription_id** | **str** | Unique ID generated for a subscription. | [optional] 
**name** | **str** | Name generated by concatenation of the product name and the selected plan. | [optional] 
**status** | **str** | The status of the subscription. It can be &lt;code&gt;live&lt;/code&gt;, &lt;code&gt;trial&lt;/code&gt;, &lt;code&gt;dunning&lt;/code&gt;, &lt;code&gt;unpaid&lt;/code&gt;, &lt;code&gt;non_renewing&lt;/code&gt;, &lt;code&gt;cancelled&lt;/code&gt;, &lt;code&gt;creation_failed&lt;/code&gt;, &lt;code&gt;cancelled_from_dunning&lt;/code&gt;, &lt;code&gt;expired&lt;/code&gt;, &lt;code&gt;trial_expired&lt;/code&gt; or &lt;code&gt;future&lt;/code&gt;. | [optional] 
**amount** | **float** | The amount that needs to be charged for the subscription. | [optional] 
**created_at** | **str** | Date at which the subscription was created. | [optional] 
**activated_at** | **str** | Date at which the subscription was activated. | [optional] 
**current_term_ends_at** | **str** | Date on which the current term of the subscription ends. | [optional] 
**current_term_starts_at** | **str** | Date on which the current term of the subscription started. | [optional] 
**last_billing_at** | **str** | The date on which the customer was billed last. | [optional] 
**next_billing_at** | **str** | The date on which the customer will be billed next. This will also be the date on which the next term of the subscription starts. | [optional] 
**expires_at** | **str** | This is applicable only when &lt;code&gt;billing_cycle&lt;/code&gt; is set for a plan. A subscription expires on the last day of the last billing cycle. | [optional] 
**interval** | **str** | Indicates the number of intervals between each billing. If interval&#x3D;2, the customer would be billed every two months or years depending on the value for interval_unit. | [optional] 
**interval_unit** | **str** | It can be either &lt;code&gt;months&lt;/code&gt; or &lt;code&gt;years&lt;/code&gt;. For interval&#x3D;2 and interval_unit&#x3D;months, the customer is billed every two months. | [optional] 
**auto_collect** | **bool** | auto_collect is set to true for creating an online subscription which will charge the customer’s card automatically on every renewal. To create an offline subscriptions, set auto_collect to false. | [optional] 
**created_time** | **str** | Time at which the subscription was created. | [optional] 
**updated_time** | **str** | Time at which the subscription details were last updated. | [optional] 
**reference_id** | **str** | A string of your choice is required to easily identify and keep track of your subscriptions. | [optional] 
**salesperson_id** | **str** | Unique Id of the sales person assigned for the subscription. | [optional] 
**salesperson_name** | **str** | Name of the sales person assigned for the subscription. | [optional] 
**currency_code** | **str** | Currency code of the currency in which the customer wants to pay. If &lt;code&gt;currency_code&lt;/code&gt; is not specified here, the currency chosen in your Zoho Billing organization will be used for billing. &lt;code&gt;currency_id&lt;/code&gt; and &lt;code&gt;currency_symbol&lt;/code&gt; are set automatically in accordance to the currency_code. | [optional] 
**currency_symbol** | **str** | Symbol of the customer&#39;s currency. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.list_all_subscriptions_response_subscriptions_inner import ListAllSubscriptionsResponseSubscriptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllSubscriptionsResponseSubscriptionsInner from a JSON string
list_all_subscriptions_response_subscriptions_inner_instance = ListAllSubscriptionsResponseSubscriptionsInner.from_json(json)
# print the JSON string representation of the object
print(ListAllSubscriptionsResponseSubscriptionsInner.to_json())

# convert the object into a dict
list_all_subscriptions_response_subscriptions_inner_dict = list_all_subscriptions_response_subscriptions_inner_instance.to_dict()
# create an instance of ListAllSubscriptionsResponseSubscriptionsInner from a dict
list_all_subscriptions_response_subscriptions_inner_from_dict = ListAllSubscriptionsResponseSubscriptionsInner.from_dict(list_all_subscriptions_response_subscriptions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


