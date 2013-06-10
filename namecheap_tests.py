# Run "nosetests" on command line to run these.

import sys
print sys.path

from namecheap import Api
from nose.tools import * # pip install nose

api_key = '' # You create this on Namecheap site
username = ''
ip_address = '' # Your IP address that you whitelisted on the site

# If you prefer, you can put the above in credentials.py instead
try:
	from credentials import api_key, username, ip_address
except:
	pass

def random_domain_name():
	import random, time
	domain_name = "%s%s.com" % (int(time.time()), random.randint(0,10**16))
	return domain_name

def test_domain_taken():
	api = Api(username, api_key, username, ip_address, sandbox = True)
	domain_name = "google.com"
	assert_equal(api.domains_check(domain_name), False)

def test_domain_available():
	api = Api(username, api_key, username, ip_address, sandbox = True)
	domain_name = random_domain_name()
	assert_equal(api.domains_check(domain_name), True)

def test_register_domain():
	api = Api(username, api_key, username, ip_address, sandbox = True)

	# Try registering a random domain. Fails if exception raised.
	domain_name = random_domain_name()
	api.domains_create(
		DomainName = domain_name,
		FirstName = 'Jack',
		LastName = 'Trotter',
		Address1 = 'Ridiculously Big Mansion, Yellow Brick Road',
		City = 'Tokushima',
		StateProvince = 'Tokushima',
		PostalCode = '771-0144',
		Country = 'Japan',
		Phone = '+81.123123123',
		EmailAddress = 'jack.trotter@example.com'
	)

def test_domains_getList():
	api = Api(username, api_key, username, ip_address, sandbox = True)
	api.domains_getList()

def test_domains_getContacts():
	# How would I test for this? This needs a known registered
	# domain to get the contact info for, but in sandbox won't
	# have any.
	pass
