# ListAllAddonsResponseAddonsInnerTagsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_option_id** | **int** | Id of the Tag Option | [optional] 
**is_tag_mandatory** | **str** |  | [optional] 
**tag_name** | **str** |  | [optional] 
**tag_id** | **int** | ID of the Tag | [optional] 
**tag_option_name** | **str** |  | [optional] 

## Example

```python
from ls_zoho_billing_addons.models.list_all_addons_response_addons_inner_tags_inner import ListAllAddonsResponseAddonsInnerTagsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListAllAddonsResponseAddonsInnerTagsInner from a JSON string
list_all_addons_response_addons_inner_tags_inner_instance = ListAllAddonsResponseAddonsInnerTagsInner.from_json(json)
# print the JSON string representation of the object
print(ListAllAddonsResponseAddonsInnerTagsInner.to_json())

# convert the object into a dict
list_all_addons_response_addons_inner_tags_inner_dict = list_all_addons_response_addons_inner_tags_inner_instance.to_dict()
# create an instance of ListAllAddonsResponseAddonsInnerTagsInner from a dict
list_all_addons_response_addons_inner_tags_inner_from_dict = ListAllAddonsResponseAddonsInnerTagsInner.from_dict(list_all_addons_response_addons_inner_tags_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


