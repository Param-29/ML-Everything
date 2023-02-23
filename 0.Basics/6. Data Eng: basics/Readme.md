Data-Enginnering: Intro
# Terminologies

## ETL

* E: Extract, T: Transform, L:Load 
* 3 steps of a data-cycle from source to usable-data

## Data-Lake
* Location to store data (*from various sources*) in most structured way possible (without any fildering/analytics)
* Data in raw format uncludes Non-relational and meta-data along with structured data
* Solutions explore way to store most amounts of data in cheapest way possible and which is also query-able. 
* *Helful for streaming services*


## Data-warehouses

* Various data-bases designed for highly structured data generated by business apps. It brings all your data together and stores it in a structured manner. It is typically used to connect and analyze data from heterogeneous sources.
* Architecture relies on the data structure to support highly performant SQL (Structured Query Language) 


![Data Lake vs Warehouse](https://www.qubole.com/wp-content/uploads/2020/12/Dl-vs-DW-infograph-1000x563.png)

### data marts

* It is a subset of the data stored in the datawarehouse.
* User/Use-case specific data in data-marts, example: customer table is data-mart and place where everything is stored together (customer, sales, transaction data) etc is data-warehouse

## OLAP & OLTP

OLTP: Online transaction processing
* i.e for backend and storange
* Normalized data used for application purpose
* Cusotmers are users of database
OLAP: Online Analytical processing
* i.e for analytical processing 
* Non-normalised huge chunk of data stored for decision make purpose
* Cusotmers are decision makes to use this data
![OLTP vs OLAP](https://www.google.com/url?sa=i&url=https%3A%2F%2Fsalesforce888.wordpress.com%2F2015%2F12%2F23%2Fdifference-between-oltp-vs-olapbi-analytics%2F&psig=AOvVaw0gZ1Ry7bk47D2zbZhGbOl4&ust=1676025527866000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCMj2heSfiP0CFQAAAAAdAAAAABAQ)

## Big-query (by GCS)

* Serverless data warehouse
* It has a seperate storage engine and different compute engine (like snowflake)


*Note:* 
* *Choose which columns to partition and cluster based on the column's you plan to most-query*

### Partitions in BigQuery

Link: https://cloud.google.com/bigquery/docs/partitioned-tables

![Partitions in table](https://www.google.com/url?sa=i&url=https%3A%2F%2Fhevodata.com%2Flearn%2Fbigquery-partition%2F&psig=AOvVaw3LCQpLizFC01NDMiRYFiWC&ust=1676029231685000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCLiVhcqtiP0CFQAAAAAdAAAAABAE)

* Physically partitioning tables (i.e stoing it in different places) to make queries run faster. (and estimate query costs)
* Example above
* SQL example below
* Number of paritions (that would be created) is limited to 4000

```sql
CREATE TABLE
  mydataset.newtable (transaction_id INT64, transaction_date DATE)
PARTITION BY
  transaction_date
```

### Clustering

![Cluster & Partiton](https://cloud.google.com/bigquery/docs/clustered-tables)

* No physical partition, and no approximation in costs prediction but it helps in creating faster queries
* It clusters rows of (to_be_clusterted_column) together increasing speed if queried around it
* Order of the columns is important
* You can specify up to 4 clustering-columns


# Keywords

* Ad-hoc Queries: One-time queries (which are generally not quired that often/experiment purposes) as opposed to general queries (which backend application makes)
# References

* [Data lakes and data-warehouses](https://www.qubole.com/data-lakes-vs-data-warehouses-the-co-existence-argument)
* [Data lake](https://aws.amazon.com/big-data/datalakes-and-analytics/what-is-a-data-lake/)