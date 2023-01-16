# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.osp_gateway import InvoiceServiceClient

MODULE_TO_TYPE_MAPPINGS["osp_gateway"] = oci.osp_gateway.models.osp_gateway_type_mapping
if CLIENT_MAP.get("osp_gateway") is None:
    CLIENT_MAP["osp_gateway"] = {}
CLIENT_MAP["osp_gateway"]["invoice_service"] = InvoiceServiceClient
