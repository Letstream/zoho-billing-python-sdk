# coding: utf-8

# flake8: noqa

"""
    Time Entries

    Time entries are various entries of time made by users in a project, based on the time they spent on a project, in a task.<br><br><b>Possible error codes: </b><br><table><thead><tr><th>Error Code</th><th>Message</th></tr></thead><tbody><tr><td><span style=\"color:#FF0000;\"> 1002</span></td><td>This task does not exist in this project. Hence, this timesheet entry cannot be made</td></tr><tr><td><span style=\"color:#FF0000;\"> 20050</span></td><td>This timesheet entry is already being timed</td></tr><tr><td><span style=\"color:#FF0000;\"> 20054</span></td><td>This timesheet is being timed. Hence, it cannot be edited</td></tr></tbody></table>

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# Define package exports
__all__ = [
    "TimeEntriesApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "DeleteTimeEntriesResponse",
    "DeleteTimeEntryResponse",
    "GetATimeEntryResponse",
    "GetTimerResponse",
    "ListTimeEntriesResponse",
    "ListTimeEntriesResponseTimeEntriesInner",
    "LogTimeEntriesRequest",
    "LogTimeEntriesResponse",
    "StartTimerResponse",
    "StopTimerResponse",
    "TimeEntryResponse",
    "UpdateTimeEntryRequest",
    "UpdateTimeEntryResponse",
    "UpdateTimeEntryResponseTimeEntry",
]

# import apis into sdk package
from ls_zoho_billing_time_entries.api.time_entries_api import TimeEntriesApi as TimeEntriesApi

# import ApiClient
from ls_zoho_billing_time_entries.api_response import ApiResponse as ApiResponse
from ls_zoho_billing_time_entries.api_client import ApiClient as ApiClient
from ls_zoho_billing_time_entries.configuration import Configuration as Configuration
from ls_zoho_billing_time_entries.exceptions import OpenApiException as OpenApiException
from ls_zoho_billing_time_entries.exceptions import ApiTypeError as ApiTypeError
from ls_zoho_billing_time_entries.exceptions import ApiValueError as ApiValueError
from ls_zoho_billing_time_entries.exceptions import ApiKeyError as ApiKeyError
from ls_zoho_billing_time_entries.exceptions import ApiAttributeError as ApiAttributeError
from ls_zoho_billing_time_entries.exceptions import ApiException as ApiException

# import models into sdk package
from ls_zoho_billing_time_entries.models.delete_time_entries_response import DeleteTimeEntriesResponse as DeleteTimeEntriesResponse
from ls_zoho_billing_time_entries.models.delete_time_entry_response import DeleteTimeEntryResponse as DeleteTimeEntryResponse
from ls_zoho_billing_time_entries.models.get_a_time_entry_response import GetATimeEntryResponse as GetATimeEntryResponse
from ls_zoho_billing_time_entries.models.get_timer_response import GetTimerResponse as GetTimerResponse
from ls_zoho_billing_time_entries.models.list_time_entries_response import ListTimeEntriesResponse as ListTimeEntriesResponse
from ls_zoho_billing_time_entries.models.list_time_entries_response_time_entries_inner import ListTimeEntriesResponseTimeEntriesInner as ListTimeEntriesResponseTimeEntriesInner
from ls_zoho_billing_time_entries.models.log_time_entries_request import LogTimeEntriesRequest as LogTimeEntriesRequest
from ls_zoho_billing_time_entries.models.log_time_entries_response import LogTimeEntriesResponse as LogTimeEntriesResponse
from ls_zoho_billing_time_entries.models.start_timer_response import StartTimerResponse as StartTimerResponse
from ls_zoho_billing_time_entries.models.stop_timer_response import StopTimerResponse as StopTimerResponse
from ls_zoho_billing_time_entries.models.time_entry_response import TimeEntryResponse as TimeEntryResponse
from ls_zoho_billing_time_entries.models.update_time_entry_request import UpdateTimeEntryRequest as UpdateTimeEntryRequest
from ls_zoho_billing_time_entries.models.update_time_entry_response import UpdateTimeEntryResponse as UpdateTimeEntryResponse
from ls_zoho_billing_time_entries.models.update_time_entry_response_time_entry import UpdateTimeEntryResponseTimeEntry as UpdateTimeEntryResponseTimeEntry
