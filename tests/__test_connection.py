import unittest
from unittest.mock import patch, MagicMock
from src.db.mongodb_connection import DBConnection

class TestDBConnection(unittest.TestCase):
    @patch('pymongo.MongoClient')
    def test_connect_to_db(self, mock_client):
        # Arrange
        mock_db = MagicMock()
        mock_client.return_value = mock_db

        # Act
        db_connection = DBConnection()
        db_connection.connect_to_db()

        # Assert
        mock_client.assert_called_once_with(db_connection.connection_string)
        self.assertEqual(db_connection.client, mock_db)
        self.assertEqual(db_connection.collection, mock_db[db_connection.db_name][db_connection.collection_name])

if __name__ == '__main__':
    unittest.main()