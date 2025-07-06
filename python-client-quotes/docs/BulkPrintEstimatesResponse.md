# BulkPrintEstimatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_quotes.models.bulk_print_estimates_response import BulkPrintEstimatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPrintEstimatesResponse from a JSON string
bulk_print_estimates_response_instance = BulkPrintEstimatesResponse.from_json(json)
# print the JSON string representation of the object
print(BulkPrintEstimatesResponse.to_json())

# convert the object into a dict
bulk_print_estimates_response_dict = bulk_print_estimates_response_instance.to_dict()
# create an instance of BulkPrintEstimatesResponse from a dict
bulk_print_estimates_response_from_dict = BulkPrintEstimatesResponse.from_dict(bulk_print_estimates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


