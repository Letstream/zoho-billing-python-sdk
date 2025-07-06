# RetrieveAHostedPageResponseData

data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription** | [**RetrieveAHostedPageResponseDataSubscription**](RetrieveAHostedPageResponseDataSubscription.md) |  | [optional] 
**invoice** | [**RetrieveAHostedPageResponseDataInvoice**](RetrieveAHostedPageResponseDataInvoice.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.retrieve_a_hosted_page_response_data import RetrieveAHostedPageResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAHostedPageResponseData from a JSON string
retrieve_a_hosted_page_response_data_instance = RetrieveAHostedPageResponseData.from_json(json)
# print the JSON string representation of the object
print(RetrieveAHostedPageResponseData.to_json())

# convert the object into a dict
retrieve_a_hosted_page_response_data_dict = retrieve_a_hosted_page_response_data_instance.to_dict()
# create an instance of RetrieveAHostedPageResponseData from a dict
retrieve_a_hosted_page_response_data_from_dict = RetrieveAHostedPageResponseData.from_dict(retrieve_a_hosted_page_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


