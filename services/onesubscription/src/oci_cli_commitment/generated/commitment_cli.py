# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.onesubscription.src.oci_cli_onesubscription.generated import onesubscription_service_cli


@click.command(cli_util.override('commitment.commitment_root_group.command_name', 'commitment'), cls=CommandGroupWithAlias, help=cli_util.override('commitment.commitment_root_group.help', """OneSubscription APIs"""), short_help=cli_util.override('commitment.commitment_root_group.short_help', """OneSubscription APIs"""))
@cli_util.help_option_group
def commitment_root_group():
    pass


@click.command(cli_util.override('commitment.commitment_group.command_name', 'commitment'), cls=CommandGroupWithAlias, help="""Subscribed Service commitment summary""")
@cli_util.help_option_group
def commitment_group():
    pass


onesubscription_service_cli.onesubscription_service_group.add_command(commitment_root_group)
commitment_root_group.add_command(commitment_group)


@commitment_group.command(name=cli_util.override('commitment.get_commitment.command_name', 'get'), help=u"""This API returns the commitment details corresponding to the id provided \n[Command Reference](getCommitment)""")
@cli_util.option('--commitment-id', required=True, help=u"""The Commitment Id""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'onesubscription', 'class': 'Commitment'})
@cli_util.wrap_exceptions
def get_commitment(ctx, from_json, commitment_id):

    if isinstance(commitment_id, six.string_types) and len(commitment_id.strip()) == 0:
        raise click.UsageError('Parameter --commitment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('onesubscription', 'commitment', ctx)
    result = client.get_commitment(
        commitment_id=commitment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@commitment_group.command(name=cli_util.override('commitment.list_commitments.command_name', 'list'), help=u"""This list API returns all commitments for a particular Subscribed Service \n[Command Reference](listCommitments)""")
@cli_util.option('--subscribed-service-id', required=True, help=u"""This param is used to get the commitments for a particular subscribed service""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the root compartment.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call. Default: (`50`)

Example: '500'""")
@cli_util.option('--page', help=u"""The value of the 'opc-next-page' response header from the previous \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending ('ASC') or descending ('DESC').""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["ORDERNUMBER", "TIMEINVOICING"]), help=u"""The field to sort by. You can provide one sort order ('sortOrder').""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'onesubscription', 'class': 'list[CommitmentSummary]'})
@cli_util.wrap_exceptions
def list_commitments(ctx, from_json, all_pages, page_size, subscribed_service_id, compartment_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('onesubscription', 'commitment', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_commitments,
            subscribed_service_id=subscribed_service_id,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_commitments,
            limit,
            page_size,
            subscribed_service_id=subscribed_service_id,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_commitments(
            subscribed_service_id=subscribed_service_id,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
