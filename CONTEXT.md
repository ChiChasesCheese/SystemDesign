# Trellis

A skeleton-constrained knowledge base for interview-grade study: one mind map
per subject decides what exists and in what order, and every piece of content —
recall prompts, source material, practice — hangs off a node of it.

## Language

### The map

**Skeleton**:
The single YAML mind map for one subject, and the only source of truth for what
topics exist, their study order, and their prerequisites.
_Avoid_: tree, outline, syllabus, curriculum

**Node**:
One topic in the skeleton. Its position fixes where its content is studied and
which Anki deck that content lands in.
_Avoid_: chapter, section, category

**Leaf**:
A node with no children — the unit content attaches to. A leaf is one interview
probe: narrow enough that "I'm weak here" names something specific to drill.
_Avoid_: subtopic, bucket

**Prerequisite**:
A `requires` edge from one node to another that must be understood first.
Validation guarantees no node is ordered before one of its prerequisites.
_Avoid_: dependency, blocker

**Domain**:
One subject with its own skeleton and content — `system-design`,
`low-level-design`. Domains are independent; nothing crosses between them except
ordinary wikilinks.
_Avoid_: deck, subject, area, vault

### The content

**Card**:
An atomic recall prompt (question/answer or cloze) attached to exactly one leaf.
The thing reviewed in spare minutes.
_Avoid_: note, flashcard, item

**Reading**:
A pointer to one authoritative external resource — its URL, why it is worth
reading, and what to take from it. Attaches to one or more nodes and is written
by us.
_Avoid_: link, source, reference, resource

**Clipping**:
A local markdown copy of the page a Reading points at, stored in the vault so
the material can be read offline inside Obsidian. Matched to its Reading by the
`source` URL, whether it was produced by `trellis clip` or by Obsidian's Web
Clipper.
_Avoid_: archive, cache, snapshot, offline copy

**Drill**:
An exercise that trains producing an answer rather than recalling one — a design
question or coding problem with constraints, grading points, and an attempt log.
Spans several nodes.
_Avoid_: exercise, problem, practice question

### The surfaces

**Vault**:
The one Obsidian vault at `vault/`, holding every domain. A domain's folder
inside it is its *content directory*, never "its vault".
_Avoid_: notes folder, library

**Map note**:
A generated note mirroring one node, listing its prerequisites, children, cards,
readings, and drills. Everything outside its managed block is the reader's own.
_Avoid_: index note, MOC, hub

**Go deeper**:
The footer on a built card carrying its node's readings — as `obsidian://` links
when the reading has been clipped, and as web links otherwise.
_Avoid_: sources, further reading, references

**Readable source**:
A reading whose page is archived in the vault as real prose (or as the paper
itself) and that is not a pointer at a book or an index. Engineering blogs,
company write-ups, papers, and single sections of a knowledge base qualify; a
book's homepage does not, unless what is archived is the chapter itself.
_Avoid_: good source, primary source

**Link coverage**:
The share of cards that have a road onward — an inline link, or a reading
inherited from their node or its ancestors. Tracked because a card with no way
deeper is a gap in the index.
_Avoid_: link rate, source coverage
