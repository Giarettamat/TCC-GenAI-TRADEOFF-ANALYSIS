# Resposta GEMINI para caso piloto 1

This analysis evaluates the provided Quality Attribute Scenario through the lens of ISO/IEC 25010 and the architectural frameworks of Bass, Clements, and Kazman.

---

## 1. Quality Attribute Conflict Analysis
Using the **ISO/IEC 25010:2011** normative vocabulary, the primary conflict occurs between the following characteristics:

* **Reliability (Availability):** The scenario demands the system remain operational despite a node crash.
* **Performance Efficiency (Resource Utilization / Time Behavior):** The requirement for redundancy and a 5-second repair time often requires "Active Redundancy" (hot standby), which consumes significant resources even during "normal operation under load."
* **Maintainability (Modularity / Analyzability):** Implementing complex fault detection and automated recovery increases the internal complexity of the software, potentially making it harder to analyze or modify without side effects.

**Primary Conflict:** **Reliability (Availability)** vs. **Performance Efficiency (Resource Utilization)**. Maintaining high availability via redundancy requires overhead that reduces the efficiency of the available hardware.

---

## 2. Proposed Architectural Decision
**Decision:** Implementation of **Active Redundancy (Hot Spare)** with an **External Fault Monitor**.

**Tactics Alignment:**
According to Bass et al., this employs two primary tactics for **Availability**:
1.  **Fault Detection:** *Condition Monitoring* (the monitor checks the health of processing nodes).
2.  **Fault Recovery:** *Active Redundancy* (hot standby) to ensure the state is synchronized across nodes.

**Justification & Alignment with Response Measures:**
* **Availability ≥ 99.9%:** By having a hot spare ready to take over the load immediately, the system avoids total downtime.
* **Time to Repair ≤ 5 seconds:** Active redundancy is the only tactic that consistently allows for sub-5-second failover, as the "spare" node already has the current state and requires no cold-boot time.
* **Degraded Mode ≤ 30 seconds:** An external load balancer/monitor can redistribute the failed node's traffic to the remaining nodes instantly while a new instance is provisioned to replace the crashed one, returning the system to full capacity within the 30-second window.

---

## 3. Mitigation Strategies
The decision to use Active Redundancy introduces overhead and complexity. Below are strategies to mitigate these impacts:

| Mitigation Strategy | Description | Cost / Trade-off |
| :--- | :--- | :--- |
| **Throttling / Graceful Degradation** | During the 30s degraded period, non-essential background tasks are paused to prioritize the Data Processing Service. | **Functional Suitability:** Temporary loss of secondary features. |
| **Automated Infrastructure Provisioning** | Use "Infrastructure as Code" (IaC) to trigger the immediate spin-up of a replacement node. | **Complexity:** Requires maintenance of deployment scripts and cloud-orchestration layers. |
| **State Synchronization Optimization** | Use asynchronous state replication between the primary and redundant nodes. | **Reliability:** Risk of minor data loss (RPO) if the crash occurs before a sync pulse. |

---

## 4. Residual Risks
Even after applying the architectural decision and mitigations, the following residual risks remain:

* **Common Mode Failure:** If the "crash fault" is caused by a bug in the software logic (e.g., a "poison pill" message), the redundant node will also crash upon processing the same data, leading to total system failure despite redundancy.
* **Split-Brain Syndrome:** In a network partition, the monitor might incorrectly assume a node has crashed when it is merely unreachable, leading to two nodes attempting to act as the primary, potentially corrupting data.
* **Resource Exhaustion during Recovery:** The process of bootstrapping a new node to end the "degraded mode" within 30 seconds may consume significant CPU/Bandwidth, further impacting the performance of the surviving nodes already under load.