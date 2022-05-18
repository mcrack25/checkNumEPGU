from app.models.WhereTable import WhereTable

class WhereController:
    def getData(self):
        data = WhereTable().select()
        return data

    def hasSnils(self, snils):
        try:
            result = WhereTable().select().where(WhereTable.snils == snils).get()
            return {"status": True, "result": result}
        except:
            return {"status": False, "result": 0}