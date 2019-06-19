try:
    from pyspark import SparkContext, SparkConf
    from pyspark.sql import SparkSession
    import pyspark.sql.functions as f
except Exception as e:
    print(e)

def get_counts():
    spark = SparkSession \
        .builder \
        .appName("letters count") \
        .master('spark://master:7077') \
        .getOrCreate()
    lines = spark.read.text("/tmp/encrypted.txt")
    count = lines.withColumn('word', f.explode(f.split(f.col('value'), '')))\
        .groupBy('word')\
        .count()\
        .sort('count', ascending=False)

    # output results
    count.show()

    # End the Spark Context
    spark.stop()

if __name__ == "__main__":
    get_counts()
