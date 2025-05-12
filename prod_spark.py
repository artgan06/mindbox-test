from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def get_product_category_pairs(
    products: DataFrame,
    categories: DataFrame,
    product_categories: DataFrame
) -> DataFrame:
    """
    Возвращает DataFrame со всеми парами (Имя продукта – Имя категории),
    а для продуктов без категорий — строку с category_name = null.
    """
    # Шаг 1: левый join products → product_categories
    joined_pc = products.alias("p") \
        .join(
            product_categories.alias("pc"),
            col("p.product_id") == col("pc.product_id"),
            how="left"
        )

    # Шаг 2: левый join полученного результата → categories
    joined_all = joined_pc \
        .join(
            categories.alias("c"),
            col("joined_pc.category_id") == col("c.category_id"),
            how="left"
        )

    # Шаг 3: оставляем только нужные колонки
    result = joined_all.select(
        col("p.product_name").alias("product_name"),
        col("c.category_name").alias("category_name")
    )

    return result
