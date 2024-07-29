from localjsondb.jsonDB import ValidatedSchemaFactory, BaseJsonDbORM, DoFactory
import pandas as pd


class _MyTemplateProp:
    name: str
    description: str = ""
    systemcontent: str = ""
    usercontent: str = ""


class _MyTemplateSchema(_MyTemplateProp, ValidatedSchemaFactory):
    pass


class MyTemplateDo(_MyTemplateProp, DoFactory):
    pass


class MyTemplateOrm(BaseJsonDbORM):
    dbpath = "./mydb/tran"
    schema = _MyTemplateSchema

    def __init__(self, _dbname):
        self.dbname = _dbname
        super().__init__()


MyTemplate = MyTemplateOrm("MyTemplate")


def getTemplateByName(_name) -> dict:
    myTemplateDo = MyTemplateDo()
    myTemplateDo.name = _name

    out = MyTemplate.jsondb.getByQuery(myTemplateDo.to_query_dict())

    if len(out) > 0:
        return out[0]
    else:
        return {}


def getNameList() -> pd.DataFrame:
    out = MyTemplate.jsondb.getAll()

    if len(out) > 0:
        df = pd.DataFrame(out)
        return df[["name", "description"]]
    else:
        return pd.DataFrame()


def upsertValueBynameAnddescription(_name, _description, _systemcontent, _usercontent) -> bool:
    """
    OK
    """
    MyTemplateDo_systemrole = MyTemplateDo()
    MyTemplateDo_systemrole.name = _name
    MyTemplateDo_systemrole.description = _description
    MyTemplateDo_systemrole.systemcontent = _systemcontent
    MyTemplateDo_systemrole.usercontent = _usercontent

    return MyTemplate.upsertByprimaryKey(MyTemplateDo_systemrole)


def deletePjByName(_name) -> bool:
    """
    OK
    """
    MyTemplateDo_systemrole = MyTemplateDo()
    MyTemplateDo_systemrole.name = _name
    return MyTemplate.delete(MyTemplateDo_systemrole)
