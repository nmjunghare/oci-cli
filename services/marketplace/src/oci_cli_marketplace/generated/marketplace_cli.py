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
from services.marketplace.src.oci_cli_marketplace.generated import marketplace_service_cli


@click.command(cli_util.override('marketplace.marketplace_root_group.command_name', 'marketplace'), cls=CommandGroupWithAlias, help=cli_util.override('marketplace.marketplace_root_group.help', """Use the Marketplace API to manage applications in Oracle Cloud Infrastructure Marketplace. For more information, see [Overview of Marketplace]"""), short_help=cli_util.override('marketplace.marketplace_root_group.short_help', """Marketplace Service API"""))
@cli_util.help_option_group
def marketplace_root_group():
    pass


@click.command(cli_util.override('marketplace.publication_summary_group.command_name', 'publication-summary'), cls=CommandGroupWithAlias, help="""The model for a summary of an Oracle Cloud Infrastructure publication.""")
@cli_util.help_option_group
def publication_summary_group():
    pass


@click.command(cli_util.override('marketplace.publication_package_group.command_name', 'publication-package'), cls=CommandGroupWithAlias, help="""A base object for all types of publication packages.""")
@cli_util.help_option_group
def publication_package_group():
    pass


@click.command(cli_util.override('marketplace.agreement_group.command_name', 'agreement'), cls=CommandGroupWithAlias, help="""The model for an end user license agreement.""")
@cli_util.help_option_group
def agreement_group():
    pass


@click.command(cli_util.override('marketplace.category_summary_group.command_name', 'category-summary'), cls=CommandGroupWithAlias, help="""The model for a summary of product categories for listings.""")
@cli_util.help_option_group
def category_summary_group():
    pass


@click.command(cli_util.override('marketplace.listing_package_summary_group.command_name', 'listing-package-summary'), cls=CommandGroupWithAlias, help="""The model for a summary of a package.""")
@cli_util.help_option_group
def listing_package_summary_group():
    pass


@click.command(cli_util.override('marketplace.tax_summary_group.command_name', 'tax-summary'), cls=CommandGroupWithAlias, help="""Tax implication that current tenant may be eligible while using specific listing""")
@cli_util.help_option_group
def tax_summary_group():
    pass


@click.command(cli_util.override('marketplace.report_collection_group.command_name', 'report-collection'), cls=CommandGroupWithAlias, help="""A collection of reports that match the parameters of the request.""")
@cli_util.help_option_group
def report_collection_group():
    pass


@click.command(cli_util.override('marketplace.listing_summary_group.command_name', 'listing-summary'), cls=CommandGroupWithAlias, help="""The model for a summary of an Oracle Cloud Infrastructure Marketplace listing.""")
@cli_util.help_option_group
def listing_summary_group():
    pass


@click.command(cli_util.override('marketplace.listing_package_group.command_name', 'listing-package'), cls=CommandGroupWithAlias, help="""A base object for all types of listing packages.""")
@cli_util.help_option_group
def listing_package_group():
    pass


@click.command(cli_util.override('marketplace.publication_group.command_name', 'publication'), cls=CommandGroupWithAlias, help="""The model for an Oracle Cloud Infrastructure Marketplace publication.""")
@cli_util.help_option_group
def publication_group():
    pass


@click.command(cli_util.override('marketplace.publisher_group.command_name', 'publisher'), cls=CommandGroupWithAlias, help="""The model for a publisher.""")
@cli_util.help_option_group
def publisher_group():
    pass


@click.command(cli_util.override('marketplace.report_type_collection_group.command_name', 'report-type-collection'), cls=CommandGroupWithAlias, help="""A collection of report types.""")
@cli_util.help_option_group
def report_type_collection_group():
    pass


@click.command(cli_util.override('marketplace.accepted_agreement_group.command_name', 'accepted-agreement'), cls=CommandGroupWithAlias, help="""The model for an accepted terms of use agreement.""")
@cli_util.help_option_group
def accepted_agreement_group():
    pass


@click.command(cli_util.override('marketplace.listing_group.command_name', 'listing'), cls=CommandGroupWithAlias, help="""The model for an Oracle Cloud Infrastructure Marketplace listing.""")
@cli_util.help_option_group
def listing_group():
    pass


marketplace_service_cli.marketplace_service_group.add_command(marketplace_root_group)
marketplace_root_group.add_command(publication_summary_group)
marketplace_root_group.add_command(publication_package_group)
marketplace_root_group.add_command(agreement_group)
marketplace_root_group.add_command(category_summary_group)
marketplace_root_group.add_command(listing_package_summary_group)
marketplace_root_group.add_command(tax_summary_group)
marketplace_root_group.add_command(report_collection_group)
marketplace_root_group.add_command(listing_summary_group)
marketplace_root_group.add_command(listing_package_group)
marketplace_root_group.add_command(publication_group)
marketplace_root_group.add_command(publisher_group)
marketplace_root_group.add_command(report_type_collection_group)
marketplace_root_group.add_command(accepted_agreement_group)
marketplace_root_group.add_command(listing_group)
# oci marketplace marketplace --> oci marketplace
marketplace_service_cli.marketplace_service_group.commands.pop(marketplace_root_group.name)
marketplace_service_cli.marketplace_service_group.add_command(publication_summary_group)
marketplace_service_cli.marketplace_service_group.add_command(publication_package_group)
marketplace_service_cli.marketplace_service_group.add_command(agreement_group)
marketplace_service_cli.marketplace_service_group.add_command(category_summary_group)
marketplace_service_cli.marketplace_service_group.add_command(listing_package_summary_group)
marketplace_service_cli.marketplace_service_group.add_command(tax_summary_group)
marketplace_service_cli.marketplace_service_group.add_command(report_collection_group)
marketplace_service_cli.marketplace_service_group.add_command(listing_summary_group)
marketplace_service_cli.marketplace_service_group.add_command(listing_package_group)
marketplace_service_cli.marketplace_service_group.add_command(publication_group)
marketplace_service_cli.marketplace_service_group.add_command(publisher_group)
marketplace_service_cli.marketplace_service_group.add_command(report_type_collection_group)
marketplace_service_cli.marketplace_service_group.add_command(accepted_agreement_group)
marketplace_service_cli.marketplace_service_group.add_command(listing_group)


@publication_group.command(name=cli_util.override('marketplace.change_publication_compartment.command_name', 'change-compartment'), help=u"""Moves the specified publication from one compartment to another. \n[Command Reference](changePublicationCompartment)""")
@cli_util.option('--publication-id', required=True, help=u"""The unique identifier for the publication.""")
@cli_util.option('--compartment-id', help=u"""The [OCID] of the compartment where you want to move the publication.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_publication_compartment(ctx, from_json, publication_id, compartment_id, if_match):

    if isinstance(publication_id, six.string_types) and len(publication_id.strip()) == 0:
        raise click.UsageError('Parameter --publication-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    result = client.change_publication_compartment(
        publication_id=publication_id,
        change_publication_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@accepted_agreement_group.command(name=cli_util.override('marketplace.create_accepted_agreement.command_name', 'create'), help=u"""Accepts a terms of use agreement for a specific package version of a listing. You must accept all terms of use for a package before you can deploy the package. \n[Command Reference](createAcceptedAgreement)""")
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier for the compartment where the agreement will be accepted.""")
@cli_util.option('--listing-id', required=True, help=u"""The unique identifier for the listing associated with the agreement.""")
@cli_util.option('--package-version', required=True, help=u"""The package version associated with the agreement.""")
@cli_util.option('--agreement-id', required=True, help=u"""The agreement to accept.""")
@cli_util.option('--signature', required=True, help=u"""A signature generated for the listing package agreements that you can retrieve with [GetAgreement].""")
@cli_util.option('--display-name', help=u"""A display name for the accepted agreement.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'marketplace', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'marketplace', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'marketplace', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'marketplace', 'class': 'dict(str, string)'}}, output_type={'module': 'marketplace', 'class': 'AcceptedAgreement'})
@cli_util.wrap_exceptions
def create_accepted_agreement(ctx, from_json, compartment_id, listing_id, package_version, agreement_id, signature, display_name, defined_tags, freeform_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['listingId'] = listing_id
    _details['packageVersion'] = package_version
    _details['agreementId'] = agreement_id
    _details['signature'] = signature

    if display_name is not None:
        _details['displayName'] = display_name

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    result = client.create_accepted_agreement(
        create_accepted_agreement_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@publication_group.command(name=cli_util.override('marketplace.create_publication.command_name', 'create'), help=u"""Creates a publication of the specified listing type with an optional default package. \n[Command Reference](createPublication)""")
@cli_util.option('--listing-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["COMMUNITY", "PARTNER", "PRIVATE"]), help=u"""The publisher category to which the publication belongs. The publisher category informs where the listing appears for use.""")
@cli_util.option('--name', required=True, help=u"""The name of the publication, which is also used in the listing.""")
@cli_util.option('--short-description', required=True, help=u"""A short description of the publication to use in the listing.""")
@cli_util.option('--support-contacts', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Contact information for getting support from the publisher for the listing.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where you want to create the publication.""")
@cli_util.option('--package-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-agreement-acknowledged', required=True, type=click.BOOL, help=u"""Whether the publisher acknowledged that they have the right and authority to share the contents of the publication and that they accepted the Oracle terms of use agreements required to create a publication.""")
@cli_util.option('--long-description', help=u"""A long description of the publication to use in the listing.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'support-contacts': {'module': 'marketplace', 'class': 'list[SupportContact]'}, 'package-details': {'module': 'marketplace', 'class': 'CreatePublicationPackage'}, 'defined-tags': {'module': 'marketplace', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'marketplace', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'support-contacts': {'module': 'marketplace', 'class': 'list[SupportContact]'}, 'package-details': {'module': 'marketplace', 'class': 'CreatePublicationPackage'}, 'defined-tags': {'module': 'marketplace', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'marketplace', 'class': 'dict(str, string)'}}, output_type={'module': 'marketplace', 'class': 'Publication'})
@cli_util.wrap_exceptions
def create_publication(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, listing_type, name, short_description, support_contacts, compartment_id, package_details, is_agreement_acknowledged, long_description, defined_tags, freeform_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['listingType'] = listing_type
    _details['name'] = name
    _details['shortDescription'] = short_description
    _details['supportContacts'] = cli_util.parse_json_parameter("support_contacts", support_contacts)
    _details['compartmentId'] = compartment_id
    _details['packageDetails'] = cli_util.parse_json_parameter("package_details", package_details)
    _details['isAgreementAcknowledged'] = is_agreement_acknowledged

    if long_description is not None:
        _details['longDescription'] = long_description

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    result = client.create_publication(
        create_publication_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_publication') and callable(getattr(client, 'get_publication')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_publication(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@publication_group.command(name=cli_util.override('marketplace.create_publication_create_image_publication_package.command_name', 'create-publication-create-image-publication-package'), help=u"""Creates a publication of the specified listing type with an optional default package. \n[Command Reference](createPublication)""")
@cli_util.option('--listing-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["COMMUNITY", "PARTNER", "PRIVATE"]), help=u"""The publisher category to which the publication belongs. The publisher category informs where the listing appears for use.""")
@cli_util.option('--name', required=True, help=u"""The name of the publication, which is also used in the listing.""")
@cli_util.option('--short-description', required=True, help=u"""A short description of the publication to use in the listing.""")
@cli_util.option('--support-contacts', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Contact information for getting support from the publisher for the listing.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment where you want to create the publication.""")
@cli_util.option('--is-agreement-acknowledged', required=True, type=click.BOOL, help=u"""Whether the publisher acknowledged that they have the right and authority to share the contents of the publication and that they accepted the Oracle terms of use agreements required to create a publication.""")
@cli_util.option('--package-details-package-version', required=True, help=u"""The package version.""")
@cli_util.option('--package-details-operating-system', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--package-details-eula', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The end user license agreeement (EULA) that consumers of this listing must accept.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--long-description', help=u"""A long description of the publication to use in the listing.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--package-details-image-id', help=u"""The unique identifier for the base image of the publication.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'support-contacts': {'module': 'marketplace', 'class': 'list[SupportContact]'}, 'defined-tags': {'module': 'marketplace', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'marketplace', 'class': 'dict(str, string)'}, 'package-details-operating-system': {'module': 'marketplace', 'class': 'OperatingSystem'}, 'package-details-eula': {'module': 'marketplace', 'class': 'list[Eula]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'support-contacts': {'module': 'marketplace', 'class': 'list[SupportContact]'}, 'defined-tags': {'module': 'marketplace', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'marketplace', 'class': 'dict(str, string)'}, 'package-details-operating-system': {'module': 'marketplace', 'class': 'OperatingSystem'}, 'package-details-eula': {'module': 'marketplace', 'class': 'list[Eula]'}}, output_type={'module': 'marketplace', 'class': 'Publication'})
@cli_util.wrap_exceptions
def create_publication_create_image_publication_package(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, listing_type, name, short_description, support_contacts, compartment_id, is_agreement_acknowledged, package_details_package_version, package_details_operating_system, package_details_eula, long_description, defined_tags, freeform_tags, package_details_image_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['packageDetails'] = {}
    _details['listingType'] = listing_type
    _details['name'] = name
    _details['shortDescription'] = short_description
    _details['supportContacts'] = cli_util.parse_json_parameter("support_contacts", support_contacts)
    _details['compartmentId'] = compartment_id
    _details['isAgreementAcknowledged'] = is_agreement_acknowledged
    _details['packageDetails']['packageVersion'] = package_details_package_version
    _details['packageDetails']['operatingSystem'] = cli_util.parse_json_parameter("package_details_operating_system", package_details_operating_system)
    _details['packageDetails']['eula'] = cli_util.parse_json_parameter("package_details_eula", package_details_eula)

    if long_description is not None:
        _details['longDescription'] = long_description

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if package_details_image_id is not None:
        _details['packageDetails']['imageId'] = package_details_image_id

    _details['packageDetails']['packageType'] = 'IMAGE'

    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    result = client.create_publication(
        create_publication_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_publication') and callable(getattr(client, 'get_publication')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_publication(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@accepted_agreement_group.command(name=cli_util.override('marketplace.delete_accepted_agreement.command_name', 'delete'), help=u"""Removes a previously accepted terms of use agreement from the list of agreements that Marketplace checks before initiating a deployment. Listings in Marketplace that require acceptance of the specified terms of use can no longer be deployed, but existing deployments aren't affected. \n[Command Reference](deleteAcceptedAgreement)""")
@cli_util.option('--accepted-agreement-id', required=True, help=u"""The unique identifier for the accepted terms of use agreement.""")
@cli_util.option('--signature', help=u"""Previously, the signature generated for the listing package terms of use agreement, but now deprecated and ignored.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_accepted_agreement(ctx, from_json, accepted_agreement_id, signature, if_match):

    if isinstance(accepted_agreement_id, six.string_types) and len(accepted_agreement_id.strip()) == 0:
        raise click.UsageError('Parameter --accepted-agreement-id cannot be whitespace or empty string')

    kwargs = {}
    if signature is not None:
        kwargs['signature'] = signature
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    result = client.delete_accepted_agreement(
        accepted_agreement_id=accepted_agreement_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@publication_group.command(name=cli_util.override('marketplace.delete_publication.command_name', 'delete'), help=u"""Deletes a publication, which also removes the associated listing from anywhere it was published, such as Marketplace or Compute. \n[Command Reference](deletePublication)""")
@cli_util.option('--publication-id', required=True, help=u"""The unique identifier for the publication.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_publication(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, publication_id, if_match):

    if isinstance(publication_id, six.string_types) and len(publication_id.strip()) == 0:
        raise click.UsageError('Parameter --publication-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    result = client.delete_publication(
        publication_id=publication_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_publication') and callable(getattr(client, 'get_publication')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_publication(publication_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@accepted_agreement_group.command(name=cli_util.override('marketplace.get_accepted_agreement.command_name', 'get'), help=u"""Gets the details of a specific, previously accepted terms of use agreement. \n[Command Reference](getAcceptedAgreement)""")
@cli_util.option('--accepted-agreement-id', required=True, help=u"""The unique identifier for the accepted terms of use agreement.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'AcceptedAgreement'})
@cli_util.wrap_exceptions
def get_accepted_agreement(ctx, from_json, accepted_agreement_id):

    if isinstance(accepted_agreement_id, six.string_types) and len(accepted_agreement_id.strip()) == 0:
        raise click.UsageError('Parameter --accepted-agreement-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    result = client.get_accepted_agreement(
        accepted_agreement_id=accepted_agreement_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@agreement_group.command(name=cli_util.override('marketplace.get_agreement.command_name', 'get'), help=u"""Returns a terms of use agreement for a package with a time-based signature that can be used to accept the agreement. \n[Command Reference](getAgreement)""")
@cli_util.option('--listing-id', required=True, help=u"""The unique identifier for the listing.""")
@cli_util.option('--package-version', required=True, help=u"""The version of the package. Package versions are unique within a listing.""")
@cli_util.option('--agreement-id', required=True, help=u"""The unique identifier for the agreement.""")
@cli_util.option('--compartment-id', help=u"""The unique identifier for the compartment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'Agreement'})
@cli_util.wrap_exceptions
def get_agreement(ctx, from_json, listing_id, package_version, agreement_id, compartment_id):

    if isinstance(listing_id, six.string_types) and len(listing_id.strip()) == 0:
        raise click.UsageError('Parameter --listing-id cannot be whitespace or empty string')

    if isinstance(package_version, six.string_types) and len(package_version.strip()) == 0:
        raise click.UsageError('Parameter --package-version cannot be whitespace or empty string')

    if isinstance(agreement_id, six.string_types) and len(agreement_id.strip()) == 0:
        raise click.UsageError('Parameter --agreement-id cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    result = client.get_agreement(
        listing_id=listing_id,
        package_version=package_version,
        agreement_id=agreement_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@listing_group.command(name=cli_util.override('marketplace.get_listing.command_name', 'get'), help=u"""Gets detailed information about a listing, including the listing's name, version, description, and resources.

If you plan to launch an instance from an image listing, you must first subscribe to the listing. When you launch the instance, you also need to provide the image ID of the listing resource version that you want.

Subscribing to the listing requires you to first get a signature from the terms of use agreement for the listing resource version. To get the signature, issue a [GetAppCatalogListingAgreements] API call. The [AppCatalogListingResourceVersionAgreements] object, including its signature, is returned in the response. With the signature for the terms of use agreement for the desired listing resource version, create a subscription by issuing a [CreateAppCatalogSubscription] API call.

To get the image ID to launch an instance, issue a [GetAppCatalogListingResourceVersion] API call. Lastly, to launch the instance, use the image ID of the listing resource version to issue a [LaunchInstance] API call. \n[Command Reference](getListing)""")
@cli_util.option('--listing-id', required=True, help=u"""The unique identifier for the listing.""")
@cli_util.option('--compartment-id', help=u"""The unique identifier for the compartment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'Listing'})
@cli_util.wrap_exceptions
def get_listing(ctx, from_json, listing_id, compartment_id):

    if isinstance(listing_id, six.string_types) and len(listing_id.strip()) == 0:
        raise click.UsageError('Parameter --listing-id cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    result = client.get_listing(
        listing_id=listing_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@listing_package_group.command(name=cli_util.override('marketplace.get_package.command_name', 'get-package'), help=u"""Get the details of the specified version of a package, including information needed to launch the package.

If you plan to launch an instance from an image listing, you must first subscribe to the listing. When you launch the instance, you also need to provide the image ID of the listing resource version that you want.

Subscribing to the listing requires you to first get a signature from the terms of use agreement for the listing resource version. To get the signature, issue a [GetAppCatalogListingAgreements] API call. The [AppCatalogListingResourceVersionAgreements] object, including its signature, is returned in the response. With the signature for the terms of use agreement for the desired listing resource version, create a subscription by issuing a [CreateAppCatalogSubscription] API call.

To get the image ID to launch an instance, issue a [GetAppCatalogListingResourceVersion] API call. Lastly, to launch the instance, use the image ID of the listing resource version to issue a [LaunchInstance] API call. \n[Command Reference](getPackage)""")
@cli_util.option('--listing-id', required=True, help=u"""The unique identifier for the listing.""")
@cli_util.option('--package-version', required=True, help=u"""The version of the package. Package versions are unique within a listing.""")
@cli_util.option('--compartment-id', help=u"""The unique identifier for the compartment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'ListingPackage'})
@cli_util.wrap_exceptions
def get_package(ctx, from_json, listing_id, package_version, compartment_id):

    if isinstance(listing_id, six.string_types) and len(listing_id.strip()) == 0:
        raise click.UsageError('Parameter --listing-id cannot be whitespace or empty string')

    if isinstance(package_version, six.string_types) and len(package_version.strip()) == 0:
        raise click.UsageError('Parameter --package-version cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    result = client.get_package(
        listing_id=listing_id,
        package_version=package_version,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@publication_group.command(name=cli_util.override('marketplace.get_publication.command_name', 'get'), help=u"""Gets the details of the specified publication. \n[Command Reference](getPublication)""")
@cli_util.option('--publication-id', required=True, help=u"""The unique identifier for the publication.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'Publication'})
@cli_util.wrap_exceptions
def get_publication(ctx, from_json, publication_id):

    if isinstance(publication_id, six.string_types) and len(publication_id.strip()) == 0:
        raise click.UsageError('Parameter --publication-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    result = client.get_publication(
        publication_id=publication_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@publication_package_group.command(name=cli_util.override('marketplace.get_publication_package.command_name', 'get'), help=u"""Gets the details of a specific package version within a given publication. \n[Command Reference](getPublicationPackage)""")
@cli_util.option('--publication-id', required=True, help=u"""The unique identifier for the publication.""")
@cli_util.option('--package-version', required=True, help=u"""The version of the package. Package versions are unique within a listing.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'PublicationPackage'})
@cli_util.wrap_exceptions
def get_publication_package(ctx, from_json, publication_id, package_version):

    if isinstance(publication_id, six.string_types) and len(publication_id.strip()) == 0:
        raise click.UsageError('Parameter --publication-id cannot be whitespace or empty string')

    if isinstance(package_version, six.string_types) and len(package_version.strip()) == 0:
        raise click.UsageError('Parameter --package-version cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    result = client.get_publication_package(
        publication_id=publication_id,
        package_version=package_version,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@accepted_agreement_group.command(name=cli_util.override('marketplace.list_accepted_agreements.command_name', 'list'), help=u"""Lists the terms of use agreements that have been accepted in the specified compartment. You can filter results by specifying query parameters. \n[Command Reference](listAcceptedAgreements)""")
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier for the compartment.""")
@cli_util.option('--display-name', help=u"""The display name of the resource.""")
@cli_util.option('--listing-id', help=u"""The unique identifier for the listing.""")
@cli_util.option('--package-version', help=u"""The version of the package. Package versions are unique within a listing.""")
@cli_util.option('--accepted-agreement-id', help=u"""The unique identifier for the accepted terms of use agreement.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMEACCEPTED"]), help=u"""The field to use to sort listed results. You can only specify one field to sort by. `TIMEACCEPTED` displays results in descending order by default. You can change your preference by specifying a different sort order.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either `ASC` or `DESC`.""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'list[AcceptedAgreementSummary]'})
@cli_util.wrap_exceptions
def list_accepted_agreements(ctx, from_json, all_pages, page_size, compartment_id, display_name, listing_id, package_version, accepted_agreement_id, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if listing_id is not None:
        kwargs['listing_id'] = listing_id
    if package_version is not None:
        kwargs['package_version'] = package_version
    if accepted_agreement_id is not None:
        kwargs['accepted_agreement_id'] = accepted_agreement_id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_accepted_agreements,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_accepted_agreements,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_accepted_agreements(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@agreement_group.command(name=cli_util.override('marketplace.list_agreements.command_name', 'list'), help=u"""Returns the terms of use agreements that must be accepted before you can deploy the specified version of a package. \n[Command Reference](listAgreements)""")
@cli_util.option('--listing-id', required=True, help=u"""The unique identifier for the listing.""")
@cli_util.option('--package-version', required=True, help=u"""The version of the package. Package versions are unique within a listing.""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--compartment-id', help=u"""The unique identifier for the compartment.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'list[AgreementSummary]'})
@cli_util.wrap_exceptions
def list_agreements(ctx, from_json, all_pages, page_size, listing_id, package_version, limit, page, compartment_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(listing_id, six.string_types) and len(listing_id.strip()) == 0:
        raise click.UsageError('Parameter --listing-id cannot be whitespace or empty string')

    if isinstance(package_version, six.string_types) and len(package_version.strip()) == 0:
        raise click.UsageError('Parameter --package-version cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_agreements,
            listing_id=listing_id,
            package_version=package_version,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_agreements,
            limit,
            page_size,
            listing_id=listing_id,
            package_version=package_version,
            **kwargs
        )
    else:
        result = client.list_agreements(
            listing_id=listing_id,
            package_version=package_version,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@category_summary_group.command(name=cli_util.override('marketplace.list_categories.command_name', 'list-categories'), help=u"""Gets the list of all the categories for listings published to Oracle Cloud Infrastructure Marketplace. Categories apply to the software product provided by the listing. \n[Command Reference](listCategories)""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--compartment-id', help=u"""The unique identifier for the compartment.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'list[CategorySummary]'})
@cli_util.wrap_exceptions
def list_categories(ctx, from_json, all_pages, page_size, limit, page, compartment_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_categories,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_categories,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_categories(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@listing_group.command(name=cli_util.override('marketplace.list_listings.command_name', 'list'), help=u"""Gets a list of listings from Oracle Cloud Infrastructure Marketplace by searching keywords and filtering according to listing attributes.

If you plan to launch an instance from an image listing, you must first subscribe to the listing. When you launch the instance, you also need to provide the image ID of the listing resource version that you want.

Subscribing to the listing requires you to first get a signature from the terms of use agreement for the listing resource version. To get the signature, issue a [GetAppCatalogListingAgreements] API call. The [AppCatalogListingResourceVersionAgreements] object, including its signature, is returned in the response. With the signature for the terms of use agreement for the desired listing resource version, create a subscription by issuing a [CreateAppCatalogSubscription] API call.

To get the image ID to launch an instance, issue a [GetAppCatalogListingResourceVersion] API call. Lastly, to launch the instance, use the image ID of the listing resource version to issue a [LaunchInstance] API call. \n[Command Reference](listListings)""")
@cli_util.option('--name', multiple=True, help=u"""The name of the listing.""")
@cli_util.option('--listing-id', help=u"""The unique identifier for the listing.""")
@cli_util.option('--image-id', help=u"""The image identifier of the listing.""")
@cli_util.option('--publisher-id', help=u"""Limit results to just this publisher.""")
@cli_util.option('--package-type', help=u"""A filter to return only packages that match the given package type exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMERELEASED"]), help=u"""The field to use to sort listed results. You can only specify one field to sort by. `TIMERELEASED` displays results in descending order by default. You can change your preference by specifying a different sort order.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either `ASC` or `DESC`.""")
@cli_util.option('--category', multiple=True, help=u"""Name of the product category or categories. If you specify multiple categories, then Marketplace returns any listing with one or more matching categories.""")
@cli_util.option('--pricing', type=custom_types.CliCaseInsensitiveChoice(["FREE", "BYOL", "PAYGO"]), multiple=True, help=u"""Name of the pricing type. If multiple pricing types are provided, then any listing with one or more matching pricing models will be returned.""")
@cli_util.option('--is-featured', type=click.BOOL, help=u"""Indicates whether to show only featured listings. If this is set to `false` or is omitted, then all listings will be returned.""")
@cli_util.option('--listing-types', type=custom_types.CliCaseInsensitiveChoice(["COMMUNITY", "PARTNER", "PRIVATE"]), multiple=True, help=u"""The type of the listing.""")
@cli_util.option('--operating-systems', multiple=True, help=u"""The operating system of the listing.""")
@cli_util.option('--compartment-id', help=u"""The unique identifier for the compartment.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'name': {'module': 'marketplace', 'class': 'list[string]'}, 'category': {'module': 'marketplace', 'class': 'list[string]'}, 'operating-systems': {'module': 'marketplace', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'name': {'module': 'marketplace', 'class': 'list[string]'}, 'category': {'module': 'marketplace', 'class': 'list[string]'}, 'operating-systems': {'module': 'marketplace', 'class': 'list[string]'}}, output_type={'module': 'marketplace', 'class': 'list[ListingSummary]'})
@cli_util.wrap_exceptions
def list_listings(ctx, from_json, all_pages, page_size, name, listing_id, image_id, publisher_id, package_type, limit, page, sort_by, sort_order, category, pricing, is_featured, listing_types, operating_systems, compartment_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None and len(name) > 0:
        kwargs['name'] = name
    if listing_id is not None:
        kwargs['listing_id'] = listing_id
    if image_id is not None:
        kwargs['image_id'] = image_id
    if publisher_id is not None:
        kwargs['publisher_id'] = publisher_id
    if package_type is not None:
        kwargs['package_type'] = package_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if category is not None and len(category) > 0:
        kwargs['category'] = category
    if pricing is not None and len(pricing) > 0:
        kwargs['pricing'] = pricing
    if is_featured is not None:
        kwargs['is_featured'] = is_featured
    if listing_types is not None and len(listing_types) > 0:
        kwargs['listing_types'] = listing_types
    if operating_systems is not None and len(operating_systems) > 0:
        kwargs['operating_systems'] = operating_systems
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_listings,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_listings,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_listings(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@listing_package_summary_group.command(name=cli_util.override('marketplace.list_packages.command_name', 'list-packages'), help=u"""Gets the list of packages for a listing.

If you plan to launch an instance from an image listing, you must first subscribe to the listing. When you launch the instance, you also need to provide the image ID of the listing resource version that you want.

Subscribing to the listing requires you to first get a signature from the terms of use agreement for the listing resource version. To get the signature, issue a [GetAppCatalogListingAgreements] API call. The [AppCatalogListingResourceVersionAgreements] object, including its signature, is returned in the response. With the signature for the terms of use agreement for the desired listing resource version, create a subscription by issuing a [CreateAppCatalogSubscription] API call.

To get the image ID to launch an instance, issue a [GetAppCatalogListingResourceVersion] API call. Lastly, to launch the instance, use the image ID of the listing resource version to issue a [LaunchInstance] API call. \n[Command Reference](listPackages)""")
@cli_util.option('--listing-id', required=True, help=u"""The unique identifier for the listing.""")
@cli_util.option('--package-version', help=u"""The version of the package. Package versions are unique within a listing.""")
@cli_util.option('--package-type', help=u"""A filter to return only packages that match the given package type exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMERELEASED"]), help=u"""The field to use to sort listed results. You can only specify one field to sort by. `TIMERELEASED` displays results in descending order by default. You can change your preference by specifying a different sort order.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either `ASC` or `DESC`.""")
@cli_util.option('--compartment-id', help=u"""The unique identifier for the compartment.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'list[ListingPackageSummary]'})
@cli_util.wrap_exceptions
def list_packages(ctx, from_json, all_pages, page_size, listing_id, package_version, package_type, limit, page, sort_by, sort_order, compartment_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(listing_id, six.string_types) and len(listing_id.strip()) == 0:
        raise click.UsageError('Parameter --listing-id cannot be whitespace or empty string')

    kwargs = {}
    if package_version is not None:
        kwargs['package_version'] = package_version
    if package_type is not None:
        kwargs['package_type'] = package_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_packages,
            listing_id=listing_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_packages,
            limit,
            page_size,
            listing_id=listing_id,
            **kwargs
        )
    else:
        result = client.list_packages(
            listing_id=listing_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@publication_package_group.command(name=cli_util.override('marketplace.list_publication_packages.command_name', 'list'), help=u"""Lists the packages in the specified publication. \n[Command Reference](listPublicationPackages)""")
@cli_util.option('--publication-id', required=True, help=u"""The unique identifier for the publication.""")
@cli_util.option('--package-version', help=u"""The version of the package. Package versions are unique within a listing.""")
@cli_util.option('--package-type', help=u"""A filter to return only packages that match the given package type exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMERELEASED"]), help=u"""The field to use to sort listed results. You can only specify one field to sort by. `TIMERELEASED` displays results in descending order by default. You can change your preference by specifying a different sort order.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either `ASC` or `DESC`.""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'list[PublicationPackageSummary]'})
@cli_util.wrap_exceptions
def list_publication_packages(ctx, from_json, all_pages, page_size, publication_id, package_version, package_type, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(publication_id, six.string_types) and len(publication_id.strip()) == 0:
        raise click.UsageError('Parameter --publication-id cannot be whitespace or empty string')

    kwargs = {}
    if package_version is not None:
        kwargs['package_version'] = package_version
    if package_type is not None:
        kwargs['package_type'] = package_type
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_publication_packages,
            publication_id=publication_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_publication_packages,
            limit,
            page_size,
            publication_id=publication_id,
            **kwargs
        )
    else:
        result = client.list_publication_packages(
            publication_id=publication_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@publication_summary_group.command(name=cli_util.override('marketplace.list_publications.command_name', 'list-publications'), help=u"""Lists the publications in the specified compartment. \n[Command Reference](listPublications)""")
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier for the compartment.""")
@cli_util.option('--listing-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["COMMUNITY", "PARTNER", "PRIVATE"]), help=u"""The type of the listing.""")
@cli_util.option('--name', multiple=True, help=u"""The name of the publication.""")
@cli_util.option('--publication-id', help=u"""The unique identifier for the publication.""")
@cli_util.option('--operating-systems', multiple=True, help=u"""The operating system of the listing.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMERELEASED"]), help=u"""The field to use to sort listed results. You can only specify one field to sort by. `TIMERELEASED` displays results in descending order by default. You can change your preference by specifying a different sort order.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either `ASC` or `DESC`.""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'name': {'module': 'marketplace', 'class': 'list[string]'}, 'operating-systems': {'module': 'marketplace', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'name': {'module': 'marketplace', 'class': 'list[string]'}, 'operating-systems': {'module': 'marketplace', 'class': 'list[string]'}}, output_type={'module': 'marketplace', 'class': 'list[PublicationSummary]'})
@cli_util.wrap_exceptions
def list_publications(ctx, from_json, all_pages, page_size, compartment_id, listing_type, name, publication_id, operating_systems, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None and len(name) > 0:
        kwargs['name'] = name
    if publication_id is not None:
        kwargs['publication_id'] = publication_id
    if operating_systems is not None and len(operating_systems) > 0:
        kwargs['operating_systems'] = operating_systems
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_publications,
            compartment_id=compartment_id,
            listing_type=listing_type,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_publications,
            limit,
            page_size,
            compartment_id=compartment_id,
            listing_type=listing_type,
            **kwargs
        )
    else:
        result = client.list_publications(
            compartment_id=compartment_id,
            listing_type=listing_type,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@publisher_group.command(name=cli_util.override('marketplace.list_publishers.command_name', 'list'), help=u"""Gets the list of all the publishers of listings available in Oracle Cloud Infrastructure Marketplace. \n[Command Reference](listPublishers)""")
@cli_util.option('--publisher-id', help=u"""Limit results to just this publisher.""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--compartment-id', help=u"""The unique identifier for the compartment.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'list[PublisherSummary]'})
@cli_util.wrap_exceptions
def list_publishers(ctx, from_json, all_pages, page_size, publisher_id, limit, page, compartment_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if publisher_id is not None:
        kwargs['publisher_id'] = publisher_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_publishers,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_publishers,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_publishers(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@report_type_collection_group.command(name=cli_util.override('marketplace.list_report_types.command_name', 'list-report-types'), help=u"""Lists available types of reports for the compartment. \n[Command Reference](listReportTypes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier for the compartment.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'ReportTypeCollection'})
@cli_util.wrap_exceptions
def list_report_types(ctx, from_json, all_pages, compartment_id, page):

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    if all_pages:
        result = cli_util.list_call_get_all_results(
            client.list_report_types,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_report_types(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@report_collection_group.command(name=cli_util.override('marketplace.list_reports.command_name', 'list-reports'), help=u"""Lists reports in the compartment that match the specified report type and date. \n[Command Reference](listReports)""")
@cli_util.option('--report-type', required=True, help=u"""The type of the report.""")
@cli_util.option('--date', required=True, type=custom_types.CLI_DATETIME, help=u"""Date, expressed in [RFC 3339] timestamp format. The service only interprets the year, month, and day parts in the input value, and ignores the hour, minute, and second parts.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier for the compartment.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'ReportCollection'})
@cli_util.wrap_exceptions
def list_reports(ctx, from_json, all_pages, report_type, date, compartment_id, page):

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    if all_pages:
        result = cli_util.list_call_get_all_results(
            client.list_reports,
            report_type=report_type,
            date=date,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_reports(
            report_type=report_type,
            date=date,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@tax_summary_group.command(name=cli_util.override('marketplace.list_taxes.command_name', 'list-taxes'), help=u"""Returns list of all tax implications that current tenant may be liable to once they launch the listing. \n[Command Reference](listTaxes)""")
@cli_util.option('--listing-id', required=True, help=u"""The unique identifier for the listing.""")
@cli_util.option('--compartment-id', help=u"""The unique identifier for the compartment.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'list[TaxSummary]'})
@cli_util.wrap_exceptions
def list_taxes(ctx, from_json, all_pages, listing_id, compartment_id):

    if isinstance(listing_id, six.string_types) and len(listing_id.strip()) == 0:
        raise click.UsageError('Parameter --listing-id cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    result = client.list_taxes(
        listing_id=listing_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@listing_summary_group.command(name=cli_util.override('marketplace.search_listings.command_name', 'search-listings'), help=u"""Queries all Marketplace Applications to find listings that match the specified criteria. To search for a listing, you can use a free text or structured search. \n[Command Reference](searchListings)""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["FreeText", "Structured"]), help=u"""The type of SearchDetails, whether FreeText or Structured.""")
@cli_util.option('--matching-context-type', type=custom_types.CliCaseInsensitiveChoice(["NONE", "HIGHLIGHTS"]), help=u"""The type of matching context returned in the response. If you specify HIGHLIGHTS, then the service will highlight fragments in its response. The default value is NONE.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'list[ListingSummary]'})
@cli_util.wrap_exceptions
def search_listings(ctx, from_json, type, matching_context_type, page, limit):

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    if matching_context_type is not None:
        _details['matchingContextType'] = matching_context_type

    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    result = client.search_listings(
        search_listings_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@listing_summary_group.command(name=cli_util.override('marketplace.search_listings_structured_search_details.command_name', 'search-listings-structured-search-details'), help=u"""Queries all Marketplace Applications to find listings that match the specified criteria. To search for a listing, you can use a free text or structured search. \n[Command Reference](searchListings)""")
@cli_util.option('--query-parameterconflict', required=True, help=u"""The structured query describing which resources to search for.""")
@cli_util.option('--matching-context-type', type=custom_types.CliCaseInsensitiveChoice(["NONE", "HIGHLIGHTS"]), help=u"""The type of matching context returned in the response. If you specify HIGHLIGHTS, then the service will highlight fragments in its response. The default value is NONE.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'list[ListingSummary]'})
@cli_util.wrap_exceptions
def search_listings_structured_search_details(ctx, from_json, query_parameterconflict, matching_context_type, page, limit):

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['query'] = query_parameterconflict

    if matching_context_type is not None:
        _details['matchingContextType'] = matching_context_type

    _details['type'] = 'Structured'

    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    result = client.search_listings(
        search_listings_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@listing_summary_group.command(name=cli_util.override('marketplace.search_listings_free_text_search_details.command_name', 'search-listings-free-text-search-details'), help=u"""Queries all Marketplace Applications to find listings that match the specified criteria. To search for a listing, you can use a free text or structured search. \n[Command Reference](searchListings)""")
@cli_util.option('--text', required=True, help=u"""The text to search for.""")
@cli_util.option('--matching-context-type', type=custom_types.CliCaseInsensitiveChoice(["NONE", "HIGHLIGHTS"]), help=u"""The type of matching context returned in the response. If you specify HIGHLIGHTS, then the service will highlight fragments in its response. The default value is NONE.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""How many records to return. Specify a value greater than zero and less than or equal to 1000. The default is 30.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace', 'class': 'list[ListingSummary]'})
@cli_util.wrap_exceptions
def search_listings_free_text_search_details(ctx, from_json, text, matching_context_type, page, limit):

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['text'] = text

    if matching_context_type is not None:
        _details['matchingContextType'] = matching_context_type

    _details['type'] = 'FreeText'

    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    result = client.search_listings(
        search_listings_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@accepted_agreement_group.command(name=cli_util.override('marketplace.update_accepted_agreement.command_name', 'update'), help=u"""Updates the display name or tags associated with a listing's previously accepted terms of use agreement. \n[Command Reference](updateAcceptedAgreement)""")
@cli_util.option('--accepted-agreement-id', required=True, help=u"""The unique identifier for the accepted terms of use agreement.""")
@cli_util.option('--display-name', help=u"""A display name for the accepted agreement.""")
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'defined-tags': {'module': 'marketplace', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'marketplace', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'marketplace', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'marketplace', 'class': 'dict(str, string)'}}, output_type={'module': 'marketplace', 'class': 'AcceptedAgreement'})
@cli_util.wrap_exceptions
def update_accepted_agreement(ctx, from_json, force, accepted_agreement_id, display_name, defined_tags, freeform_tags, if_match):

    if isinstance(accepted_agreement_id, six.string_types) and len(accepted_agreement_id.strip()) == 0:
        raise click.UsageError('Parameter --accepted-agreement-id cannot be whitespace or empty string')
    if not force:
        if defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    result = client.update_accepted_agreement(
        accepted_agreement_id=accepted_agreement_id,
        update_accepted_agreement_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@publication_group.command(name=cli_util.override('marketplace.update_publication.command_name', 'update'), help=u"""Updates the details of an existing publication. \n[Command Reference](updatePublication)""")
@cli_util.option('--publication-id', required=True, help=u"""The unique identifier for the publication.""")
@cli_util.option('--name', help=u"""The name of the publication, which is also used in the listing.""")
@cli_util.option('--short-description', help=u"""A short description of the publication to use in the listing.""")
@cli_util.option('--long-description', help=u"""A long description of the publication to use in the listing.""")
@cli_util.option('--support-contacts', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Contact information for getting support from the publisher for the listing.

This option is a JSON list with items of type SupportContact.  For documentation on SupportContact please see our API reference: https://docs.cloud.oracle.com/api/#/en/marketplace/20181001/datatypes/SupportContact.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'support-contacts': {'module': 'marketplace', 'class': 'list[SupportContact]'}, 'defined-tags': {'module': 'marketplace', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'marketplace', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'support-contacts': {'module': 'marketplace', 'class': 'list[SupportContact]'}, 'defined-tags': {'module': 'marketplace', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'marketplace', 'class': 'dict(str, string)'}}, output_type={'module': 'marketplace', 'class': 'Publication'})
@cli_util.wrap_exceptions
def update_publication(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, publication_id, name, short_description, long_description, support_contacts, defined_tags, freeform_tags, if_match):

    if isinstance(publication_id, six.string_types) and len(publication_id.strip()) == 0:
        raise click.UsageError('Parameter --publication-id cannot be whitespace or empty string')
    if not force:
        if support_contacts or defined_tags or freeform_tags:
            if not click.confirm("WARNING: Updates to support-contacts and defined-tags and freeform-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if name is not None:
        _details['name'] = name

    if short_description is not None:
        _details['shortDescription'] = short_description

    if long_description is not None:
        _details['longDescription'] = long_description

    if support_contacts is not None:
        _details['supportContacts'] = cli_util.parse_json_parameter("support_contacts", support_contacts)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    client = cli_util.build_client('marketplace', 'marketplace', ctx)
    result = client.update_publication(
        publication_id=publication_id,
        update_publication_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_publication') and callable(getattr(client, 'get_publication')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_publication(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
