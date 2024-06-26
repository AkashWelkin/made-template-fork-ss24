import sqlite3
import pytest
import os
import pandas as pd
import unittest
from unittest.mock import patch
import numpy as np
from sqlalchemy import create_engine
from ExtractData import ExtractData


class ETLSystemTest(unittest.TestCase):
    
    @patch('ExtractData.KaggleApi')
    def test_download_dataset(self, MockKaggleApi):
        mock_api = MockKaggleApi.return_value
        extract = ExtractData()
        extract.download_dataset('alessandrolobello/agri-food-co2-emission-dataset-forecasting-ml')
        
        mock_api.authenticate.assert_called_once()
        mock_api.dataset_download_files.assert_called_once_with('alessandrolobello/agri-food-co2-emission-dataset-forecasting-ml', path=extract.download_dir, unzip=True)

    @patch('pandas.read_csv')
    def test_load_and_clean_data(self, mock_read_csv):
        mock_data = pd.DataFrame({
            'Year': [1990, 1991, None, 1994],
            'Savanna fires': [14.72, 12.1, None, None]
        })
        mock_read_csv.return_value = mock_data

        extract = ExtractData()
        cleaned_data = extract.load_and_clean_data('Agrofood_co2_emission.csv')

        self.assertFalse(cleaned_data.isnull().values.any())
        self.assertIn('Year', cleaned_data.columns)
        self.assertIn('Savanna fires', cleaned_data.columns)

    @patch('ExtractData.create_engine')
    @patch('pandas.DataFrame.to_sql')
    def test_save_data(self, mock_to_sql, mock_create_engine):
        mock_engine = mock_create_engine.connect().return_value
        mock_data = pd.DataFrame({
             'Year': [1990, 1991, 1992, 1994],
             'Savanna fires': [14.72, 12.1, 12.4, 0.45]
         })
        extract = ExtractData()
        extract.save_data('ClimateDB', mock_data,'mock_db')

        mock_to_sql.assert_called_once_with('mock_db', con=mock_engine, if_exists='replace', index=False)



@pytest.fixture
def dbConnect():
    db_path = os.path.join(os.path.dirname(__file__), '../data/ClimateDB.sqlite')
    #db_path = "../data/ClimateDB.sqlite"
    if not os.path.isfile(db_path):
        pytest.fail("Error:DB path does not exist")
    try:
        connection = sqlite3.connect(db_path)
        print("Connection established")
        print(connection)
        yield connection
    finally:
        connection.close()

def test_db_exist(dbConnect):
    cursor = dbConnect.cursor()
    cursor.execute("select name from sqlite_master where type='table';")
    tables = cursor.fetchall()
    assert len(tables)>0, " Database Schmea is empty, no tables found!!!! Invalid DB!!"

def test_db_tables_exist(dbConnect):
    cursor = dbConnect.cursor()
    cursor.execute("select name from sqlite_master where type='table';")
    tables = cursor.fetchall()
    assert ('emission',) in tables and ('population',) in tables, "tables not found!!!!"
    
def test_table_size(dbConnect):
    table_shape = {
        'emission': (6965, 31),
        'population': (234, 19)
    }
    for table_name,expected_shape in table_shape.items():
        df = pd.read_sql_query(f"select * from {table_name}",dbConnect)
        assert expected_shape==df.shape, f"{table_name} table has missing data."
        

if __name__ == '__main__':
    unittest.main()     
    