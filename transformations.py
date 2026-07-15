import dlt
from pyspark.sql.functions import *
from pyspark.sql.types import *

@dlt.table(
    name = "bronze_orders"

)
def bronze_orders():
    return(
        spark.readStream.format('cloudFiles')\
            .option('cloudFiles.format', 'csv')\
            .option('cloudFiles.schemaEvolutionMode', 'rescue')\
            .option('cloudFiles.inferColumnTypes', 'true')\
            .load('/Volumes/dlt/default/dlt_files/')
            
    )