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
        .master(<TODO>) \
        .getOrCreate()
    lines = <TODO>
    count = lines.withColumn('letter', f.explode(f.split(f.col('value'), '')))\
        .groupBy('letter')\
        .count()\
        .sort('count', ascending=False)

    # output results
    count.show()

    # End the Spark Context
    spark.stop()

if __name__ == "__main__":
    get_counts()
