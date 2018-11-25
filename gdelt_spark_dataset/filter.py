import os
from pyspark.sql import *
from pyspark.sql.functions import unix_timestamp, udf, to_date
from pyspark.sql.types import *
from datetime import datetime
spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext

# The codes of the countires of interest
fips_codes = ['AU','BE','BU','HR','CY','EZ','DK','EN','FI','FR','GM','GR','HU','EI','IT','LG','LH','LU','MT','NL','PL','PO','RO','LO','SI','SP','SW','UK','NO','LS','IC','SZ']

# The schema of the data frame
EVENTS_SCHEMA = StructType([
    StructField("GLOBALEVENTID",LongType(),True),
    StructField("Day_DATE",StringType(),True),
    StructField("MonthYear_Date",StringType(),True),
    StructField("Year_Date",StringType(),True),
    StructField("FractionDate",FloatType(),True),
    StructField("Actor1Code",StringType(),True),
    StructField("Actor1Name",StringType(),True),
    StructField("Actor1CountryCode",StringType(),True),
    StructField("Actor1KnownGroupCode",StringType(),True),
    StructField("Actor1EthnicCode",StringType(),True),
    StructField("Actor1Religion1Code",StringType(),True),
    StructField("Actor1Religion2Code",StringType(),True),
    StructField("Actor1Type1Code",StringType(),True),
    StructField("Actor1Type2Code",StringType(),True),
    StructField("Actor1Type3Code",StringType(),True),
    StructField("Actor2Code",StringType(),True),
    StructField("Actor2Name",StringType(),True),
    StructField("Actor2CountryCode",StringType(),True),
    StructField("Actor2KnownGroupCode",StringType(),True),
    StructField("Actor2EthnicCode",StringType(),True),
    StructField("Actor2Religion1Code",StringType(),True),
    StructField("Actor2Religion2Code",StringType(),True),
    StructField("Actor2Type1Code",StringType(),True),
    StructField("Actor2Type2Code",StringType(),True),
    StructField("Actor2Type3Code",StringType(),True),
    StructField("IsRootEvent",LongType(),True),
    StructField("EventCode",StringType(),True),
    StructField("EventBaseCode",StringType(),True),
    StructField("EventRootCode",StringType(),True),
    StructField("QuadClass",LongType(),True),
    StructField("GoldsteinScale",FloatType(),True),
    StructField("NumMentions",LongType(),True),
    StructField("NumSources",LongType(),True),
    StructField("NumArticles",LongType(),True),
    StructField("AvgTone",FloatType(),True),
    StructField("Actor1Geo_Type",LongType(),True),
    StructField("Actor1Geo_FullName",StringType(),True),
    StructField("Actor1Geo_CountryCode",StringType(),True),
    StructField("Actor1Geo_ADM1Code",StringType(),True),
    StructField("Actor1Geo_ADM2Code",StringType(),True),
    StructField("Actor1Geo_Lat",FloatType(),True),
    StructField("Actor1Geo_Long",FloatType(),True),
    StructField("Actor1Geo_FeatureID",StringType(),True),
    StructField("Actor2Geo_Type",LongType(),True),
    StructField("Actor2Geo_FullName",StringType(),True),
    StructField("Actor2Geo_CountryCode",StringType(),True),
    StructField("Actor2Geo_ADM1Code",StringType(),True),
    StructField("Actor2Geo_ADM2Code",StringType(),True),
    StructField("Actor2Geo_Lat",FloatType(),True),
    StructField("Actor2Geo_Long",FloatType(),True),
    StructField("Actor2Geo_FeatureID",StringType(),True),
    StructField("ActionGeo_Type",LongType(),True),
    StructField("ActionGeo_FullName",StringType(),True),
    StructField("ActionGeo_CountryCode",StringType(),True),
    StructField("ActionGeo_ADM1Code",StringType(),True),
    StructField("ActionGeo_ADM2Code",StringType(),True),
    StructField("ActionGeo_Lat",FloatType(),True),
    StructField("ActionGeo_Long",FloatType(),True),
    StructField("ActionGeo_FeatureID",StringType(),True),
    StructField("DATEADDED",LongType(),True),
    StructField("SOURCEURL",StringType(),True)
    ])


# HDFS directory where the gdelt dataset is stored on the cluster
DATA_DIR="hdfs:///datasets/gdeltv2"
# Read all export.csv files from the dataset
spark_df = spark.read.option("delimiter", "\t").csv(schema=EVENTS_SCHEMA, path=os.path.join(DATA_DIR, "*.export.CSV"))

# Broadcast the countries codes to speed up the filtering
fips_codes_broadcast = sc.broadcast(fips_codes)

# Filter the events, the events "Actor1", "Actor2" or "ActionGeo" must be in one of our countries of interest
filtered_df = spark_df.filter( (spark_df["Actor1Geo_CountryCode"].isin(fips_codes_broadcast.value)) |
                              (spark_df["Actor2Geo_CountryCode"].isin(fips_codes_broadcast.value)) |
                              (spark_df["ActionGeo_CountryCode"].isin(fips_codes_broadcast.value)))

# Save the filtered dataset in HDFS format
# Chage /user/mitrevski with /user/gaspracc
filtered_df.write.mode('overwrite').parquet("hdfs:///user/mitrevsk/data_frame.parquet")