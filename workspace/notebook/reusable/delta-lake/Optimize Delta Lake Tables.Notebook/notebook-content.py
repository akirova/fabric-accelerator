# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "056f28ae-dc2d-46d1-a603-44719accafbd",
# META       "default_lakehouse_name": "lh_silver",
# META       "default_lakehouse_workspace_id": "3639c676-d1c8-4910-8c36-f4148f3703eb"
# META     }
# META   }
# META }

# CELL ********************

%run /DeltaLakeFunctions

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Iterate through all tables in lakehouse and run OPTIMIZE and VACCUM commands

# CELL ********************

df = spark.sql("show tables")
tableList = df.select("tableName").rdd.flatMap(lambda x:x).collect()
# print (tables)
for table in tableList:
    print ("optimizing",table)
    optimizeDelta(table)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
