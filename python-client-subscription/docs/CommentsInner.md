# CommentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_id** | **str** | Unique Id to denote the comment fro the particular invoice. | [optional] 
**description** | **object** | Small description about the comment. | [optional] 
**commented_by_id** | **str** | Unique Id to denote who has commented. | [optional] 
**commented_by** | **str** | Name of the user who added the comment. | [optional] 
**comment_type** | **str** | It denotes whether user comment or system comment. | [optional] 
**var_date** | **object** | Date on which the comment was created. | [optional] 
**time** | **str** | Time at which the comment was commented. | [optional] 
**operation_type** | **str** | Type of operation performed on the invoice. | [optional] 
**transaction_id** | **str** | Unique ID to denote the transaction. | [optional] 
**transaction_type** | **object** | Small description about the type of transaction. | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.comments_inner import CommentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsInner from a JSON string
comments_inner_instance = CommentsInner.from_json(json)
# print the JSON string representation of the object
print(CommentsInner.to_json())

# convert the object into a dict
comments_inner_dict = comments_inner_instance.to_dict()
# create an instance of CommentsInner from a dict
comments_inner_from_dict = CommentsInner.from_dict(comments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


