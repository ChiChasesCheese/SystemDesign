# Obsidian is the reading surface; Anki links into it

Cards used to send you to a browser to read anything deeper, which meant a
third app, a different typography, and no offline copy. Cards now carry an
`obsidian://open?vault=…&file=…` link to the **reading note**, whose managed
tail embeds the archived article — so reviewing, reading, and note-taking all
happen in Obsidian, with the web original kept one ↗ away.

**Why the link names a note instead of a path.** Devices disagree about where
the vault root is: a phone syncing through a git client clones the whole
repository (root = repo), while the laptop opens `vault/` directly. A bare
name is resolved by Obsidian wherever the note sits, so one link works on
both — at the cost of requiring names to be unique across the vault, which is
why a clipping is stored as `<reading>-clip` rather than reusing its
reading's name.

**Consequences.** The vault must be named `vault` on every device, since that
name travels inside thousands of card fields. Reading notes are committed, so
the link always lands somewhere useful even when the clipped article is
missing. Clippings themselves stay out of git — they are other people's
writing and this repo is public — so they reach a phone only through Obsidian
Sync/iCloud, or by making the repo private and dropping the ignore rule.
