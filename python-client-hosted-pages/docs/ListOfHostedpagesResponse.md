# ListOfHostedpagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**hosted_pages** | [**List[ListOfHostedpagesResponseHostedPagesInner]**](ListOfHostedpagesResponseHostedPagesInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.list_of_hostedpages_response import ListOfHostedpagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOfHostedpagesResponse from a JSON string
list_of_hostedpages_response_instance = ListOfHostedpagesResponse.from_json(json)
# print the JSON string representation of the object
print(ListOfHostedpagesResponse.to_json())

# convert the object into a dict
list_of_hostedpages_response_dict = list_of_hostedpages_response_instance.to_dict()
# create an instance of ListOfHostedpagesResponse from a dict
list_of_hostedpages_response_from_dict = ListOfHostedpagesResponse.from_dict(list_of_hostedpages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


