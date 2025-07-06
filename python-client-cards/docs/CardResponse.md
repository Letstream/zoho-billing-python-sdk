# CardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Unique ID associated with the customer. | [optional] 
**card_id** | **str** | Card ID of the card from which payment is about to made by the customer. | [optional] 
**last_four_digits** | **int** | Last four digits of the customer&#39;s card. | [optional] 
**expiry_month** | **int** | Expiry month of the customer&#39;s card. | [optional] 
**expiry_year** | **int** | Expiry year of the customer&#39;s card. | [optional] 
**payment_gateway** | **str** | Payment gateway through which payment needs to be made. Supported payment gateway values &lt;code&gt;test_gateway&lt;/code&gt;, &lt;code&gt;payflow_pro&lt;/code&gt;, &lt;code&gt;stripe&lt;/code&gt;, &lt;code&gt;2checkout&lt;/code&gt;, &lt;code&gt;authorize_net&lt;/code&gt;, &lt;code&gt;payments_pro&lt;/code&gt;, &lt;code&gt;forte&lt;/code&gt;, &lt;code&gt;worldpay&lt;/code&gt;, &lt;code&gt;wepay&lt;/code&gt;. | [optional] 
**first_name** | **str** | Customer&#39;s first name in card. | [optional] 
**last_name** | **str** | Customer&#39;s last name in card. | [optional] 
**street** | **str** | The street mentioned in the customer&#39;s card address. | [optional] 
**city** | **str** | City mentioned in the customer&#39;s card address. | [optional] 
**state** | **str** | State mentioned in the customer&#39;s card address. | [optional] 
**zip** | **str** | Zip code mentioned in the customer&#39;s card address. | [optional] 
**country** | **str** | The country mentioned in the customer&#39;s card address. | [optional] 
**created_time** | **str** | Time at which the contact person was created. | [optional] 
**updated_time** | **str** | Time at which the contact person details were last updated. | [optional] 

## Example

```python
from ls_zoho_billing_cards.models.card_response import CardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CardResponse from a JSON string
card_response_instance = CardResponse.from_json(json)
# print the JSON string representation of the object
print(CardResponse.to_json())

# convert the object into a dict
card_response_dict = card_response_instance.to_dict()
# create an instance of CardResponse from a dict
card_response_from_dict = CardResponse.from_dict(card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


