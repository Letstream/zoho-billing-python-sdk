# ListAllCustomersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**customers** | [**List[ListAllCustomersResponseCustomersInner]**](ListAllCustomersResponseCustomersInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_customers.models.list_all_customers_response import ListAllCustomersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllCustomersResponse from a JSON string
list_all_customers_response_instance = ListAllCustomersResponse.from_json(json)
# print the JSON string representation of the object
print(ListAllCustomersResponse.to_json())

# convert the object into a dict
list_all_customers_response_dict = list_all_customers_response_instance.to_dict()
# create an instance of ListAllCustomersResponse from a dict
list_all_customers_response_from_dict = ListAllCustomersResponse.from_dict(list_all_customers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


