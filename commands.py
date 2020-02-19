from ludwig.train_parquet import create_preprocessed_parquet, train_parquet

"""
model def:
input_features:
    -
        name: text
        type: text
        level: word
output_features:
    -
        name: intent
        type: category
training:
    epochs: 2
    
    
data:
text,intent,counts,locale
yes yes yes yes,accept,5,en
beautiful,other,1,en
beautiful beautiful,other,1,en
okay now eggmania that I will do 1546 Oak Tree Road in Woodbridge Township,other,1,en
Beach Fair,other,1,en
Beach Fair please,other,1,en
all right,accept,1,en
where's Abigail from,other,1,en
like I'm doing,other,1,en

"""

"""
# Get the sample data from HDFS
hdfs dfs -get /user/smiryala/dispatch_bot/train.csv
hdfs dfs -get /user/smiryala/dispatch_bot/test.csv
hdfs dfs -get /user/smiryala/dispatch_bot/validation.csv
"""

from ludwig.train_parquet import create_preprocessed_parquet, train_parquet

create_preprocessed_parquet(
    model_definition={},
    model_definition_file='model_definition.yaml',
    data_train_csv='train.csv',
    data_validation_csv='validation.csv',
    data_test_csv='test.csv'
)

# Upload the parquet files to a folder in HDFS
train_parquet(
    model_definition={},
    model_definition_file='model_definition.yaml',
    train_parquet_path='hdfs:///user/smiryala/dispatch_bot/train.parquet',
    validation_parquet_path='hdfs:///user/smiryala/dispatch_bot/validation.parquet',
    test_parquet_path='hdfs:///user/smiryala/dispatch_bot/test.parquet',
    train_set_metadata_json='train.json',
)
