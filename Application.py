from pathlib import Path

import joblib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="MovieMatch AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PREMIUM CINEMATIC THEME
# ============================================================

st.markdown(
    """
    <style>
    :root {
        --bg: #090909;
        --panel: #141414;
        --panel-soft: #1c1c1c;
        --gold: #f5c518;
        --orange: #ff8a00;
        --red: #e50914;
        --text: #f5f5f5;
        --muted: #b3b3b3;
        --border: #2d2d2d;
    }

    .stApp {
        background:
            radial-gradient(circle at top right, rgba(229, 9, 20, 0.14), transparent 28%),
            radial-gradient(circle at top left, rgba(245, 197, 24, 0.08), transparent 24%),
            linear-gradient(180deg, #090909 0%, #111111 100%);
        color: var(--text);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f0f0f 0%, #151515 100%);
        border-right: 1px solid #2a2a2a;
    }

    [data-testid="stSidebar"] * {
        color: #f1f1f1;
    }

    h1, h2, h3 {
        color: #ffffff !important;
        letter-spacing: -0.02em;
    }

    p, li {
        color: #d1d1d1;
    }

    .hero {
        position: relative;
        overflow: hidden;
        padding: 42px;
        border-radius: 24px;
        background:
            linear-gradient(110deg, rgba(0,0,0,.92) 0%, rgba(0,0,0,.70) 55%, rgba(229,9,20,.28) 100%),
            linear-gradient(135deg, #2a0b0d, #111111 65%);
        border: 1px solid #3a3a3a;
        box-shadow: 0 25px 70px rgba(0,0,0,.45);
        margin-bottom: 26px;
    }

    .hero::after {
        content: "🎞️";
        position: absolute;
        right: 28px;
        top: 8px;
        font-size: 8rem;
        opacity: 0.14;
        transform: rotate(-8deg);
    }

    .hero-kicker {
        color: var(--gold);
        font-size: .85rem;
        font-weight: 800;
        letter-spacing: .18em;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    .hero-title {
        color: #fff;
        font-size: 3.4rem;
        font-weight: 900;
        line-height: 1.05;
        margin-bottom: 12px;
    }

    .hero-subtitle {
        color: #f3f3f3;
        font-size: 1.25rem;
        max-width: 780px;
        margin-bottom: 18px;
    }

    .hero-chip {
        display: inline-block;
        margin-right: 8px;
        margin-top: 8px;
        padding: 7px 12px;
        border-radius: 999px;
        background: rgba(245,197,24,.12);
        border: 1px solid rgba(245,197,24,.35);
        color: #ffe57a;
        font-size: .86rem;
        font-weight: 700;
    }

    .kpi-card {
        background: linear-gradient(145deg, #171717, #101010);
        border: 1px solid #2f2f2f;
        border-radius: 18px;
        padding: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,.28);
        min-height: 132px;
    }

    .kpi-label {
        color: #a9a9a9;
        font-size: .9rem;
        text-transform: uppercase;
        letter-spacing: .08em;
    }

    .kpi-value {
        color: #ffffff;
        font-size: 2rem;
        font-weight: 900;
        margin-top: 8px;
    }

    .kpi-note {
        color: #f5c518;
        font-size: .86rem;
        margin-top: 4px;
    }

    .feature-card {
        background: linear-gradient(145deg, #181818, #111111);
        border: 1px solid #2d2d2d;
        border-radius: 18px;
        padding: 20px;
        min-height: 180px;
        transition: transform .2s ease, border-color .2s ease;
    }

    .feature-card:hover {
        transform: translateY(-3px);
        border-color: #5a5a5a;
    }

    .feature-icon {
        font-size: 2rem;
        margin-bottom: 8px;
    }

    .feature-title {
        color: #fff;
        font-size: 1.1rem;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .feature-copy {
        color: #bdbdbd;
        font-size: .95rem;
        line-height: 1.55;
    }

    .movie-card {
        background: linear-gradient(145deg, #191919, #101010);
        border: 1px solid #2f2f2f;
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 14px;
        box-shadow: 0 12px 28px rgba(0,0,0,.25);
    }

    .movie-rank {
        color: var(--gold);
        font-size: .8rem;
        font-weight: 900;
        letter-spacing: .12em;
        text-transform: uppercase;
    }

    .movie-title {
        color: #fff;
        font-size: 1.25rem;
        font-weight: 850;
        margin: 4px 0 8px;
    }

    .movie-meta {
        color: #b8b8b8;
        font-size: .9rem;
    }

    .score-pill {
        display: inline-block;
        padding: 6px 10px;
        border-radius: 999px;
        background: rgba(229,9,20,.14);
        border: 1px solid rgba(229,9,20,.42);
        color: #ff8c93;
        font-weight: 800;
        font-size: .84rem;
    }

    .section-label {
        color: var(--gold);
        font-size: .82rem;
        font-weight: 900;
        letter-spacing: .16em;
        text-transform: uppercase;
        margin-bottom: 5px;
    }

    [data-testid="stMetric"] {
        background: linear-gradient(145deg, #171717, #111111);
        border: 1px solid #303030;
        padding: 18px;
        border-radius: 16px;
    }

    [data-testid="stMetricLabel"] {
        color: #b5b5b5 !important;
    }

    [data-testid="stMetricValue"] {
        color: #ffffff !important;
    }

    .stButton > button,
    .stDownloadButton > button {
        background: linear-gradient(90deg, #e50914, #ff5a1f);
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: 800;
        padding: .7rem 1.1rem;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {
        background: linear-gradient(90deg, #c90812, #e64f1d);
        transform: translateY(-1px);
    }

    [data-testid="stDataFrame"] {
        border: 1px solid #2f2f2f;
        border-radius: 14px;
        overflow: hidden;
    }

    div[data-testid="stAlert"] {
        border-radius: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"

RECOMMENDATIONS_PATH = MODELS_DIR / "user_recommendations.csv"
POPULAR_MOVIES_PATH = MODELS_DIR / "popular_movies.csv"
MOVIES_PATH = MODELS_DIR / "movies.csv"
USERS_PATH = MODELS_DIR / "users.csv"
RATINGS_PATH = MODELS_DIR / "ratings.csv"
METRICS_PATH = MODELS_DIR / "model_metrics.pkl"


# ============================================================
# DATA LOADING
# ============================================================

@st.cache_data(show_spinner=False)
def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


@st.cache_resource(show_spinner=False)
def load_metrics(path: Path) -> dict:
    return joblib.load(path)


load_errors = []

def safe_csv(path: Path, name: str) -> pd.DataFrame:
    try:
        return load_csv(path)
    except Exception as exc:
        load_errors.append(f"{name}: {exc}")
        return pd.DataFrame()


recommendations_df = safe_csv(
    RECOMMENDATIONS_PATH,
    "user_recommendations.csv",
)
popular_movies_df = safe_csv(
    POPULAR_MOVIES_PATH,
    "popular_movies.csv",
)
movies_df = safe_csv(MOVIES_PATH, "movies.csv")
users_df = safe_csv(USERS_PATH, "users.csv")
ratings_df = safe_csv(RATINGS_PATH, "ratings.csv")

try:
    metrics = load_metrics(METRICS_PATH)
except Exception as exc:
    metrics = {
        "Train Precision@10": 0.594161,
        "Test Precision@10": 0.217698,
        "Test Recall@10": 0.246173,
        "Test AUC": 0.939927,
        "Users": 943,
        "Movies": 1682,
        "Ratings": 100000,
        "Positive Interactions": 55375,
    }
    load_errors.append(f"model_metrics.pkl: {exc}")


def metric(keys, default):
    for key in keys:
        if key in metrics:
            return float(metrics[key])
    return float(default)


train_precision = metric(
    ["Train Precision@10", "train_precision_at_10"],
    0.594161,
)
test_precision = metric(
    ["Test Precision@10", "test_precision_at_10"],
    0.217698,
)
test_recall = metric(
    ["Test Recall@10", "test_recall_at_10"],
    0.246173,
)
test_auc = metric(
    ["Test AUC", "test_auc"],
    0.939927,
)


def style_plot(fig):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#111111",
        font_color="#f0f0f0",
        title_font_color="#f5c518",
        margin=dict(l=30, r=20, t=70, b=30),
    )
    return fig


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.title("🎬 MovieMatch AI")
    st.caption("Personalized Cinema Discovery")

    st.divider()

    page = st.radio(
        "Browse",
        [
            "🏠 Discover",
            "🎯 For You",
            "🔥 Trending",
            "📊 Audience Insights",
            "📈 Model Studio",
            "ℹ️ About",
        ],
    )

    st.divider()

    if load_errors:
        st.warning("Some project files could not be loaded.")
        with st.expander("View details"):
            for error in load_errors:
                st.write(error)
    else:
        st.success("🟢 Recommendation Engine Ready")

    st.markdown("**Model**")
    st.caption("LightFM · WARP Loss")

    st.markdown("**Dataset**")
    st.caption("MovieLens 100K")


# ============================================================
# HOME / DISCOVER
# ============================================================

if page == "🏠 Discover":
    st.markdown(
        """
        <div class="hero">
            <div class="hero-kicker">AI-Powered Recommendations</div>
            <div class="hero-title">MovieMatch AI</div>
            <div class="hero-subtitle">
                A personalized cinema discovery experience powered by
                collaborative filtering and intelligent ranking.
            </div>
            <span class="hero-chip">LightFM</span>
            <span class="hero-chip">WARP Loss</span>
            <span class="hero-chip">MovieLens 100K</span>
            <span class="hero-chip">Top-N Ranking</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)

    stats = [
        ("Viewers", f"{len(users_df):,}" if not users_df.empty else "943", "Personal profiles"),
        ("Movies", f"{len(movies_df):,}" if not movies_df.empty else "1,682", "Titles ranked"),
        ("Ratings", f"{len(ratings_df):,}" if not ratings_df.empty else "100,000", "Preference signals"),
        ("Test AUC", f"{test_auc * 100:.2f}%", "Ranking quality"),
    ]

    for column, (label, value, note) in zip([c1, c2, c3, c4], stats):
        with column:
            st.markdown(
                f"""
                <div class="kpi-card">
                    <div class="kpi-label">{label}</div>
                    <div class="kpi-value">{value}</div>
                    <div class="kpi-note">{note}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.divider()

    st.markdown('<div class="section-label">How it works</div>', unsafe_allow_html=True)
    st.header("From ratings to recommendations")

    f1, f2, f3, f4 = st.columns(4)

    cards = [
        ("⭐", "Preference Signals", "Ratings of 4 and 5 are treated as positive interactions."),
        ("🧠", "Latent Learning", "LightFM learns hidden user and movie representations."),
        ("🎯", "WARP Ranking", "The model focuses on improving the top of the recommendation list."),
        ("🍿", "Personalized Picks", "Each viewer receives a ranked set of unseen movies."),
    ]

    for column, (icon, title, copy) in zip([f1, f2, f3, f4], cards):
        with column:
            st.markdown(
                f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <div class="feature-title">{title}</div>
                    <div class="feature-copy">{copy}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.divider()

    st.markdown('<div class="section-label">Highlights</div>', unsafe_allow_html=True)
    st.header("Built for exploration")

    left, right = st.columns(2)

    with left:
        st.success(
            """
            **Personalized movie discovery**

            Select a viewer, choose the number of recommendations, inspect
            ranked scores, and download the final recommendation list.
            """
        )

    with right:
        st.info(
            """
            **Rich analytics**

            Explore popular titles, rating patterns, active users, audience
            occupations, and model evaluation metrics.
            """
        )


# ============================================================
# FOR YOU
# ============================================================

elif page == "🎯 For You":
    st.markdown('<div class="section-label">Personalized feed</div>', unsafe_allow_html=True)
    st.title("🎯 Recommendations For You")

    if recommendations_df.empty:
        st.error("Recommendation data is unavailable.")
        st.stop()

    available_users = sorted(
        recommendations_df["user_id"].dropna().astype(int).unique()
    )

    control1, control2 = st.columns([2, 1])

    with control1:
        selected_user = st.selectbox(
            "Choose a MovieLens user",
            available_users,
        )

    with control2:
        top_n = st.slider(
            "Number of recommendations",
            min_value=5,
            max_value=20,
            value=10,
        )

    user_recs = (
        recommendations_df[
            recommendations_df["user_id"].astype(int) == int(selected_user)
        ]
        .sort_values("rank")
        .head(top_n)
        .copy()
    )

    profile = None
    if not users_df.empty:
        match = users_df[
            users_df["user_id"].astype(int) == int(selected_user)
        ]
        if not match.empty:
            profile = match.iloc[0]

    if profile is not None:
        st.subheader("Viewer profile")
        p1, p2, p3, p4 = st.columns(4)
        with p1:
            st.metric("User ID", int(profile["user_id"]))
        with p2:
            st.metric("Age", int(profile["age"]))
        with p3:
            st.metric("Gender", str(profile["gender"]))
        with p4:
            st.metric("Occupation", str(profile["occupation"]))

    st.divider()
    st.subheader(f"Top {len(user_recs)} Picks")

    if user_recs.empty:
        st.warning("No recommendations are available for this user.")
    else:
        card_columns = st.columns(2)

        for index, (_, row) in enumerate(user_recs.iterrows()):
            with card_columns[index % 2]:
                score = float(row.get("recommendation_score", 0.0))
                title = str(row.get("title", "Unknown Movie"))
                release = str(row.get("release_date", "Unknown"))
                rank = int(row.get("rank", index + 1))
                imdb_url = row.get("imdb_url", "")

                st.markdown(
                    f"""
                    <div class="movie-card">
                        <div class="movie-rank">Rank #{rank}</div>
                        <div class="movie-title">{title}</div>
                        <div class="movie-meta">Release: {release}</div>
                        <div style="margin-top:10px;">
                            <span class="score-pill">Score {score:.4f}</span>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

              
    st.divider()

    table_columns = [
        column
        for column in [
            "rank",
            "title",
            "release_date",
            "recommendation_score",
                    ]
        if column in user_recs.columns
    ]

    table = user_recs[table_columns].rename(
        columns={
            "rank": "Rank",
            "title": "Movie",
            "release_date": "Release Date",
            "recommendation_score": "Recommendation Score",
            
        }
    )

    if "Recommendation Score" in table.columns:
        table["Recommendation Score"] = table["Recommendation Score"].round(4)

    st.dataframe(
        table,
        width="stretch",
        hide_index=True,
       
       
    )

    st.download_button(
        "⬇️ Download this recommendation list",
        data=user_recs.to_csv(index=False).encode("utf-8"),
        file_name=f"moviematch_user_{selected_user}.csv",
        mime="text/csv",
    )


# ============================================================
# TRENDING
# ============================================================

elif page == "🔥 Trending":
    st.markdown('<div class="section-label">What viewers love</div>', unsafe_allow_html=True)
    st.title("🔥 Trending Movies")

    if popular_movies_df.empty:
        st.error("Popular movie data is unavailable.")
        st.stop()

    c1, c2, c3 = st.columns([1, 1, 1])

    with c1:
        ranking_method = st.selectbox(
            "Ranking method",
            ["Most Rated", "Highest Rated"],
        )

    with c2:
        top_n = st.slider(
            "Movies to display",
            min_value=5,
            max_value=30,
            value=15,
        )

    with c3:
        max_count = int(popular_movies_df["rating_count"].max())
        min_ratings = st.number_input(
            "Minimum rating count",
            min_value=1,
            max_value=max_count,
            value=min(100, max_count),
            step=10,
        )

    filtered = popular_movies_df[
        popular_movies_df["rating_count"] >= min_ratings
    ].copy()

    if ranking_method == "Most Rated":
        filtered = filtered.sort_values(
            ["rating_count", "average_rating"],
            ascending=False,
        )
    else:
        filtered = filtered.sort_values(
            ["average_rating", "rating_count"],
            ascending=False,
        )

    filtered = filtered.head(top_n)

    st.subheader("Leaderboard")

    leaderboard = filtered.copy()
    leaderboard.insert(0, "rank", range(1, len(leaderboard) + 1))

    display_columns = [
        column
        for column in [
            "rank",
            "title",
            "rating_count",
            "average_rating",
            "release_date",
           
        ]
        if column in leaderboard.columns
    ]

    st.dataframe(
        leaderboard[display_columns].rename(
            columns={
                "rank": "Rank",
                "title": "Movie",
                "rating_count": "Rating Count",
                "average_rating": "Average Rating",
                "release_date": "Release Date",
               
            }
        ),
        width="stretch",
        hide_index=True,
        
    )

    chart = px.bar(
        filtered.sort_values("rating_count"),
        x="rating_count",
        y="title",
        orientation="h",
        title="Audience Popularity",
        labels={
            "rating_count": "Number of Ratings",
            "title": "Movie",
        },
    )
    chart.update_traces(marker_color="#e50914")
    st.plotly_chart(style_plot(chart), width="stretch")


# ============================================================
# AUDIENCE INSIGHTS
# ============================================================

elif page == "📊 Audience Insights":
    st.markdown('<div class="section-label">Dataset exploration</div>', unsafe_allow_html=True)
    st.title("📊 Audience Insights")

    if ratings_df.empty:
        st.error("Ratings data is unavailable.")
        st.stop()

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric("Total Ratings", f"{len(ratings_df):,}")

    with m2:
        st.metric("Unique Users", f"{ratings_df['user_id'].nunique():,}")

    with m3:
        st.metric("Unique Movies", f"{ratings_df['movie_id'].nunique():,}")

    with m4:
        st.metric("Average Rating", f"{ratings_df['rating'].mean():.2f}")

    st.divider()

    rating_distribution = (
        ratings_df["rating"]
        .value_counts()
        .sort_index()
        .rename_axis("Rating")
        .reset_index(name="Count")
    )

    fig1 = px.bar(
        rating_distribution,
        x="Rating",
        y="Count",
        text="Count",
        title="Rating Distribution",
    )
    fig1.update_traces(marker_color="#f5c518")
    st.plotly_chart(style_plot(fig1), width="stretch")

    user_activity = (
        ratings_df.groupby("user_id")
        .size()
        .reset_index(name="rating_count")
        .sort_values("rating_count", ascending=False)
        .head(20)
    )

    fig2 = px.bar(
        user_activity,
        x="user_id",
        y="rating_count",
        title="Most Active Viewers",
        labels={
            "user_id": "User ID",
            "rating_count": "Ratings Given",
        },
    )
    fig2.update_traces(marker_color="#ff8a00")
    st.plotly_chart(style_plot(fig2), width="stretch")

    if not users_df.empty:
        occupations = (
            users_df["occupation"]
            .value_counts()
            .head(15)
            .rename_axis("Occupation")
            .reset_index(name="Users")
        )

        fig3 = px.pie(
            occupations,
            names="Occupation",
            values="Users",
            hole=0.48,
            title="Audience Occupations",
        )
        st.plotly_chart(style_plot(fig3), width="stretch")


# ============================================================
# MODEL STUDIO
# ============================================================

elif page == "📈 Model Studio":
    st.markdown('<div class="section-label">Evaluation dashboard</div>', unsafe_allow_html=True)
    st.title("📈 Model Studio")

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric("Train Precision@10", f"{train_precision * 100:.2f}%")

    with m2:
        st.metric("Test Precision@10", f"{test_precision * 100:.2f}%")

    with m3:
        st.metric("Test Recall@10", f"{test_recall * 100:.2f}%")

    with m4:
        st.metric("Test AUC", f"{test_auc * 100:.2f}%")

    st.divider()

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=test_auc * 100,
            number={"suffix": "%"},
            title={"text": "Test AUC"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#f5c518"},
                "steps": [
                    {"range": [0, 60], "color": "#2a2a2a"},
                    {"range": [60, 80], "color": "#3a2e14"},
                    {"range": [80, 100], "color": "#402216"},
                ],
                "threshold": {
                    "line": {"color": "#e50914", "width": 4},
                    "thickness": 0.75,
                    "value": test_auc * 100,
                },
            },
        )
    )
    gauge.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="#f5f5f5",
        height=380,
    )

    left, right = st.columns([1, 1])

    with left:
        st.plotly_chart(gauge, width="stretch")

    with right:
        performance_df = pd.DataFrame(
            {
                "Metric": [
                    "Train Precision@10",
                    "Test Precision@10",
                    "Test Recall@10",
                    "Test AUC",
                ],
                "Score": [
                    train_precision * 100,
                    test_precision * 100,
                    test_recall * 100,
                    test_auc * 100,
                ],
            }
        )

        bars = px.bar(
            performance_df,
            x="Metric",
            y="Score",
            text="Score",
            title="Metric Comparison",
        )
        bars.update_traces(
            marker_color=["#ff8a00", "#e50914", "#f5c518", "#b91c1c"],
            texttemplate="%{text:.2f}%",
        )
        bars.update_layout(yaxis_range=[0, 100])
        st.plotly_chart(style_plot(bars), width="stretch")

    st.info(
        """
        **How to read the results**

        Precision@10 measures relevance within the top 10 suggestions.
        Recall@10 measures how many hidden relevant movies are recovered.
        AUC measures overall ranking quality. A Test AUC of about 93.99%
        indicates strong separation between preferred and non-preferred movies.
        """
    )

    st.subheader("Final Training Configuration")

    config = pd.DataFrame(
        {
            "Parameter": [
                "Algorithm",
                "Loss",
                "Latent Components",
                "Learning Rate",
                "Epochs",
                "Threads",
            ],
            "Value": [
                "LightFM",
                "WARP",
                50,
                0.03,
                40,
                1,
            ],
        }
    )

    st.dataframe(config, width="stretch", hide_index=True)


# ============================================================
# ABOUT
# ============================================================

elif page == "ℹ️ About":
    st.markdown('<div class="section-label">Project story</div>', unsafe_allow_html=True)
    st.title("ℹ️ About MovieMatch AI")

    st.write(
        "MovieMatch AI is a personalized movie discovery system built "
        "with LightFM and the MovieLens 100K dataset."
    )

    st.divider()

    a1, a2, a3 = st.columns(3)

    about_cards = [
        (
            "🧠",
            "Recommendation Model",
            "LightFM learns user and movie embeddings and optimizes top-ranked suggestions with WARP loss.",
        ),
        (
            "🎞️",
            "Dataset",
            "MovieLens 100K provides 100,000 ratings from 943 users across 1,682 movies.",
        ),
        (
            "📊",
            "Interactive Experience",
            "The dashboard combines personalized picks, trending titles, audience insights, and evaluation views.",
        ),
    ]

    for column, (icon, title, copy) in zip([a1, a2, a3], about_cards):
        with column:
            st.markdown(
                f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <div class="feature-title">{title}</div>
                    <div class="feature-copy">{copy}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.divider()
    st.subheader("Technology Stack")

    technologies = pd.DataFrame(
        {
            "Technology": [
                "Python",
                "LightFM",
                "Pandas",
                "NumPy",
                "Streamlit",
                "Plotly",
                "Joblib",
            ],
            "Purpose": [
                "Application development",
                "Recommendation modelling",
                "Data processing",
                "Numerical operations",
                "Interactive dashboard",
                "Visual analytics",
                "Artifact loading",
            ],
        }
    )

    st.dataframe(technologies, width="stretch", hide_index=True)

    st.divider()
    st.subheader("Future Scope")

    st.success(
        """
        - Genre-aware hybrid recommendations
        - Cold-start support for new users
        - Similar-movie discovery
        - Poster and trailer integration
        - Live user ratings and feedback loops
        - Diversity-aware ranking
        """
    )


st.divider()
st.caption("🎬 MovieMatch AI · Personalized Cinema Discovery")
st.caption("Built with LightFM, MovieLens 100K, Streamlit, and Plotly")



