---
id: ai-embeddings-as-coordinates
node: ai.foundations
type: cloze
---
An **embedding** is a fixed-length vector of floats (e.g. 1,536 dimensions) an embedding model produces for a piece of text — coordinates in a space where {{c1::semantic similarity becomes geometric distance}}, so "find related content" becomes {{c2::nearest-neighbor search}} over stored vectors. Two operational facts: embeddings are computed by a **separate, cheap model call** (not the chat model), and vectors from {{c3::different embedding models are incompatible}} — you can only compare vectors produced by the same model. This is the primitive underneath all vector search.
