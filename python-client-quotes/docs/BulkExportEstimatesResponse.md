# BulkExportEstimatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_quotes.models.bulk_export_estimates_response import BulkExportEstimatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkExportEstimatesResponse from a JSON string
bulk_export_estimates_response_instance = BulkExportEstimatesResponse.from_json(json)
# print the JSON string representation of the object
print(BulkExportEstimatesResponse.to_json())

# convert the object into a dict
bulk_export_estimates_response_dict = bulk_export_estimates_response_instance.to_dict()
# create an instance of BulkExportEstimatesResponse from a dict
bulk_export_estimates_response_from_dict = BulkExportEstimatesResponse.from_dict(bulk_export_estimates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


