# sharding
>Sharding is a method for distributing data across multiple machines. MongoDB uses sharding to support deployments with **very large data sets** and **high throughput operations**.

>MongoDB supports horizontal scaling through sharding.

>MongoDB shards data at the **collection level**, distributing the collection data across the shards in the cluster.

## sharded cluster
A MongoDB sharded cluster consists of the following components:

* **shard**: Each shard contains a subset of the sharded **data**. Each shard can be deployed as a replica set.
* **mongos**: The mongos acts as a **query router**, providing an interface between client applications and the sharded cluster.
* **config servers**: Config servers store **metadata and configuration settings** for the cluster. As of MongoDB 3.4, config servers must be deployed as a replica set (CSRS). 

### Production configuration
![](https://docs.mongodb.com/manual/_images/sharded-cluster-production-architecture.png)

### Development configuration
![](https://docs.mongodb.com/manual/_images/sharded-cluster-test-architecture.png)


