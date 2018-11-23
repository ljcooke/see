# To do

## For v2.0.0

- Remove the `pattern` and `r` arguments (see `handle_deprecated_args`).

- Update `SeeResult.filter_ignoring_case` to support wildcard patterns
  and to require regular expression strings to be in the form `/pattern/`,
  to be consistent with `SeeResult.filter`.

- Update `SeeResult.exclude` to support wildcard patterns
  and to require regular expression strings to be in the form `/pattern/`,
  to be consistent with `SeeResult.filter`.
