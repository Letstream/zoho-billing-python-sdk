# Card

Customer's card object. This contains <code>payment_gateway</code>, <code>last_four_digits</code>, <code>expiry_month</code> and <code>expiry_year</code>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **object** | Customer&#39;s card ID. | [optional] 
**last_four_digits** | **int** | Last four digits of the customer&#39;s card. | [optional] 
**payment_gateway** | **str** | Payment gateway through which payment needs to be made. | [optional] 
**expiry_month** | **int** | Expiry month of the customer&#39;s card. | [optional] 
**expiry_year** | **int** | Expiry year of the customer&#39;s card. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.card import Card

# TODO update the JSON string below
json = "{}"
# create an instance of Card from a JSON string
card_instance = Card.from_json(json)
# print the JSON string representation of the object
print(Card.to_json())

# convert the object into a dict
card_dict = card_instance.to_dict()
# create an instance of Card from a dict
card_from_dict = Card.from_dict(card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


