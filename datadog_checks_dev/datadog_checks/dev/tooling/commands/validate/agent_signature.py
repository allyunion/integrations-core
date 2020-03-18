# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import click

from ...utils import complete_valid_checks, get_valid_checks, has_legacy_signature
from ..console import CONTEXT_SETTINGS, echo_failure, echo_success


@click.command(
    'legacy-signature',
    context_settings=CONTEXT_SETTINGS,
    short_help='Validate that no integration uses the legacy signature',
)
@click.argument('check', autocompletion=complete_valid_checks, required=False)
def legacy_signature(check):
    """Validate that no integration uses the legacy signature."""
    if check:
        checks = [check]
    else:
        checks = sorted(get_valid_checks())

    has_failed = False
    for check in checks:
        if has_legacy_signature(check):
            has_failed = True
            echo_failure(f'Check {check} uses legacy agent signature.')
    if not has_failed:
        echo_success(f'All checks use the new agent signature.')
    return
