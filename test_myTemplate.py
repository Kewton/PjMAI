from app.myjsondb.myTemplate import upsertValueBynameAnddescription, deletePjByName, getTemplateByName, getNameList


def test_upsert():
    upsertValueBynameAnddescription(
        # formname
        "test_name",
        # keyname
        "teset_description",
        # value
        """
        あいうえお
        """
        ,
        """
        あいうえお@
        """
    )

    upsertValueBynameAnddescription(
        # formname
        "test_name",
        # keyname
        "teset_description_1",
        # value
        """
        あいうえお_1
        """
        ,
        """
        あいうえお@
        """
    )

    upsertValueBynameAnddescription(
        # formname
        "test_name_2",
        # keyname
        "teset_description",
        # value
        """
        あいうえお_2
        """
        ,
        """
        あいうえお5
        """
    )

    upsertValueBynameAnddescription(
        # formname
        "test_name_3",
        # keyname
        "teset_description_3",
        # value
        """
        あいうえお_3
        """
        ,
        "aiueo_3"
    )


def test_delete():
    deletePjByName("test_name_2")


if __name__ == '__main__':
    test_upsert()
    test_delete()
    print("-- 1 --")
    print(getTemplateByName("test_name"))
    print("-- 2 --")
    print(getTemplateByName("test_name_2"))
    print("-- all --")
    print(getNameList())
    #df = pd.DataFrame(getAllTemplate())
    #print(df.head())