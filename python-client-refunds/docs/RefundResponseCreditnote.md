# RefundResponseCreditnote

It contains details of the credit note for which the refund has to made. Each object contains <code>creditnote_id</code>, <code>creditnote_number</code>, <code>date</code>, <code>amount</code>, <code>refund_amount</code> and <code>balance_amount</code>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creditnote_id** | **str** | Credit note ID of the credit note involved in this refund. | [optional] 
**creditnote_number** | **str** | Credit note number (starts with CN) of the credit note. | [optional] 
**var_date** | **object** | The date on which the credit note is raised. | [optional] 
**amount** | **object** | The total amount for which the credit note is raised. | [optional] 
**refund_amount** | **float** | The amount for which the refund is to be made. | [optional] 
**balance_amount** | **float** | Unused credits. | [optional] 

## Example

```python
from ls_zoho_billing_refunds.models.refund_response_creditnote import RefundResponseCreditnote

# TODO update the JSON string below
json = "{}"
# create an instance of RefundResponseCreditnote from a JSON string
refund_response_creditnote_instance = RefundResponseCreditnote.from_json(json)
# print the JSON string representation of the object
print(RefundResponseCreditnote.to_json())

# convert the object into a dict
refund_response_creditnote_dict = refund_response_creditnote_instance.to_dict()
# create an instance of RefundResponseCreditnote from a dict
refund_response_creditnote_from_dict = RefundResponseCreditnote.from_dict(refund_response_creditnote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


