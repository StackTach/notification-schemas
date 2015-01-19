# notification-schemas
Primarily intended as an area for initial dev and discussion of schemas describing the various OpenStack notifications.

Currently this is all hand-coded based on captured notifications and/or examination of source code.

The nova schemas were derived by examining the [Notigen templates](https://github.com/Stackforge/stacktach-notigen).

There is some simple validation performed. Each schema file is validated against the draft 4 meta-schema. However this does not follow refs so there may still be uncaught errors.
