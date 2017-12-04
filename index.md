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

# Managing git submodules

Git submodules are a nice feature for reusing git repositories. It allows users
to embed git repositories into other git repositories. But it's user interface
doesn't seem to be much intuitive -- as the amount of [related Stack Overflow
questions][so-git-submodules] suggests.

For now, Gitless does not support managing git submodules. The following
sections propose how this support may be implemented in Gitless such that its
interface gets intuitive enough for turning the feature into an easy-to-use one
even for inexperienced git users.

### Initializing parent repository's submodules

Repository's submodules aren't initialized by default when cloning or fetching
new versions of a git repository using git. Users must manage them in a separate
fashion.

This behavior may seem unintuitive for novice users and forces them to learn
about additional concepts and commands flags in order to effectively make use of
the submodule feature -- also fostering [q&a][so-git-clone-including-submodules]
with thousands of views and votes.

#### What happens in git

When user clones or update a git repository which holds other git repositories
within it (through the git submodules feature) using the default commands (i.e.
without any flags for also initializing submodules) such as

    $ git clone git@github.com:user/gitrepo

the inner repositories appear as if they were empty.

<script type="text/javascript" src="https://asciinema.org/a/150977.js"
id="asciicast-150977" async></script>

#### What may happen in gitless

*Note: these modifications are undergoing design. Refer to [gitless/#56][gl-56]
for more info.*

Submodules are initialized by default when the repository including them is
initialized or updated. A simple

    $ mkdir gitrepo && cd gitrepo
    $ gl init gitrepo

should lead to an initialized git repository including all their submodules'
up-to-date contents.

[git]: http://git-scm.com/
[gitless]: http://gitless.com
[so-q-add-empty-dir]: https://stackoverflow.com/questions/115983
[gl-pr-157]: https://github.com/sdg-mit/gitless/pull/157
[gl-56]: https://github.com/sdg-mit/gitless/issues/56
[so-git-submodules]: https://stackoverflow.com/questions/tagged/git-submodules
[so-git-clone-including-submodules]: https://stackoverflow.com/questions/3796927
