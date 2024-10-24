"""Yahoo Finance Cash Flow Statement Model."""

from typing import Any, Dict, List, Literal, Optional

from jinniuai_data_store.reader import get_jindata_reader
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.cash_flow import (
    CashFlowStatementData,
    CashFlowStatementQueryParams,
)
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_core.provider.utils.errors import EmptyDataError
from pydantic import Field, model_validator

from openbb_xiaoyuan.utils.references import (
    get_report_month,
    get_query_finance_sql,
    groupByTime_sql,
)


class XiaoYuanCashFlowStatementQueryParams(CashFlowStatementQueryParams):
    __json_schema_extra__ = {
        "period": {
            "choices": ["fy", "q1", "q2ytd", "q3ytd", "annual"],
        }
    }

    period: Literal["fy", "q1", "q2ytd", "q3ytd", "annual"] = Field(
        default="fy",
        description=QUERY_DESCRIPTIONS.get("period", ""),
    )
    limit: Optional[int] = Field(default=None)


class XiaoYuanCashFlowStatementData(CashFlowStatementData):
    """Yahoo Finance Cash Flow Statement Data."""

    __alias_dict__ = {
        "sales_of_goods_and_provision_of_labour_received_cash": "销售商品提供劳务收到的现金",
        "received_tax_refunds": "收到的税费返还",
        "received_other_cash_related_to_operating_activities": "收到其他与经营活动有关的现金",
        "pledged_loans_net_increase": "质押贷款净增加额",
        "operating_activities_cash_inflows_subtotal": "经营活动现金流入小计",
        "purchase_of_goods_and_acceptance_of_labour_expenses_paid_cash": "购买商品、接受劳务支付的现金",
        "payments_to_employees_and_cash_paid_for_employees": "支付给职工以及为职工支付的现金",
        "paid_various_taxes": "支付的各项税费",
        "paid_other_cash_related_to_operating_activities": "支付其他与经营活动有关的现金",
        "operating_activities_cash_outflows_subtotal": "经营活动现金流出小计",
        "operating_activities_net_cash_flow": "经营活动产生的现金流量净额",
        "disposal_of_fixed_assets_intangible_assets_and_other_long_term_assets_recovered_net_amount": "处置固定资产、无形资产和其他长期资产收回的现金净额",
        "recovery_of_investments_received_cash": "收回投资收到的现金",
        "receipt_of_investment_income_cash": "取得投资收益收到的现金",
        "disposal_of_subsidiaries_and_other_business_units_received_cash_net_amount": "处置子公司及其他营业单位收到的现金净额",
        "received_other_cash_related_to_investing_activities": "收到其他与投资活动有关的现金",
        "investing_activities_cash_inflows_subtotal": "投资活动现金流入小计",
        "construction_of_fixed_assets_intangible_assets_and_other_long_term_assets_expenses_paid_cash": "购建固定资产、无形资产和其他长期资产支付的现金",
        "investment_expenses_paid_cash": "投资支付的现金",
        "acquisition_of_subsidiaries_and_other_business_units_paid_cash_net_amount": "取得子公司及其他营业单位支付的现金净额",
        "paid_other_cash_related_to_investing_activities": "支付其他与投资活动有关的现金",
        "investing_activities_cash_outflows_subtotal": "投资活动现金流出小计",
        "investing_activities_net_cash_flow": "投资活动产生的现金流量净额",
        "absorbed_investment_received_cash": "吸收投资收到的现金",
        "subsidiaries_absorbed_minority_investors_investment_received_cash": "子公司吸收少数股东投资收到的现金",
        "obtained_borrowing_received_cash": "取得借款收到的现金",
        "issued_bonds_received_cash": "发行债券收到的现金",
        "received_other_cash_related_to_financing_activities": "收到其他与筹资活动有关的现金",
        "financing_activities_cash_inflows_subtotal": "筹资活动现金流入小计",
        "repayment_of_debt_expenses_paid_cash": "偿还债务支付的现金",
        "distribution_of_dividends_profits_or_interest_paid_cash": "分配股利、利润或偿付利息支付的现金",
        "subsidiaries_paid_dividends_profits_to_minority_shareholders": "子公司支付给少数股东的股利、利润",
        "paid_other_cash_related_to_financing_activities": "支付其他与筹资活动有关的现金",
        "financing_activities_cash_outflows_subtotal": "筹资活动现金流出小计",
        "financing_activities_net_cash_flow": "筹资活动产生的现金流量净额",
        "exchange_rate_changes_effect_on_cash_and_cash_equivalents": "汇率变动对现金及现金等价物的影响",
        "cash_and_cash_equivalents_net_increase": "现金及现金等价物净增加额",
        "plus_beginning_cash_and_cash_equivalents_balance": "加：期初现金及现金等价物余额",
        "end_cash_and_cash_equivalents_balance": "期末现金及现金等价物余额",
        "customer_deposits_and_interbank_and_other_financial_institutions_deposits_net_increase": "客户存款和同业及其他金融机构存放款项净增加额",
        "paid_insurance_dividends_cash": "支付保单红利的现金",
        "borrowing_from_central_bank_net_increase": "向中央银行借款净增加额",
        "borrowing_from_other_financial_institutions_net_increase": "向其他金融机构拆入资金净增加额",
        "received_original_insurance_contract_premiums_cash": "收到原保险合同保费取得的现金",
        "received_reinsurance_business_net_cash": "收到再保险业务现金净额",
        "policyholder_savings_and_investment_funds_net_increase": "保户储金及投资款净增加额",
        "disposal_of_trading_financial_assets_net_increase": "处置交易性金融资产净增加额",
        "customer_loans_and_advances_net_increase": "客户贷款及垫款净增加额",
        "deposits_with_central_bank_and_interbank_net_increase": "存放中央银行和同业款项净增加",
        "paid_original_insurance_contract_claims_cash": "支付原保险合同赔付款项的现金",
        "paid_interest_fees_and_commissions_cash": "支付利息、手续费及佣金的现金",
        "received_interest_fees_and_commissions_cash": "收取的利息、手续费及佣金的现金",
        "borrowing_funds_net_increase": "拆入资金净增加额",
        "repurchase_business_funds_net_increase": "回购业务资金净增加额",
        "operating_activities_cash_inflow_adjustment_items": "经营活动现金流入的调整项目",
        "operating_activities_cash_inflow_error_amount": "经营活动现金流入的差错金额",
        "net_cash_flow_error_amount_from_operating_activities": "经营活动现金流量净额的差错金额",
        "investing_activities_cash_inflow_adjustment_items": "投资活动现金流入的调整项目",
        "investing_activities_cash_inflow_error_amount": "投资活动现金流入的差错金额",
        "investing_activities_cash_outflow_adjustment_items": "投资活动现金流出的调整项目",
        "investing_activities_cash_outflow_error_amount": "投资活动现金流出的差错金额",
        "net_cash_flow_error_amount_from_investing_activities": "投资活动现金流量净额的差错金额",
        "financing_activities_cash_inflow_adjustment_items": "筹资活动现金流入的调整项目",
        "financing_activities_cash_inflow_error_amount": "筹资活动现金流入的差错金额",
        "financing_activities_cash_outflow_adjustment_items": "筹资活动现金流出的调整项目",
        "financing_activities_cash_outflow_error_amount": "筹资活动现金流出的差错金额",
        "net_cash_flow_error_amount_from_financing_activities": "筹资活动现金流量净额的差错金额",
        "adjustment_items_affecting_cash_and_cash_equivalents": "影响现金及现金等价物的调整项目",
        "error_amount_affecting_cash_and_cash_equivalents": "影响现金及现金等价物的差错金额",
        "adjustment_items_affecting_end_cash_and_cash_equivalents_balance": "影响期末现金及现金等价物余额的调整项目",
        "error_amount_affecting_end_cash_and_cash_equivalents_balance": "影响期末现金及现金等价物余额的差错金额",
        "adjustment_items_for_operating_activities_cash_outflows": "经营活动现金流出的调整项目",
        "error_amount_for_operating_activities_cash_outflows": "经营活动现金流出的差错金额",
        "depreciation_of_fixed_assets_oil_and_gas_assets_depletion_production_biological_assets_depreciation": "固定资产折旧、油气资产折耗、生产性生物资产折旧",
        "asset_impairment_provision": "资产减值准备",
        "intangible_assets_amortization": "无形资产摊销",
        "long_term_deferred_expenses_amortization": "长期待摊费用摊销",
        "loss_on_disposal_of_fixed_assets_intangible_assets_and_other_long_term_assets": "处置固定资产、无形资产和其他长期资产的损失",
        "loss_on_scrapping_of_fixed_assets": "固定资产报废损失",
        "period_ending": "报告期",
    }

    @model_validator(mode="before")
    @classmethod
    def replace_zero(cls, values):  # pylint: disable=no-self-argument
        """Check for zero values and replace with None."""
        return (
            {k: None if v == 0 else v for k, v in values.items()}
            if isinstance(values, dict)
            else values
        )


class XiaoYuanCashFlowStatementFetcher(
    Fetcher[
        XiaoYuanCashFlowStatementQueryParams,
        List[XiaoYuanCashFlowStatementData],
    ]
):
    """Transform the query, extract and transform the data from the Yahoo Finance endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> XiaoYuanCashFlowStatementQueryParams:
        """Transform the query parameters."""
        return XiaoYuanCashFlowStatementQueryParams(**params)

    @staticmethod
    def extract_data(
        # pylint: disable=unused-argument
        query: XiaoYuanCashFlowStatementQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[XiaoYuanCashFlowStatementData]:
        factors = [
            "销售商品提供劳务收到的现金",
            "收到的税费返还",
            "收到其他与经营活动有关的现金",
            "质押贷款净增加额",
            "经营活动现金流入小计",
            "购买商品、接受劳务支付的现金",
            "支付给职工以及为职工支付的现金",
            "支付的各项税费",
            "支付其他与经营活动有关的现金",
            "经营活动现金流出小计",
            "经营活动产生的现金流量净额",
            "处置固定资产、无形资产和其他长期资产收回的现金净额",
            "收回投资收到的现金",
            "取得投资收益收到的现金",
            "处置子公司及其他营业单位收到的现金净额",
            "收到其他与投资活动有关的现金",
            "投资活动现金流入小计",
            "购建固定资产、无形资产和其他长期资产支付的现金",
            "投资支付的现金",
            "取得子公司及其他营业单位支付的现金净额",
            "支付其他与投资活动有关的现金",
            "投资活动现金流出小计",
            "投资活动产生的现金流量净额",
            "吸收投资收到的现金",
            "子公司吸收少数股东投资收到的现金",
            "取得借款收到的现金",
            "发行债券收到的现金",
            "收到其他与筹资活动有关的现金",
            "筹资活动现金流入小计",
            "偿还债务支付的现金",
            "分配股利、利润或偿付利息支付的现金",
            "子公司支付给少数股东的股利、利润",
            "支付其他与筹资活动有关的现金",
            "筹资活动现金流出小计",
            "筹资活动产生的现金流量净额",
            "汇率变动对现金及现金等价物的影响",
            "现金及现金等价物净增加额",
            "加：期初现金及现金等价物余额",
            "期末现金及现金等价物余额",
            "客户存款和同业及其他金融机构存放款项净增加额",
            "支付保单红利的现金",
            "向中央银行借款净增加额",
            "向其他金融机构拆入资金净增加额",
            "收到原保险合同保费取得的现金",
            "收到再保险业务现金净额",
            "保户储金及投资款净增加额",
            "处置交易性金融资产净增加额",
            "客户贷款及垫款净增加额",
            "存放中央银行和同业款项净增加",
            "支付原保险合同赔付款项的现金",
            "支付利息、手续费及佣金的现金",
            "收取的利息、手续费及佣金的现金",
            "拆入资金净增加额",
            "回购业务资金净增加额",
            "经营活动现金流入的调整项目",
            "经营活动现金流入的差错金额",
            "经营活动现金流量净额的差错金额",
            "投资活动现金流入的调整项目",
            "投资活动现金流入的差错金额",
            "投资活动现金流出的调整项目",
            "投资活动现金流出的差错金额",
            "投资活动现金流量净额的差错金额",
            "筹资活动现金流入的调整项目",
            "筹资活动现金流入的差错金额",
            "筹资活动现金流出的调整项目",
            "筹资活动现金流出的差错金额",
            "筹资活动现金流量净额的差错金额",
            "影响现金及现金等价物的调整项目",
            "影响现金及现金等价物的差错金额",
            "影响期末现金及现金等价物余额的调整项目",
            "影响期末现金及现金等价物余额的差错金额",
            "经营活动现金流出的调整项目",
            "经营活动现金流出的差错金额",
            "固定资产折旧、油气资产折耗、生产性生物资产折旧",
            "资产减值准备",
            "无形资产摊销",
            "长期待摊费用摊销",
            "处置固定资产、无形资产和其他长期资产的损失",
            "固定资产报废损失",
        ]
        reader = get_jindata_reader()
        symbols = query.symbol.split(",")
        report_month = get_report_month(query.period)

        finance_sql = get_query_finance_sql(factors, symbols, report_month)
        df = reader._run_query(
            script=groupByTime_sql + finance_sql,
        )
        if df is None or df.empty:
            raise EmptyDataError()
        df["报告期"] = df["报告期"].apply(lambda x: x.strftime("%Y-%m-%d"))
        df["timestamp"] = df["timestamp"].apply(lambda x: x.strftime("%Y-%m-%d"))
        df = df.sort_values(by="报告期", ascending=False)
        data = df.to_dict(orient="records")

        return data

    @staticmethod
    def transform_data(
        # pylint: disable=unused-argument
        query: XiaoYuanCashFlowStatementQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[XiaoYuanCashFlowStatementData]:
        """Transform the data."""
        return [XiaoYuanCashFlowStatementData.model_validate(d) for d in data]
