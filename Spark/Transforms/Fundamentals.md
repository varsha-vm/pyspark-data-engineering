Spark fundamentals:
1. Spark is a distributed computing engine and also a framework, which is developed to mainly process the data of different size, structure and volume parallel.
2. Spark is an open source frame-work, which processes the data on JVM.
3. Spark is often used in tandem with storage systems such as HDFS, S3 etc to storage the spark processed data.
4. Furthermore, Spark also has cluster manager, to facilitate or orcestrate the distribution of applications across the cluster.
5. Different type of cluster manager available - Stand alone, Hadoop YARN, Mesos, Kubernetes.
6. Spark is not only a DCE, but also a framework that provides capabilities such as ANSI SQL, batch, stream and ML APIs to process the data efficiently in multi languages.
7. Spark is adopted by various companies for their data solutions mainly due to its features like easy to use, multi language support, open source, unified, abstraction from complexities.

Spark Architecture: (How spark is designed)
1. Spark has manly components. One of the main component is spark core, which is nothing but set of libraries(methods and functions) written in scalable to process the data.
2. Spark core has wrapper written around multi-languages such as python, R, Java. Hence, any code written using these languages will be ultimately compiled into Scala.
3. Further, each of the multiple language interfaces has api around it such as sql api, dataframe api, MLLib api, structure streaming api for near real time data processing, pandas api.
4. API are nothing but methods available in a particular language interface for data engineerings/scientists to use it to interact with spark.
5. Ultimately, whatever an engineer wants to do using the apis of spark on the data that they have, will be converted into RDDs.
6. Simple words, spark code is the main brain to process data, which is written is Scala. However, for folks who are comfortable with other language and different use-cases such as structured  streaming, batch processing, ML model, etc, Can use APIs written in different languages to process Data in spark. Eg: The data transformation that we write on a regular basis, is the Spark SQL components and we use python interfaces and APIs.
7. What are the libraries available on top of spark core?
    1. Spark SQL
    2. Structure streaming
    3. MLLIB
    5. Graphx
8. Why spark?
    1. Easy to use.
    2. Unified platform (to work on various use-cases)
    3. Abstract parallel processing from users.
