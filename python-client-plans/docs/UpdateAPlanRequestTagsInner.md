# UpdateAPlanRequestTagsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_id** | **int** | ID of the Tag | [optional] 
**tag_option_id** | **int** | Id of the Tag Option | [optional] 

## Example

```python
from ls_zoho_billing_plans.models.update_a_plan_request_tags_inner import UpdateAPlanRequestTagsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAPlanRequestTagsInner from a JSON string
update_a_plan_request_tags_inner_instance = UpdateAPlanRequestTagsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateAPlanRequestTagsInner.to_json())

# convert the object into a dict
update_a_plan_request_tags_inner_dict = update_a_plan_request_tags_inner_instance.to_dict()
# create an instance of UpdateAPlanRequestTagsInner from a dict
update_a_plan_request_tags_inner_from_dict = UpdateAPlanRequestTagsInner.from_dict(update_a_plan_request_tags_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


