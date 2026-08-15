# Obsidian is the reading surface; Anki links into it

Cards used to send you to a browser to read anything deeper, which meant a
third app, a different typography, and no offline copy. We now clip each
reading's page into the vault and point cards at the local copy with an
`obsidian://open?vault=…&file=…` link, keeping the original web URL beside it
as a fallback — so reviewing, reading, and note-taking all happen in Obsidian.

**Consequences.** The vault directory's name (`vault`) is baked into thousands
of card fields, so renaming it breaks every deep link until the decks are
rebuilt and re-imported. The same name must exist on every device that reviews
the deck, and the clippings must be synced there — on iOS that means an
Obsidian vault named `vault` fed by Obsidian Sync, iCloud, or a git client.
Clipped pages are other people's writing: they stay out of git (this repo is
public) and are regenerated locally with `trellis clip`.
