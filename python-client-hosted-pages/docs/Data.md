# Data

Returned data for the HostedPages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription** | [**DataSubscription**](DataSubscription.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.data import Data

# TODO update the JSON string below
json = "{}"
# create an instance of Data from a JSON string
data_instance = Data.from_json(json)
# print the JSON string representation of the object
print(Data.to_json())

# convert the object into a dict
data_dict = data_instance.to_dict()
# create an instance of Data from a dict
data_from_dict = Data.from_dict(data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


