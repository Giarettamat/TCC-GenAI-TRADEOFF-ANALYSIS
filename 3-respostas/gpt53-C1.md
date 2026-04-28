# Resposta GPT para caso piloto 1

Here’s a structured analysis aligned with ISO/IEC 25010:2011 and Bass, Clements, and Kazman (2021).

---

## **1. Quality attributes in conflict (ISO/IEC 25010:2011)**

The scenario is clearly centered on **fault tolerance and continuity**, but achieving that introduces trade-offs.

### **Primary attribute (goal)**

* **Reliability**

  * **Availability** (system remains operational ≥ 99.9%)
  * **Fault tolerance** (continues operating via redundancy after node crash)
  * **Recoverability** (time to repair ≤ 5 seconds; degraded mode ≤ 30 seconds)

### **Conflicting attributes**

1. **Performance efficiency**

   * **Time behavior** (failover detection, switching, synchronization overhead)
   * **Resource utilization** (redundant nodes consume CPU/memory even when idle)
   * **Capacity** (handling load while one node is down)

2. **Maintainability**

   * **Complexity / Modularity / Analyzability**
     Redundant, distributed logic (failover, replication, health checks) increases system complexity.

3. **Security**

   * **Integrity / Confidentiality**
     Replication and synchronization between nodes increase the attack surface and risk of data inconsistency or leakage.

---

## **2. Architectural decision (with justification)**

### **Decision**

Adopt an **active-passive redundancy architecture with heartbeat monitoring and automatic failover**, combined with **state replication**.

### **Mapped tactics (Bass, Clements, Kazman)**

* **Fault detection tactics**

  * Heartbeat / health checks between nodes

* **Fault recovery tactics**

  * **Active-passive redundancy**
  * **Failover (switch to standby node)**

* **Fault prevention / containment**

  * Process isolation per node

* **State management**

  * Checkpointing or near-real-time replication

### **Alignment with response measures**

* **Availability ≥ 99.9%**
  → Redundancy ensures service continuity even after node crash

* **Time to repair ≤ 5 seconds**
  → Heartbeat detection + automatic failover enables fast recovery

* **Degraded mode ≤ 30 seconds**
  → Temporary reduced capacity while standby node takes over and stabilizes

This decision directly satisfies all three constraints.

---

## **3. Mitigation strategies for negative impacts**

### **Impact 1: Performance overhead (replication + monitoring)**

**Mitigation:**

* Use **asynchronous replication** where possible
* Optimize heartbeat intervals dynamically (adaptive health checks)

**Trade-off:**

* Risk of **data loss or inconsistency** during failover (eventual consistency)

---

### **Impact 2: Increased resource utilization (redundant nodes idle)**

**Mitigation:**

* Use **active-active for partial workloads** (hybrid model)
* Or leverage **autoscaling/cloud standby instances**

**Trade-off:**

* Higher infrastructure cost or increased architectural complexity

---

### **Impact 3: Increased system complexity (maintainability)**

**Mitigation:**

* Encapsulate failover logic in **infrastructure layer (e.g., orchestrator like Kubernetes)**
* Use standardized frameworks for resilience

**Trade-off:**

* Dependency on external platforms/tools
* Learning curve for team

---

### **Impact 4: Security exposure (replication channels)**

**Mitigation:**

* Encrypt inter-node communication (TLS)
* Use authentication between nodes
* Apply least-privilege policies

**Trade-off:**

* Added latency (affects time behavior)
* More complex key management

---

## **4. Residual risks after mitigation**

Even after applying mitigations, some risks remain:

1. **Split-brain scenario**

   * Both nodes assume active role due to network partition
     → Leads to data inconsistency

2. **Replication lag**

   * In asynchronous replication, latest state may be lost during failover

3. **Detection delay variability**

   * Heartbeat tuning may not always guarantee ≤ 5s under extreme load

4. **Cascading failures under high load**

   * When operating in degraded mode, remaining node may become overloaded

5. **Operational complexity**

   * Debugging distributed failures is inherently harder than monolithic failures

---

### **Summary insight**

This is a classic **reliability vs performance/complexity trade-off**. The proposed solution (redundancy + failover) is standard and effective, but it shifts the burden into **operational complexity, cost, and consistency management**—which must be consciously controlled through mitigations.
