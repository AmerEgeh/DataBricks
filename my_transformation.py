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

# ==========================================
# 2. SILVER LAYER: Cleaning & Validation
# ==========================================
@dlt.table(
    name = 'silver_orders',
    comment = "Cleaned orders with dropped invalid records"
)
# Apply Data Quality Expectations
@dlt.expect_or_drop('valid_order_id', 'order_id IS NOT NULL')
@dlt.expect_or_drop('valid_amount', 'amount > 0')

def create_silver_table():
    # Read incrementally from the Bronze table
    clean_df = dlt.read_stream('bronze_orders')

    return clean_df


