# USACO Gold: Time is Mooney

**Problem Link:** [USACO 2020 January Contest, Gold - Problem 1](https://usaco.org/index.php?page=viewproblem2&cpid=993)

### 🧠 Core Concept: Time-Expanded Graph (Unrolling Cycles)
The fundamental lesson from this problem is **"Unrolling the Graph Level-Wise."**
In a graph with positive cycles, a standard longest-path algorithm fails because it can loop infinitely. However, by treating **Time ($t$)** as a dimension, we transform the cyclic graph into a **DAG (Directed Acyclic Graph)** where edges only move forward from layer $t$ to $t+1$.

### 💡 The Approach

#### 1. The Observation (Bounding $T$)
The cost of travel is $C \cdot T^2$, while the maximum income is linear ($1000 \cdot T$).
* **Income:** Grows linearly.
* **Cost:** Grows quadratically.
* **Limit:** At $T=1000$, the cost ($1,000,000$) outweighs the maximum possible theoretical income.
* **Conclusion:** We only need to simulate up to **1000 days**.

#### 2. Dynamic Programming State
Instead of just tracking `[City]`, we track `[Time][City]`. This allows us to visit the same city multiple times at different timestamps, effectively "leveraging" loops to accumulate profit.

* **State:** `dp[i][t]`
    * Maximum Moonies earned arriving at **City $i$** at exactly **Time $t$**.
* **Transition:**
    For every directed edge $u \to v$:
    $$dp[v][t+1] = \max(dp[v][t+1], \quad dp[u][t] + \text{moonies}[v])$$
* **Constraint:** We only transition from reachable states (`dp[u][t] != -1`).

#### 3. The "Accountant" (Final Answer)
We separate the **earning phase** from the **cost phase**.
1.  Run the DP to calculate raw income for all 1000 days.
2.  Iterate through `t` from 0 to 1000.
3.  Check `dp[1][t]` (Trips must end at City 1).
4.  Subtract the cost: $\text{Profit} = dp[1][t] - (C \cdot t^2)$.
5.  The answer is the maximum profit found.

### 🚀 Key Takeaway
**"Level-wise Unrolling"** allows us to use cycles to our advantage without getting stuck in them. By unrolling the graph into time layers, a cycle $1 \to 2 \to 1$ simply becomes a valid path from **Layer $t$ (City 1)** $\to$ **Layer $t+1$ (City 2)** $\to$ **Layer $t+2$ (City 1)**.

---
*Solved as part of USACO Gold preparation.*