extractMonthDayFromTime = """
def extractMonthDayFromTime(time) {
    return substr(string(time), 5)
};
"""

getFiscalQuarterFromTime = """
def getFiscalQuarterFromTime(time) {
    i = monthOfYear(time);
    if (i==3){
        return 'q1'
    }
    if (i==6){
        return 'q2'
    }
    if (i==9){
        return 'q3'
    }
    if (i==12){
        return 'q4'
    }
    };
"""


def get_query_finance_sql(factor_names: list, symbol: list, report_month: str) -> str:
    return f"""
        t = select timestamp,报告期, symbol, factor_name ,value 
        from loadTable("dfs://finance_factors_1Y", `cn_finance_factors_1Q) 
        where factor_name in {factor_names} 
            and symbol in {symbol} 
            {report_month} 
        t = select value from t pivot by timestamp,symbol,报告期,factor_name;
        select *,getFiscalQuarterFromTime(报告期) as fiscal_period,year(报告期) as fiscal_year 
        from t context by symbol,报告期;
        """


def get_report_month(period: str, limit=-4) -> str:
    period_to_month = {
        "ytd": "",
        "annual": "12",
    }
    if period not in period_to_month:
        raise ValueError(f"Invalid period: {period}")
    month = period_to_month[period]
    return (
        (
            f" and monthOfYear(报告期) = {month}  context by symbol,factor_name,extractMonthDayFromTime(报告期) "
            f"order by 报告期 limit {limit} ;"
        )
        if month
        else f"context by symbol,factor_name,extractMonthDayFromTime(报告期) "
        f"order by 报告期 limit {limit};"
    )


def get_specific_daily_sql(factor_names: list, symbol: list, date_list: list) -> str:
    return f"""
        timestamp = {date_list};
        date_list_table = table(timestamp);
        timestamp_table = select datetime(date(timestamp)) from date_list_table;
        t = select timestamp, symbol, factor_name,value
            from loadTable("dfs://factors_6M", `cn_factors_1D)
            where factor_name in {factor_names} and
            timestamp in timestamp_table
            and symbol in {symbol};
        t = select value from t where value is not null pivot by timestamp, symbol, factor_name;
        t
        """
