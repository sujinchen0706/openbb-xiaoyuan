groupByTime_sql = """
def groupByTime(time) {
    return substr(string(time), 5)
}
"""


# Script 组合
def get_query_finance_sql(factor_names: list, symbol: list, report_month: str) -> str:
    return f"""
        t = select timestamp,报告期, symbol, factor_name ,value 
        from loadTable("dfs://finance_factors_1Y", `cn_finance_factors_1Q) 
        where factor_name in {factor_names} 
            and symbol in {symbol} 
            {report_month} 
        t = select value from t where value is not null pivot by 报告期,timestamp,symbol, factor_name;
        t
        """


def get_1y_query_finance_sql(
    factor_names: list, symbol: list, report_month: str
) -> str:
    return f"""
        t = select timestamp,报告期, symbol, factor_name ,value 
        from loadTable("dfs://finance_factors_1Y", `cn_finance_factors_1Y) 
        where factor_name in {factor_names} 
            and symbol in {symbol} 
            {report_month} 

        t = select value from t where value is not null pivot by 报告期,timestamp,symbol, factor_name;
        t
        """


def get_report_month(period: str) -> str:
    period_to_month = {
        "fy": "",
        "q1": "03",
        "q2": "06",
        "q3": "09",
        "q2ytd": "06",
        "q3ytd": "09",
        "annual": "12",
    }
    if period not in period_to_month:
        raise ValueError(f"Invalid period: {period}")
    month = period_to_month[period]
    return (
        (
            f" and monthOfYear(报告期) = {month} context by symbol, "
            f"factor_name, groupByTime(报告期) order by 报告期 limit -4 ;"
        )
        if month
        else "context by symbol, factor_name, groupByTime(报告期) order by 报告期 limit -1;"
    )
