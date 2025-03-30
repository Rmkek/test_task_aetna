import jsonlines
from sqlalchemy import create_engine, Column, String, MetaData, Table, Integer
from sqlalchemy.dialects.postgresql import JSONB

# Database connection
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/insurance_data"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Define the table
insurance_data = Table(
    'insurance_data',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('negotiation_arrangement', String),
    Column('name', String),
    Column('billing_code_type', String),
    Column('billing_code_type_version', String),
    Column('billing_code', String),
    Column('description', String),
    Column('negotiated_rates', JSONB),
)

# Drop existing tables and create new ones
metadata.drop_all(engine)
metadata.create_all(engine)

# Read and insert all lines in batches
BATCH_SIZE = 1000
batch = []
total_records = 0

print("Starting data import...")

with jsonlines.open('in_network_00.jsonl') as reader:
    with engine.connect() as connection:
        for line in reader:
            batch.append(line)
            
            if len(batch) >= BATCH_SIZE:
                connection.execute(
                    insurance_data.insert(),
                    batch
                )
                connection.commit()
                total_records += len(batch)
                print(f"Processed {total_records} records...")
                batch = []
        
        # Insert any remaining records
        if batch:
            connection.execute(
                insurance_data.insert(),
                batch
            )
            connection.commit()
            total_records += len(batch)

print(f"\nData import completed! Total records inserted: {total_records}")