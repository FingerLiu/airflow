#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from __future__ import annotations

import unittest

from airflow.providers.amazon.aws.hooks.sqs import SqsHook

try:
    from moto import mock_sqs
except ImportError:
    mock_sqs = None


@unittest.skipIf(mock_sqs is None, "moto sqs package missing")
class TestSqsHook(unittest.TestCase):
    @mock_sqs
    def test_get_conn(self):
        hook = SqsHook(aws_conn_id="aws_default")
        assert hook.get_conn() is not None
