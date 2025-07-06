# AddonResponseTagsInner


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
from openapi_client.models.addon_response_tags_inner import AddonResponseTagsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddonResponseTagsInner from a JSON string
addon_response_tags_inner_instance = AddonResponseTagsInner.from_json(json)
# print the JSON string representation of the object
print(AddonResponseTagsInner.to_json())

# convert the object into a dict
addon_response_tags_inner_dict = addon_response_tags_inner_instance.to_dict()
# create an instance of AddonResponseTagsInner from a dict
addon_response_tags_inner_from_dict = AddonResponseTagsInner.from_dict(addon_response_tags_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


