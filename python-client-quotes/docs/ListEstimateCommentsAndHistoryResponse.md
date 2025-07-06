# ListEstimateCommentsAndHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**comments** | [**List[ListEstimateCommentsAndHistoryResponseCommentsInner]**](ListEstimateCommentsAndHistoryResponseCommentsInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.list_estimate_comments_and_history_response import ListEstimateCommentsAndHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListEstimateCommentsAndHistoryResponse from a JSON string
list_estimate_comments_and_history_response_instance = ListEstimateCommentsAndHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(ListEstimateCommentsAndHistoryResponse.to_json())

# convert the object into a dict
list_estimate_comments_and_history_response_dict = list_estimate_comments_and_history_response_instance.to_dict()
# create an instance of ListEstimateCommentsAndHistoryResponse from a dict
list_estimate_comments_and_history_response_from_dict = ListEstimateCommentsAndHistoryResponse.from_dict(list_estimate_comments_and_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


