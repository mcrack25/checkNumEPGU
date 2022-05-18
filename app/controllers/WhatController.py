from app.models.WhatTable import WhatTable

class WhatController:
    def getData(self):
        data = WhatTable().select()
        return data