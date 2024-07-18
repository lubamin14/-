from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Создание Spark сессии
spark = SparkSession.builder.appName("product_category_pairs").getOrCreate()

# Пример входных данных (замените на свои данные)
data = [
    ("product1", "category1"),
    ("product1", "category2"),
    ("product2", "category2"),
    ("product3", None),
    ("product4", "category3")
]

# Создание DataFrame из входных данных
df = spark.createDataFrame(data, ["product", "category"])

# Выбор всех пар «Имя продукта – Имя категории»
product_category_pairs = df.select("product", "category").na.drop()
product_category_pairs.show()

# Нахождение имен всех продуктов, у которых нет категорий
products_without_category = df.filter(col("category").isNull()).select("product")
products_without_category.show()
