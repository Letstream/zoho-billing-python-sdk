# UpdateAnAddonRequestTagsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_id** | **int** | ID of the Tag | [optional] 
**tag_option_id** | **int** | Id of the Tag Option | [optional] 

## Example

```python
from openapi_client.models.update_an_addon_request_tags_inner import UpdateAnAddonRequestTagsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnAddonRequestTagsInner from a JSON string
update_an_addon_request_tags_inner_instance = UpdateAnAddonRequestTagsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateAnAddonRequestTagsInner.to_json())

# convert the object into a dict
update_an_addon_request_tags_inner_dict = update_an_addon_request_tags_inner_instance.to_dict()
# create an instance of UpdateAnAddonRequestTagsInner from a dict
update_an_addon_request_tags_inner_from_dict = UpdateAnAddonRequestTagsInner.from_dict(update_an_addon_request_tags_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


