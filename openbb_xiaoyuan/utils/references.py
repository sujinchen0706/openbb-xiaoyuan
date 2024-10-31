extractMonthDayFromTime = """
def extractMonthDayFromTime(time) {
    return substr(string(time), 5)
};
"""

getFiscalQuarterFromTime = """
def getFiscalQuarterFromTime(time) {
    i = monthOfYear(time);
    print i;
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


# Script 组合
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
            # f" and monthOfYear(报告期) = {month} context by symbol,timestamp order by 报告期 limit {limit} ;"
            f" and monthOfYear(报告期) = {month}  context by symbol,factor_name,extractMonthDayFromTime(报告期) order by 报告期 limit {limit} ;"
        )
        if month
        else f"context by symbol,factor_name,extractMonthDayFromTime(报告期) order by 报告期 limit {limit};"
    )
