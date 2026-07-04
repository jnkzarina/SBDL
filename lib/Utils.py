from pyspark.sql import SparkSession

#
# def get_spark_session(env):
#     if env == "LOCAL":
#         spark = SparkSession.builder \
#             .appName("SBDL") \
#             .config(
#                 "spark.driver.extraJavaOptions",
#                 "-Dlog4j.configurationFile=file:///C:/SBDL/log4j2.properties"
#             ) \
#             .master("local[2]") \
#             .enableHiveSupport() \
#             .getOrCreate()
#         return spark
#     else:
#         return SparkSession.builder \
#             .enableHiveSupport() \
#             .getOrCreate()


def get_spark_session(env):
    if env == "LOCAL":
        spark = (
            SparkSession.builder
            .appName("SBDL")
            .config(
                "spark.driver.extraJavaOptions",
                "-Dlog4j.configurationFile=file:///C:/Demo/ScholarNest/SBDL_Workspace/SBDL/log4j2.properties"
            )
            .config(
                "spark.executor.extraJavaOptions",
                "-Dlog4j.configurationFile=file:///C:/Demo/ScholarNest/SBDL_Workspace/SBDL/log4j2.properties"
            )
            .getOrCreate()
        )
        return spark
    else:
        return SparkSession.builder \
            .enableHiveSupport() \
            .getOrCreate()
