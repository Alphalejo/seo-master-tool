import streamlit as st
import pandas as pd
import plotly.express as px

def show_analytics_dashboard(data, broken_links=None):
    if not data:
        st.warning("No data available to generate charts.")
        return

    df = pd.DataFrame(data)
    df['Status'] = df['length'].apply(lambda x: 'Optimized' if 45 <= x <= 60 else 'Needs Review')

    col1, col2 = st.columns(2)

    with col1:
        # SEO Health Donut Chart
        fig_pie = px.pie(
            df, names='Status', title="Overall SEO Health",
            color='Status', color_discrete_map={'Optimized': '#27ae60', 'Needs Review': '#e74c3c'},
            hole=0.4
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    with col2:
        # Title Length Distribution
        fig_hist = px.histogram(
            df, x="length", nbins=15, title="Title Length Distribution",
            labels={'length': 'Character Count'}, color_discrete_sequence=['#3498db']
        )
        fig_hist.add_vline(x=45, line_dash="dash", line_color="green", annotation_text="Min (45)")
        fig_hist.add_vline(x=60, line_dash="dash", line_color="green", annotation_text="Max (60)")
        st.plotly_chart(fig_hist, use_container_width=True)

    # Broken Links Chart (only if broken link check was run)
    if broken_links is not None:
        st.divider()
        df_broken = pd.DataFrame(broken_links) if broken_links else pd.DataFrame(columns=['Status'])

        # Count all internal links to calculate healthy ones
        total_checked = len(set(link for _, link in [(r['Page'], r['Broken Link']) for r in broken_links])) if broken_links else 0
        total_pages = len(data)

        status_counts = df_broken['Status'].value_counts().reset_index()
        status_counts.columns = ['Status', 'Count']

        # Add healthy links row
        healthy_count = total_pages - len(df_broken)
        if healthy_count > 0:
            status_counts = pd.concat([
                pd.DataFrame([{'Status': 'Healthy', 'Count': healthy_count}]),
                status_counts
            ], ignore_index=True)

        color_map = {
            'Healthy': '#27ae60',
            '404': '#e74c3c',
            '404 (soft)': '#e67e22',
            'Timeout': '#f39c12',
            'Connection Error': '#8e44ad',
            'Redirect Loop': '#c0392b',
        }

        fig_links = px.pie(
            status_counts, names='Status', values='Count',
            title="Link Health Status", hole=0.4,
            color='Status', color_discrete_map=color_map
        )
        st.plotly_chart(fig_links, use_container_width=True)