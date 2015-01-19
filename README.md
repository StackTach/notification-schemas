# notification-schemas
Primarily intended as an area for initial dev and discussion of schemas describing the various OpenStack notifications.

Currently this is all hand-coded based on captured notifications and/or examination of source code.

The nova schemas were derived by examining the [Notigen templates](https://github.com/Stackforge/stacktach-notigen).

There is some simple validation performed. Each schema file is validated against the official [JSON meta-schemas](http://json-schema.org/documentation.html). Specifically the Draft 4 version as packaged with [python-jsonschema](https://pypi.python.org/pypi/jsonschema).

Note that this validation does not follow refs so there may still be uncaught errors in the event the refs are not pointing to the correct locations.
