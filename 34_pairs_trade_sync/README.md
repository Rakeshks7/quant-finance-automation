# Pairs Trade Synchronization (Legging In)

An execution logic for Statistical Arbitrage that mitigates Legging Risk (the risk that one side of a pair fills while the other runs away).

## Workflow Logic

1. **Input:** A signal to trade a pair (e.g., Long Stock A / Short Stock B).
2. **Logic:** Identify the "Illiquid" leg (Limit Order candidate) and the "Liquid" leg (Market Order candidate).
3. **Step 1:** Submit **Leg 1** as a Limit Order.

   * *Pause:* The workflow waits here. It does NOT submit Leg 2 yet.

4. **Step 2:** The Broker sends a "Fill Confirmation" webhook to n8n when Leg 1 is executed.
5. **Step 3:** n8n immediately fires **Leg 2** as a Market Order.

   * *Why?* Since Leg 1 is now real exposure, we must hedge it *instantly*, regardless of slippage on Leg 2.

## Why this is Pro

Amateurs fire both orders as Market Orders (paying double spread) or Limit Orders (risking only one filling). This "Hybrid" approach is the industry standard for Stat Arb.

