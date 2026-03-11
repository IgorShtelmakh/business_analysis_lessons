import pandas as pd
from langchain_anthropic import ChatAnthropic
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

from .database import engine

TABLE_NAMES = [
    "customers",
    "suppliers",
    "products",
    "pickup_locations",
    "orders",
    "order_items",
    "marketing_campaigns",
    "customer_support",
    "website_traffic",
    "product_reviews",
]


def _load_dataframes() -> list[pd.DataFrame]:
    return [pd.read_sql_table(name, engine) for name in TABLE_NAMES]


def _build_prefix(names: list[str]) -> str:
    parts = "\n".join(f"  df{i} = {name}" for i, name in enumerate(names))
    return (
        "You have access to the following pandas DataFrames "
        "from a Ukrainian electronics e-commerce store:\n"
        f"{parts}\n\n"
        "Answer the user's question by writing pandas code. "
        "Return the final answer in plain text."
    )


def ask_dataframes(question: str) -> str:
    dfs = _load_dataframes()
    llm = ChatAnthropic(model="claude-sonnet-4-6", temperature=0)
    agent = create_pandas_dataframe_agent(
        llm,
        dfs,
        prefix=_build_prefix(TABLE_NAMES),
        allow_dangerous_code=True,
        verbose=True,
    )
    result = agent.invoke({"input": question})
    return result["output"]
