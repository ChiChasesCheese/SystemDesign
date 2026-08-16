---
nodes: [networking.cdn, storage.object, architecture.serverless, foundations.estimation, foundations.numbers]
tags: [classic, flagship]
---
# Drill: Design a video platform

Upload, transcode, and stream video to a global audience. The design is
decided by two numbers — the size of the media and the cost of moving it —
so this is the drill where estimation is not a warm-up but the answer.

**Constraints to state and honor**
- 500 hours of video uploaded per minute; a 10-minute 1080p source is ~1 GB.
- Playback starts within 2 seconds, worldwide, and adapts to a phone dropping from wifi to 4G.
- Transcoding produces 6 renditions per source; a failed transcode must not lose the upload.
- Egress is the dominant cost line. Design decisions that halve it are worth naming.

**Grading points**
- Storage and egress estimated first, and the estimate used to argue for the CDN rather than to decorate it ([[foundations-storage-estimate-method]], [[foundations-when-estimates-change-design]]).
- Uploads going straight to object storage with multipart and resumability, never through the application tier ([[storage-multipart-ranged-io]], [[storage-object-vs-filesystem]], [[storage-compute-separation]]).
- Conditional writes or object versioning used so a retried upload cannot half-overwrite a source ([[storage-s3-conditional-writes]]).
- Transcoding as a fan-out of independent jobs — the textbook fit for elastic, bursty, stateless compute, with cold starts and the timeout ceiling named ([[architecture-serverless-constraints]], [[architecture-cold-starts]], [[architecture-serverless-economics]]).
- The transcode pipeline made restartable per rendition, with orchestration that survives a worker dying mid-job ([[architecture-serverless-orchestration]], [[architecture-serverless-backpressure]]).
- Segmented delivery (HLS/DASH) explained as what makes adaptive bitrate and CDN caching possible at all ([[networking-cdn-what-belongs-at-edge]], [[networking-push-vs-pull-cdn]]).
- Cache key and versioning discipline for renditions, so re-encoding a title does not require a global purge ([[networking-cdn-cache-key]], [[networking-cdn-purge-vs-versioning]]).
- Bandwidth arithmetic sanity-checked against real numbers — how much a single edge node can actually serve ([[foundations-latency-sequential-reads]], [[storage-s3-numbers]]).

**Attempt log**
- [ ] Attempt 1 (date, 40 min, self-graded notes):
