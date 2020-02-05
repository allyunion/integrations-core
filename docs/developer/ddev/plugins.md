# Plugins

-----

## tox

Our [tox plugin](https://github.com/DataDog/integrations-core/blob/master/datadog_checks_dev/datadog_checks/dev/plugin/tox.py)
dynamically adds environments based on the presence of options defined in the `[testenv]` section of each integration's
`tox.ini` file.

### Style

Setting `dd_check_style` to `true` will enable 2 environments for enforcing our [style conventions](../guidelines/style.md):

1. `style` - This will check the formatting and will error if any issues are found. You may use the `-s/--style` flag
   of `ddev test` to execute only this environment.
2. `format_style` - This will format the code for you, resolving the most common issues caught by `style` environment.
   You can run the formatter by using the `-fs/--format-style` flag of `ddev test`.

## pytest



### Environment manager

### Agent check runner
