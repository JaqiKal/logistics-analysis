# Logistics Analysis

A growing collection of simple Python scripts to **visualize common flows in Supply Chain Management (SCM)** using Matplotlib.

## 🎯 Goal

Provide visual, data-driven examples of real-world SCM challenges and metrics — from warehouse flow to lead time variability — using clean, well-structured Python code.

## 📦 SCM examples

Each example will live in its own folder with a self-contained Python script and visualization.

<!-- markdownlint-disable MD033 -->
<details>
<summary>📊 Transportation Cost Analysis</summary>

- Analyze transportation costs across different routes
- Use scatter plots to compare cost vs distance

- 📁 Folder: transportation-cost-analysis/
- 📄 Script: transport_cost.py

![Graph](../logistics-analysis/documentation/image/graph-tca.webp)

</details>

<details>
<summary>📈 Product Flow Through Warehouse</summary>

- A line chart showing incoming and outgoing product quantities over one week.

- 📁 Folder: `product-flow-analysis/`  
- 📄 Script: `productflow.py`

![Graph](../logistics-analysis/documentation/image/graph-pftw.webp)

</details>

<details>
<summary>📦 Inventory Levels Over Time</summary>

- Simulate daily stock levels
- Show reorder points & safety stock
- Visualize with line charts

- 📁 Folder: inventory-levels-over-time/
- 📄 Script: inventory_sim.py

![Graph](../logistics-analysis/documentation/image/graph-ils.webp)

</details>

<details>

<summary>🚚 Order Fulfillment Timeline</summary>

- Visualize order entry → processing → shipping
- Use horizontal timeline (e.g., Gantt-style or step lines)

- 📁 Folder: order-fulfillment-timeline/
- 📄 Script: order_timeline.py

![Graph](../logistics-analysis/documentation/image/graph-oft.webp)

</details>

<details>

<summary>⏱️ Lead Time Variability</summary>

- Compare supplier lead times
- Use bar charts with error bars to show variability and risk

- 📁 Folder: lead-time-variability/
- 📄 Script: leadtime_chart.py

![Graph](../logistics-analysis/documentation/image/graph-ltv.webp)

</details>

<details>

<summary>⚖️ Demand vs Capacity</summary>

- Match incoming orders vs available capacity
- Spot bottlenecks with comparative bar charts

- 📁 Folder: demand-vs-capacity/
- 📄 Script: capacity_balance.py

![Graph](../logistics-analysis/documentation/image/graph-dvsc.webp)

</details>

<details>

<summary>🔁 Cycle Time Analysis</summary>

- Show time from raw material to final product
- Use stacked bars or time-flow graphs

- 📁 Folder: cycle-time-analysis/
- 📄 Script: cycle_time.py

![Graph](../logistics-analysis/documentation/image/graph-cta.webp)

</details>
<!-- markdownlint-enable MD033 -->

## 🛠 Tech Stack

- Python 3.12+
- Matplotlib
- Virtual Environment (`.venv`)
- VS Code (recommended)

---

## 📌 Usage

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/logistics-analysis

# Navigate into a folder and activate your virtual environment
cd product-flow-analysis
python ../.venv/Scripts/activate

# Run a script
python [script_name.py]   e.g. python productflow.py 
