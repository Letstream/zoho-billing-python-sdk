# UpdateSalesPersonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**salesperson_id** | **object** | Unique Id of the sales person assigned for the subscription. | 
**salesperson_name** | **str** | Name of the sales person assigned for the subscription. | 

## Example

```python
from ls_zoho_billing_subscription.models.update_sales_person_request import UpdateSalesPersonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSalesPersonRequest from a JSON string
update_sales_person_request_instance = UpdateSalesPersonRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSalesPersonRequest.to_json())

# convert the object into a dict
update_sales_person_request_dict = update_sales_person_request_instance.to_dict()
# create an instance of UpdateSalesPersonRequest from a dict
update_sales_person_request_from_dict = UpdateSalesPersonRequest.from_dict(update_sales_person_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


