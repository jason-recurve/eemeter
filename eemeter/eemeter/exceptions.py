#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

   Copyright 2014-2023 OpenEEmeter contributors

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""
__all__ = (
    "EEMeterError",
    "NoBaselineDataError",
    "NoReportingDataError",
    "MissingModelParameterError",
    "UnrecognizedModelTypeError",
)


class EEMeterError(Exception):
    """Base class for EEmeter library errors."""

    pass


class NoBaselineDataError(EEMeterError):
    """Error indicating lack of baseline data."""

    pass


class NoReportingDataError(EEMeterError):
    """Error indicating lack of reporting data."""

    pass


class MissingModelParameterError(EEMeterError):
    """Error indicating missing model parameter."""

    pass


class UnrecognizedModelTypeError(EEMeterError):
    """Error indicating unrecognized model type."""

    pass


class DataSufficiencyError(EEMeterError):
    """Error indicating insufficient data to fit model on."""

    pass


class PoorModelFitError(EEMeterError):
    """Error indicating attempt to predict with a poorly fit model."""

    pass