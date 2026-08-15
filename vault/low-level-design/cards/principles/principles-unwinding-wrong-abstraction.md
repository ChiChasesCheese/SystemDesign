---
id: principles-unwinding-wrong-abstraction
node: principles.simplicity
type: qa
---
## Q
A shared helper now takes `(input, boolean isLegacy, Mode mode)` and branches on them; the fourth caller needs a fifth flag. What's the prescribed fix, and why isn't it "add the flag"?

## A
The flags are the abstraction telling you the callers don't actually share behavior. Adding another compounds it — every caller pays for paths it never takes, and every change risks all four.

Prescription (Sandi Metz's "unwinding"):
1. **Re-inline** the helper back into each caller, flags resolved to constants.
2. Delete the branches each caller can't reach — now you can see what is genuinely common.
3. Re-extract only that, along the real seam, if anything is left.

Rule to state: **a boolean parameter that selects behavior is a merged-too-early signal**, and sunk cost in the existing helper is not a reason to keep it.
