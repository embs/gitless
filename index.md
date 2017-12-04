---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: home
---

*[Git][git] is a powerful and ubiquotous tool for version
control. [Gitless][gitless] builds on it to provide first-time users a more
pleasant experience. This page describes some challenging situations novice
users may face when trying to perform some tasks using git and how we can ease
them through Gitless.*

# Tracking empty directories

Git is meant for managing files only. This makes users unable of tracking
directories which have nothing inside (but some other directories perhaps).
This limitation may sound unintuitive for novice users and has made many people
adopt workarounds -- as disposed in this popular [Stack Overflow
question][so-q-add-empty-dir].

#### What happens in git

When user creates an empty directory (or a nested structure of empty
directories) and issues a git command like, for instance,

    $ git add src/main/java

in an attempt of staging these empty directories structures for committing
them into their's git repository, nothing happens: directory is not staged and
there is no feedback message neither.

<script type="text/javascript" src="https://asciinema.org/a/150948.js"
id="asciicast-150948" async></script>

#### What may happen in gitless

*Note: these modifications are undergoing implementation. Refer to
[gitless/#157][gl-pr-157] for more info.*

Users can track their empty directories structures in gitless using the same
command for tracking files: `gl track`. When they do so, tracked empty
directories can be committed and published as any other versioned files.

<script type="text/javascript" src="https://asciinema.org/a/150958.js"
id="asciicast-150958" async></script>

As expected, the tracked directories are included when updating or initializing
from a remote repository which has some of them:

<script type="text/javascript" src="https://asciinema.org/a/150961.js"
id="asciicast-150961" async></script>

[git]: http://git-scm.com/
[gitless]: http://gitless.com
[so-q-add-empty-dir]: https://stackoverflow.com/questions/115983
[gl-pr-157]: https://github.com/sdg-mit/gitless/pull/157
