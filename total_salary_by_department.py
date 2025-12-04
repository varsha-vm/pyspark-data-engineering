from pyspark.sql import SparkSession
import pyspark.sql.functions as F

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

df.groupBy("department").agg(F.sum("salary").alias("total_salary")).show()

df.show()