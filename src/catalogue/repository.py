from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.catalogue.models.database import Product, AdditionalProduct, RecommendedProduct
from src.common.databases.postgres import get_session
from src.common.repository.sqlalchemy import BaseSQLAlchemyRepository


class ProductRepository(BaseSQLAlchemyRepository[Product]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=Product, session=session)


def get_product_repository(session: AsyncSession = Depends(get_session)) -> ProductRepository:
    return ProductRepository(session=session)


class AdditionalProductsRepository(BaseSQLAlchemyRepository[AdditionalProduct]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=AdditionalProduct, session=session)


def get_additional_products_repository(session: AsyncSession = Depends(get_session)) -> AdditionalProductsRepository:
    return AdditionalProductsRepository(session=session)


class RecommendedProductsRepository(BaseSQLAlchemyRepository[RecommendedProduct]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=RecommendedProduct, session=session)


def get_recommended_products_repository(session: AsyncSession = Depends(get_session)) -> RecommendedProductsRepository:
    return RecommendedProductsRepository(session=session)
