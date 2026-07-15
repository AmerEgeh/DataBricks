import dlt
from pyspark.sql.functions import *
from pyspark.sql.types import *

@dlt.table(
    name = "bronze_orders"

)
def bronze_orders():
    return(
        spark.readStream.format('cloudfiles')\
            .option('cloudfiles.format', 'csv')\
            .option('cloudfiles.schemaEvolutionMode', 'rescue')\
            .option('cloudfiles.inferColumnTypes', 'true')\
            .load('/Volumes/dlt/default/dlt_files/')
            
    )