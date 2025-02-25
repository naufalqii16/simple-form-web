import unittest
from app import app, db
from flask import url_for

class FlaskAppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Setup sebelum semua test dijalankan."""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Gunakan database sementara
        cls.client = app.test_client()
        with app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        """Cleanup setelah semua test selesai."""
        with app.app_context():
            db.drop_all()

    def test_homepage(self):
        """Test apakah halaman utama bisa diakses."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_database_connection(self):
        """Test apakah database bisa diakses."""
        with app.app_context():
            result = db.session.execute("SELECT 1").fetchone()
            self.assertEqual(result[0], 1)

    def test_insert_data(self):
        """Test apakah data bisa disimpan ke database."""
        with app.app_context():
            db.session.execute("INSERT INTO attendance (student_id) VALUES ('67890')")
            db.session.commit()
            result = db.session.execute("SELECT student_id FROM attendance WHERE student_id='67890'").fetchone()
            self.assertIsNotNone(result)

    def test_retrieve_data(self):
        """Test apakah bisa mengambil data yang benar."""
        with app.app_context():
            db.session.execute("INSERT INTO attendance (student_id) VALUES ('112233')")
            db.session.commit()
            result = db.session.execute("SELECT student_id FROM attendance WHERE student_id='112233'").fetchone()
            self.assertEqual(result[0], '112233')

if __name__ == '__main__':
    unittest.main()
