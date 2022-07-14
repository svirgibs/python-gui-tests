import pytest

from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Test programs\\Free Address Book\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture