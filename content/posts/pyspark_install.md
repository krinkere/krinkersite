Title: How to install Spark and use it from python via pyspark
Date: 2018-04-11 8:22
Modified: 2018-04-11 8:22
Status: published
Category: How To article
Tags: python, spark, pyspark
Slug: install_spark
Authors: Al Krinker
Summary: How to install Spark on your Linux system, and use it from Python

- Visit [Spark](http://spark.apache.org/downloads.html) to download tgz version of spark with hadoop
- Unzip and move it to /opt directory
```commandline
$ tar -xzf spark-2.3.0-bin-hadoop2.7.tgz
$ mv spark-2.3.0-bin-hadoop2.7 /opt/spark-2.3.0
```
- Create sym link
```commandline
$ ln -s /opt/spark-2.3.0 /opt/spark
```
- Add it to bash
```commandline
export SPARK_HOME=/opt/spark
export PATH=$SPARK_HOME/bin:$PATH
```
- At this point Spark is installed on your machine. Test it
```commandline
$ pyspark

Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.3.0
      /_/

Using Python version 3.6.4 (default, Jan 16 2018 18:10:19)
SparkSession available as 'spark'.
```
- Connect it to your python scripts, by installing findspark to point python to the location of the Spark
```commandline
$ pip install findspark
```
- Install pyspark to be able to use Spark from python
```commandline
$ pip install pyspark
```
- Now you will be able to use Spark from your python scripts
```python
import findspark
import pyspark
from pyspark.sql import SQLContext, Row

findspark.init(spark_home="/opt/spark")
conf = pyspark.SparkConf().setAppName('tf_fraud')
sc = pyspark.SparkContext(conf=conf)
sqlctx = SQLContext(sc)
connection_url = "jdbc:oracle:thin:"+username+"/"+password+"@"+ip+":"+str(port)+"/"+SID

df_pyspark = sqlctx.read.format('jdbc').options(url=connection_url, dbtable="employee", driver="oracle.jdbc.OracleDriver").load()
print(df_pyspark.printSchema())
cad_ser_nums = df_pyspark.foreach(print)
```
