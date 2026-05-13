

# 5 test_settings_load_defaults_when_env_missing`
#force taking off .env variables and check if defaults are loaded

from app.core.settings import Settings


def test_settings_load_defaults_when_env_missing(monkeypatch):

    monkeypatch.delenv("MONGO_URI", raising=False)
    monkeypatch.delenv("MONGO_DB_NAME", raising=False)
    monkeypatch.delenv("MONGO_TEST_DB_NAME", raising=False)

    settings = Settings(_env_file=None)
# we assert the default values so it doesnt crash when .env is missing and defaults are used
    assert settings.MONGO_URI == "mongodb://localhost:27017"
    assert settings.MONGO_DB_NAME == "ems_db"
    assert settings.MONGO_TEST_DB_NAME == "ems_test_db"

    #6 `test_settings_read_mongo_uri_from_env`
    #in the future if the default value of MONGO_URI changes, this test will ensure that the env variable is still read correctly and overrides the default

def test_settings_read_mongo_uri_from_env(monkeypatch):

    monkeypatch.setenv(
        "MONGO_URI",
        "mongodb://testserver:27017"
    )

    settings = Settings(_env_file=None)

    assert settings.MONGO_URI == "mongodb://testserver:27017"

