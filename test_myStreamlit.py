from app.myjsondb.myStreamlit import upsertValueByFormnameAndKeyName, getValueKeyListByFormnameAndKeyName, getValueByFormnameAndKeyNameAndValueKey


def test_upsert():
    upsertValueByFormnameAndKeyName(
        # formname
        "common",
        # keyname
        "system",
        # value
        {
            "llmmodellist": [
                "gpt-4o",
                "gpt-4o-mini",
                "gpt-4",
                "gpt-3.5-turbo",
                "gpt-4-32k",
                "gpt-4-turbo",
                "claude-3-opus-20240229",
                "claude-3-sonnet-20240229",
                "claude-3-haiku-20240307"
            ]
        }
    )


if __name__ == '__main__':
    test_upsert()
    print(getValueKeyListByFormnameAndKeyName("common", "system"))
    print(getValueByFormnameAndKeyNameAndValueKey("common", "system", "llmmodellist"))
