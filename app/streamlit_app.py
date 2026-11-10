from __future__ import annotations

from pathlib import Path

import altair as alt
import pandas as pd
import pydeck as pdk
import streamlit as st
import base64
import textwrap

from backend.data_service import (
    load_annual_registry,
    load_map_geojson,
    load_master_data,
    load_registry,
    load_shap_importance,
    load_test_predictions,
)
from backend.model_service import model_summary


APP_DIR = Path(__file__).resolve().parent
def image_data_uri(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


registry_icon = image_data_uri(
    APP_DIR / "assets" / "registry-icon.png"
)
st.set_page_config(
    page_title="Climate & ESG Risk Intelligence Germany",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(f"<style>{(APP_DIR / 'assets' / 'styles.css').read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def app_data():
    return {
        "registry": load_registry(),
        "master": load_master_data(),
        "annual_registry": load_annual_registry(),
        "geojson": load_map_geojson(),
        "model": model_summary(),
        "predictions": load_test_predictions(),
        "shap": load_shap_importance(),
    }


data = app_data()
registry = data["registry"]
master = data["master"]
annual_registry = data["annual_registry"]

st.sidebar.title("Climate Risk Intelligence")
page = st.sidebar.radio(
    "Explore the platform",
    [
        "Overview",
        "Risk Map",
        "District Explorer",
        "Model Explainability",
        "Sector Applications",
        "Methodology & Limitations",
        "About the Project",
    ],
)
st.sidebar.divider()
st.sidebar.caption("Prototype decision-support application · Germany · 1990–2025")


def hero(subtitle: str) -> None:
    st.markdown(
        f"""
<div class="hero">
<svg class="ai-network" viewBox="0 0 520 220"
     preserveAspectRatio="none" aria-hidden="true">
<g class="network-lines">
<line x1="40" y1="48" x2="145" y2="88"/>
<line x1="40" y1="48" x2="120" y2="170"/>
<line x1="145" y1="88" x2="245" y2="42"/>
<line x1="145" y1="88" x2="260" y2="125"/>
<line x1="120" y1="170" x2="260" y2="125"/>
<line x1="120" y1="170" x2="230" y2="195"/>
<line x1="245" y1="42" x2="370" y2="72"/>
<line x1="245" y1="42" x2="340" y2="155"/>
<line x1="260" y1="125" x2="370" y2="72"/>
<line x1="260" y1="125" x2="340" y2="155"/>
<line x1="230" y1="195" x2="340" y2="155"/>
<line x1="370" y1="72" x2="475" y2="40"/>
<line x1="370" y1="72" x2="460" y2="125"/>
<line x1="340" y1="155" x2="460" y2="125"/>
<line x1="340" y1="155" x2="445" y2="195"/>
<line x1="40" y1="48" x2="85" y2="112"/>
<line x1="85" y1="112" x2="145" y2="88"/>
<line x1="85" y1="112" x2="120" y2="170"/>
<line x1="145" y1="88" x2="195" y2="138"/>
<line x1="195" y1="138" x2="260" y2="125"/>
<line x1="195" y1="138" x2="230" y2="195"/>
<line x1="245" y1="42" x2="305" y2="78"/>
<line x1="305" y1="78" x2="370" y2="72"/>
<line x1="305" y1="78" x2="340" y2="155"/>
<line x1="260" y1="125" x2="305" y2="78"/>
<line x1="340" y1="155" x2="400" y2="112"/>
<line x1="370" y1="72" x2="420" y2="35"/>
<line x1="420" y1="35" x2="475" y2="40"/>
<line x1="400" y1="112" x2="460" y2="125"/>
<line x1="400" y1="112" x2="445" y2="195"/>
<line x1="460" y1="125" x2="495" y2="82"/>
</g>

<g class="network-signals">
<path d="M40 48 L145 88 L245 42 L370 72 L475 40"/>
<path d="M120 170 L260 125 L340 155 L445 195"/>
</g>

<g class="network-nodes">
<circle cx="40" cy="48" r="2.5"/>
<circle cx="145" cy="88" r="3.5"/>
<circle cx="120" cy="170" r="2.5"/>
<circle cx="245" cy="42" r="3"/>
<circle cx="260" cy="125" r="4"/>
<circle cx="230" cy="195" r="2"/>
<circle cx="370" cy="72" r="3.5"/>
<circle cx="340" cy="155" r="3"/>
<circle cx="475" cy="40" r="2.5"/>
<circle cx="460" cy="125" r="4"/>
<circle cx="445" cy="195" r="2.5"/>
<circle cx="85" cy="112" r="2.2"/>
<circle cx="195" cy="138" r="2.4"/>
<circle cx="305" cy="78" r="2.6"/>
<circle cx="400" cy="112" r="2.4"/>
<circle cx="420" cy="35" r="2.1"/>
<circle cx="495" cy="82" r="2.2"/>
</g>
</svg>

<div class="hero-content">
<h1>AI-Powered Climate & ESG Risk Intelligence Platform for Germany</h1>
<p>{subtitle}</p>
</div>
</div>
""",
        unsafe_allow_html=True,
    )


if page == "Overview":
    hero("Multi-sector regional decision support combining climate hazards, "
    "socioeconomic indicators and explainable artificial intelligence.")
    analysed_districts = registry["district_code"].nunique()

    st.markdown(
        """
    <div class="climate-metrics-row">
    <div class="climate-metric metric-red">
    <div class="metric-ring">
    <strong>10,404</strong>
    </div>
    <span>District-year<br>observations</span>
    </div>

    <div class="climate-metric metric-green">
    <div class="metric-ring">
    <strong>289</strong>
    </div>
    <span>Analysed<br>districts</span>
    </div>

    <div class="climate-metric metric-amber">
    <div class="metric-ring metric-ring-wide">
    <strong>1990–2025</strong>
    </div>
    <span>Analysis<br>period</span>
    </div>

    <div class="climate-metric metric-plum">
    <div class="metric-ring">
    <strong>5</strong>
    </div>
    <span>Model<br>inputs</span>
    </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.subheader("What the platform provides")

    capabilities = [
        (
            "🌡",
            "Regional Risk Score",
            "A Regional Climate Risk Score (RCRS) on a transparent 0–100 scale.",
            "#b63f32",
            "#fff0ed",
        ),
        (
    f'<img src="{registry_icon}" alt="Registry documents" class="capability-icon-image">',
    "National Risk Registry",
    "District risk classes, national rankings and long-term median scores.",
    "#d97706",
    "#fff7ed",
),
        (
            "🗺",
            "Interactive Risk Map",
            "Explore all 400 current NUTS-3 districts, including 111 clearly marked as not modelled.",
            "#6f8f3d",
            "#f2f7e9",
        ),
        (
            "📈",
            "Annual District Profiles",
            "Inspect climate-risk trajectories and individual climate and socioeconomic indicators.",
            "#963f32",
            "#faefeb",
        ),
        (
            "🧠",
            "Explainable AI",
            "Review model performance and SHAP-based explanations of predictor influence.",
            "#6e4165",
            "#f7eef6",
        ),
    ]

    first_row = st.columns(3)

    for column, (icon, title, description, accent, tint) in zip(
    first_row, capabilities[:3]
    ):
     with column:
        st.markdown(
            f"""
            <div class="capability-card"
                style="--accent: {accent}; --tint: {tint};">
                <div class="capability-icon">{icon}</div>
                <h4>{title}</h4>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    second_row = st.columns(2)

    for column, (icon, title, description, accent, tint) in zip(
    second_row, capabilities[3:]
    ):
     with column:
        st.markdown(
            f"""
            <div class="capability-card"
                style="--accent: {accent}; --tint: {tint};">
                <div class="capability-icon">{icon}</div>
                <h4>{title}</h4>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    class_order = ["Low", "Medium", "High"]

    class_counts = (
    registry["median_risk_class"]
    .value_counts()
    .rename_axis("Risk class")
    .reset_index(name="Districts")
    )

    st.subheader("National Risk Snapshot")

    modelled_districts = int(class_counts["Districts"].sum())
    total_districts = 400
    not_modelled_districts = total_districts - modelled_districts
    coverage_ratio = modelled_districts / total_districts

    snapshot_left, snapshot_right = st.columns([1, 1], gap="large")

    with snapshot_left:
         st.markdown("#### Risk class distribution")
         risk_doughnut = (
        alt.Chart(class_counts)
        .mark_arc(
            innerRadius=90,
            outerRadius=155,
            cornerRadius=6,
        )
        .encode(
            theta=alt.Theta(
                "Districts:Q",
                title="Number of districts",
            ),
            color=alt.Color(
                "Risk class:N",
                scale=alt.Scale(
                    domain=class_order,
                    range=["#c7e09e", "#ffc15e", "#ff6363"],
                ),
   legend=alt.Legend(
    title="Risk class",
    orient="right",
    direction="vertical",
    titleFontSize=16,
    titleFontWeight="bold",
    labelFontSize=15,
    symbolSize=220,
    symbolStrokeWidth=2,
    rowPadding=10,
    offset=-220,
),
            ),
            tooltip=[
                alt.Tooltip("Risk class:N", title="Risk class"),
                alt.Tooltip("Districts:Q", title="Districts"),
            ],
        )
    )

    centre_number = (
        alt.Chart(pd.DataFrame({"Districts": [modelled_districts]}))
        .mark_text(
            fontSize=32,
            fontWeight="bold",
            color="#4a1f2b",
            dy=-8,
        )
        .encode(text="Districts:Q")
    )

    centre_label = (
        alt.Chart(pd.DataFrame({"Label": ["modelled districts"]}))
        .mark_text(
            fontSize=14,
            color="#4b4b52",
            dy=20,
        )
        .encode(text="Label:N")
    )

    national_snapshot = (
        risk_doughnut + centre_number + centre_label
    ).properties(height=340)

    st.altair_chart(national_snapshot, width="stretch")

    st.caption(
        "Risk classes use fixed thresholds derived from the training "
        "distribution; district totals are therefore not expected to be equal."
    )

    with snapshot_right:
     st.markdown("#### Coverage summary")

    st.markdown(
        f"""
<div class="coverage-summary">
<div class="coverage-stat">
<span class="coverage-label">Modelled districts</span>
<strong>{modelled_districts} of {total_districts}</strong>
<span class="coverage-badge coverage-badge-blue">{coverage_ratio:.1%} coverage</span>
</div>
<div class="coverage-bar" role="img" aria-label="{modelled_districts} modelled and {not_modelled_districts} not modelled">
<div class="coverage-modelled" style="width: {coverage_ratio:.1%};"></div>
<div class="coverage-unmodelled" style="width: {not_modelled_districts / total_districts:.1%};"></div>
</div>
<div class="coverage-bar-labels">
<span><i class="coverage-key key-blue"></i>Modelled</span>
<span><i class="coverage-key key-grey"></i>Not modelled</span>
</div>
<div class="coverage-stat coverage-stat-secondary">
<span class="coverage-label">Not modelled</span>
<strong>{not_modelled_districts} districts</strong>
<span class="coverage-badge coverage-badge-grey">{not_modelled_districts / total_districts:.1%} of Germany</span>
</div>
</div>
<div class="note">The 111 districts remain visible in light grey on the Risk Map. They are explicitly identified as not modelled because consistent identifiers across the source datasets could not be established.</div>
""",
        unsafe_allow_html=True,
    )

if page == "Risk Map":
    hero("Explore median district-level climate risk across the 1990–2025 analytical period.")
    st.markdown(
        """<div class="legend-row">
        <span class="legend-item"><i class="swatch" style="background:#c7e09e"></i>Low (≤31.37)</span>
        <span class="legend-item"><i class="swatch" style="background:#ffc15e"></i>Medium (31.37–43.39)</span>
        <span class="legend-item"><i class="swatch" style="background:#ff6363"></i>High (&gt;43.39)</span>
        <span class="legend-item"><i class="swatch" style="background:#b4bac2"></i>Not modelled</span>
        </div>""",
        unsafe_allow_html=True,
    )
    layer = pdk.Layer(
        "GeoJsonLayer",
        data["geojson"],
        pickable=True,
        stroked=True,
        filled=True,
        get_fill_color="properties.fill_colour",
        get_line_color=[255, 255, 255, 170],
        line_width_min_pixels=0.5,
    )
    view = pdk.ViewState(latitude=51.15, longitude=10.45, zoom=5.25)
    tooltip = {"html": "<b>{display_name}</b><br/>RCRS: {display_score}<br/>Class: {display_class}", "style": {"backgroundColor": "#123047", "color": "white"}}
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view, tooltip=tooltip, map_style="https://basemaps.cartocdn.com/gl/positron-gl-style/style.json",), width="stretch")
    st.caption("Grey districts were excluded because consistent identifiers across the climate, boundary and socioeconomic sources could not be established for Version 1.")

    with st.expander("View continuous median predicted RCRS map"):
        st.markdown(
            "This map displays the continuous median predicted Regional Climate "
            "Risk Score for each modelled NUTS-3 district across 1990–2025."
        )
        st.image(
            "app/assets/continuous-median-rcrs-map.png",
            caption=(
                "Continuous median predicted RCRS by NUTS-3 district, "
                "1990–2025. Unmodelled districts are shown in grey."
            ),
            width="stretch",
        )

if page == "District Explorer":
    hero("Search an analysed district and inspect its long-term risk profile and predictor history.")
    district = st.selectbox("Select a district", sorted(registry["district_name"].tolist()))
    district_row = registry.loc[registry["district_name"].eq(district)].iloc[0]
    district_history = master.loc[master["district_name"].eq(district)].sort_values("year")

    district_annual = annual_registry.loc[
    annual_registry["district_name"].eq(district)
].sort_values("year")
    
    cols = st.columns(4)
    cols[0].metric("Median RCRS", f"{district_row['median_predicted_rcrs']:.2f}")
    cols[1].metric("Risk class", district_row["median_risk_class"])
    cols[2].metric("National rank", f"{int(district_row['national_climate_risk_rank'])} of 289")
    cols[3].metric("Years represented", int(district_row["years_represented"]))

    st.subheader("Annual Regional Climate Risk Score")

    risk_line = (
        alt.Chart(district_annual)
        .mark_line(
            color="#176b87",
            strokeWidth=2.5,
        )
        
        .encode(
            x=alt.X(
                "year:Q",
                title="Year",
                axis=alt.Axis(format="d"),
            ),
            y=alt.Y(
                "predicted_rcrs:Q",
                title="Regional Climate Risk Score",
                scale=alt.Scale(domain=[0, 100]),
            ),
        )
    )

    risk_points = (
        alt.Chart(district_annual)
        .mark_point(
            filled=True,
            size=75,
            stroke="white",
            strokeWidth=1,
        )
        .encode(
            x=alt.X("year:Q", axis=alt.Axis(format="d")),
            y=alt.Y(
                "predicted_rcrs:Q",
                scale=alt.Scale(domain=[0, 100]),
            ),
            color=alt.Color(
                "predicted_risk_class:N",
                title="Risk class",
                scale=alt.Scale(
                    domain=["Low", "Medium", "High"],
                    range=["#c7e09e", "#ffc15e", "#ff6363"],
                ),
            ),
            tooltip=[
    alt.Tooltip(
        "district_name:N",
        title="District",
    ),
    alt.Tooltip("year:Q", title="Year", format="d"),
    alt.Tooltip(
        "predicted_rcrs:Q",
        title="RCRS",
        format=".2f",
    ),
    alt.Tooltip(
        "predicted_risk_class:N",
        title="Risk class",
    ),
],
        )
    )

    annual_risk_chart = (
        risk_line + risk_points
    ).properties(height=300)

    st.altair_chart(
        annual_risk_chart,
        width="stretch",
    )
    st.subheader("Annual predictor history")

    feature_labels = {
        "heatwave": "Heatwave days",
        "flood": "Extreme precipitation (Rx5day)",
        "drought": "Drought magnitude",
        "gdp_per_capita": "GDP per capita",
        "unemployment_rate": "Unemployment rate",
    }

    selected_feature = st.selectbox(
        "Choose one indicator",
        options=list(feature_labels),
        format_func=feature_labels.get,
    )

    predictor_chart = (
    alt.Chart(district_history)
    .mark_line(
        point=alt.OverlayMarkDef(
            filled=True,
            fill="#74446F",
            stroke="white",
            strokeWidth=1.2,
            size=75,
        ),
        color="#2F6F8F",
        strokeWidth=2.5,
    )
    .encode(
        x=alt.X(
            "year:Q",
            title="Year",
            axis=alt.Axis(format="d"),
        ),
        y=alt.Y(
            f"{selected_feature}:Q",
            title=feature_labels[selected_feature],
        ),
        tooltip=[
            alt.Tooltip(
                "district_name:N",
                title="District",
            ),
            alt.Tooltip(
                "year:Q",
                title="Year",
                format="d",
            ),
            alt.Tooltip(
                f"{selected_feature}:Q",
                title=feature_labels[selected_feature],
                format=".2f",
            ),
        ],
    )
    .properties(height=280)
)

    st.altair_chart(
        predictor_chart,
        width="stretch",
    )
    st.dataframe(district_history.rename(columns=feature_labels), width="stretch", hide_index=True)

if page == "Model Explainability":
    hero("Explore how the five input indicators shape the model’s Regional Climate Risk Score estimates.")
    st.subheader("Global SHAP feature importance")

    st.caption(
        "Relative influence of the five climate and socioeconomic indicators "
        "on the model’s Regional Climate Risk Score estimates."
    )

    shap = data["shap"].copy()

    value_column = next(
        (column for column in shap.columns if column != "feature"),
        shap.columns[-1],
    )

    feature_column = (
        "feature"
        if "feature" in shap.columns
        else shap.columns[0]
    )

    shap_labels = {
        "heatwave": "Heatwave days",
        "flood": "Extreme precipitation (Rx5day)",
        "drought": "Drought magnitude",
        "gdp_per_capita": "GDP per capita",
        "unemployment_rate": "Unemployment rate",
    }

    shap["Display feature"] = (
        shap[feature_column]
        .map(shap_labels)
        .fillna(
            shap[feature_column]
            .str.replace("_", " ", regex=False)
            .str.title()
        )
    )

    shap_chart = (
        alt.Chart(shap)
        .mark_bar(
            color="#f39c12",
            cornerRadiusEnd=4,
        )
        .encode(
            x=alt.X(
                f"{value_column}:Q",
                title="Mean absolute SHAP value",
            ),
            y=alt.Y(
                "Display feature:N",
                title=None,
                sort="-x",
                axis=alt.Axis(labelLimit=220),
            ),
            tooltip=[
                alt.Tooltip(
                    "Display feature:N",
                    title="Indicator",
                ),
                alt.Tooltip(
                    f"{value_column}:Q",
                    title="Mean absolute SHAP value",
                    format=".3f",
                ),
            ],
        )
        .properties(height=300)
    )

    st.altair_chart(
        shap_chart,
        width="stretch",
    )

    st.info(
        "This chart shows which of the five input indicators most strongly "
        "influence the model’s approximation of the constructed Regional "
        "Climate Risk Score. It supports interpretation of the scoring "
        "workflow and should not be read as independent validation against "
        "observed climate losses, insurance claims or infrastructure failures."
    )

if page == "Sector Applications":
    hero(
        "Translate one common regional climate-risk evidence base into "
        "carefully bounded multi-sector applications."
    )

    st.markdown(
        """
        <div class="note sector-intro">
            <strong>Decision-support boundary</strong><br>
            The RCRS is a regional screening indicator. Combine it with
            sector-specific exposure, asset, operational and impact data
            before making investment, underwriting or policy decisions.
        </div>
        """,
        unsafe_allow_html=True,
    )

    sectors = [
        {
            "icon": "🏦",
            "title": "Banking, Finance & Insurance",
            "use": (
                "Screen regional exposure and portfolio concentrations; "
                "prioritise locations for deeper climate due diligence."
            ),
            "boundary": (
                "Does not estimate credit losses, claims or premiums."
            ),
            "accent": "burgundy",
        },
        {
            "icon": "🏗️",
            "title": "Infrastructure & Energy",
            "use": (
                "Identify districts where asset siting, resilience assessment "
                "and adaptation investment may require closer attention."
            ),
            "boundary": (
                "Does not assess individual assets or engineering failure."
            ),
            "accent": "amber",
        },
        {
            "icon": "🌱",
            "title": "Agriculture & Land Management",
            "use": (
                "Compare regional heat, drought and extreme-precipitation "
                "conditions relevant to production and land-use planning."
            ),
            "boundary": (
                "Does not predict crop yield or farm-level loss."
            ),
            "accent": "green",
        },
        {
            "icon": "🏛️",
            "title": "Government & Climate Adaptation",
            "use": (
                "Support regional screening, policy prioritisation and the "
                "allocation of further assessment resources."
            ),
            "boundary": (
                "Does not replace local vulnerability assessments or "
                "public consultation."
            ),
            "accent": "plum",
        },
    ]

    positions = ["node-nw", "node-ne", "node-sw", "node-se"]

    orbit_nodes = []
    pathway_rows = []

    for index, (sector, position) in enumerate(
        zip(sectors, positions),
        start=1,
    ):
        orbit_nodes.append(
            f"""
            <div class="sector-node {position} node-{sector['accent']}">
                <div class="sector-node-icon">{sector['icon']}</div>
                <span class="sector-node-number">0{index}</span>
                <strong>{sector['title']}</strong>
            </div>
            """
        )

        pathway_rows.append(
            f"""
            <section class="sector-detail detail-{sector['accent']}">
                <div class="sector-detail-heading">
                    <span class="sector-detail-icon">{sector['icon']}</span>
                    <div>
                        <span class="sector-detail-number">0{index}</span>
                        <h3>{sector['title']}</h3>
                    </div>
                </div>

                <div class="sector-detail-copy">
                    <div>
                        <span class="pathway-label">SCREENING USE</span>
                        <p>{sector['use']}</p>
                    </div>

                    <div class="sector-boundary-copy">
                        <span class="pathway-label">DECISION BOUNDARY</span>
                        <p>{sector['boundary']}</p>
                    </div>
                </div>
            </section>
            """
        )

    orbit_nodes_html = "".join(orbit_nodes)
    pathway_rows_html = "".join(pathway_rows)

    sector_visual_html = f"""
    <div class="sector-constellation-layout">

        <div class="sector-orbit" aria-label="RCRS sector application network">
            <svg
                class="sector-connectors"
                viewBox="0 0 600 420"
                preserveAspectRatio="none"
                aria-hidden="true"
            >
                <line x1="300" y1="210" x2="115" y2="92"></line>
                <line x1="300" y1="210" x2="485" y2="92"></line>
                <line x1="300" y1="210" x2="115" y2="328"></line>
                <line x1="300" y1="210" x2="485" y2="328"></line>

                <circle cx="115" cy="92" r="4"></circle>
                <circle cx="485" cy="92" r="4"></circle>
                <circle cx="115" cy="328" r="4"></circle>
                <circle cx="485" cy="328" r="4"></circle>
            </svg>

            <div class="sector-core">
                <span>CLIMATE</span>
                <strong>RCRS</strong>
                <small>regional risk signal</small>
            </div>

            {orbit_nodes_html}
        </div>

        <div class="sector-pathways">
            <div class="sector-pathways-heading">
                <span>APPLICATION PATHWAYS</span>
                <h2>From regional signal to sector screening</h2>
            </div>

            {pathway_rows_html}
        </div>
    </div>
    """

    sector_visual_html = "\n".join(
    line.strip()
    for line in sector_visual_html.splitlines()
    if line.strip()
    )

    st.markdown(
        sector_visual_html,
        unsafe_allow_html=True,
    )

if page == "Methodology & Limitations":
    hero("Understand how the prototype was developed, what its results mean and where its responsible-use boundaries lie.")
    flow_ribbons_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 245" preserveAspectRatio="none">
    <path d="M10 42 C135 42 130 202 215 202 S300 42 410 42" fill="none" stroke="#a53f32" stroke-width="34" stroke-linecap="round" opacity=".9"/>
    <path d="M10 122 C120 122 145 55 215 55 S310 122 410 122" fill="none" stroke="#d97706" stroke-width="34" stroke-linecap="round" opacity=".9"/>
    <path d="M10 202 C120 202 145 122 215 122 S300 202 410 202" fill="none" stroke="#2d7d9a" stroke-width="34" stroke-linecap="round" opacity=".9"/>
    <g fill="white" stroke-width="4"><circle cx="10" cy="42" r="6" stroke="#a53f32"/><circle cx="410" cy="42" r="6" stroke="#a53f32"/><circle cx="10" cy="122" r="6" stroke="#d97706"/><circle cx="410" cy="122" r="6" stroke="#d97706"/><circle cx="10" cy="202" r="6" stroke="#2d7d9a"/><circle cx="410" cy="202" r="6" stroke="#2d7d9a"/></g>
    </svg>"""
    flow_ribbons_uri = "data:image/svg+xml;base64," + base64.b64encode(
        flow_ribbons_svg.encode("utf-8")
    ).decode("ascii")
    methodology_html = textwrap.dedent("""
        <style>
        .method-page-heading { margin: 1.25rem 0 .15rem; color: #293040; }
        .method-page-kicker {
            margin: 0 0 1.2rem; color: #6d7480; font-size: .92rem;
        }
        .method-route {
            position: relative; margin: .4rem 0 2.5rem; padding: 1.1rem 2rem 1.4rem;
        }
        .method-route::before {
            content: ""; position: absolute; left: 10%; right: 10%; top: 4.15rem;
            height: 12rem; border: 7px solid #5bb7c9; border-left-color: transparent;
            border-radius: 0 4rem 4rem 0; opacity: .24;
        }
        .method-route::after {
            content: ""; position: absolute; left: 10%; bottom: 1.55rem;
            width: 18px; height: 18px; border-left: 7px solid #5bb7c9;
            border-bottom: 7px solid #5bb7c9; transform: rotate(45deg); opacity: .55;
        }
        .method-row {
            position: relative; z-index: 2; display: grid; grid-template-columns: repeat(3, 1fr);
            column-gap: 3.2rem;
        }
        .method-row.bottom { margin-top: 3.8rem; direction: rtl; }
        .method-step { text-align: center; direction: ltr; }
        .method-node {
            width: 3.25rem; height: 3.25rem; margin: 0 auto .7rem; border-radius: 50%;
            display: grid; place-items: center; color: white; font-weight: 800;
            font-size: 1rem; border: 5px solid #f8fafc; box-shadow: 0 7px 18px rgba(31,52,73,.16);
        }
        .method-icon { display: block; font-size: 1.4rem; margin-bottom: .35rem; }
        .method-step h3 { font-size: .98rem; margin: 0 0 .32rem; color: #293040; }
        .method-step p { max-width: 15rem; margin: 0 auto; color: #69707b; font-size: .78rem; line-height: 1.48; }
        .node-1 { background: #a53f32; } .node-2 { background: #d97706; }
        .node-3 { background: #2d7d9a; } .node-4 { background: #6b3f76; }
        .node-5 { background: #719b32; } .node-6 { background: #174f6b; }

        .limits-heading { margin-top: .6rem; }
        .limits-intro { margin: 0 0 1rem; color: #6d7480; font-size: .92rem; }
        .limits-flow {
            display: grid; grid-template-columns: minmax(12rem, 1fr) 1.25fr minmax(12rem, 1fr);
            align-items: center; column-gap: 1rem; margin: .25rem 0 1.5rem;
        }
        .flow-side { display: grid; gap: 1rem; }
        .flow-item { position: relative; padding: .25rem 0 .25rem 1rem; border-left: 3px solid var(--flow); }
        .flow-side.right .flow-item { padding: .25rem 1rem .25rem 0; border-left: 0; border-right: 3px solid var(--flow); }
        .flow-number { color: var(--flow); font-size: .68rem; font-weight: 800; letter-spacing: .13em; }
        .flow-item h3 { color: var(--flow); font-size: .93rem; margin: .12rem 0 .24rem; }
        .flow-item p { color: #69707b; font-size: .76rem; line-height: 1.45; margin: 0; }
        .flow-ribbons { width: 100%; height: 245px; overflow: visible; }
        .flow-ribbons path { fill: none; stroke-width: 34; stroke-linecap: round; opacity: .9; }
        .flow-ribbons .r1 { stroke: #a53f32; } .flow-ribbons .r2 { stroke: #d97706; }
        .flow-ribbons .r3 { stroke: #2d7d9a; }
        .flow-ribbons circle { fill: white; stroke-width: 4; }
        .use-boundary {
            display: grid; grid-template-columns: auto 1fr; gap: 1rem; align-items: center;
            margin: .6rem 0 1.2rem; padding: 1rem 1.25rem; border-top: 1px solid #e4c9c2;
            border-bottom: 1px solid #e4c9c2; background: linear-gradient(90deg, rgba(165,63,50,.07), transparent);
        }
        .boundary-mark {
            width: 3rem; height: 3rem; border-radius: 50%; display: grid; place-items: center;
            background: #a53f32; color: white; font-size: 1.35rem;
        }
        .use-boundary strong { display: block; color: #8d342a; font-size: .78rem; letter-spacing: .12em; margin-bottom: .2rem; }
        .use-boundary p { margin: 0; color: #4f5662; font-size: .84rem; line-height: 1.5; }
        @media (max-width: 900px) {
            .method-route::before, .method-route::after, .flow-ribbons { display: none; }
            .method-row, .method-row.bottom { grid-template-columns: 1fr; gap: 1.4rem; margin-top: 1.4rem; direction: ltr; }
            .limits-flow { grid-template-columns: 1fr; }
            .flow-side.right .flow-item { padding: .25rem 0 .25rem 1rem; border-right: 0; border-left: 3px solid var(--flow); }
        }
        </style>

        <h2 class="method-page-heading">Methodology</h2>
        <p class="method-page-kicker">From multi-source evidence to an explainable national climate-risk registry</p>

        <section class="method-route" aria-label="Six-stage methodology pathway">
            <div class="method-row top">
                <article class="method-step">
                    <span class="method-icon">🗃️</span><div class="method-node node-1">01</div>
                    <h3>Data Integration</h3><p>Climate hazards and socioeconomic indicators harmonised into district-year observations.</p>
                </article>
                <article class="method-step">
                    <span class="method-icon">🎚️</span><div class="method-node node-2">02</div>
                    <h3>Transformation</h3><p>Five predictors log-transformed and scaled using training-data parameters.</p>
                </article>
                <article class="method-step">
                    <span class="method-icon">◉</span><div class="method-node node-3">03</div>
                    <h3>RCRS Construction</h3><p>IPCC-informed risk score constructed using training data only.</p>
                </article>
            </div>
            <div class="method-row bottom">
                <article class="method-step">
                    <span class="method-icon">🧠</span><div class="method-node node-4">04</div>
                    <h3>PyTorch FFNN</h3><p>A feed-forward neural network trained to approximate the RCRS.</p>
                </article>
                <article class="method-step">
                    <span class="method-icon">🔎</span><div class="method-node node-5">05</div>
                    <h3>SHAP Explanation</h3><p>Global and local model behaviour interpreted through feature contributions.</p>
                </article>
                <article class="method-step">
                    <span class="method-icon">▦</span><div class="method-node node-6">06</div>
                    <h3>District Registry</h3><p>Annual predictions aggregated by district median for the 1990–2025 NCRR-G.</p>
                </article>
            </div>
        </section>

        <h2 class="method-page-heading limits-heading">Limitations and development pathway</h2>
        <p class="limits-intro">Three connected evidence boundaries define how the prototype should be interpreted—and where it can develop next.</p>

        <section class="limits-flow" aria-label="Limitations linked to future development">
            <div class="flow-side left">
                <article class="flow-item" style="--flow:#a53f32"><span class="flow-number">01 · CURRENT LIMIT</span><h3>Data coverage</h3><p>289 of 400 current districts are modelled; climate variables were transferred from NUTS-2 to NUTS-3.</p></article>
                <article class="flow-item" style="--flow:#d97706"><span class="flow-number">02 · CURRENT LIMIT</span><h3>Indicator depth</h3><p>GDP per capita and unemployment provide limited proxies for vulnerability and adaptive capacity.</p></article>
                <article class="flow-item" style="--flow:#2d7d9a"><span class="flow-number">03 · CURRENT LIMIT</span><h3>Analytical boundary</h3><p>The constructed score, random split and district median do not test future climate or preserve annual extremes.</p></article>
            </div>

            <img class="flow-ribbons" src="__FLOW_RIBBONS_URI__" alt="Three connected limitation and development pathways">

            <div class="flow-side right">
                <article class="flow-item" style="--flow:#a53f32"><span class="flow-number">COVERAGE PATHWAY</span><h3>Complete spatial coverage</h3><p>Use versioned historical crosswalks and updated district-level socioeconomic data.</p></article>
                <article class="flow-item" style="--flow:#d97706"><span class="flow-number">EVIDENCE PATHWAY</span><h3>Richer risk indicators</h3><p>Add exposure, vulnerability, observed impacts and sector-specific evidence.</p></article>
                <article class="flow-item" style="--flow:#2d7d9a"><span class="flow-number">VALIDATION PATHWAY</span><h3>Scenario-based validation</h3><p>Test temporal performance and integrate future climate-scenario evidence.</p></article>
            </div>
        </section>

        <aside class="use-boundary">
            <div class="boundary-mark">⚖</div>
            <div><strong>SCREENING, NOT FINAL DECISION-MAKING</strong><p>Outputs support exploration and prioritisation. They do not replace regulatory, credit, underwriting, engineering or local vulnerability assessments.</p></div>
        </aside>
        """).strip().replace("__FLOW_RIBBONS_URI__", flow_ribbons_uri)
    methodology_html = "\n".join(
        line.strip()
        for line in methodology_html.splitlines()
        if line.strip()
    )
    st.markdown(
        methodology_html,
        unsafe_allow_html=True,
    )

if page == "About the Project":
    hero(
        "Meet the project author and explore the professional, "
        "technical and data foundations behind the platform."
    )

    author_image = image_data_uri(APP_DIR / "assets" / "about-human-ai.png")
    st.markdown(
        textwrap.dedent(f"""
        <style>
        .about-title {{ margin: 1.25rem 0 .35rem; color: #293040; }}
        .about-lead {{ max-width: 62rem; color: #535b67; font-size: .94rem; line-height: 1.65; margin: 0 0 1.5rem; }}
        .author-signature {{
            display: grid; grid-template-columns: minmax(15rem, .72fr) 1.45fr;
            gap: 2.2rem; align-items: center; margin: .3rem 0 2.2rem;
        }}
        .author-visual {{ position: relative; height: 23rem; overflow: hidden; border-radius: 46% 54% 48% 52% / 35% 38% 62% 65%; box-shadow: 0 18px 42px rgba(21,54,75,.18); }}
        .author-visual img {{ width: 100%; height: 100%; object-fit: cover; object-position: 50% 31%; display: block; }}
        .author-visual span {{ position: absolute; left: 1rem; bottom: .85rem; padding: .28rem .6rem; border-radius: 999px; background: rgba(10,34,49,.72); color: white; font-size: .61rem; letter-spacing: .1em; }}
        .author-copy .eyebrow, .architecture-eyebrow {{ color: #2d7d9a; font-weight: 800; letter-spacing: .14em; font-size: .7rem; }}
        .author-copy h2 {{ margin: .35rem 0 .35rem; font-size: 1.65rem; color: #293040; }}
        .author-roles {{ color: #a53f32; font-size: .82rem; font-weight: 650; line-height: 1.55; margin-bottom: .85rem; }}
        .author-copy p {{ color: #59616d; font-size: .86rem; line-height: 1.62; }}
        .author-quote {{ margin: 1rem 0; padding: .75rem 0 .75rem 1rem; border-left: 3px solid #d97706; color: #35404c !important; font-style: italic; }}
        .author-links {{ display: flex; flex-wrap: wrap; gap: .65rem; margin-top: 1rem; }}
        .author-links a {{ padding: .48rem .9rem; border: 1px solid #2d7d9a; border-radius: 999px; color: #235f76 !important; text-decoration: none; font-size: .75rem; font-weight: 700; }}
        .architecture-head {{ margin: .4rem 0 1rem; }}
        .architecture-head h2 {{ margin: .25rem 0 .2rem; color: #293040; }}
        .architecture-head p {{ margin: 0; color: #6b727d; font-size: .86rem; }}
        .architecture-tower {{ margin: 1rem 0 2.4rem; display: grid; gap: .42rem; }}
        .tower-row {{ display: grid; grid-template-columns: 1fr 22rem 1fr; align-items: center; min-height: 4.4rem; }}
        .tower-core {{ width: var(--width); justify-self: center; position: relative; }}
        .tower-platform {{
            position: relative; min-height: 3.65rem; display: grid; grid-template-columns: 2.3rem 1fr;
            align-items: center; gap: .45rem; padding: .45rem 1.1rem .6rem; color: white;
            background: linear-gradient(135deg, color-mix(in srgb, var(--layer) 88%, white), var(--layer));
            clip-path: polygon(9% 0, 91% 0, 100% 28%, 92% 100%, 8% 100%, 0 28%);
            filter: drop-shadow(0 7px 7px rgba(27,46,61,.18));
        }}
        .tower-platform::after {{ content:""; position:absolute; left:9%; right:8%; bottom:0; height:.38rem; background:rgba(0,0,0,.15); }}
        .tower-icon {{ width:2rem; height:2rem; border-radius:50%; display:grid; place-items:center; background:rgba(255,255,255,.18); font-size:1rem; font-weight:800; }}
        .tower-platform strong {{ font-size:.8rem; line-height:1.25; }}
        .tower-callout {{ position:relative; max-width:19rem; padding:.2rem 1rem; }}
        .tower-callout::after {{ content:""; position:absolute; top:50%; width:2.5rem; height:1px; background:var(--layer); opacity:.55; }}
        .tower-callout.left {{ justify-self:end; text-align:right; border-right:3px solid var(--layer); margin-right:1rem; }}
        .tower-callout.left::after {{ right:-2.65rem; }}
        .tower-callout.right {{ justify-self:start; text-align:left; border-left:3px solid var(--layer); margin-left:1rem; }}
        .tower-callout.right::after {{ left:-2.65rem; }}
        .tower-callout span {{ display:block; color:var(--layer); font-size:.63rem; font-weight:850; letter-spacing:.11em; margin-bottom:.2rem; }}
        .tower-callout p {{ margin:0; color:#626a75; font-size:.71rem; line-height:1.42; }}
        .tower-empty {{ min-height:1px; }}
        .provenance {{ display: grid; grid-template-columns: repeat(3,1fr); align-items: start; margin: .8rem 0 1.2rem; position: relative; }}
        .provenance::before {{ content:""; position:absolute; left:16%; right:16%; top:1.75rem; height:1px; background:#bfd6dc; }}
        .source-node {{ position: relative; text-align:center; z-index:1; }}
        .source-node b {{ width:3.5rem; height:3.5rem; margin:0 auto .55rem; display:grid; place-items:center; border-radius:50%; color:white; background:var(--source); border:5px solid #f8fafc; box-shadow:0 5px 14px rgba(28,58,77,.13); font-size:.72rem; }}
        .source-node strong {{ display:block; color:#303946; font-size:.8rem; margin-bottom:.18rem; }}
        .source-node span {{ color:#707782; font-size:.7rem; }}
        .source-note {{ text-align:center; color:#7a8089; font-size:.7rem; margin-bottom:1.5rem; }}
        .version-ribbon {{ display:flex; flex-wrap:wrap; justify-content:center; gap:.2rem 1.5rem; padding:.78rem 1rem; background:linear-gradient(90deg,#5a2831,#b54e2e,#d97706); color:white; border-radius:.7rem; font-size:.7rem; font-weight:800; letter-spacing:.09em; }}
        .version-ribbon span:not(:last-child)::after {{ content:"·"; margin-left:1.5rem; opacity:.7; }}
        .version-note {{ text-align:center; max-width:58rem; margin:.75rem auto 1.2rem; color:#646b75; font-size:.78rem; }}
        @media (max-width: 850px) {{
            .author-signature {{ grid-template-columns: 1fr; }} .author-visual {{ height: 21rem; }}
            .tower-row {{ grid-template-columns:1fr; gap:.35rem; margin-bottom:1rem; }}
            .tower-core {{ width:100% !important; grid-row:1; }}
            .tower-callout.left, .tower-callout.right {{ grid-row:2; justify-self:stretch; text-align:left; margin:0; border-left:3px solid var(--layer); border-right:0; }}
            .tower-callout::after, .tower-empty {{ display:none; }}
            .provenance {{ grid-template-columns:1fr; gap:1rem; }}
            .provenance::before {{ display:none; }}
        }}
        </style>

        <h2 class="about-title">About the project</h2>
        <p class="about-lead">Conceived and developed by <strong>Purity Rima Mbaabu-Fuerst</strong>, this AI Engineering prototype integrates climate science, geospatial data, socioeconomic evidence, machine learning and explainable AI to support regional climate-risk screening across Germany.</p>

        <section class="author-signature">
            <div class="author-visual"><img src="{author_image}" alt="Concept illustration of an African woman working at the intersection of climate, geospatial intelligence and AI"><span>CONCEPT ILLUSTRATION</span></div>
            <div class="author-copy">
                <span class="eyebrow">PROJECT AUTHOR</span>
                <h2>Purity Rima Mbaabu-Fuerst</h2>
                <div class="author-roles">AI Engineering · Data Science & Machine Learning · Climate & Sustainability Intelligence · Geospatial Analytics · Digital Transformation</div>
                <p>Purity works at the intersection of climate change, geospatial intelligence, sustainability and responsible artificial intelligence. Her work focuses on transforming environmental and socioeconomic evidence into intelligence that supports policy, investment and resilience decisions.</p>
                <p class="author-quote">“Translating environmental and socioeconomic data into accessible intelligence for policy, investment and resilience decisions.”</p>
                <div class="author-links"><a href="https://www.linkedin.com/in/purity-mbaabu-b47a5b54/" target="_blank">LinkedIn profile ↗</a><a href="https://github.com/purityrima/climate-esg-risk-intelligence-germany" target="_blank">GitHub repository ↗</a></div>
            </div>
        </section>

        <div class="architecture-head"><span class="architecture-eyebrow">PROJECT ARCHITECTURE</span><h2>From evidence foundation to decision support</h2><p>Five connected layers summarise the platform’s technical and analytical foundation.</p></div>
        <section class="architecture-tower" aria-label="Five-layer project architecture">
            <div class="tower-row" style="--layer:#a53f32"><div class="tower-callout left"><span>APPLICATION LAYER</span><p>Streamlit · Altair · PyDeck · national registry · interactive map · district profiles</p></div><div class="tower-core" style="--width:62%"><div class="tower-platform" style="--layer:#a53f32"><b class="tower-icon">↗</b><strong>Decision-Support<br>Application</strong></div></div><div class="tower-empty"></div></div>
            <div class="tower-row" style="--layer:#d97706"><div class="tower-empty"></div><div class="tower-core" style="--width:72%"><div class="tower-platform" style="--layer:#d97706"><b class="tower-icon">✦</b><strong>AI & Explainability</strong></div></div><div class="tower-callout right"><span>INTELLIGENCE LAYER</span><p>PyTorch FFNN · 5–64–32–1 architecture · train/validation/test evaluation · SHAP</p></div></div>
            <div class="tower-row" style="--layer:#719b32"><div class="tower-callout left"><span>RISK LAYER</span><p>10,404 observations · 289 districts · five predictors · IPCC-informed RCRS</p></div><div class="tower-core" style="--width:82%"><div class="tower-platform" style="--layer:#719b32"><b class="tower-icon">◎</b><strong>Risk Intelligence</strong></div></div><div class="tower-empty"></div></div>
            <div class="tower-row" style="--layer:#2d7d9a"><div class="tower-empty"></div><div class="tower-core" style="--width:91%"><div class="tower-platform" style="--layer:#2d7d9a"><b class="tower-icon">⌘</b><strong>Data & Spatial<br>Engineering</strong></div></div><div class="tower-callout right"><span>ENGINEERING LAYER</span><p>Python · pandas · xarray · GeoPandas · temporal harmonisation · administrative crosswalks</p></div></div>
            <div class="tower-row" style="--layer:#174f6b"><div class="tower-callout left"><span>FOUNDATION LAYER</span><p>ERA5 climate indicators · INKAR socioeconomic data · Eurostat/GISCO boundaries</p></div><div class="tower-core" style="--width:100%"><div class="tower-platform" style="--layer:#174f6b"><b class="tower-icon">◉</b><strong>Evidence Foundation</strong></div></div><div class="tower-empty"></div></div>
        </section>

        <div class="architecture-head"><span class="architecture-eyebrow">DATA PROVENANCE</span><h2>Authoritative source foundations</h2></div>
        <section class="provenance">
            <div class="source-node" style="--source:#2d7d9a"><b>CDS</b><strong>Copernicus</strong><span>ERA5-derived climate evidence</span></div>
            <div class="source-node" style="--source:#719b32"><b>BBSR</b><strong>INKAR / BBSR</strong><span>District socioeconomic evidence</span></div>
            <div class="source-node" style="--source:#6b3f76"><b>EU</b><strong>Eurostat / GISCO</strong><span>Administrative geography</span></div>
        </section>
        <p class="source-note">Original data providers retain ownership and responsibility for their respective datasets.</p>

        <div class="version-ribbon"><span>VERSION 1</span><span>PORTFOLIO PROTOTYPE</span><span>GERMANY</span><span>1990–2025</span><span>289 DISTRICTS</span></div>
        <p class="version-note">Designed for transparent regional screening and exploration—not operational risk rating or future-climate forecasting.</p>
        """).strip(),
        unsafe_allow_html=True,
    )
