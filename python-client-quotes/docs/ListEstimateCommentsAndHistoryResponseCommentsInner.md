# ListEstimateCommentsAndHistoryResponseCommentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_id** | **str** | The ID of the comment | [optional] 
**estimate_id** | **str** | The  unique id of a particular quote | [optional] 
**description** | **str** | A short note on the estimate comments | [optional] 
**commented_by_id** | **str** | Comment by comment ID | [optional] 
**commented_by** | **str** | Name of the person who has commented | [optional] 
**comment_type** | **str** | Type of comment made | [optional] 
**var_date** | **str** | Date on the quote. | [optional] 
**date_description** | **str** | Number of days since the comment has been made | [optional] 
**time** | **str** | time when quote was created | [optional] 
**operation_type** | **str** | Type of operation on quote | [optional] 
**transaction_id** | **str** | ID of the transaction | [optional] 
**transaction_type** | **str** | Type of the transaction performed | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.list_estimate_comments_and_history_response_comments_inner import ListEstimateCommentsAndHistoryResponseCommentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListEstimateCommentsAndHistoryResponseCommentsInner from a JSON string
list_estimate_comments_and_history_response_comments_inner_instance = ListEstimateCommentsAndHistoryResponseCommentsInner.from_json(json)
# print the JSON string representation of the object
print(ListEstimateCommentsAndHistoryResponseCommentsInner.to_json())

# convert the object into a dict
list_estimate_comments_and_history_response_comments_inner_dict = list_estimate_comments_and_history_response_comments_inner_instance.to_dict()
# create an instance of ListEstimateCommentsAndHistoryResponseCommentsInner from a dict
list_estimate_comments_and_history_response_comments_inner_from_dict = ListEstimateCommentsAndHistoryResponseCommentsInner.from_dict(list_estimate_comments_and_history_response_comments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


