# ListAllActiveCreditCardsOfACustomerResponseCardsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** | Card ID of the card from which payment is about to made by the customer. | [optional] 
**customer_id** | **str** | Unique ID associated with the customer. | [optional] 
**status** | **str** | Status of the card. | [optional] 
**last_four_digits** | **int** | Last four digits of the customer&#39;s card. | [optional] 
**expiry_month** | **int** | Expiry month of the customer&#39;s card. | [optional] 
**expiry_year** | **int** | Expiry year of the customer&#39;s card. | [optional] 
**payment_gateway** | **str** | Payment gateway through which payment needs to be made. Supported payment gateway values &lt;code&gt;test_gateway&lt;/code&gt;, &lt;code&gt;payflow_pro&lt;/code&gt;, &lt;code&gt;stripe&lt;/code&gt;, &lt;code&gt;2checkout&lt;/code&gt;, &lt;code&gt;authorize_net&lt;/code&gt;, &lt;code&gt;payments_pro&lt;/code&gt;, &lt;code&gt;forte&lt;/code&gt;, &lt;code&gt;worldpay&lt;/code&gt;, &lt;code&gt;wepay&lt;/code&gt;. | [optional] 
**created_time** | **str** | Time at which the contact person was created. | [optional] 
**updated_time** | **str** | Time at which the contact person details were last updated. | [optional] 

## Example

```python
from ls_zoho_billing_cards.models.list_all_active_credit_cards_of_a_customer_response_cards_inner import ListAllActiveCreditCardsOfACustomerResponseCardsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllActiveCreditCardsOfACustomerResponseCardsInner from a JSON string
list_all_active_credit_cards_of_a_customer_response_cards_inner_instance = ListAllActiveCreditCardsOfACustomerResponseCardsInner.from_json(json)
# print the JSON string representation of the object
print(ListAllActiveCreditCardsOfACustomerResponseCardsInner.to_json())

# convert the object into a dict
list_all_active_credit_cards_of_a_customer_response_cards_inner_dict = list_all_active_credit_cards_of_a_customer_response_cards_inner_instance.to_dict()
# create an instance of ListAllActiveCreditCardsOfACustomerResponseCardsInner from a dict
list_all_active_credit_cards_of_a_customer_response_cards_inner_from_dict = ListAllActiveCreditCardsOfACustomerResponseCardsInner.from_dict(list_all_active_credit_cards_of_a_customer_response_cards_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


