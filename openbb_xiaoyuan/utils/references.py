FIN_METRICS_PER_SHARE = [
    "期末摊薄每股收益（元）",
    "扣非每股收益（元）",
    "每股收益EPSTTM（元）",
    "每股净资产（元）",
    "每股营业总收入（元）",
    "每股营业收入（元）",
    "每股营业收入TTM（元）",
    "每股息税前利润（元）",
    "每股资本公积（元）",
    "每股盈余公积（元）",
    "每股未分配利润（元）",
    "每股留存收益（元）",
    "每股经营活动产生的现金流量净额（元）",
    "每股经营活动产生的现金流量净额TTM（元）",
    "每股现金流量净额（元）",
    "每股现金流量净额TTM（元）",
    "每股企业自由现金流量（元）",
    "每股股东自由现金流量（元）",
]

groupByTime_sql = """
def groupByTime(time) {
    return substr(string(time), 5)
}
"""


# Script 组合
def get_query_financel_sql(factor_names: list, symbol: str, report_month: str) -> str:
    return f"""
        t = select 报告期, symbol, factor_name ,value 
        from loadTable("dfs://finance_factors_1Y", `cn_finance_factors_1Q) 
        where factor_name in {factor_names} 
            and symbol in {[symbol]} 
            {report_month} 
        t = select value from t pivot by factor_name,报告期;
        t
        """


def get_report_month(period: str) -> str:
    period_to_month = {
        "fy": "",
        "q1": "03",
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
            f"factor_name, groupByTime(报告期) order by 报告期 limit -4;"
        )
        if month
        else "context by symbol, factor_name, groupByTime(报告期) order by 报告期 limit -1;"
    )
