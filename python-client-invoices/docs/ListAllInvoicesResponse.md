# ListAllInvoicesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**invoices** | [**List[ListAllInvoicesResponseInvoicesInner]**](ListAllInvoicesResponseInvoicesInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.list_all_invoices_response import ListAllInvoicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllInvoicesResponse from a JSON string
list_all_invoices_response_instance = ListAllInvoicesResponse.from_json(json)
# print the JSON string representation of the object
print(ListAllInvoicesResponse.to_json())

# convert the object into a dict
list_all_invoices_response_dict = list_all_invoices_response_instance.to_dict()
# create an instance of ListAllInvoicesResponse from a dict
list_all_invoices_response_from_dict = ListAllInvoicesResponse.from_dict(list_all_invoices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


