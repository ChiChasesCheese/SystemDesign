---
id: ai-hnsw-vs-ivf
node: ai.vector-search
type: qa
---
## Q
HNSW vs IVF for a vector index: how does each search, and what pushes you from HNSW to IVF(+PQ)?

## A
- **HNSW**: multi-layer graph of neighbors; search greedily descends from sparse top layers to the dense bottom. Best recall/latency at query time and supports incremental inserts — but the graph lives in **RAM**, roughly (vector + neighbor links) per point.
- **IVF**: cluster the space (k-means); search only the `nprobe` closest clusters. Cheaper memory, and with **product quantization** vectors compress ~10–50x, enabling billion-scale and disk-based serving — at some recall cost.

Switch when memory, not latency, is the binding constraint (typically ≥ hundreds of millions of vectors).
