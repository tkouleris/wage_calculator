import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index_loads(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Wage Calculator', response.data)
        # Check if some Greek labels are present
        self.assertIn('Έδρα Εταιρείας'.encode('utf-8'), response.data)
        self.assertIn('Αθήνα'.encode('utf-8'), response.data)

    def test_form_submission(self):
        response = self.app.post('/', data={
            'company_hq': '0',
            'way_of_working': '0',
            'company_size': '0',
            'education': '0',
            'gender': '0',
            'team_leader': '0',
            'job_roles': ['AI / ML', 'Backend'],
            'technologies': ['Python', 'React']
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Selection received!', response.data)

if __name__ == '__main__':
    unittest.main()
