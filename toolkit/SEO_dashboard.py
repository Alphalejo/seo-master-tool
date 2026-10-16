import streamlit as st
import pandas as pd
import plotly.express as px

def show_analytics_dashboard(data, broken_links=None):
    if not data:
        st.warning("No data available to generate charts.")
        return

    df = pd.DataFrame(data)
    df['title_status'] = df['length'].apply(lambda x: 'Optimized' if 45 <= x <= 60 else 'Needs Review')

    # --- Description categorization ---
    def desc_status(row):
        if not row['description']:
            return 'Missing'
        elif row['desc_length'] < 120:
            return 'Too Short'
        elif row['desc_length'] > 158:
            return 'Too Long'
        else:
            return 'Optimized'

    df['desc_status'] = df.apply(desc_status, axis=1)

    # Duplicate detection
    desc_counts = df[df['description'] != '']['description'].value_counts()
    duplicate_count = int((desc_counts > 1).sum())
    total_count = len(df)

    # --- ROW 1: Title charts ---
    st.markdown("#### 🏷️ SEO Titles")
    col1, col2 = st.columns(2)

    with col1:
        fig_pie = px.pie(
            df, names='title_status', title="Overall Title Health",
            color='title_status',
            color_discrete_map={'Optimized': '#27ae60', 'Needs Review': '#e74c3c'},
            hole=0.4
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    with col2:
        fig_hist = px.histogram(
            df, x="length", nbins=15, title="Title Length Distribution",
            labels={'length': 'Character Count'}, color_discrete_sequence=['#3498db']
        )
        fig_hist.add_vline(x=45, line_dash="dash", line_color="green", annotation_text="Min (45)")
        fig_hist.add_vline(x=60, line_dash="dash", line_color="green", annotation_text="Max (60)")
        st.plotly_chart(fig_hist, use_container_width=True)

    # --- ROW 2: Description charts ---
    st.markdown("#### 📝 Meta Descriptions")
    col3, col4, col5 = st.columns(3)

    with col3:
        fig_desc = px.pie(
            df, names='desc_status', title="Description Health",
            color='desc_status',
            color_discrete_map={
                'Optimized': '#27ae60',
                'Too Short': '#f39c12',
                'Too Long': '#e67e22',
                'Missing': '#e74c3c'
            },
            hole=0.4
        )
        st.plotly_chart(fig_desc, use_container_width=True)

    with col4:
        fig_desc_hist = px.histogram(
            df[df['description'] != ''], x="desc_length", nbins=15,
            title="Description Length Distribution",
            labels={'desc_length': 'Character Count'},
            color_discrete_sequence=['#9b59b6']
        )
        fig_desc_hist.add_vline(x=120, line_dash="dash", line_color="green", annotation_text="Min (120)")
        fig_desc_hist.add_vline(x=158, line_dash="dash", line_color="green", annotation_text="Max (158)")
        st.plotly_chart(fig_desc_hist, use_container_width=True)

    with col5:
        fig_dup = px.pie(
            names=['Unique', 'Duplicated'],
            values=[total_count - duplicate_count, duplicate_count],
            title="Duplicate Descriptions",
            color_discrete_sequence=['#27ae60', '#e74c3c'],
            hole=0.4
        )
        st.plotly_chart(fig_dup, use_container_width=True)

    # --- Broken links chart ---
    if broken_links is not None:
        st.divider()
        st.markdown("#### 🔗 Link Health")
        df_broken = pd.DataFrame(broken_links) if broken_links else pd.DataFrame(columns=['Status'])

        status_counts = df_broken['Status'].value_counts().reset_index()
        status_counts.columns = ['Status', 'Count']

        healthy_count = total_count - len(df_broken)
        if healthy_count > 0:
            status_counts = pd.concat([
                pd.DataFrame([{'Status': 'Healthy', 'Count': healthy_count}]),
                status_counts
            ], ignore_index=True)

        color_map = {
            'Healthy': '#27ae60',
            '404': '#e74c3c',
            'Timeout': "#ffef16",
            'Connection Error': '#8e44ad',
            'Redirect Loop': '#c0392b',
        }

        fig_links = px.pie(
            status_counts, names='Status', values='Count',
            title="Link Health Status", hole=0.4,
            color='Status', color_discrete_map=color_map
        )
        st.plotly_chart(fig_links, use_container_width=True)