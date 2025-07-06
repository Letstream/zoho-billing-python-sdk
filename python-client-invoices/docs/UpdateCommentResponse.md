# UpdateCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**comment_id** | **str** | Unique Id to denote the comment fro the particular invoice. | [optional] 
**invoice_id** | **str** | Unique ID generated for an invoice. | [optional] 
**description** | **str** | Small description of the payment made for the invoice. | [optional] 
**commented_by_id** | **str** | Unique Id to denote who has commented. | [optional] 
**commented_by** | **str** | It denotes the name of the user who has commented or the system. | [optional] 
**var_date** | **str** | Date on which the invoice is paid. | [optional] 
**date_description** | **str** | Number of days since the comment was made | [optional] 
**time** | **str** | Denotes the time at which the comment was created. | [optional] 
**comment_type** | **str** | It denotes whether user comment or system comment. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.update_comment_response import UpdateCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCommentResponse from a JSON string
update_comment_response_instance = UpdateCommentResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateCommentResponse.to_json())

# convert the object into a dict
update_comment_response_dict = update_comment_response_instance.to_dict()
# create an instance of UpdateCommentResponse from a dict
update_comment_response_from_dict = UpdateCommentResponse.from_dict(update_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


