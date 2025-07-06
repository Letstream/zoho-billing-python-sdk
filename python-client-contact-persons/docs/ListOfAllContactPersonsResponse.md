# ListOfAllContactPersonsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**contact_persons** | [**List[ListOfAllContactPersonsResponseContactPersonsInner]**](ListOfAllContactPersonsResponseContactPersonsInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_contact_persons.models.list_of_all_contact_persons_response import ListOfAllContactPersonsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOfAllContactPersonsResponse from a JSON string
list_of_all_contact_persons_response_instance = ListOfAllContactPersonsResponse.from_json(json)
# print the JSON string representation of the object
print(ListOfAllContactPersonsResponse.to_json())

# convert the object into a dict
list_of_all_contact_persons_response_dict = list_of_all_contact_persons_response_instance.to_dict()
# create an instance of ListOfAllContactPersonsResponse from a dict
list_of_all_contact_persons_response_from_dict = ListOfAllContactPersonsResponse.from_dict(list_of_all_contact_persons_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


