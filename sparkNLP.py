import sparknlp
from sparknlp.base import *
from sparknlp.annotator import *
from pyspark.sql import SparkSession
from sparknlp.pretrained import PretrainedPipeline

spark = SparkSession.builder \
    .appName("Spark NLP")\
    .master("local[4]")\
    .config("spark.driver.memory","16G")\
    .config("spark.driver.maxResultSize", "0") \
    .config("spark.kryoserializer.buffer.max", "2000M")\
    .config("spark.jars.packages", "com.johnsnowlabs.nlp:spark-nlp_2.12:3.4.2")\
    .getOrCreate()


sparknlp.start()

explain_document_pipeline = PretrainedPipeline("explain_document_ml")

annotations = explain_document_pipeline.annotate("We are very happy about SparkNLP.InshALLAH i wo master it")

print(annotations)

