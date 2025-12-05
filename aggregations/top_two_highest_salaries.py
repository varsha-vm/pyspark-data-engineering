from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.window import Window


# Start Spark
spark = SparkSession.builder.appName("DeptSalary").getOrCreate()

# Sample Data
data = [
    ("Asha", "IT", 90000),
    ("Ravi", "IT", 85000),
    ("Kiran", "IT", 90000),
    ("Meera", "HR", 70000),
    ("John", "HR", 68000)
]

df = spark.createDataFrame(data, ["name", "department", "salary"])

window = Window.partitionBy(F.col("department")).orderBy(F.col("salary").desc())

df = df.withColumn("rank", F.dense_rank().over(window))

df.filter(df.rank <=2).dropDuplicates(["department", "salary"]).select("department", "name", "salary", "rank").show()