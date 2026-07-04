# class Log4j(object):
#     def __init__(self, spark):
#         log4j = spark._jvm.org.apache.log4j
#         self.logger = log4j.LogManager.getLogger("sbdl")
#
#     def warn(self, message):
#         self.logger.warn(message)
#
#     def info(self, message):
#         self.logger.info(message)
#
#     def error(self, message):
#         self.logger.error(message)
#
#     def debug(self, message):
#         self.logger.debug(message)
#
#
#
# class Log4j:
#     def __init__(self, spark):
#         # Access the JVM Log4j2 logger
#         log4j = spark._jvm.org.apache.logging.log4j
#
#         # Use the Spark app name as the logger name
#         self.logger = log4j.LogManager.getLogger(spark.sparkContext.appName)
#
#     def info(self, message):
#         self.logger.info(message)
#
#     def warn(self, message):
#         self.logger.warn(message)
#
#     def error(self, message):
#         self.logger.error(message)

#
# class Log4j:
#     def __init__(self, spark):
#         log4j = spark._jvm.org.apache.logging.log4j
#         self.logger = log4j.LogManager.getLogger(spark.sparkContext.appName)
#
#     def info(self, message):
#         self.logger.info(message)
#
#     def warn(self, message):
#         self.logger.warn(message)
#
#     def error(self, message):
#         self.logger.error(message)

# class Log4j:
#     def __init__(self, spark):
#         log4j = spark._jvm.org.apache.logging.log4j
#         self.logger = log4j.LogManager.getLogger(spark.sparkContext.appName)
#
#     def info(self, message):
#         self.logger.info(message)
#
#     def warn(self, message):
#         self.logger.warn(message)
#
#     def error(self, message):
#         self.logger.error(message)


# class Log4j:
#     def __init__(self, spark):
#         log = spark._jvm.org.apache.spark.internal.Logging
#         self.logger = log.getLogger(spark.sparkContext.appName)
#
#     def info(self, message):
#         self.logger.info(message)
#
#     def warn(self, message):
#         self.logger.warn(message)
#
#     def error(self, message):
#         self.logger.error(message)

class Log4j:
    def __init__(self, spark):
        self.logger = spark._jvm.org.slf4j.LoggerFactory.getLogger(
            spark.sparkContext.appName
        )

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)
