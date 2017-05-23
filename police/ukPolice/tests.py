from django.contrib.auth.models	import User
from django.test import TestCase
from models	import Crime, Outcome, Neighbourhood, NeighbourhoodPriority

class Association_TestCase(TestCase):

    def test_crime_outcome_association(self): # Tests the association between Crime and Outcome (on Associated_crime)
        """Test Outcome-Crime association"""
        user1 = User.objects.create(username="123456789x")
        test_crime = Crime.objects.create(policeman_assignated=user1)
        test_outcome = Outcome.objects.create(code="12345", name="Working", Associated_crime=test_crime)
        self.assertEqual(test_crime, test_outcome.Associated_crime)

    def test_crime_outcome_association_different(self): # Tests if changing the associated crime works
        """Test Outcome-Crime association"""
        user1 = User.objects.create(username="123456789x")
        user2 = User.objects.create(username="987654321h")
        test_crime = Crime.objects.create(policeman_assignated=user1)
        test_crime2 = Crime.objects.create(policeman_assignated=user2)
        test_outcome = Outcome.objects.create(code="12345", name="Working", Associated_crime=test_crime)
        test_outcome.Associated_crime = test_crime2
        self.assertNotEqual(test_crime, test_outcome.Associated_crime)

    def test_neighbourhood_association(self): # Tests if n_id is the same on both models (after associating)
        """Test neighbourhood association"""
        test_n = Neighbourhood.objects.create(n_id="1234", n_name="NY_test")
        test_np = NeighbourhoodPriority.objects.create(neighbourhood=test_n)
        self.assertEqual(test_n.n_id, test_np.neighbourhood.n_id)

    def test_neighbourhood_association_different(self): # Tests if changing values of Neighbourhood affects the NeighbourhoodPriority
        """Test neighbourhood association"""
        test_n = Neighbourhood.objects.create(n_id="1234", n_name="NY_test")
        test_np = NeighbourhoodPriority.objects.create(neighbourhood=test_n)
        test_n.n_id = "4321"
        self.assertNotEqual(test_n.n_id, "1234")
