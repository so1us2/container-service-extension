# container-service-extension
# Copyright (c) 2019 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2-Clause

from enum import Enum
from enum import unique


@unique
class MinorErrorCode(int, Enum):
    """Collection of error code and related messages."""

    DEFAULT_ERROR_CODE = -1

    REQUEST_KEY_CLUSTER_NAME_MISSING = 4000
    REQUEST_KEY_CLUSTER_NAME_INVALID = 4001
    REQUEST_KEY_COMPUTE_POLICY_ACTION_MISSING = 4002
    REQUEST_KEY_COMPUTE_POLICY_ACTION_INVALID = 4003
    REQUEST_KEY_COMPUTE_POLICY_NAME_MISSING = 4004
    REQUEST_KEY_COMPUTE_POLICY_NAME_INVALID = 4005
    REQUEST_KEY_K8S_PROVIDER_MISSING = 4006
    REQUEST_KEY_K8S_PROVIDER_INVALID = 4007
    REQUEST_KEY_NETWORK_NAME_MISSING = 4008
    REQUEST_KEY_NETWORK_NAME_INVALID = 4009
    REQUEST_KEY_NODE_NAME_MISSING = 4010
    REQUEST_KEY_NODE_NAME_INVALID = 4011
    REQUEST_KEY_NODE_NAMES_LIST_MISSING = 4012
    REQUEST_KEY_NODE_NAMES_LIST_INVALID = 4013
    REQUEST_KEY_NUM_WORKERS_MISSING = 4014
    REQUEST_KEY_NUM_WORKERS_INVALID = 4015
    REQUEST_KEY_ORG_NAME_MISSING = 4016
    REQUEST_KEY_ORG_NAME_INVALID = 4017
    REQUEST_KEY_OVDC_ID_MISSING = 4018
    REQUEST_KEY_OVDC_ID_INVALID = 4019
    REQUEST_KEY_OVDC_NAME_MISSING = 4020
    REQUEST_KEY_OVDC_NAME_INVALID = 4021
    REQUEST_KEY_PKS_CLUSTER_DOMAIN_MISSING = 4022
    REQUEST_KEY_PKS_CLUSTER_DOMAIN_INVALID = 4023
    REQUEST_KEY_PKS_EXT_HOST_MISSING = 4024
    REQUEST_KEY_PKS_EXT_HOST_INVALID = 4025
    REQUEST_KEY_PKS_PLAN_NAME_MISSING = 4026
    REQUEST_KEY_PKS_PLAN_NAME_INVALID = 4027
    REQUEST_KEY_SERVER_ACTION_MISSING = 4028
    REQUEST_KEY_SERVER_ACTION_INVALID = 4029
