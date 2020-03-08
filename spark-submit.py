import pyspark as ps    # for the pyspark suite

if __name__ == "__main__":
    # we try to create a SparkSession to work locally on all cpus available
    spark = ps.sql.SparkSession.builder \
            .master("local[4]") \
            .appName("individual") \
            .getOrCreate()

    # Grab sparkContext from the SparkSession object
    sc = spark.sparkContext
    sc.setLogLevel('ERROR')

    # link to the s3 repository from Part 3
    link = 's3a://mortar-example-data/airline-data'
    airline_rdd = sc.textFile(link)
    print("There are dfdf " + str(airline_rdd.count()))