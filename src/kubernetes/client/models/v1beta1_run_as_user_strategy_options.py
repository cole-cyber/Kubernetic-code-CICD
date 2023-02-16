# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1RunAsUserStrategyOptions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, ranges=None, rule=None):
        """
        V1beta1RunAsUserStrategyOptions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ranges': 'list[V1beta1IDRange]',
            'rule': 'str'
        }

        self.attribute_map = {
            'ranges': 'ranges',
            'rule': 'rule'
        }

        self._ranges = ranges
        self._rule = rule

    @property
    def ranges(self):
        """
        Gets the ranges of this V1beta1RunAsUserStrategyOptions.
        Ranges are the allowed ranges of uids that may be used.

        :return: The ranges of this V1beta1RunAsUserStrategyOptions.
        :rtype: list[V1beta1IDRange]
        """
        return self._ranges

    @ranges.setter
    def ranges(self, ranges):
        """
        Sets the ranges of this V1beta1RunAsUserStrategyOptions.
        Ranges are the allowed ranges of uids that may be used.

        :param ranges: The ranges of this V1beta1RunAsUserStrategyOptions.
        :type: list[V1beta1IDRange]
        """

        self._ranges = ranges

    @property
    def rule(self):
        """
        Gets the rule of this V1beta1RunAsUserStrategyOptions.
        Rule is the strategy that will dictate the allowable RunAsUser values that may be set.

        :return: The rule of this V1beta1RunAsUserStrategyOptions.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """
        Sets the rule of this V1beta1RunAsUserStrategyOptions.
        Rule is the strategy that will dictate the allowable RunAsUser values that may be set.

        :param rule: The rule of this V1beta1RunAsUserStrategyOptions.
        :type: str
        """
        if rule is None:
            raise ValueError("Invalid value for `rule`, must not be `None`")

        self._rule = rule

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta1RunAsUserStrategyOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
