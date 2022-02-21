from toto.lib import whats_my_name

#testing whoami
def test_whoami():

    res = whats_my_name()

    assert "Yannis" in res.split()
