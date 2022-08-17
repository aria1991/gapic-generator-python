# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.api import monitored_resource_pb2  # type: ignore
from google.cloud.logging_v2.types import log_entry
from google.protobuf import duration_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore

__manifest__ = (
        'DeleteLogRequest',
        'WriteLogEntriesRequest',
        'ListLogEntriesRequest',
        'ListMonitoredResourceDescriptorsRequest',
        'ListLogsRequest',
        'TailLogEntriesRequest',
)


class DeleteLogRequest(proto.Message):
    r"""The parameters to DeleteLog.

    Attributes:
        log_name (str):
            Required. The resource name of the log to delete:

            ::

                "projects/[PROJECT_ID]/logs/[LOG_ID]"
                "organizations/[ORGANIZATION_ID]/logs/[LOG_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]"
                "folders/[FOLDER_ID]/logs/[LOG_ID]"

            ``[LOG_ID]`` must be URL-encoded. For example,
            ``"projects/my-project-id/logs/syslog"``,
            ``"organizations/1234567890/logs/cloudresourcemanager.googleapis.com%2Factivity"``.
            For more information about log names, see
            [LogEntry][google.logging.v2.LogEntry].
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    log_name = proto.Field(
        proto.STRING,
        number=1,
    )


class WriteLogEntriesRequest(proto.Message):
    r"""The parameters to WriteLogEntries.

    Attributes:
        log_name (str):
            Optional. A default log resource name that is assigned to
            all log entries in ``entries`` that do not specify a value
            for ``log_name``:

            ::

                "projects/[PROJECT_ID]/logs/[LOG_ID]"
                "organizations/[ORGANIZATION_ID]/logs/[LOG_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]"
                "folders/[FOLDER_ID]/logs/[LOG_ID]"

            ``[LOG_ID]`` must be URL-encoded. For example:

            ::

                "projects/my-project-id/logs/syslog"
                "organizations/1234567890/logs/cloudresourcemanager.googleapis.com%2Factivity"

            The permission ``logging.logEntries.create`` is needed on
            each project, organization, billing account, or folder that
            is receiving new log entries, whether the resource is
            specified in ``logName`` or in an individual log entry.
        resource (google.api.monitored_resource_pb2.MonitoredResource):
            Optional. A default monitored resource object that is
            assigned to all log entries in ``entries`` that do not
            specify a value for ``resource``. Example:

            ::

                { "type": "gce_instance",
                  "labels": {
                    "zone": "us-central1-a", "instance_id": "00000000000000000000" }}

            See [LogEntry][google.logging.v2.LogEntry].
        labels (Mapping[str, str]):
            Optional. Default labels that are added to the ``labels``
            field of all log entries in ``entries``. If a log entry
            already has a label with the same key as a label in this
            parameter, then the log entry's label is not changed. See
            [LogEntry][google.logging.v2.LogEntry].
        entries (Sequence[google.cloud.logging_v2.types.LogEntry]):
            Required. The log entries to send to Logging. The order of
            log entries in this list does not matter. Values supplied in
            this method's ``log_name``, ``resource``, and ``labels``
            fields are copied into those log entries in this list that
            do not include values for their corresponding fields. For
            more information, see the
            [LogEntry][google.logging.v2.LogEntry] type.

            If the ``timestamp`` or ``insert_id`` fields are missing in
            log entries, then this method supplies the current time or a
            unique identifier, respectively. The supplied values are
            chosen so that, among the log entries that did not supply
            their own values, the entries earlier in the list will sort
            before the entries later in the list. See the
            ``entries.list`` method.

            Log entries with timestamps that are more than the `logs
            retention
            period <https://cloud.google.com/logging/quota-policy>`__ in
            the past or more than 24 hours in the future will not be
            available when calling ``entries.list``. However, those log
            entries can still be `exported with
            LogSinks <https://cloud.google.com/logging/docs/api/tasks/exporting-logs>`__.

            To improve throughput and to avoid exceeding the `quota
            limit <https://cloud.google.com/logging/quota-policy>`__ for
            calls to ``entries.write``, you should try to include
            several log entries in this list, rather than calling this
            method for each individual log entry.
        partial_success (bool):
            Optional. Whether valid entries should be written even if
            some other entries fail due to INVALID_ARGUMENT or
            PERMISSION_DENIED errors. If any entry is not written, then
            the response status is the error associated with one of the
            failed entries and the response includes error details keyed
            by the entries' zero-based index in the ``entries.write``
            method.
        dry_run (bool):
            Optional. If true, the request should expect
            normal response, but the entries won't be
            persisted nor exported. Useful for checking
            whether the logging API endpoints are working
            properly before sending valuable data.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    log_name = proto.Field(
        proto.STRING,
        number=1,
    )
    resource = proto.Field(
        proto.MESSAGE,
        number=2,
        message=monitored_resource_pb2.MonitoredResource,
    )
    labels = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    entries = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=log_entry.LogEntry,
    )
    partial_success = proto.Field(
        proto.BOOL,
        number=5,
    )
    dry_run = proto.Field(
        proto.BOOL,
        number=6,
    )


class ListLogEntriesRequest(proto.Message):
    r"""The parameters to ``ListLogEntries``.

    Attributes:
        resource_names (Sequence[str]):
            Required. Names of one or more parent resources from which
            to retrieve log entries:

            ::

                "projects/[PROJECT_ID]"
                "organizations/[ORGANIZATION_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]"
                "folders/[FOLDER_ID]"

            May alternatively be one or more views
            projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]
            organization/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]
            billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]
            folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]

            Projects listed in the ``project_ids`` field are added to
            this list.
        filter (str):
            Optional. A filter that chooses which log entries to return.
            See `Advanced Logs
            Queries <https://cloud.google.com/logging/docs/view/advanced-queries>`__.
            Only log entries that match the filter are returned. An
            empty filter matches all log entries in the resources listed
            in ``resource_names``. Referencing a parent resource that is
            not listed in ``resource_names`` will cause the filter to
            return no results. The maximum length of the filter is 20000
            characters.
        order_by (str):
            Optional. How the results should be sorted. Presently, the
            only permitted values are ``"timestamp asc"`` (default) and
            ``"timestamp desc"``. The first option returns entries in
            order of increasing values of ``LogEntry.timestamp`` (oldest
            first), and the second option returns entries in order of
            decreasing timestamps (newest first). Entries with equal
            timestamps are returned in order of their ``insert_id``
            values.
        page_size (int):
            Optional. The maximum number of results to return from this
            request. Default is 50. If the value is negative or exceeds
            1000, the request is rejected. The presence of
            ``next_page_token`` in the response indicates that more
            results might be available.
        page_token (str):
            Optional. If present, then retrieve the next batch of
            results from the preceding call to this method.
            ``page_token`` must be the value of ``next_page_token`` from
            the previous response. The values of other method parameters
            should be identical to those in the previous call.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    resource_names = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    filter = proto.Field(
        proto.STRING,
        number=2,
    )
    order_by = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token = proto.Field(
        proto.STRING,
        number=5,
    )


class ListMonitoredResourceDescriptorsRequest(proto.Message):
    r"""The parameters to ListMonitoredResourceDescriptors

    Attributes:
        page_size (int):
            Optional. The maximum number of results to return from this
            request. Non-positive values are ignored. The presence of
            ``nextPageToken`` in the response indicates that more
            results might be available.
        page_token (str):
            Optional. If present, then retrieve the next batch of
            results from the preceding call to this method.
            ``pageToken`` must be the value of ``nextPageToken`` from
            the previous response. The values of other method parameters
            should be identical to those in the previous call.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    page_size = proto.Field(
        proto.INT32,
        number=1,
    )
    page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class ListLogsRequest(proto.Message):
    r"""The parameters to ListLogs.

    Attributes:
        parent (str):
            Required. The resource name that owns the logs:

            ::

                "projects/[PROJECT_ID]"
                "organizations/[ORGANIZATION_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]"
                "folders/[FOLDER_ID]".
        page_size (int):
            Optional. The maximum number of results to return from this
            request. Non-positive values are ignored. The presence of
            ``nextPageToken`` in the response indicates that more
            results might be available.
        page_token (str):
            Optional. If present, then retrieve the next batch of
            results from the preceding call to this method.
            ``pageToken`` must be the value of ``nextPageToken`` from
            the previous response. The values of other method parameters
            should be identical to those in the previous call.
        resource_names (Sequence[str]):
            Optional. The resource name that owns the logs:
            projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]
            organization/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]
            billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]
            folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]

            To support legacy queries, it could also be:
            "projects/[PROJECT_ID]" "organizations/[ORGANIZATION_ID]"
            "billingAccounts/[BILLING_ACCOUNT_ID]" "folders/[FOLDER_ID]".
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token = proto.Field(
        proto.STRING,
        number=3,
    )
    resource_names = proto.RepeatedField(
        proto.STRING,
        number=8,
    )


class TailLogEntriesRequest(proto.Message):
    r"""The parameters to ``TailLogEntries``.

    Attributes:
        resource_names (Sequence[str]):
            Required. Name of a parent resource from which to retrieve
            log entries:

            ::

                "projects/[PROJECT_ID]"
                "organizations/[ORGANIZATION_ID]"
                "billingAccounts/[BILLING_ACCOUNT_ID]"
                "folders/[FOLDER_ID]"

            May alternatively be one or more views:
            "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]"
            "organization/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]"
            "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]"
            "folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]".
        filter (str):
            Optional. A filter that chooses which log entries to return.
            See `Advanced Logs
            Filters <https://cloud.google.com/logging/docs/view/advanced_filters>`__.
            Only log entries that match the filter are returned. An
            empty filter matches all log entries in the resources listed
            in ``resource_names``. Referencing a parent resource that is
            not in ``resource_names`` will cause the filter to return no
            results. The maximum length of the filter is 20000
            characters.
        buffer_window (google.protobuf.duration_pb2.Duration):
            Optional. The amount of time to buffer log
            entries at the server before being returned to
            prevent out of order results due to late
            arriving log entries. Valid values are between
            0-60000 milliseconds. Defaults to 2000
            milliseconds.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    resource_names = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    filter = proto.Field(
        proto.STRING,
        number=2,
    )
    buffer_window = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )


__all__ = tuple(sorted(__manifest__))