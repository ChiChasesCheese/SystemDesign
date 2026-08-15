---
id: infra-containers-vs-vms
node: infra.containers
type: qa
---
## Q
Containers and VMs both isolate workloads. What is the actual isolation mechanism of each, and what does the difference buy in density and cost in security?

## A
- **VM**: a hypervisor virtualizes hardware; every guest boots its **own kernel**. Strong boundary, but seconds to boot and GBs of overhead per instance.
- **Container**: ordinary processes on a **shared host kernel**, isolated by **namespaces** (what they can see — PIDs, network, mounts) and **cgroups** (what they can use — CPU, memory). Millisecond starts, MBs of overhead → order-of-magnitude better packing density.
- The shared kernel is the security catch: one kernel exploit escapes the container. That's why multi-tenant platforms run untrusted code in **microVMs** (Firecracker, gVisor) — VM-grade boundary at near-container startup cost.
