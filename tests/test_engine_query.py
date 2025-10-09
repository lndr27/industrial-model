from industrial_model import PaginatedResult, col, select
from industrial_model.statements.expressions import and_

from .hubs import generate_engine
from .models import (
    CogniteAsset,
    CogniteAssetType,
    CogniteDescribable,
    CogniteEquipment,
    FunctionalLocation,
    ReportingUnit,
)

# def test_engine_query_describable() -> None:
#     engine = generate_engine()
#
#     select_statements = [
#         select(CogniteDescribable).limit(10),
#         select(CogniteDescribable).where(CogniteDescribable.name == "test"),
#     ]
#
#     for statement in select_statements:
#         result = engine.query(statement)
#         assert isinstance(result, PaginatedResult)
#
#
# def test_engine_query_asset_type() -> None:
#     engine = generate_engine()
#
#     select_statements = [
#         select(CogniteAssetType)
#         .limit(10)
#         .where(CogniteAssetType.code == "TESTING_123")
#         .asc(CogniteAssetType.code),
#     ]
#
#     for statement in select_statements:
#         result = engine.query(statement)
#         assert isinstance(result, PaginatedResult)
#
#
# def test_engine_query_equipment() -> None:
#     engine = generate_engine()
#
#     select_statements = [
#         select(CogniteEquipment).where(col(CogniteEquipment.asset).exists_()).limit(10),
#         select(CogniteEquipment)
#         .where(col(CogniteEquipment.asset).exists_() & col("externalId").in_(["123"]))
#         .limit(10),
#     ]
#
#     for statement in select_statements:
#         result = engine.query(statement)
#         assert isinstance(result, PaginatedResult)
#
#
# def test_engine_query_asset() -> None:
#     engine = generate_engine()
#
#     select_statements = [
#         select(CogniteAsset)
#         .where(
#             col(CogniteAsset.parent).nested_(CogniteAsset.external_id == "PARENT-123")
#         )
#         .limit(1),
#         select(CogniteAsset)
#         .where(
#             col(CogniteAsset.path).contains_any_(
#                 [{"externalId": "CHILD-456", "space": "cdf_cdm"}]
#             )
#         )
#         .limit(1),
#     ]
#
#     for statement in select_statements:
#         result = engine.query(statement)
#         assert isinstance(result, PaginatedResult)
#
#


def test_something() -> None:
    engine = generate_engine()

    statement = (
        select(FunctionalLocation)
        .pre_filter(
            col(FunctionalLocation.reporting_units),
            and_(col(ReportingUnit.external_id).equals_("UNT-FRAVAE")),
        )
        .limit(10)
    )

    result = engine.query(statement)
    assert isinstance(result, PaginatedResult)
    print(result.data[0].model_dump_json(indent=2))


if __name__ == "__main__":
    test_something()
