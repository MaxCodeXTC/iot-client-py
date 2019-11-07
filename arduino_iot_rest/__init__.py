# coding: utf-8

# flake8: noqa

"""
    Iot API

    Collection of all public API endpoints.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.1"

# import apis into sdk package
from arduino_iot_rest.api.devices_v2_api import DevicesV2Api
from arduino_iot_rest.api.properties_v2_api import PropertiesV2Api
from arduino_iot_rest.api.series_v2_api import SeriesV2Api
from arduino_iot_rest.api.things_v2_api import ThingsV2Api

# import ApiClient
from arduino_iot_rest.api_client import ApiClient
from arduino_iot_rest.configuration import Configuration
from arduino_iot_rest.exceptions import OpenApiException
from arduino_iot_rest.exceptions import ApiTypeError
from arduino_iot_rest.exceptions import ApiValueError
from arduino_iot_rest.exceptions import ApiKeyError
from arduino_iot_rest.exceptions import ApiException
# import models into sdk package
from arduino_iot_rest.models.arduino_devicev2 import ArduinoDevicev2
from arduino_iot_rest.models.arduino_devicev2_webhook import ArduinoDevicev2Webhook
from arduino_iot_rest.models.arduino_devicev2properties import ArduinoDevicev2properties
from arduino_iot_rest.models.arduino_devicev2propertyvalue import ArduinoDevicev2propertyvalue
from arduino_iot_rest.models.arduino_devicev2propertyvalue_value import ArduinoDevicev2propertyvalueValue
from arduino_iot_rest.models.arduino_devicev2propertyvalue_value_statistics import ArduinoDevicev2propertyvalueValueStatistics
from arduino_iot_rest.models.arduino_devicev2propertyvalues import ArduinoDevicev2propertyvalues
from arduino_iot_rest.models.arduino_devicev2propertyvalues_last_evaluated_key import ArduinoDevicev2propertyvaluesLastEvaluatedKey
from arduino_iot_rest.models.arduino_property import ArduinoProperty
from arduino_iot_rest.models.arduino_series_batch import ArduinoSeriesBatch
from arduino_iot_rest.models.arduino_series_raw_batch import ArduinoSeriesRawBatch
from arduino_iot_rest.models.arduino_series_raw_batch_lastvalue import ArduinoSeriesRawBatchLastvalue
from arduino_iot_rest.models.arduino_series_raw_last_value_response import ArduinoSeriesRawLastValueResponse
from arduino_iot_rest.models.arduino_series_raw_response import ArduinoSeriesRawResponse
from arduino_iot_rest.models.arduino_series_response import ArduinoSeriesResponse
from arduino_iot_rest.models.arduino_thing import ArduinoThing
from arduino_iot_rest.models.batch_last_value_requests_media_v1 import BatchLastValueRequestsMediaV1
from arduino_iot_rest.models.batch_query_raw_last_value_request_media_v1 import BatchQueryRawLastValueRequestMediaV1
from arduino_iot_rest.models.batch_query_raw_request_media_v1 import BatchQueryRawRequestMediaV1
from arduino_iot_rest.models.batch_query_raw_requests_media_v1 import BatchQueryRawRequestsMediaV1
from arduino_iot_rest.models.batch_query_raw_response_series_media_v1 import BatchQueryRawResponseSeriesMediaV1
from arduino_iot_rest.models.batch_query_request_media_v1 import BatchQueryRequestMediaV1
from arduino_iot_rest.models.batch_query_requests_media_v1 import BatchQueryRequestsMediaV1
from arduino_iot_rest.models.create_devices_v2_payload import CreateDevicesV2Payload
from arduino_iot_rest.models.create_things_v2_payload import CreateThingsV2Payload
from arduino_iot_rest.models.devicev2 import Devicev2
from arduino_iot_rest.models.error import Error
from arduino_iot_rest.models.model_property import ModelProperty
from arduino_iot_rest.models.properties_value import PropertiesValue
from arduino_iot_rest.models.properties_values import PropertiesValues
from arduino_iot_rest.models.property_value import PropertyValue
from arduino_iot_rest.models.thing import Thing
from arduino_iot_rest.models.thing_sketch import ThingSketch

