from pyvis.network import Network
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="AI Data Center Graph", layout="wide")
st.title("AI Data Center Value Chain Graph")

ai_data_center_graph = {
    "AI Tokens": ["AI Data Center"],

    "AI Data Center": [
        "AI Racks", "Grid Infrastructure", "Cooling Systems", "Optical Networking",
        "Physical Building", "Storage Systems", "Software Stack",
        "Water", "Steel", "Concrete"
    ],

    "AI Racks": ["AI Servers", "Network Switches", "Power Delivery"],

    "AI Servers": [
        "AI GPU", "Networking", "Power Delivery",
        "Cooling Systems", "Storage Systems", "Software Stack"
    ],

    "AI GPU": ["GPU Dies", "HBM", "Advanced Substrates", "Interposers", "CoWoS Packaging"],
    "CoWoS Packaging": ["GPU Dies", "HBM", "Advanced Substrates", "Interposers", "Micro-Bumps", "Bonding Equipment", "Precision Manufacturing"],
    "Interposers": ["Silicon", "Advanced Chemicals", "Precision Manufacturing"],
    "Micro-Bumps": ["Copper", "Advanced Chemicals", "Precision Manufacturing"],
    "Bonding Equipment": ["Precision Components", "Steel", "Electronics", "Advanced Optics"],

    "GPU Dies": ["Wafers", "EUV Lithography", "Advanced Chemicals", "Ultra Pure Water", "Energy", "Photomasks", "Chip Design IP", "Fab Infrastructure"],

    "HBM": ["DRAM Dies", "TSV Stacking", "Memory Controllers", "Silicon Interposer", "Advanced Bonding"],
    "DRAM Dies": ["Memory Wafers", "Lithography", "Advanced Chemicals", "Ultra Pure Water", "Energy", "Fab Equipment"],
    "Memory Wafers": ["Silicon Wafers"],
    "TSV Stacking": ["DRAM Dies", "Advanced Chemicals", "Precision Manufacturing", "Bonding Equipment"],
    "Memory Controllers": ["Logic Chips", "Advanced Substrates", "Firmware"],
    "Silicon Interposer": ["Silicon Wafers", "Advanced Chemicals", "Precision Manufacturing"],
    "Advanced Bonding": ["Bonding Equipment", "Micro-Bumps", "Precision Manufacturing"],

    "Advanced Substrates": ["PCB", "High Purity Copper", "Glass Fiber", "Advanced Chemicals", "Precision Manufacturing"],
    "PCB": ["Copper", "Glass", "Chemicals", "Epoxy Resin"],
    "Glass Fiber": ["High Purity Glass", "Energy", "Chemicals"],
    "High Purity Glass": ["Silica", "Chemicals", "Energy"],

    "Logic Chips": ["Wafers", "EUV Lithography", "Advanced Chemicals", "Ultra Pure Water", "Energy"],
    "EUV Lithography": ["EUV Machines", "Photomasks", "Photoresists", "Ultra Pure Water", "Energy"],
    "EUV Machines": ["Precision Optics", "Lasers", "Mechatronics", "Steel", "Electronics"],
    "Photomasks": ["High Purity Glass", "Patterning Materials", "Precision Manufacturing"],
    "Photoresists": ["Specialty Chemicals", "Petrochemicals"],

    "Fab Infrastructure": ["Cleanrooms", "Ultra Pure Water", "Industrial Gases", "Power Infrastructure", "Chemical Handling Systems"],
    "Fab Equipment": ["Lithography Tools", "Etching Tools", "Deposition Tools", "Metrology Tools"],
    "Lithography Tools": ["Precision Optics", "Lasers", "Electronics", "Steel"],
    "Etching Tools": ["Industrial Gases", "Specialty Chemicals", "Vacuum Systems", "Electronics"],
    "Deposition Tools": ["Industrial Gases", "Specialty Chemicals", "Vacuum Systems", "Precision Components"],
    "Metrology Tools": ["Precision Optics", "Lasers", "Electronics"],

    "Silicon Wafers": ["Quartz Sand", "Polysilicon", "Crystal Growth", "Wafer Slicing", "Wafer Polishing"],
    "Wafers": ["Silicon Wafers"],
    "Polysilicon": ["Quartz Sand", "Energy", "Chemicals"],
    "Crystal Growth": ["Polysilicon", "Energy", "Precision Equipment"],
    "Wafer Slicing": ["Silicon Ingots", "Precision Equipment", "Abrasives"],
    "Wafer Polishing": ["Silicon Wafers", "Slurry Chemicals", "Ultra Pure Water"],

    "Network Switches": ["Switch ASICs", "PCB", "Optical Transceivers", "Power Modules", "Cooling Components"],
    "Switch ASICs": ["GPU Dies", "Advanced Substrates", "High Purity Copper"],
    "Optical Transceivers": ["Lasers", "Photonic Chips", "Optical Fiber", "Connectors", "PCB"],
    "Photonic Chips": ["Wafers", "Lithography", "Advanced Chemicals", "Precision Manufacturing"],
    "Optical Fiber": ["High Purity Glass", "Chemical Processing", "Precision Manufacturing", "Coating Materials"],
    "Optical Networking": ["Optical Fiber", "Optical Transceivers", "Network Switches", "Connectors", "Network Software"],
    "Connectors": ["Copper", "Plastics", "Precision Manufacturing"],
    "Network Software": ["Software Engineers", "Firmware", "Testing Infrastructure"],
    "Networking": ["Network Switches", "Optical Networking", "Networking Cards"],
    "Networking Cards": ["ASICs", "PCB", "Optical Transceivers", "Firmware"],
    "ASICs": ["Wafers", "Advanced Chemicals", "EUV Lithography", "Advanced Substrates"],

    "Power Delivery": ["Power Modules", "VRM", "Copper", "Capacitors", "Power Supplies"],
    "Power Modules": ["Semiconductors", "Copper", "Ceramics", "Advanced Substrates"],
    "VRM": ["Power Modules", "Capacitors", "Inductors", "PCB"],
    "Power Supplies": ["Copper", "Steel", "Semiconductors", "Capacitors", "Transformers"],
    "Capacitors": ["Aluminum", "Ceramics", "Chemicals"],
    "Inductors": ["Copper", "Ferrites", "Magnetic Materials"],
    "Semiconductors": ["Wafers", "Chemicals", "Energy"],

    "Grid Infrastructure": ["Transformers", "Switchgear", "Transmission Lines", "Substations", "Backup Batteries", "Diesel Generators"],
    "Power Infrastructure": ["Grid Infrastructure", "Power Delivery"],
    "Transformers": ["Copper", "Electrical Steel", "Insulation Materials", "Industrial Oils"],
    "Switchgear": ["Copper", "Steel", "Insulation Materials", "Electronics"],
    "Transmission Lines": ["Copper", "Aluminum", "Steel", "Insulators"],
    "Substations": ["Transformers", "Switchgear", "Concrete", "Steel", "Control Systems"],
    "Backup Batteries": ["Lithium", "Nickel", "Graphite", "Copper", "Battery Chemicals"],
    "Diesel Generators": ["Diesel Engines", "Steel", "Copper", "Fuel Supply"],

    "Cooling Systems": ["Pumps", "Heat Exchangers", "Cooling Towers", "Pipes", "Liquid Coolant", "Water Infrastructure"],
    "Cooling Components": ["Heat Exchangers", "Pumps", "Liquid Coolant"],
    "Pumps": ["Steel", "Copper", "Motors", "Seals"],
    "Heat Exchangers": ["Copper", "Aluminum", "Steel", "Precision Manufacturing"],
    "Cooling Towers": ["Steel", "Concrete", "Pumps", "Fans", "Water"],
    "Pipes": ["Steel", "Copper", "Plastics"],
    "Liquid Coolant": ["Chemical Refining", "Industrial Fluids", "Additives", "Petrochemicals"],
    "Water Infrastructure": ["Water", "Pumps", "Pipes", "Filtration Systems", "Treatment Chemicals"],

    "Concrete": ["Cement", "Sand", "Gravel", "Water", "Energy"],
    "Cement": ["Limestone", "Clay", "Energy"],
    "Steel": ["Iron Ore", "Coal", "Energy", "Blast Furnaces"],
    "High Purity Copper": ["Copper", "Energy", "Refining Chemicals"],

    "Advanced Chemicals": ["Specialty Chemicals", "Industrial Chemicals", "Petrochemicals", "Ultra Pure Water"],
    "Industrial Chemicals": ["Oil/Gas", "Water", "Energy"],
    "Specialty Chemicals": ["Industrial Chemicals", "Petrochemicals", "Precision Processing"],
    "Chemical Processing": ["Industrial Chemicals", "Energy", "Water"],
    "Chemical Refining": ["Oil/Gas", "Industrial Chemicals", "Energy"],
    "Industrial Gases": ["Air Separation", "Energy", "Gas Storage"],
    "Ultra Pure Water": ["Water", "Filtration Systems", "Treatment Chemicals", "Energy"],

    "Precision Manufacturing": ["Precision Equipment", "Metrology Tools", "Skilled Labor", "Energy"],
    "Precision Components": ["Steel", "Aluminum", "Copper", "Precision Manufacturing"],
    "Precision Optics": ["High Purity Glass", "Rare Earths", "Precision Manufacturing"],
    "Lasers": ["Rare Earths", "Semiconductor Components", "Precision Optics", "Advanced Manufacturing"],
    "Advanced Optics": ["Precision Optics", "High Purity Glass", "Rare Earths"],
    "Mechatronics": ["Motors", "Electronics", "Precision Components", "Software"],
    "Electronics": ["PCB", "Semiconductors", "Copper", "Capacitors"],
    "Motors": ["Copper", "Steel", "Rare Earth Magnets"],
    "Rare Earth Magnets": ["Rare Earths", "Iron", "Boron", "Energy"],

    "Software Stack": ["CUDA / AI Runtime", "Orchestration", "Inference Stack", "Distributed Training", "Monitoring Systems"],
    "CUDA / AI Runtime": ["Software Engineers", "GPU Architecture", "Developer Ecosystem"],
    "Orchestration": ["Software Engineers", "Networking", "Storage Systems"],
    "Inference Stack": ["AI Models", "AI Servers", "Networking", "Storage Systems"],
    "Distributed Training": ["AI Models", "AI GPU", "Networking", "Storage Systems"],

    "Storage Systems": ["NAND Flash", "Hard Drives", "Storage Controllers", "Networking"],
    "NAND Flash": ["Wafers", "Lithography", "Advanced Chemicals", "Energy"],
    "Hard Drives": ["Precision Motors", "Magnetic Materials", "Aluminum", "Electronics"],
    "Storage Controllers": ["ASICs", "Firmware", "PCB"],

    "Physical Building": ["Steel", "Concrete", "Electrical Systems", "Cooling Systems", "Security Systems"],
    "Electrical Systems": ["Copper", "Switchgear", "Transformers", "Power Supplies"],
    "Security Systems": ["Cameras", "Sensors", "Networking", "Software"],
    "Cameras": ["Image Sensors", "Optics", "Electronics"],
    "Sensors": ["Semiconductors", "Electronics", "Software"],
}


all_nodes = sorted(
    set(ai_data_center_graph.keys()) |
    {item for deps in ai_data_center_graph.values() for item in deps}
)


def get_all_dependencies(node, graph, memo=None, visiting=None):
    if memo is None:
        memo = {}
    if visiting is None:
        visiting = set()

    if node in memo:
        return memo[node]

    if node not in graph:
        memo[node] = set()
        return set()

    if node in visiting:
        return set()

    visiting.add(node)

    deps = set(graph[node])

    for dep in graph[node]:
        deps |= get_all_dependencies(dep, graph, memo, visiting)

    visiting.remove(node)
    memo[node] = deps
    return deps


dependency_sets = {
    node: get_all_dependencies(node, ai_data_center_graph)
    for node in all_nodes
}

complexity_levels = {
    node: len(dependency_sets[node])
    for node in all_nodes
}


def classify_node(node: str) -> str:
    lvl = complexity_levels[node]

    if lvl == 0:
        return "00 Raw / Base"
    elif lvl <= 3:
        return "01 Simple"
    elif lvl <= 10:
        return "02 Low Complexity"
    elif lvl <= 25:
        return "03 Medium Complexity"
    elif lvl <= 50:
        return "04 High Complexity"
    elif lvl <= 100:
        return "05 Very High Complexity"
    else:
        return "06 Endgame Complexity"


group_colors = {
    "00 Raw / Base": "#2ECC71",
    "01 Simple": "#A3E635",
    "02 Low Complexity": "#FACC15",
    "03 Medium Complexity": "#FB923C",
    "04 High Complexity": "#EF4444",
    "05 Very High Complexity": "#A855F7",
    "06 Endgame Complexity": "#FFFFFF"
}


bus_nodes = sorted(all_nodes, key=lambda n: (complexity_levels[n], n))

x_gap = 280
y_gap = 220

group_order = [
    "06 Endgame Complexity",
    "05 Very High Complexity",
    "04 High Complexity",
    "03 Medium Complexity",
    "02 Low Complexity",
    "01 Simple",
    "00 Raw / Base",
]

group_y = {
    group: i * y_gap
    for i, group in enumerate(group_order)
}

positions = {}

for group in group_order:
    group_nodes = [
        node for node in bus_nodes
        if classify_node(node) == group
    ]

    group_nodes = sorted(group_nodes, key=lambda n: (complexity_levels[n], n))

    for i, node in enumerate(group_nodes):
        positions[node] = {
            "x": i * x_gap,
            "y": group_y[group]
        }


net = Network(
    height="950px",
    width="100%",
    directed=True,
    notebook=False,
    bgcolor="#111111",
    font_color="white",
    cdn_resources="in_line"
)

net.toggle_physics(False)

edge_hidden_color = "rgba(160,160,160,0.03)"


for node in bus_nodes:
    group = classify_node(node)
    color = group_colors.get(group, "#9E9E9E")
    x = positions[node]["x"]
    y = positions[node]["y"]

    net.add_node(
        node,
        label=node,
        title=(
            f"{node}<br>"
            f"Complexity group: {group}<br>"
            f"Total dependencies: {complexity_levels[node]}"
        ),
        group=group,
        color=color,
        x=x,
        y=y,
        fixed=True,
        physics=False,
        shape="box",
        font={"color": "white", "size": 18},
        margin=10
    )


recipe_y_offset = 95

for product, components_list in ai_data_center_graph.items():
    if product not in positions:
        continue

    product_x = positions[product]["x"]
    product_y = positions[product]["y"]

    recipe_id = f"RECIPE::{product}"
    recipe_y = product_y + recipe_y_offset

    net.add_node(
        recipe_id,
        label=f"make\n{product}",
        title=f"Recipe creates: {product}<br>Inputs: {', '.join(components_list)}",
        color="#222222",
        borderWidth=2,
        shape="diamond",
        x=product_x,
        y=recipe_y,
        fixed=True,
        physics=False,
        font={"color": "#FFFFFF", "size": 14}
    )

    for component in components_list:
        if component not in positions:
            continue

        net.add_edge(
            component,
            recipe_id,
            title=f"{component} is input for {product}",
            color=edge_hidden_color,
            width=1,
            arrows="to"
        )

    net.add_edge(
        recipe_id,
        product,
        title=f"recipe outputs {product}",
        color=edge_hidden_color,
        width=1,
        arrows="to"
    )


net.set_options("""
{
  "layout": {
    "improvedLayout": false
  },
  "interaction": {
    "hover": true,
    "navigationButtons": true,
    "keyboard": true,
    "dragNodes": true,
    "zoomView": true,
    "dragView": true
  },
  "edges": {
    "smooth": {
      "enabled": true,
      "type": "cubicBezier",
      "forceDirection": "vertical",
      "roundness": 0.45
    }
  },
  "physics": {
    "enabled": false
  }
}
""")


html = net.generate_html(notebook=False)

highlight_js = """
<script>
function getAllDependencies(clickedNodeId) {
    const dependencyNodes = new Set();
    const dependencyEdges = new Set();
    const visited = new Set();

    function walk(targetNodeId) {
        if (visited.has(targetNodeId)) {
            return;
        }

        visited.add(targetNodeId);

        const incomingEdges = edges.get().filter(e => e.to === targetNodeId);

        incomingEdges.forEach(edge => {
            const sourceNode = edge.from;

            dependencyEdges.add(edge.id);
            dependencyNodes.add(sourceNode);

            walk(sourceNode);
        });
    }

    dependencyNodes.add(clickedNodeId);
    walk(clickedNodeId);

    return {
        nodes: dependencyNodes,
        edges: dependencyEdges
    };
}

function resetStyles() {
    const allNodes = nodes.get();
    const allEdges = edges.get();

    nodes.update(allNodes.map(n => ({
        id: n.id,
        opacity: 0.18,
        borderWidth: 1,
        font: {
            color: "rgba(255,255,255,0.25)"
        }
    })));

    edges.update(allEdges.map(e => ({
        id: e.id,
        color: "rgba(160,160,160,0.03)",
        width: 1,
        hidden: false
    })));
}

function highlightDependencyTree(clickedNodeId) {
    resetStyles();

    const result = getAllDependencies(clickedNodeId);

    nodes.update(Array.from(result.nodes).map(id => ({
        id: id,
        opacity: 1,
        borderWidth: 3,
        font: {
            color: "#FFFFFF"
        }
    })));

    edges.update(Array.from(result.edges).map(id => ({
        id: id,
        color: "#FFFFFF",
        width: 3
    })));
}

network.on("click", function(params) {
    if (params.nodes.length > 0) {
        const clickedNodeId = params.nodes[0];
        highlightDependencyTree(clickedNodeId);
    } else {
        resetStyles();
    }
});

resetStyles();
</script>
"""

html = html.replace("</body>", highlight_js + "\n</body>")

components.html(html, height=1600, width=None, scrolling=True)


# =========================
# TABELA ELEMENTÓW
# =========================

used_by_count = {node: 0 for node in all_nodes}

for product, components_list in ai_data_center_graph.items():
    for component in components_list:
        used_by_count[component] = used_by_count.get(component, 0) + 1

table_rows = []

for node in all_nodes:
    table_rows.append({
        "lvl": classify_node(node),
        "element": node,
        "materials_to_create": complexity_levels[node],
        "used_in_products_count": used_by_count.get(node, 0),
    })

df_elements = pd.DataFrame(table_rows)

df_elements = df_elements.sort_values(
    by=["materials_to_create", "used_in_products_count"],
    ascending=[False, False]
).reset_index(drop=True)

st.subheader("Tabela elementów value chain")

st.dataframe(
    df_elements,
    use_container_width=True,
    height=900
)