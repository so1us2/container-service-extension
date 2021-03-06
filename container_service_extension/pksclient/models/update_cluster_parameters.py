# coding: utf-8

"""
    PKS

    PKS API  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UpdateClusterParameters(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'kubernetes_worker_instances': 'int',
        'kubernetes_profile_name': 'str',
        'network_profile_name': 'str',
        'kubelet_drain_timeout': 'str',
        'kubelet_drain_grace_period': 'str',
        'kubelet_drain_force': 'str',
        'kubelet_drain_ignore_daemonsets': 'str',
        'kubelet_drain_delete_local_data': 'str',
        'kubelet_drain_force_node': 'str',
        'insecure_registries': 'list[str]',
        'custom_ca_certs': 'list[CustomCaCert]',
        'cluster_tags': 'list[ClusterTag]',
        'delete_all_tags': 'bool'
    }

    attribute_map = {
        'kubernetes_worker_instances': 'kubernetes_worker_instances',
        'kubernetes_profile_name': 'kubernetes_profile_name',
        'network_profile_name': 'network_profile_name',
        'kubelet_drain_timeout': 'kubelet_drain_timeout',
        'kubelet_drain_grace_period': 'kubelet_drain_grace_period',
        'kubelet_drain_force': 'kubelet_drain_force',
        'kubelet_drain_ignore_daemonsets': 'kubelet_drain_ignore_daemonsets',
        'kubelet_drain_delete_local_data': 'kubelet_drain_delete_local_data',
        'kubelet_drain_force_node': 'kubelet_drain_force_node',
        'insecure_registries': 'insecure_registries',
        'custom_ca_certs': 'custom_ca_certs',
        'cluster_tags': 'cluster_tags',
        'delete_all_tags': 'delete_all_tags'
    }

    def __init__(self, kubernetes_worker_instances=None, kubernetes_profile_name=None, network_profile_name=None, kubelet_drain_timeout=None, kubelet_drain_grace_period=None, kubelet_drain_force=None, kubelet_drain_ignore_daemonsets=None, kubelet_drain_delete_local_data=None, kubelet_drain_force_node=None, insecure_registries=None, custom_ca_certs=None, cluster_tags=None, delete_all_tags=False):  # noqa: E501
        """UpdateClusterParameters - a model defined in Swagger"""  # noqa: E501

        self._kubernetes_worker_instances = None
        self._kubernetes_profile_name = None
        self._network_profile_name = None
        self._kubelet_drain_timeout = None
        self._kubelet_drain_grace_period = None
        self._kubelet_drain_force = None
        self._kubelet_drain_ignore_daemonsets = None
        self._kubelet_drain_delete_local_data = None
        self._kubelet_drain_force_node = None
        self._insecure_registries = None
        self._custom_ca_certs = None
        self._cluster_tags = None
        self._delete_all_tags = None
        self.discriminator = None

        if kubernetes_worker_instances is not None:
            self.kubernetes_worker_instances = kubernetes_worker_instances
        if kubernetes_profile_name is not None:
            self.kubernetes_profile_name = kubernetes_profile_name
        if network_profile_name is not None:
            self.network_profile_name = network_profile_name
        if kubelet_drain_timeout is not None:
            self.kubelet_drain_timeout = kubelet_drain_timeout
        if kubelet_drain_grace_period is not None:
            self.kubelet_drain_grace_period = kubelet_drain_grace_period
        if kubelet_drain_force is not None:
            self.kubelet_drain_force = kubelet_drain_force
        if kubelet_drain_ignore_daemonsets is not None:
            self.kubelet_drain_ignore_daemonsets = kubelet_drain_ignore_daemonsets
        if kubelet_drain_delete_local_data is not None:
            self.kubelet_drain_delete_local_data = kubelet_drain_delete_local_data
        if kubelet_drain_force_node is not None:
            self.kubelet_drain_force_node = kubelet_drain_force_node
        if insecure_registries is not None:
            self.insecure_registries = insecure_registries
        if custom_ca_certs is not None:
            self.custom_ca_certs = custom_ca_certs
        if cluster_tags is not None:
            self.cluster_tags = cluster_tags
        if delete_all_tags is not None:
            self.delete_all_tags = delete_all_tags

    @property
    def kubernetes_worker_instances(self):
        """Gets the kubernetes_worker_instances of this UpdateClusterParameters.  # noqa: E501


        :return: The kubernetes_worker_instances of this UpdateClusterParameters.  # noqa: E501
        :rtype: int
        """
        return self._kubernetes_worker_instances

    @kubernetes_worker_instances.setter
    def kubernetes_worker_instances(self, kubernetes_worker_instances):
        """Sets the kubernetes_worker_instances of this UpdateClusterParameters.


        :param kubernetes_worker_instances: The kubernetes_worker_instances of this UpdateClusterParameters.  # noqa: E501
        :type: int
        """
        if kubernetes_worker_instances is not None and kubernetes_worker_instances < 1:  # noqa: E501
            raise ValueError("Invalid value for `kubernetes_worker_instances`, must be a value greater than or equal to `1`")  # noqa: E501

        self._kubernetes_worker_instances = kubernetes_worker_instances

    @property
    def kubernetes_profile_name(self):
        """Gets the kubernetes_profile_name of this UpdateClusterParameters.  # noqa: E501


        :return: The kubernetes_profile_name of this UpdateClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._kubernetes_profile_name

    @kubernetes_profile_name.setter
    def kubernetes_profile_name(self, kubernetes_profile_name):
        """Sets the kubernetes_profile_name of this UpdateClusterParameters.


        :param kubernetes_profile_name: The kubernetes_profile_name of this UpdateClusterParameters.  # noqa: E501
        :type: str
        """

        self._kubernetes_profile_name = kubernetes_profile_name

    @property
    def network_profile_name(self):
        """Gets the network_profile_name of this UpdateClusterParameters.  # noqa: E501


        :return: The network_profile_name of this UpdateClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._network_profile_name

    @network_profile_name.setter
    def network_profile_name(self, network_profile_name):
        """Sets the network_profile_name of this UpdateClusterParameters.


        :param network_profile_name: The network_profile_name of this UpdateClusterParameters.  # noqa: E501
        :type: str
        """

        self._network_profile_name = network_profile_name

    @property
    def kubelet_drain_timeout(self):
        """Gets the kubelet_drain_timeout of this UpdateClusterParameters.  # noqa: E501


        :return: The kubelet_drain_timeout of this UpdateClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._kubelet_drain_timeout

    @kubelet_drain_timeout.setter
    def kubelet_drain_timeout(self, kubelet_drain_timeout):
        """Sets the kubelet_drain_timeout of this UpdateClusterParameters.


        :param kubelet_drain_timeout: The kubelet_drain_timeout of this UpdateClusterParameters.  # noqa: E501
        :type: str
        """

        self._kubelet_drain_timeout = kubelet_drain_timeout

    @property
    def kubelet_drain_grace_period(self):
        """Gets the kubelet_drain_grace_period of this UpdateClusterParameters.  # noqa: E501


        :return: The kubelet_drain_grace_period of this UpdateClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._kubelet_drain_grace_period

    @kubelet_drain_grace_period.setter
    def kubelet_drain_grace_period(self, kubelet_drain_grace_period):
        """Sets the kubelet_drain_grace_period of this UpdateClusterParameters.


        :param kubelet_drain_grace_period: The kubelet_drain_grace_period of this UpdateClusterParameters.  # noqa: E501
        :type: str
        """

        self._kubelet_drain_grace_period = kubelet_drain_grace_period

    @property
    def kubelet_drain_force(self):
        """Gets the kubelet_drain_force of this UpdateClusterParameters.  # noqa: E501


        :return: The kubelet_drain_force of this UpdateClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._kubelet_drain_force

    @kubelet_drain_force.setter
    def kubelet_drain_force(self, kubelet_drain_force):
        """Sets the kubelet_drain_force of this UpdateClusterParameters.


        :param kubelet_drain_force: The kubelet_drain_force of this UpdateClusterParameters.  # noqa: E501
        :type: str
        """

        self._kubelet_drain_force = kubelet_drain_force

    @property
    def kubelet_drain_ignore_daemonsets(self):
        """Gets the kubelet_drain_ignore_daemonsets of this UpdateClusterParameters.  # noqa: E501


        :return: The kubelet_drain_ignore_daemonsets of this UpdateClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._kubelet_drain_ignore_daemonsets

    @kubelet_drain_ignore_daemonsets.setter
    def kubelet_drain_ignore_daemonsets(self, kubelet_drain_ignore_daemonsets):
        """Sets the kubelet_drain_ignore_daemonsets of this UpdateClusterParameters.


        :param kubelet_drain_ignore_daemonsets: The kubelet_drain_ignore_daemonsets of this UpdateClusterParameters.  # noqa: E501
        :type: str
        """

        self._kubelet_drain_ignore_daemonsets = kubelet_drain_ignore_daemonsets

    @property
    def kubelet_drain_delete_local_data(self):
        """Gets the kubelet_drain_delete_local_data of this UpdateClusterParameters.  # noqa: E501


        :return: The kubelet_drain_delete_local_data of this UpdateClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._kubelet_drain_delete_local_data

    @kubelet_drain_delete_local_data.setter
    def kubelet_drain_delete_local_data(self, kubelet_drain_delete_local_data):
        """Sets the kubelet_drain_delete_local_data of this UpdateClusterParameters.


        :param kubelet_drain_delete_local_data: The kubelet_drain_delete_local_data of this UpdateClusterParameters.  # noqa: E501
        :type: str
        """

        self._kubelet_drain_delete_local_data = kubelet_drain_delete_local_data

    @property
    def kubelet_drain_force_node(self):
        """Gets the kubelet_drain_force_node of this UpdateClusterParameters.  # noqa: E501


        :return: The kubelet_drain_force_node of this UpdateClusterParameters.  # noqa: E501
        :rtype: str
        """
        return self._kubelet_drain_force_node

    @kubelet_drain_force_node.setter
    def kubelet_drain_force_node(self, kubelet_drain_force_node):
        """Sets the kubelet_drain_force_node of this UpdateClusterParameters.


        :param kubelet_drain_force_node: The kubelet_drain_force_node of this UpdateClusterParameters.  # noqa: E501
        :type: str
        """

        self._kubelet_drain_force_node = kubelet_drain_force_node

    @property
    def insecure_registries(self):
        """Gets the insecure_registries of this UpdateClusterParameters.  # noqa: E501


        :return: The insecure_registries of this UpdateClusterParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._insecure_registries

    @insecure_registries.setter
    def insecure_registries(self, insecure_registries):
        """Sets the insecure_registries of this UpdateClusterParameters.


        :param insecure_registries: The insecure_registries of this UpdateClusterParameters.  # noqa: E501
        :type: list[str]
        """

        self._insecure_registries = insecure_registries

    @property
    def custom_ca_certs(self):
        """Gets the custom_ca_certs of this UpdateClusterParameters.  # noqa: E501


        :return: The custom_ca_certs of this UpdateClusterParameters.  # noqa: E501
        :rtype: list[CustomCaCert]
        """
        return self._custom_ca_certs

    @custom_ca_certs.setter
    def custom_ca_certs(self, custom_ca_certs):
        """Sets the custom_ca_certs of this UpdateClusterParameters.


        :param custom_ca_certs: The custom_ca_certs of this UpdateClusterParameters.  # noqa: E501
        :type: list[CustomCaCert]
        """

        self._custom_ca_certs = custom_ca_certs

    @property
    def cluster_tags(self):
        """Gets the cluster_tags of this UpdateClusterParameters.  # noqa: E501


        :return: The cluster_tags of this UpdateClusterParameters.  # noqa: E501
        :rtype: list[ClusterTag]
        """
        return self._cluster_tags

    @cluster_tags.setter
    def cluster_tags(self, cluster_tags):
        """Sets the cluster_tags of this UpdateClusterParameters.


        :param cluster_tags: The cluster_tags of this UpdateClusterParameters.  # noqa: E501
        :type: list[ClusterTag]
        """

        self._cluster_tags = cluster_tags

    @property
    def delete_all_tags(self):
        """Gets the delete_all_tags of this UpdateClusterParameters.  # noqa: E501


        :return: The delete_all_tags of this UpdateClusterParameters.  # noqa: E501
        :rtype: bool
        """
        return self._delete_all_tags

    @delete_all_tags.setter
    def delete_all_tags(self, delete_all_tags):
        """Sets the delete_all_tags of this UpdateClusterParameters.


        :param delete_all_tags: The delete_all_tags of this UpdateClusterParameters.  # noqa: E501
        :type: bool
        """

        self._delete_all_tags = delete_all_tags

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UpdateClusterParameters, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateClusterParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
